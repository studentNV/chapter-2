# Lesson 2.1

## Home work 2.1

ДЗ состоит в создании контейнеров, сконфигурированных по аналогии с тем, как это было необходимо сделать для виртуальных машин в экзаменационном задании по Hadoop кластеру. 
Вам потребуется:
1.	Создать аккаунт на Docker Hub с публичным репозиторием.

2.	Создать Dockerfiles для сборки образов headnode и worker.  Для хранения файлов Namenode и Datanode сервиса HDFS, а также Nodemanager сервиса YARN следует использовать Docker volumes.  Также поменяется способ запуска процессов, они должны стартовать при запуске контейнеров.

3.	Собрать образа и запушить в репозиторий.

4.	Предоставить два Dockerfiles и имена образов в формате <your account>/<image name>:<tag>, которые можно запустить и проверить, что сервисы доступны и работают. При этом предполагается, что проверяющий не знает, что куда монтировать volumes и какие порты необходимо пробрасывать для корректной работы сервисов.

5.	* Создать docker-compose.yml файл, запускающий оба образа. 

#### 1) Первый докер файл `vm1-headnode` => https://github.com/studentNV/chapter-2/blob/lesson21-24/21-24esson/vm1-headnode/Dockerfile
#### 2) Второй докер файл `vm1-worker`=> https://github.com/studentNV/chapter-2/blob/lesson21-24/21-24esson/vm1-worker/Dockerfile
#### 3) Первый докер файл был собран с помощью следующей команды
```bash
sudo docker build -t  docker_headnode:1.6 .
```
#### 4) Второй докер файл был собран с помощью следующей команды
```bash
sudo docker build -t  docker_worker:1.6 .
```
#### 5) Перед запуском образов необходимо создать `VOLUMES` и сеть для докеров с помощью команд представленных ниже
```bash
sudo docker volume create vm1-headnode
sudo docker volume create vm2-worker
sudo docker network create -d bridge net-for-hadoop
```
#### 6) Первый докер образ необходимо запускать с помощью следующей команды
```bash
sudo docker run --name vm1-headnode -v vm1-headnode:/opt/hadoop  --network=net-for-hadoop -p 9870:9870 -p 8088:8088 --add-host vm1-headnode:0.0.0.0 -d docker_headnode:1.6
```
#### 7) Перед запуском воторого докера необходимо посмотреть какой у певого ip с помощью команды
```bash
sudo docker inspect vm1-headnode | grep  IPAddress    
```
#### 8) Второй докер образ необходимо запускать с помощью следующей команды (вместо моего ip `172.18.0.2` необходимо вводить ip который вывелся на 7 этапе)
```bash
sudo docker run --name vm2-worker -v vm2-worker:/opt/hadoop --network=net-for-hadoop --add-host vm1-headnode:172.18.0.2 -d docker_worker:1.6
```
#### После всего проделанного можно проверять наши `VOLUMES` с помощью команд
```bash
sudo ls /var/lib/docker/volumes/vm1-headnode/_data/
sudo ls /var/lib/docker/volumes/vm2-worker/_data/
```
#### Можно открыть браузер у себя на хостовой машине и в строке URL прописать `127.0.0.1:9870` `127.0.0.1:8088` и увидеть корректную работу
#### По поводу сети, я пытался делать через `--link` докеры друг друга видели даже корректно отрабатывал `curl` но связи через `hadoop` не бьло

#### Информация Docker Hub 
```bash
studentnv/docker_headnode:1.6  
studentnv/docker_worker:1.6
```
#### Зная себя на всякий случай оставлю это здесь
```bash
https://hub.docker.com/repository/docker/studentnv/docker_headnode
https://hub.docker.com/repository/docker/studentnv/docker_worker
```
#### 9) docker-compose
> после запуска `docker-compose` создасться сеть и два `volumes`
```bash
net-for-hadoop
compose_data-volume-headnode
compose_data-volume-worker
```
> в папке с файлом `docker-compose.yml` прописываем данную строку
```bash
docker-compose up -d
```
> Содержимое файла `docker-compose.yml` => https://github.com/studentNV/chapter-2/blob/lesson21-24/21-24esson/compose/docker-compose.yml

> после запуска `docker-compose` можно проверять наши `volume` с помощью команд:
```bash
ls /var/lib/docker/volumes/compose_data-volume-headnode/_data/hadoop/
ls /var/lib/docker/volumes/compose_data-volume-worker/_data/hadoop/
```
### p.s. Докер файлы очень плохо написаны, но "причесать" их не было времени, понимаю что много личшнего таких как пользователи и директории.
