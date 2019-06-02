
sudo yum -y groupinstall "Development tools"
sudo yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
sudo wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
sudo tar -xvJf  Python-3.6.2.tar.xz
cd Python-3.6.2
sudo ./configure --prefix=/usr/local/python3
sudo make
sudo make install
sudo ln -s /usr/local/python3/bin/python3 /usr/bin/python3 && sudo ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
sudo yum install python-virtualenv