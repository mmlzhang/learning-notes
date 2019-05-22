

复杂SQL

```sql
select * from (SELECT t.id, t.end_time, t.creative_limit, (select count(id) from creative
    as c where c.task_id = t.id and c.status = 'selected' ) as 'selected' FROM task as t where t.status = 'active')
    as temp where temp.selected >= temp.creative_limit or temp.end_time <= now();
```

join SQL

```sql
select t.ad_plan_id, t.task_id  from task_ad_plan t left join ad_plan a on a.id=t.ad_plan_id where a.status='active'; 
```

