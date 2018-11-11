chorme



command

```shell
sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/ & wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add - &sudo apt-get update & sudo apt-get install google-chrome-stable & /usr/bin/google-chrome-stable
```



fish

软件源所在文件目录

```
/etc/apt/sources.list.d

apt update
apt install fish

```

