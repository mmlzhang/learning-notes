

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

