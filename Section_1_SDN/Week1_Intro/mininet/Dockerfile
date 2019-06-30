FROM python:3
LABEL Author="Nate Bachmeier"
LABEL Course="TIM-7010: Computer Networks and Mobile Computing"
LABEL School="NorthCentral University"

RUN apt-get -y update && apt-get -y install \
  sudo

WORKDIR /git
RUN git clone git://github.com/mininet/mininet \
  && cd mininet \
  && git checkout 2.2.2 \
  && ./util/install.sh -a
