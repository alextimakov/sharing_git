# Работа с Docker
```shell script
# create new image and run container from it
# https://vsupalov.com/developing-with-python3-8-on-ubuntu-18-04/
docker pull ubuntu:18.04
docker run -t -d --name app_name  # конфигурирую нужное внутри 
docker commit app_name correct_image:latest
docker container rm app_name
docker run -p 0.0.0.0:8000:8000 -t -d --name app_name correct_image:latest
docker exec -it app_name bash

# run apache nifi with docker without auth
docker pull apache/nifi
docker run -p 0.0.0.0:8080:8080 -t -d --name nifi apache/nifi
docker exec -it nifi bash

# check container logs
docker logs container_id | less
docker logs --tail=100 -t --since 2020-04-20T09:00:00 container_id
docker logs container_id 2>&1 | grep listening

# check container stats
docker stats --all --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}" container_id

# run container with mounted volume
docker run -v /source/:/usr/bin/docker -p 0.0.0.0:8080:8080 -t -d --name nifi apache/nifi

# work with images
docker images
docker image rm image_id

# 
```