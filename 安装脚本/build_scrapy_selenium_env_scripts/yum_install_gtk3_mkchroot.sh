#! /bin/bash

#----------------------------------------------------------------------
# Description: a script to prepare a build environment for building GTK3
# Author: Artem S. Tashkinov
# Created at: Thu Jun 26 16:50:40 YEKT 2014
# Computer: localhost.localdomain
# System: Linux 3.15.0-ic on i686
#
# Copyright (c) 2014 Artem S. Tashkinov.  All rights reserved.
# Licensed under: LGPL 2.1 or later
#----------------------------------------------------------------------


wget http://mirror.yandex.ru/centos/6.5/os/i386/Packages/centos-release-6-5.el6.centos.11.1.i686.rpm

croot=/tmp/CentOS
mkdir -p $croot $croot/proc $croot/dev
mount -o bind /dev $croot/dev
mount -o bind /dev/pts $croot/dev/pts
mount -o bind /proc $croot/proc
rpm -ivh --root $croot centos-release-6-5.el6.centos.11.1.i686.rpm
yum --installroot=$croot install gcc make bison rpm-build expat-devel \
  fontpackages-devel gcc-c++ libtool bash mc yum freetype-devel tar which gettext \
  libXext-devel libXrender-devel libXi-devel libpng-devel libjpeg-turbo-devel \
  libtiff-devel perl-XML-Parser flex libxml2-devel popt-devel libXtst-devel
chroot $croot
