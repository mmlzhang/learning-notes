

ELK安装：<https://c4ys.com/archives/552>





#### 配置logstash

```bash
cd /opt/server/logstash-5.5.0/config
touch python-logstash.conf
---------------输入以下内容-------------------
input {
  udp {
    port => 5959 #udp的端口
    codec => json#输入的格式为json格式
  }
}
output {
elasticsearch {
    hosts => ["10.100.172.111:9200"] #es的地址
    index => "python-message-%{+YYYY.MM.dd}" #存入到es的索引名
        }
  stdout {
    codec => rubydebug
  }
}

#到logstash的bin目录下，启动Logstash
[root@inte-es-node1 bin]# ./logstash -f ../config/python-logstash.conf
```

安装python-logstash

`pip install python-logstash`

```python
import logging
import logstash
import sys

#host为logstash的IP地址
host = '10.100.172.111'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
#创建一个ogHandler
test_logger.addHandler(logstash.LogstashHandler(host, 5959))


test_logger.error('这是一行测试日志')
# test_logger.info('python-logstash: test logs  tash info message.')
# test_logger.warning('python-logstash: test logstash warning message.')
```



```python
import logging
import logstash
import sys

host = 'localhost'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')

# add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
test_logger.info('python-logstash: test extra fields', extra=extra)
```

