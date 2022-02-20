# Lesson 2.1

## Home work 2.1

ДЗ состоит в создании контейнеров, сконфигурированных по аналогии с тем, как это было необходимо сделать для виртуальных машин в экзаменационном задании по Hadoop кластеру. 
Вам потребуется:
1.	Создать аккаунт на Docker Hub с публичным репозиторием.

2.	Создать Dockerfiles для сборки образов headnode и worker.  Для хранения файлов Namenode и Datanode сервиса HDFS, а также Nodemanager сервиса YARN следует использовать Docker volumes.  Также поменяется способ запуска процессов, они должны стартовать при запуске контейнеров.

3.	Собрать образа и запушить в репозиторий.

4.	Предоставить два Dockerfiles и имена образов в формате <your account>/<image name>:<tag>, которые можно запустить и проверить, что сервисы доступны и работают. При этом предполагается, что проверяющий не знает, что куда монтировать volumes и какие порты необходимо пробрасывать для корректной работы сервисов.

5.	* Создать docker-compose.yml файл, запускающий оба образа. 

#### 1) Первый докер файл `vm1-headnode`
```bash
FROM centos:7
RUN yum install java-1.8.0-openjdk -y && \
    yum install wget -y && \
    wget https://archive.apache.org/dist/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz && \
    mkdir /opt/hadoop-3.1.2/ && \
    tar -xvf  hadoop-3.1.2.tar.gz -C /opt/hadoop-3.1.2/ && \
    rm hadoop-3.1.2.tar.gz && \
    useradd hadoop && useradd yarn && useradd hdfs && \
    usermod -a -G hadoop hdfs && \
    usermod -a -G hadoop yarn
RUN mkdir -p /opt/hadoop/namenode-dir /opt/hadoop/namenode-dir && \
    chown hdfs:hadoop /opt/hadoop/namenode-dir /opt/hadoop/namenode-dir
RUN mkdir -p /usr/local/hadoop/current/ && \
    ln -s /opt/hadoop-3.1.2/* /usr/local/hadoop/current/
RUN yum install wget -y && \
    wget https://gist.githubusercontent.com/rdaadr/2f42f248f02aeda18105805493bb0e9b/raw/6303e424373b3459bcf3720b253c01373666fe7c/hadoop-env.sh -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh  && \
    sed -i 's|"%PATH_TO_OPENJDK8_INSTALLATION%"|/usr/lib/jvm/jre-1.8.0-openjdk|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh && \
    sed -i 's|"%PATH_TO_HADOOP_INSTALLATION"|/usr/local/hadoop/current/hadoop-3.1.2/|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh && \
    sed -i 's|"%HADOOP_HEAP_SIZE%"|512M|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh && \
    wget https://gist.githubusercontent.com/rdaadr/64b9abd1700e15f04147ea48bc72b3c7/raw/2d416bf137cba81b107508153621ee548e2c877d/core-site.xml -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/core-site.xml && \
    sed -i 's|%HDFS_NAMENODE_HOSTNAME%|vm1-headnode|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/core-site.xml && \
    wget https://gist.githubusercontent.com/rdaadr/2bedf24fd2721bad276e416b57d63e38/raw/640ee95adafa31a70869b54767104b826964af48/hdfs-site.xml -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hdfs-site.xml && \
    sed -i 's|%NAMENODE_DIRS%|/opt/hadoop/namenode-dir,/opt/hadoop/namenode-dir|'  /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hdfs-site.xml && \
    sed -i 's|%DATANODE_DIRS%|/opt/hadoop/datanode-dir,/opt/hadoop/datanode-dir|'  /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hdfs-site.xml && \
    wget https://gist.githubusercontent.com/Stupnikov-NA/ba87c0072cd51aa85c9ee6334cc99158/raw/bda0f760878d97213196d634be9b53a089e796ea/yarn-site.xml -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml  && \
    sed -i 's|%YARN_RESOURCE_MANAGER_HOSTNAME%|vm1-headnode|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml && \
    sed -i 's|%NODE_MANAGER_LOCAL_DIR%|/opt/hadoop/nodemanager-local-dir,/opt/hadoop/nodemanager-local-dir|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml && \
    sed -i 's|%NODE_MANAGER_LOG_DIR%|/opt/hadoop/nodemanager-log-dir,/opt/hadoop/nodemanager-log-dir|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml

RUN mkdir /usr/local/hadoop/current/hadoop-3.1.2/logs && \
    chown -R :hadoop /usr/local/hadoop/current/hadoop-3.1.2/logs && \
    chmod -R g+wxr /usr/local/hadoop/current/hadoop-3.1.2/logs
    
RUN touch /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-namenode-resourcemanager.sh && \
    echo "#!/bin/bash" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-namenode-resourcemanager.sh && \
    echo "su -l hdfs -c \"/usr/local/hadoop/current/hadoop-3.1.2/bin/hdfs namenode -format cluster1\"" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-namenode-resourcemanager.sh && \
    echo "su -l hdfs -c \"/usr/local/hadoop/current/hadoop-3.1.2/bin/hdfs --daemon start namenode\"" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-namenode-resourcemanager.sh && \
    echo "su -l hdfs -c \"/usr/local/hadoop/current/hadoop-3.1.2/bin/yarn --daemon start resourcemanager\"" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-namenode-resourcemanager.sh && \
    echo "while :" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-namenode-resourcemanager.sh && \
    echo "do" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-namenode-resourcemanager.sh && \
    echo "sleep 10" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-namenode-resourcemanager.sh && \
    echo "done" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-namenode-resourcemanager.sh
    
ENTRYPOINT ["/bin/bash", "/usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-namenode-resourcemanager.sh"]
 
````
#### 2) Второй докер файл `vm1-worker`
```bash
FROM centos:7
RUN yum install java-1.8.0-openjdk -y && \
    yum install wget -y && \
    wget https://archive.apache.org/dist/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz && \
    mkdir /opt/hadoop-3.1.2/ && \
    tar -xvf  hadoop-3.1.2.tar.gz -C /opt/hadoop-3.1.2/ && \
    rm hadoop-3.1.2.tar.gz && \
    useradd hadoop && useradd yarn && useradd hdfs && \
    usermod -a -G hadoop hdfs && \
    usermod -a -G hadoop yarn
    
