FROM python

COPY . /home
WORKDIR /home/kinezio

RUN apt-get update && \
        apt-get upgrade --assume-yes && \
        apt-get install --assume-yes python3-pip && \
        apt-get install --assume-yes screen && \
        apt-get install nano && \
        pip install --upgrade pip && \
        pip install -r ../requirements.txt 

CMD ["bash", "/home/kinezio/.start.sh"]
