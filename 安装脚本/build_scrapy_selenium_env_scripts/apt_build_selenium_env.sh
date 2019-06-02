FROM ubuntu:16.04

RUN apt-get -q update

# Install python dependencies
RUN apt-get -qqy install libxml2-dev libxslt1-dev python3.5-dev python3.5 python3-pip libssl-dev libffi-dev build-essential

#===============
# Google Chrome
#===============
RUN apt-get -qqy install wget && \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - &&\
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list &&\
  apt-get update -qqy  --allow-unauthenticated&&\
  apt-get -qqy --allow-unauthenticated install google-chrome-stable &&\
  rm /etc/a# Install fonts
pt/sources.list.d/google-chrome.list &&\
  rm -rf /var/lib/apt/lists/*

RUN apt-get -q update
RUN apt-get install -qqy ttf-ancient-fonts-symbola ttf-ubuntu-font-family ttf-unifont ttf-adf-accanthis ttf-adf-baskervald ttf-adf-berenis ttf-adf-gillius ttf-adf-ikarius ttf-adf-irianis ttf-adf-libris ttf-adf-mekanus ttf-adf-oldania ttf-adf-romande ttf-adf-switzera ttf-adf-tribun ttf-adf-universalis ttf-adf-verana ttf-aenigma ttf-alee ttf-ancient-fonts ttf-anonymous-pro ttf-arabeyes ttf-atarismall ttf-baekmuk ttf-bitstream-vera ttf-dejavu ttf-dejavu-core ttf-dejavu-extra ttf-denemo ttf-engadget ttf-essays1743 ttf-femkeklaver ttf-fifthhorseman-dkg-handwriting ttf-freefarsi ttf-freefont ttf-georgewilliams ttf-goudybookletter ttf-hanazono ttf-isabella ttf-jsmath ttf-junicode ttf-kacst ttf-kacst-one ttf-liberation ttf-lyx ttf-marvosym ttf-oxygen-font-family ttf-radisnoir ttf-sjfonts ttf-staypuft ttf-summersby ttf-tagbanwa ttf-tiresias ttf-tomsontalks ttf-unfonts-core ttf-unfonts-extra ttf-wqy-microhei ttf-wqy-zenhei ttf2ufm ttfautohint

# Install x11vnc
RUN apt-get install -qqy x11vnc

# Install fluxbox
RUN apt-get install -qqy fluxbox

# install phantomjs
RUN apt-get install -qqy phantomjs

# Install java and git
RUN apt-get install -qqy git default-jdk

# Configure x11vnc
RUN mkdir -p ~/.vnc &&\
  x11vnc -storepasswd secret ~/.vnc/passwd

# Install xvfb
RUN apt-get install -qqy xvfb

# Install chrome webdriver
RUN apt-get -qqy install unzip && \
  wget -N -q http://chromedriver.storage.googleapis.com/2
  .25/chromedriver_linux64.zip -P ~/Downloads && \
  unzip ~/Downloads/chromedriver_linux64.zip -d ~/Downloads && \
  chmod +x ~/Downloads/chromedriver && \
  mv -f ~/Downloads/chromedriver /usr/local/share/chromedriver && \
  ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver && \
  ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

# Configure locale
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
RUN locale-gen en_US.UTF-8

# Following line fixes
# https://github.com/SeleniumHQ/docker-selenium/issues/87
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null