---
title: Mysql锁和事物
date: 2019-05-27 11:44:16
tags: Mysql
---

## 什么场景下用表锁

InnoDB默认采用行锁，在未使用索引字段查询时升级为表锁。MySQL这样设计并不是给你挖坑。它有自己的设计目的。即便你在条件中使用了索引字段，MySQL会根据自身的执行计划，考虑是否使用索引(所以explain命令中会有possible_key 和 key)。如果MySQL认为全表扫描效率更高，它就不会使用索引，这种情况下InnoDB将使用表锁，而不是行锁。因此，在分析锁冲突时，别忘了检查SQL的执行计划，以确认是否真正使用了索引。

第一种情况：**全表更新**。事务需要更新大部分或全部数据，且表又比较大。若使用行锁，会导致事务执行效率低，从而可能造成其他事务长时间锁等待和更多的锁冲突。

第二种情况：**多表查询**。事务涉及多个表，比较复杂的关联查询，很可能引起死锁，造成大量事务回滚。这种情况若能一次性锁定事务涉及的表，从而可以避免死锁、减少数据库因事务回滚带来的开销

1 InnoDB 支持表锁和行锁，使用索引作为检索条件修改数据时采用行锁，否则采用表锁。
2 InnoDB 自动给修改操作加锁，给查询操作不自动加锁
3 行锁可能因为未使用索引而升级为表锁，所以除了检查索引是否创建的同时，也需要通过explain执行计划查询索引是否被实际使用。
4 行锁相对于表锁来说，优势在于高并发场景下表现更突出，毕竟锁的粒度小。
5 当表的大部分数据需要被修改，或者是多表复杂关联查询时，建议使用表锁优于行锁。
6 为了保证数据的一致完整性，任何一个数据库都存在锁定机制。锁定机制的优劣直接影响到一个数据库的并发处理能力和性能。

## 表锁

表锁的优势：开销小；加锁快；无死锁
表锁的劣势：锁粒度大，发生锁冲突的概率高，并发处理能力低
加锁的方式：自动加锁。查询操作（SELECT），会自动给涉及的所有表加读锁，更新操作（UPDATE、DELETE、INSERT），会自动给涉及的表加写锁。也可以显示加锁：
共享读锁：lock table tableName read;
独占写锁：lock table tableName write;
批量解锁：unlock tables;

## 行锁

行锁的劣势：开销大；加锁慢；会出现死锁
行锁的优势：锁的粒度小，发生锁冲突的概率低；处理并发的能力强
加锁的方式：自动加锁。对于UPDATE、DELETE和INSERT语句，InnoDB会自动给涉及数据集加排他锁；对于普通SELECT语句，InnoDB不会加任何锁；当然我们也可以显示的加锁：
共享锁：select * from tableName where ... + lock in share more
排他锁：select * from tableName where ... + for update 
**InnoDB和MyISAM的最大不同点**有两个：一，InnoDB支持事务(transaction)；二，默认采用行级锁。加锁可以保证事务的一致性，可谓是有人(锁)的地方，就有江湖(事务)；

### 行锁优化

1 尽可能让所有数据检索都通过索引来完成，避免无索引行或索引失效导致行锁升级为表锁。
2 尽可能避免间隙锁带来的性能下降，减少或使用合理的检索范围。
3 尽可能减少事务的粒度，比如控制事务大小，而从减少锁定资源量和时间长度，从而减少锁的竞争等，提供性能。
4 尽可能低级别事务隔离，隔离级别越高，并发的处理能力越低



### 事务常见问题

**更新丢失**（Lost Update）
原因：当多个事务选择同一行操作，并且都是基于最初选定的值，由于每个事务都不知道其他事务的存在，就会发生更新覆盖的问题。类比github提交冲突。

**脏读**（Dirty Reads）
原因：事务A读取了事务B已经修改但尚未提交的数据。若事务B回滚数据，事务A的数据存在不一致性的问题。

**不可重复读**（Non-Repeatable Reads）
原因：事务A第一次读取最初数据，第二次读取事务B已经提交的修改或删除数据。导致两次读取数据不一致。不符合事务的隔离性。

**幻读**（Phantom Reads）
原因：事务A根据相同条件第二次查询到事务B提交的新增数据，两次数据结果集不一致。不符合事务的隔离性。

### 事务的隔离级别

数据库的事务隔离越严格，并发副作用越小，但付出的代价也就越大。这是因为事务隔离实质上是将事务在一定程度上"串行"进行，这显然与"并发"是矛盾的。根据自己的业务逻辑，权衡能接受的最大副作用。从而平衡了"隔离" 和 "并发"的问题。MySQL默认隔离级别是可重复读。脏读，不可重复读，幻读，其实都是数据库读一致性问题，必须由数据库提供一定的事务隔离机制来解决。

```mysql
+------------------------------+---------------------+--------------+--------------+--------------+
| 隔离级别                      | 读数据一致性         | 脏读         | 不可重复 读   | 幻读         |
+------------------------------+---------------------+--------------+--------------+--------------+
| 未提交读(Read uncommitted)    | 最低级别            | 是            | 是           | 是           | 
+------------------------------+---------------------+--------------+--------------+--------------+
| 已提交读(Read committed)      | 语句级              | 否           | 是           | 是           |
+------------------------------+---------------------+--------------+--------------+--------------+
| 可重复读(Repeatable read)     | 事务级              | 否           | 否           | 是           |
+------------------------------+---------------------+--------------+--------------+--------------+
| 可序列化(Serializable)        | 最高级别，事务级     | 否           | 否           | 否           |
+------------------------------+---------------------+--------------+--------------+--------------+
```

查看当前数据库的事务隔离级别：show variables like 'tx_isolation';

```mysql
mysql> show variables like 'tx_isolation';
+---------------+-----------------+
| Variable_name | Value           |
+---------------+-----------------+
| tx_isolation  | REPEATABLE-READ |
+---------------+-----------------+
```

### 排他锁

排他锁，也称写锁，独占锁，当前写操作没有完成前，它会阻断其他写锁和读锁。
![img](assets/160df13cc9e5d70e)

```mysql
# Transaction_A
mysql> set autocommit=0;
mysql> select * from innodb_lock where id=4 for update;
+----+------+------+
| id | k    | v    |
+----+------+------+
|  4 | 4    | 4000 |
+----+------+------+
1 row in set (0.00 sec)

mysql> update innodb_lock set v='4001' where id=4;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> commit;
Query OK, 0 rows affected (0.04 sec)
# Transaction_B
mysql> select * from innodb_lock where id=4 for update;
+----+------+------+
| id | k    | v    |
+----+------+------+
|  4 | 4    | 4001 |
+----+------+------+
1 row in set (9.53 sec)
```

### 共享锁

共享锁，也称读锁，多用于判断数据是否存在，多个读操作可以同时进行而不会互相影响。当如果事务对读锁进行修改操作，很可能会造成死锁。如下图所示。
![img](assets/160df13cd5156062)

```mysql
# Transaction_A
mysql> set autocommit=0;
mysql> select * from innodb_lock where id=4 lock in share mode;
+----+------+------+
| id | k    | v    |
+----+------+------+
|  4 | 4    | 4001 |
+----+------+------+
1 row in set (0.00 sec)

mysql> update innodb_lock set v='4002' where id=4;
Query OK, 1 row affected (31.29 sec)
Rows matched: 1  Changed: 1  Warnings: 0
# Transaction_B
mysql> set autocommit=0;
mysql> select * from innodb_lock where id=4 lock in share mode;
+----+------+------+
| id | k    | v    |
+----+------+------+
|  4 | 4    | 4001 |
+----+------+------+
1 row in set (0.00 sec)

mysql> update innodb_lock set v='4002' where id=4;
ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction
```

### 分析行锁定

通过检查InnoDB_row_lock 状态变量分析系统上的行锁的争夺情况 show status like 'innodb_row_lock%'

```mysql
mysql> show status like 'innodb_row_lock%';
+-------------------------------+-------+
| Variable_name                 | Value |
+-------------------------------+-------+
| Innodb_row_lock_current_waits | 0     |
| Innodb_row_lock_time          | 0     |
| Innodb_row_lock_time_avg      | 0     |
| Innodb_row_lock_time_max      | 0     |
| Innodb_row_lock_waits         | 0     |
+-------------------------------+-------+
```

innodb_row_lock_current_waits: 当前正在等待锁定的数量
innodb_row_lock_time: 从系统启动到现在锁定总时间长度；非常重要的参数，
innodb_row_lock_time_avg: 每次等待所花平均时间；非常重要的参数，
innodb_row_lock_time_max: 从系统启动到现在等待最常的一次所花的时间；
innodb_row_lock_waits: 系统启动后到现在总共等待的次数；非常重要的参数。直接决定优化的方向和策略。