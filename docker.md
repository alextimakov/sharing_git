### base
- виртуализация vs контейнеризация
    - изоляция (требования разных приложений)
    - безопасность
    - убирается прослойка гипервизора (запускается вся ОС)
    - контейнерная виртуализация (LXC - Linux Containers) - 
    в основе лежит разнесение по namespace'ам, куча виртуалок, 1 машина
    - зачем, если можно запускать всё в отдельных namespace'ах?
    - namespace - изолированная область (окружение), где запускается процесс (не видит другие)
    - внутри контейнера - только то, что нужно для запуска приложения (обвязка)
- docker container
    - app -> container -> registry -> pull
    - обновление -> убили старое, выкатили новое
    - docker compatibility matrix
    - docker swarm == kubernetes (разные разрабы, идея одна и та же)
    - `curl -sSL https://get.docker.com | sh`
    - docker - клиент, dockerd - сервер
    - dockerhub - github для образов
    - `docker exec -it <container-id> bash` - демоном
    - `docker logs <container-id>`
    - docker перехватывает весь stdout \ stderr - его можно пересылать
    - у контейнеров могут быть разные машины
    - switch docker0 + Network Address Translation - контейнеры подтыкаются к 1 свитчеру
    - `iptables -t nat -L -n` - dNAT
    - контейнеры видят друг друга
    - контейнер несёт в себе все данные - все данные перед "перезапуском" на хостовую систему
    - контейнер состоит из слоёв
    - `docker inspect <container-id> | less`
    - логи можно складывать в elasticsearch
    - `docker run --net=<bridge_name>` - подрубиться к нужному хосту
    - `docker network list`
    - `brctl show`
    - `docker images`
    - запускаем кучу app в 1 network - говорим, куда в какой ip смотреть
    - nginx?
 - docker image
    - у каждого имажа есть dockerfile
    - dockerfile -> docker build -> docker push
    - в dockerfile - FROM + RUN + ARG + COPY + EXPOSE + ENTRYPOINT (слои)
    - на dockerhub'e можно создать репозиторий под образ - `docker login`
    - config на ./.docker/config.json
    - `dker.ru` \ `goharbor.io`
    - `docker build -t <registry_ip:port>`
- docker-compose
    - описывает как запускать сервисы (app+image+ports)
    - создаст сетку и запустит все сервисы в ней
    - запускает всё на 1 локальной машине
    - конфиг в формате yml
- запуски контейнеров
    - 3 варианта:
        - docker run
        - docker-compose 
        - оркестрация (kubernetes - swarm - rancher) 
        - запускается много app на разных машинах = кластер
        - машины разбиваются на мастера и ноды
        - мастерам даются compose'ы -> раскидывают запуски имажев app по нодам

     
### glossary
- chroot
- overhead
- iops
- Архитектура и реализация FreeBSD
- проброс volume'ов (для БД) - можно подмонтировать временную директорию
- docker registry можно сделать свой (есть у гитлаба, гугла, амазона и пр)
- smoke testing
- overlay сетка (контейнеры на разных хостах видят друг друга)
- `iputils-ping`
- `traceroute` | `HTTP headers`
- `relay + DKIM + DNS`
- `SOA data`