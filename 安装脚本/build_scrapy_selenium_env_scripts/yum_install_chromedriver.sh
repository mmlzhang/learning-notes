
sudo mkdir -p /tmp/python_egg_cached /tmp/run /tmp/chromedriver
sudo chmod 777 -R /tmp
sudo wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/2.44/chromedriver_linux64.zip
sudo unzip /tmp/chromedriver.zip chromedriver -d /tmp/chromedriver/
sudo chmod +x /tmp/chromedriver/chromedriver
sudo mv -f /tmp/chromedriver/chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver