FROM ubuntu:16.04
LABEL maintainer="by DATO"
ARG UID=1000
RUN apt-get update && apt-get install -y nano
RUN useradd -m stepik -u $UID
ENV EDITOR=/usr/bin/nano
USER stepik
WORKDiR /home/stepik
VOLUME /home/stepik
ENTRYPOINT ["bash", "-c", "nano"]
~id−u id -u id−u(whoami)
1000