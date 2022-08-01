FROM ubuntu:20.04

MAINTAINER FelipeCastro "felipe.castroa@alumnos.uv.cl"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip libmysqlclient-dev python3-dev

RUN apt-get install -y git
RUN pip install python-dotenv
RUN apt install make -y
RUN pip install cmake
RUN apt-get install -y libboost-container-dev
RUN apt-get install -y python3-dolfin
RUN apt-get install -y python3-mshr

COPY ./requeriments.txt /app/requeriments.txt

RUN python3 --version
RUN pip3 --version


WORKDIR /app
RUN pip install -r ./requeriments.txt

COPY . /app

EXPOSE 80

ENTRYPOINT [ "python3" ]

CMD [ "src/main.py" ] 