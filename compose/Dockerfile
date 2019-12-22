FROM ubuntu:18.04
RUN apt update
RUN echo 'y' | apt install python3-pip
COPY requirements.txt /scripts/
RUN pip3 install -r ./scripts/requirements.txt
WORKDIR /src/