RUN mkdir -p /opt/hadoop/mount1/datanode-dir /opt/hadoop/mount2/datanode-dir && \
    chown hdfs:hadoop /opt/hadoop/mount1/datanode-dir/ /opt/hadoop/mount2/datanode-dir/
    
RUN mkdir -p /usr/local/hadoop/current/ && \
    ln -s /opt/hadoop-3.1.2/* /usr/local/hadoop/current/ && \
    mkdir -p /opt/hadoop/mount1/nodemanager-local-dir /opt/hadoop/mount2/nodemanager-local-dir /opt/hadoop/mount1/nodemanager-log-dir /opt/hadoop/mount2/nodemanager-log-dir && \
    chown yarn:hadoop /opt/hadoop/mount1/nodemanager-local-dir /opt/hadoop/mount2/nodemanager-local-dir /opt/hadoop/mount1/nodemanager-log-dir /opt/hadoop/mount2/nodemanager-log-dir
    
RUN yum install wget -y && \
    wget https://gist.githubusercontent.com/rdaadr/2f42f248f02aeda18105805493bb0e9b/raw/6303e424373b3459bcf3720b253c01373666fe7c/hadoop-env.sh -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh  && \
    sed -i 's|"%PATH_TO_OPENJDK8_INSTALLATION%"|/usr/lib/jvm/jre-1.8.0-openjdk|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh && \
    sed -i 's|"%PATH_TO_HADOOP_INSTALLATION"|/usr/local/hadoop/current/hadoop-3.1.2/|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh && \
    sed -i 's|"%HADOOP_HEAP_SIZE%"|512M|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh && \ 
    wget https://gist.githubusercontent.com/rdaadr/64b9abd1700e15f04147ea48bc72b3c7/raw/2d416bf137cba81b107508153621ee548e2c877d/core-site.xml -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/core-site.xml && \   
    sed -i 's|%HDFS_NAMENODE_HOSTNAME%|vm1-headnode|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/core-site.xml && \
    wget https://gist.githubusercontent.com/rdaadr/2bedf24fd2721bad276e416b57d63e38/raw/640ee95adafa31a70869b54767104b826964af48/hdfs-site.xml -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hdfs-site.xml && \
    sed -i 's|%NAMENODE_DIRS%|/opt/hadoop/mount1/namenode-dir,/opt/hadoop/mount2/namenode-dir|'  /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hdfs-site.xml && \
    sed -i 's|%DATANODE_DIRS%|/opt/hadoop/mount1/datanode-dir,/opt/hadoop/mount2/datanode-dir|'  /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hdfs-site.xml && \
    wget https://gist.githubusercontent.com/Stupnikov-NA/ba87c0072cd51aa85c9ee6334cc99158/raw/bda0f760878d97213196d634be9b53a089e796ea/yarn-site.xml -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml  && \
    sed -i 's|%YARN_RESOURCE_MANAGER_HOSTNAME%|vm1-headnode|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml && \
    sed -i 's|%NODE_MANAGER_LOCAL_DIR%|/opt/hadoop/mount1/nodemanager-local-dir,/opt/hadoopmount2/nodemanager-local-dir|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml && \
    sed -i 's|%NODE_MANAGER_LOG_DIR%|/opt/hadoop/mount1/nodemanager-log-dir,/opt/hadoop/mount2/nodemanager-log-dir|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml


RUN mkdir /usr/local/hadoop/current/hadoop-3.1.2/logs && \
    chown -R :hadoop /usr/local/hadoop/current/hadoop-3.1.2/logs && \
    chmod -R g+wxr /usr/local/hadoop/current/hadoop-3.1.2/logs 
    
RUN touch /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "#!/bin/bash" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "su -l hdfs -c \"/usr/local/hadoop/current/hadoop-3.1.2/bin/hdfs --daemon start datanode\"" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "su -l yarn -c \"/usr/local/hadoop/current/hadoop-3.1.2/bin/yarn --daemon start nodemanager\"" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh.sh && \
    echo "while :" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "do" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "sleep 10" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "done" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh
    
ENTRYPOINT ["/bin/bash", "/usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh"]
```
  
#### 3) Первый докер файл был собран с помощью следующей команды
```bash
sudo docker build -t  docker_headnode:1.6 .
```
#### 4) Второй докер файл был собран с помощью следующей команды
```bash
sudo docker build -t  docker_worker:1.6 .
```
#### 5) Перед запуском образов необходимо создать `VOLUMES` с помощью команд представленных ниже
```bash
sudo docker volume create vm1-headnode
sudo docker volume create vm2-worker
```
#### 6) Первый докер образ необходимо запускать с помощью следующей команды
```bash
sudo docker run --name vm1-headnode -v vm1-headnode:/opt/hadoop -p 9870:9870 -p 8088:8088 --add-host vm1-headnode:127.0.0.1 -d docker_headnode:1.6
```
#### 7) Второй докер образ необходимо запускать с помощью следующей команды
```bash
sudo docker run -v vm2-worker:/opt/hadoop --name vm2-worker --link vm1-headnode:vm1-headnode -d docker_worker:1.6
```
#### После всего проделанного можно проверять наши `VOLUMES` с помощью команд
```bash
sudo ls /var/lib/docker/volumes/vm1-headnode/_data/
sudo ls /var/lib/docker/volumes/vm2-worker/_data/
```
#### Можно открыть браузер у себя на хостовой машине и в строке URL прописать `127.0.0.1:9870` и увидеть корректную работу
#### Так же у меня возникла проблема с `resourcemanager` он ни в какую не захотел нормально работать, сам демон запускаеться без ошибок но веб-страничка ничего непоказывает, curl выдаёт следующее
```bash
[root@be71e50c69c0 /]# curl -vvv 127.0.0.1:8088 
* About to connect() to 127.0.0.1 port 8088 (#0) 
*   Trying 127.0.0.1... 
* Connected to 127.0.0.1 (127.0.0.1) port 8088 (#0) 
> GET / HTTP/1.1 
> User-Agent: curl/7.29.0 
> Host: 127.0.0.1:8088 
> Accept: */* 
> 
< HTTP/1.1 302 Found 
< Date: Sat, 19 Feb 2022 18:48:09 GMT 
< Cache-Control: no-cache 
< Expires: Sat, 19 Feb 2022 18:48:09 GMT 
< Date: Sat, 19 Feb 2022 18:48:09 GMT 
< Pragma: no-cache 
< Content-Type: text/plain;charset=utf-8 
< X-Frame-Options: SAMEORIGIN 
< Vary: Accept-Encoding 
< Location: http://127.0.0.1:8088/cluster 
< Content-Length: 0 
< 
* Connection #0 to host 127.0.0.1 left intact
```
####  И вторая проблема мне кажется тоже связана с некорректной работой `resourcemanager` нет правильного взаимодействия между докерами, хоть оба друг друга видят, а второй докер может делать curl `curl vm1-headnode:9870` и выводиться правильная информация. Если вы подскажите где ошибка я буду очень рад, потратил оооочень много времени, но так и не понял. (помимо ошибки в ДНК ничего не нашёл)

#### Информация Docker Hub 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
