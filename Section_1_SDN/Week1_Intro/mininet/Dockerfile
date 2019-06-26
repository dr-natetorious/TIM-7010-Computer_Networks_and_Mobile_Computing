FROM debian:stretch
LABEL Author="Nate Bachmeier"
LABEL Course="TIM-7010: Computer Networks and Mobile Computing"
LABEL School="NorthCentral University"

RUN apt-get -y update && yes yes | apt-get -y install \
  mininet \
  wireshark

# Setup VNC services for remote terminal
RUN apt-get -y install \
  xfce4 xfce4-goodies gnome-icon-theme tightvncserver sudo

RUN adduser --disabled-password --gecos "vnc,vnc,vnc,vnc" vnc \
  && gpasswd -a vnc sudo
USER vnc

EXPOSE 5901
