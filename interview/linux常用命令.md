```sh
clear 清屏

cd – 后退

cd $MYPATH 进入指定目录(环境变量已设)

ls –l 列出文件

ls –al 列出所有文件，包含隐藏文件

whoami 查看自己用户名

cd mydir 进入目录

cd my* 进入目录

tar cvf ddd.tar abc.* def ghi 压缩文件(可以多个)

tar xvf ddd.tar 解压缩

rm –rf mydir 删除目录，不带确认

grep abc *.pc 文件内容中查找abc

grep –c abc *.txt 查找内容abc，并统计

grep –i abc *.txt 查找内容abc，大小写不敏感

set|grep TL_ABC 在环境变量中过滤TL_ABC

diff abc.txt /usera/def.txt 比较文件

find . –name “abc*” 目录中查找文件

cp –p abc.txt /mydir/abc_d.txt 拷贝

ps –ef|grep UserA 列出某用户的进程

shellABC.sh > abc.log 覆盖输出

shellABC.sh >> abc.log 追加输出

exit 退出

su –userABC 切换用户

last 查看最近登录的用户

Esc+K 重复上次输入的命令(多次k向上翻)

   编辑上次的命令： Esc+i 插入 Esc+x 删除 h 向左 l 向右

ipcs –oq|grep 5000 查看消息队列

make 自动查找目录下的makefile并编译

man sighold 查看该函数定义 man socket

cat abc.txt 查看文件

more abc.txt 分页查看文件

vi abc.txt 编辑文件

netstat –i 查看网卡

netstat –r 查看路由

alias pss=’ps –ef|grep abc’ 设置快捷shell名pss，常用在.profile中

which pss ，或which cc 查cc所在的目录

PS1=’$PWD>’;export PS1 显示当前目录，而不是$ (常用在.profile中)

set –o vi 常用在Esc显示^K的情况下

cp /dev/null abc.log 清空文件 (大文件常常vi打不开(:%d)，直接用此命令)

. .profile 修改$HOME的.profile文件后不用重新登陆，用此命令立刻生效

set|grep ABC, 查看环境变量，或用env

who|wc –l 统计在线人数

pwd 查看当前目录

ipcs –oq 查看消息队列是否拥堵

tail –f abc.log　跟踪文件末尾

chmod +x find_me.sh 加执行权限

netstat –an|grep 52 查看包含52的端口网络状态

netstat –an|grep LISTEN 查看侦听端口网络状态

ls –l|grep ‘^d’ 列出目录

ls –l|grep ‘^[^d]’ 列出非目录

grep userABC /etc/services 查看DB2端口等信息

grep userABC /etc/passwd 查看$HOME所在目录

dbx –a 99878 调试attach到PID(有关dbx调试命令见其他)

# Shell进阶命令

 sudo !!                    以 root 的身份执行上一条命令
 ctrl r                       在命令历史中查找
 history                     查看命令历史
 !88                          运行命令历史中的编号为88的命令
  ^old^new               替换前一条命令里的部分字符串并重新执行上一条命令
  du -s * | sort -n -r    当前目录里的文件和文件夹按大小排序排列
  > file.txt                  创建一个空文件，比 touch 短
  top -p pid                监控某个进程的CPU和内存消耗情况，ps aux获得PID，或者 ps -p pid -o %cpu,%mem,cmd
  netstat -tulpn           显示侦听的端口
  netstat -anop           显示侦听的端口和侦听在这个端口号的进程
  tail -f /path/to/file.log sed '/^Finished: SUCCESS$/ q' 当 file.log 里出现 Finished: SUCCESS 时候就退出 tail，这个命令用于实时监控并过滤 log 是否出现了某条记录。
  ssh user@server bash < /path/to/local/script.sh 在远程机器上运行一段脚本。这条命令最大的好处就是不用把脚本拷到远程机器上。
  lsof –i                     实时查看本机网络服务的活动状态。
```

