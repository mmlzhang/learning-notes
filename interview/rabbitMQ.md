

## Rabbitmq 常用三种exchange类型：

## Fanout exchange：

这是处理逻辑最简单的exchange类型，实际上它没有任何逻辑，它把进入该exchange的消息全部转发给每一个绑定的队列中，如果这个exchange没有队列与之绑定，消息会被丢弃。

## Direct exchange

这种类型的交换机Fancout 类型的交换机智能一些，它会根据routing key来决定把消息具体扔到哪个消息队列中。通过exchange发消息的时候会指定一个routing key，只有当routing key和与队列绑定的routing key一样的时候，消息才对发送到对应的消息队列。即，如果与某个队列绑定的routing key叫hello.world，则通过exchange发送的routing key必须也是hello.world，该队列才能接收到消息（可按上述步骤进行验证）。这种情况下，队列之间是互斥关系，一个消息最多只能进入一个队列。

## Topic exchange

Topic exchange是最灵活的exchange，它会把exchange的routing key与绑定队列的routing key进行模式匹配。Routing key中可以包含 `*`和`#`两种符号，#号可以用来匹配一个或者多个单词，`*`用来匹配正好一个单词。官方的下图很好地说明了这个问题，读者最好自己动手验证一下。

```python

import os
import sys
import pika
 
 
def createVerifyCardQueues():
    credentials = pika.PlainCredentials('your user', 'your password')
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1',5672,"/",credentials))
    channel = connection.channel()
 
    name_prefix = "merchant.verifycard.async"
    exchange_name = "paybiz.merchant.exchange"
    channel.queue_declare()
    start=10
    end = 26
    for biz_type in range(start, end):
        queue_name = name_prefix + str(biz_type)
        channel.queue_declare(queue_name,False,True)
        channel.queue_bind(queue_name,exchange_name,queue_name)
 
if __name__ == "__main__":
    createVerifyCardQueues()
```





#### 生产者

```python
import pika

credentials = pika.PlainCredentials('admin','123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.56.19',5672,'/',credentials))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='balance')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='balance',
                      body='Hello World!')
print("[x] Sent 'Hello World!'")
connection.close()
```

查看队列中的消息

```shell
rabbitmqctl list_queues

Listing queues ...
hello    1
```



#### 消费者

```python

import pika

credentials = pika.PlainCredentials('admin','123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.56.19',5672,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='balance')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback,
                      queue='balance',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
```





RabbitMQ是一个在AMQP基础上完整的，可复用的企业消息系统。他遵循Mozilla Public License开源协议。

MQ全称为Message Queue, 消息队列（MQ）是一种应用程序对应用程序的通信方法。应用程序通过读写出入队列的消息（针对应用程序的数据）来通信，而无需专用连接来链接它们。消 息传递指的是程序之间通过在消息中发送数据进行通信，而不是通过直接调用彼此来通信，直接调用通常是用于诸如远程过程调用的技术。排队指的是应用程序通过 队列来通信。队列的使用除去了接收和发送应用程序同时执行的要求。

RabbitMQ安装

```python
安装配置epel源
  $ rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
安装erlang
  $ yum -y install erlang
安装RabbitMQ
  $ yum -y install rabbitmq-server
复制代码
```

注意：service rabbitmq-server start/stop

安装API

```python
pip install pika
or
easy_install pika
or
源码
https://pypi.python.org/pypi/pika
复制代码
```

使用API操作RabbitMQ

基于Queue实现生产者消费者模型

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import Queue
import threading
message = Queue.Queue(10)
def producer(i):
   while True:
       message.put(i)

def consumer(i):
   while True:
       msg = message.get()

for i in range(12):
   t = threading.Thread(target=producer, args=(i,))
   t.start()

for i in range(10):
   t = threading.Thread(target=consumer, args=(i,))
   t.start()
复制代码
```

对于RabbitMQ来说，生产和消费不再针对内存里的一个Queue对象，而是某台服务器上的RabbitMQ Server实现的消息队列。

```python
#!/usr/bin/env python
import pika

# ######################### 生产者 #########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
       host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                     routing_key='hello',
                     body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()

# ########################## 消费者 ##########################
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
       host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
   print(" [x] Received %r" % body)

channel.basic_consume(callback,
                     queue='hello',
                     no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
复制代码
```

1、acknowledgment 消息不丢失

no-ack ＝ False，如果消费者遇到情况(its channel is closed, connection is closed, or TCP connection is lost)挂掉了，那么，RabbitMQ会重新将该任务添加到队列中。

消费者

```python
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(
       host='10.211.55.4'))
channel = connection.channel()
channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
   print(" [x] Received %r" % body)
   import time
   time.sleep(10)
   print 'ok'
   ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                     queue='hello',
                     no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
复制代码
```

2、durable   消息不丢失

生产者

```python
#!/usr/bin/env python
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.211.55.4'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='hello', durable=True)

channel.basic_publish(exchange='',
                     routing_key='hello',
                     body='Hello World!',
                     properties=pika.BasicProperties(
                         delivery_mode=2, # make message persistent
                     ))
