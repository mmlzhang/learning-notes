

## Rabbitmq 常用三种exchange类型：

## Fanout exchange：

这是处理逻辑最简单的exchange类型，实际上它没有任何逻辑，它把进入该exchange的消息全部转发给每一个绑定的队列中，如果这个exchange没有队列与之绑定，消息会被丢弃。

## Direct exchange

这种类型的交换机Fancout 类型的交换机智能一些，它会根据routing key来决定把消息具体扔到哪个消息队列中。通过exchange发消息的时候会指定一个routing key，只有当routing key和与队列绑定的routing key一样的时候，消息才对发送到对应的消息队列。即，如果与某个队列绑定的routing key叫hello.world，则通过exchange发送的routing key必须也是hello.world，该队列才能接收到消息（可按上述步骤进行验证）。这种情况下，队列之间是互斥关系，一个消息最多只能进入一个队列。

## Topic exchange

Topic exchange是最灵活的exchange，它会把exchange的routing key与绑定队列的routing key进行模式匹配。Routing key中可以包含 *和#两种符号，#号可以用来匹配一个或者多个单词，*用来匹配正好一个单词。官方的下图很好地说明了这个问题，读者最好自己动手验证一下。



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

