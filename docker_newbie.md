# Работа с Docker
```shell script
# https://vsupalov.com/developing-with-python3-8-on-ubuntu-18-04/
docker pull ubuntu:18.04
docker run -t -d --name app_name  # конфигурирую нужное внутри 
docker commit app_name correct_image:latest
docker container rm app_name
docker run -p 0.0.0.0:8000:8000 -t -d --name app_name correct_image:latest
docker exec -it app_name bash
```