print(" [x] Sent 'Hello World!'")
connection.close()
复制代码
```

消费者

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.211.55.4'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='hello', durable=True)


def callback(ch, method, properties, body):
   print(" [x] Received %r" % body)
   import time
   time.sleep(10)
   print 'ok'
   ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                     queue='hello',
                     no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
复制代码
```

3、消息获取顺序

默认消息队列里的数据是按照顺序被消费者拿走，例如：消费者1 去队列中获取 奇数 序列的任务，消费者1去队列中获取 偶数 序列的任务。

channel.basic_qos(prefetch_count=1) 表示谁来谁取，不再按照奇偶数排列

消费者

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.211.55.4'))
channel = connection.channel()
# make message persistent
channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
   print(" [x] Received %r" % body)
   import time
   time.sleep(10)
   print 'ok'
   ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                     queue='hello',
                     no_ack=False)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
复制代码
```

4、发布订阅



![img](assets/164c9e979b46a239)



发布订阅和简单的消息队列区别在于，发布订阅会将消息发送给所有的订阅者，而消息队列中的数据被消费一次便消失。所以，RabbitMQ实现发布和订阅时，会为每一个订阅者创建一个队列，而发布者发布消息时，会将消息放置在所有相关队列中。

exchange type = fanout

发布者

```python
#!/usr/bin/env python
import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(
       host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                        type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                     routing_key='',
                     body=message)
print(" [x] Sent %r" % message)
connection.close()

复制代码
```

订阅者

```python
#!/usr/bin/env python
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(
       host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs',
                        type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                  queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
   print(" [x] %r" % body)
channel.basic_consume(callback,
                     queue=queue_name,
                     no_ack=True)
channel.start_consuming()
复制代码
```

5、关键字发送



![img](assets/164c9ea1e221e1d5)



exchange type = direct

之前事例，发送消息时明确指定某个队列并向其中发送消息，RabbitMQ还支持根据关键字发送，即：队列绑定关键字，发送者将数据根据关键字发送到消息exchange，exchange根据 关键字 判定应该将数据发送至指定队列。

消费者

```python
#!/usr/bin/env python
import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(
       host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',
                        type='direct')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
severities = sys.argv[1:]
if not severities:
   sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
   sys.exit(1)
for severity in severities:
   channel.queue_bind(exchange='direct_logs',
                      queue=queue_name,
                      routing_key=severity)
print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
   print(" [x] %r:%r" % (method.routing_key, body))
channel.basic_consume(callback,
                     queue=queue_name,
                     no_ack=True)
channel.start_consuming()
复制代码
```

生产者

```python
#!/usr/bin/env python
import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(
       host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',
                        type='direct')
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                     routing_key=severity,
                     body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
复制代码
```

6、模糊匹配



![img](assets/164c9eab68df4752)



exchange type = topic

在topic类型下，可以让队列绑定几个模糊的关键字，之后发送者将数据发送到exchange，exchange将传入”路由值“和 ”关键字“进行匹配，匹配成功，则将数据发送到指定队列。

# 表示可以匹配 0 个 或 多个 单词

- 表示只能匹配 一个 单词

发送者路由值              队列中

```python
old.boy.python          old.*  -- 不匹配
old.boy.python          old.#  -- 匹配
复制代码
```

消费者

```python
#!/usr/bin/env python
import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(
       host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',
                        type='topic')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
binding_keys = sys.argv[1:]
if not binding_keys:
   sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
   sys.exit(1)
for binding_key in binding_keys:
   channel.queue_bind(exchange='topic_logs',
                      queue=queue_name,
                      routing_key=binding_key)
print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
   print(" [x] %r:%r" % (method.routing_key, body))
channel.basic_consume(callback,
                     queue=queue_name,
                     no_ack=True)
channel.start_consuming()
复制代码
```

生产者

```python
#!/usr/bin/env python
import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(
       host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',
                        type='topic')
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                     routing_key=routing_key,
                     body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
复制代码
```

设置链接密码

```python
sudo rabbitmqctl add_user wupeiqi 123
# 设置用户为administrator角色
sudo rabbitmqctl set_user_tags wupeiqi administrator
# 设置权限
sudo rabbitmqctl set_permissions -p "/" root ".*" ".*" ".*"
# 然后重启rabbiMQ服务
sudo /etc/init.d/rabbitmq-server restart

# 然后可以使用刚才的用户远程连接rabbitmq server了。
------------------------------
credentials = pika.PlainCredentials("wupeiqi","123")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.14.47',credentials=credentials))
复制代码
```

设置超时时间

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika
from pika.adapters.blocking_connection import BlockingChannel
credentials = pika.PlainCredentials("root", "123")
conn = pika.BlockingConnection(pika.ConnectionParameters(host='10.211.55.20', credentials=credentials))
# 超时时间
conn.add_timeout(5, lambda: channel.stop_consuming())
channel = conn.channel()
channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
   print(" [x] Received %r" % body)
   channel.stop_consuming()
channel.basic_consume(callback,
                     queue='hello',
                     no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

```