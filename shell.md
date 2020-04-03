# Набор полезных команд и утилит

## shell команды
```shell script
# Поиск необходимого текста в массиве информации (например, файле)
grep "2017" file.csv

# Результат поиска можно сразу писать в новый файл
grep "2017" file.csv > file_2017.csv

# Поиск текущих процессов
ps aux | grep process_name
 
# В случае необходимости, можно убить процесс, посмотрев его PID с помощью htop
kill -9 PID_number

# Команда для просмотра оставшегося места на диске
df -h /
 
# Можно посмотреть, что занимает больше всего места на диске
ls -hlS
 
# Посмотреть, сколько места занимает каждая из субдиректорий в указанной директории
du -h --max-depth=1 /path/to/directory | sort -h

# Команда для запуска скрипта каждые number_seconds секунд и обновления результатов работы скрипта script_name
watch -n number_seconds script_name
 
# Например, чтобы проверять содержимое текущей папки каждые 5 секунд, нужна такая команда
watch -n 5 ls

# мониторинг всех входящих соединений по выбранному порту
netstat -natlc | grep '7474'

# посмотреть все открытые ssh соединения к серверу
lsof -i -n | egrep '\<ssh\>'
 
# посмотреть все открытые файлы в указанной директории
lsof +D folder/

# Отправить на удалённый сервер, запускать с локала
scp -i ~/.ssh/path/to_pem_file /path/to/local/file user@server_ip:./desired/file/location
 
# Скачать на локал с удалённого сервера, запускать с локала
scp -i ~/.ssh/path/to_pem_file user@server_ip:./path/to/desired/file/   ~/my_projects/

# Проверить, доступен ли интересующий сервер
curl -Is server_ip

# Настройка swap на ubuntu 17.04+
swapoff -a
dd if=/dev/zero of=/swap.img bs=1G count=4
mkswap /swap.img
swapon -a
grep SwapTotal /proc/meminfo

# поиск файла по имени
find ~/ -type f -name 'file_name'

# поиск регулярными выражениями
find -regextype egrep -regex '.*/[a-z]{3}.*[^i]$'

# маунт папки в требуемую директорию
mount --bind /source /target
 
# отобразить пользователей \ группы
users | groups

# отобразить последние Х строк файла
tail -n X file_name

# создать символическую ссылку
ln -s /source /target

# изменить владельца директории
chown -R $USER:group /directory

# задать требуемое (тут - 774) разрешение на директорию
chmod -R 774 /directory

# работа с пользователем в ubuntu
sudo adduser username

# дать пользователю административные права
sudo usermod -aG sudo username

# удалить пользователя (вместе с его папкой)
sudo deluser --remove-home username

# посмотреть, сколько файлов в директории
ls | wc -l
```


## tmux cheatsheet
```shell script
# открыть новую сессию 
tmux new -s session_name

# показать все существующие сессии
tmux ls

# подключиться к существующей сессии
tmux a -t session_name

# убить сессию
tmux kill-session -t session_name

# сделать detach от сессии
ctrl+b d
```


## vim cheatsheet
```shell script
# удалить линии с a по b
:a,bd
 
# перейти к символу x
:goto x
 
# поиск по ключевому слову
:?keyword | :/keyword
 
# удалить строку
dd
```
