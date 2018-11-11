celery的使用



https://blog.csdn.net/Shyllin/article/details/80940643



https://www.cnblogs.com/forward-wang/p/5970806.html



启动命令

celery -A task_dir_name beat

```
http://127.0.0.1:5555/user/celery/?v1=aaaa&v2=bbb
```


可使用 AWS 的 SQS 和 DynmoDB

windows

```

pip install eventlet
celery -A <mymodule> worker -l info -P eventlet
```

http://www.cnblogs.com/cwp-bg/p/8759638.html

