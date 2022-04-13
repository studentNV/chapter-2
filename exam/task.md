
## Задача:
1.	Форкнуть GitHub репозиторий (web-приложение) по адресу https://github.com/merovigen/student-exam2 в личный GitHub репозиторий.
> Переходим в нужный рипозиторий и справа сверху жмём кнопку `Fork`. Далее идём в свой личный репозиторий и проверяем рузультат `https://github.com/studentNV/student-exam2`
2.	Ознакомиться с документацией к проекту и с кодом приложения. Разобраться как запускать тесты приложения и само приложение. Работающее приложение должно выводить страницу в браузере с калькулятором на JS и хостнеймом сервера, на котором оно запущено.
sudo systemctl stop firewalld
```bash
========Install Web=========
sudo yum update -y	
sudo yum install git -y	
git clone https://github.com/studentNV/student-exam2.git
cd student-exam2		
sudo yum install python3 -y	
python3 -m venv venv	
sudo firewall-cmd --add-port=5000/tcp	
sudo firewall-cmd --runtime-to-permanent	
sudo firewall-cmd --reload	
sudo firewall-cmd --list-all	
. venv/bin/activate	
pip install --upgrade pip		
pip install -e .	
export FLASK_APP=js_example	
flask run --host=0.0.0.0
========Run Web=========
cd student-exam2
. venv/bin/activate
export FLASK_APP=js_example
flask run --host=0.0.0.0
========Start Tests Web=========
cd student-exam2
. venv/bin/activate
pip install -e '.[test]'
coverage run -m pytest
coverage report
```
3.	Написать Dockerfile для web-приложения. Образ, собранный из этого Dockerfile, должен содержать все файлы/утилиты/библиотеки, необходимые для работы web-приложения, а также само приложение. При запуске контейнера на основе данного образа, должно запускаться web-приложение внутри контейнера с экспортированным на host-машину портом, то есть команда `curl 127.0.0.1:[PORT]`, выполненная с host-машины (centos) должна возвращать такой же результат, как и в п.2.
```bash
========Install Docker=========
sudo yum update
sudo yum install yum-utils devicemapper-persistent-data -y
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker-ce
sudo systemctl start docker && sudo systemctl enable docker
sudo systemctl status docker
========Start Docker=========
sudo docker build -t centos_web:web_app .
sudo docker run --name centos_web -p 5050:5000 -d centos_web:web_
sudo docker build -t slim_web:1.6 .
sudo docker run -p 5000:5000 -d docker_exam2_slim_web:1.6
```
> Docker files:	
> dockerfile_centos_web -> https://github.com/studentNV/chapter-2/blob/main/exam/dockerfile_centos_web/Dockerfile   
> dockerfile_slim_web -> https://github.com/studentNV/chapter-2/blob/main/exam/dockerfile_slim_web/Dockerfile  
4.	Запустить и выполнить первоначальную настройку Jenkins, работающего внутри docker-контейнера. Для выполнения данного пункта можно воспользоваться официальным docker образом Jenkins.
```bash
========Start docker Jenkins=========
sudo docker run -p 8080:8080 -p 50000:50000 --name jenkins_exam jenkins/jenkins:latest
sudo docker run -p 8080:8080 -p 50000:50000 --name jenkins_exam -v /home/sit/docker_jenkins:/var/jenkins_home jenkins/jenkins:latest
sudo docker start jenkins_exam
-p 5000:5000 required to attach slave servers; port 50000 is used to communicate between master and slaves
created user: sitis
password: 123
========Experiment start docker jenkins with docker web=========
ssudo docker run --name centos_web -p 5050:5000 -d centos_web:web_app
```
5.	Создать пользователей admin и developer, включить matrix access и настроить права доступа:      
•	admin – полные права на все     
•	developer:      
i.	Overall: read       
ii.	Job: build, cancel, discover, read, workspace       
iii.	Agent: build  

![image](https://user-images.githubusercontent.com/95025513/162625705-7f6626c0-c8aa-4359-96e1-78db47dd85b5.png)

6.	Установить плагин Ansible и настроить в Global Tool Configuration путь до директории с ansible который установлен на агенте (подробнее в п.7).
> После выполнения 10 пункта выполняем поставленную задачу

![image](https://user-images.githubusercontent.com/95025513/162733584-8988a0ea-0746-4ac6-832b-45dd4231c7af.png)

7.	Для сборки и тестирования web-приложения нужно использовать не Jenkins-мастер, установленный и настроенный ранее, а специальный Jenkins-агент, работающий в отдельном docker-контейнере. Для начала нужно подготовить образ этого агента. Для этого требуется написать Dockerfile для Jenkins-агента. В образе должны присутствовать: java8, ansible, python3, пользователь Jenkins и SSH-ключ для авторизации Jenkins-мастера. Способ подключения агента – SSH.
> `Dockerfile` -> https://github.com/studentNV/chapter-2/blob/main/exam/jenkins_agent_ansible/Dockerfile
```bash
sudo docker build -t jenkins_agent_ansible:jenkins_agent .
sudo docker run --privileged=true --name jenkins_agent -v /var/run/docker.sock:/var/run/docker.sock  -d studentnv/exam2:jenkins_agent
```
> Для получения ключа и IP адреса используемые команды, которые нам понадобяться при подключении аегнта
```bash
sudo docker exec -it jenkins_agent_ansible cat /var/lib/Jenkins/.ssh/id_rsa
sudo docker inspect jenkins_agent_ansible | grep IPAddress
```
8.	Зарегистрировать аккаунт на https://hub.docker.com/ и создать приватный репозиторий, в котором должны храниться созданные в п.3 и п.7 образы.
> `docker` из пунка 3
```bash
sudo docker build -t centos_web:web_app .
sudo docker run -p 5050:5000 -d centos_web:web_app
sudo docker commit centos_web studentnv/exam2:web_app
sudo docker push studentnv/exam2:web_app
```
> `docker` из пунка 7
```bash
sudo docker build -t jenkins_agent_ansible:jenkins_agent .
sudo docker run --name jenkins_agent_ansible -d jenkins_agent_ansible:jenkins_agent
sudo docker commit jenkins_agent_ansible studentnv/exam2:jenkins_agent
sudo docker push studentnv/exam2:jenkins_agent
```
> Dockerhub rep -> https://hub.docker.com/repository/docker/studentnv/exam2   

9.	Добавить Jenkins credentials (SSH Username with private key) для авторизации на агенте.
> При помощи команды `sudo docker exec -it jenkins_agent_ansible cat /var/lib/Jenkins/.ssh/id_rsa` получаем нужный нам привыйтный ключ и добавляем его на `jenkins`

![image](https://user-images.githubusercontent.com/95025513/162732107-7068e9c8-8f3e-44f8-a8de-683688afa500.png)

10.	Запустить контейнер для Jenkins агента и подключить агента к мастеру Jenkins.
> Получаем нужный `IP-addres` при помощи команды `sudo docker inspect jenkins_agent_ansible | grep IPAddress` и подключаем агент, не забыв указать наш новосозданный `credentials`

![image](https://user-images.githubusercontent.com/95025513/162732972-f3fd9595-0187-4465-b5ba-4722d51f793d.png)
> Смотрим лог и наслаждаемся результатом

![image](https://user-images.githubusercontent.com/95025513/162733100-1a343cbe-d069-4a25-8a0a-c79df832dcf6.png)
![image](https://user-images.githubusercontent.com/95025513/162733148-6b976105-8b4e-4db7-9c08-d593a587d281.png)

11.	Запретить сборки на мастере Jenkins (настроить число executors на мастере равным 0)
> Заходим в настройки мастере `Jenkins` и меняем колличество `executors`

![image](https://user-images.githubusercontent.com/95025513/162733929-cf0b3765-cc7e-45fc-b1ce-b4ad4b99bcb3.png)
![image](https://user-images.githubusercontent.com/95025513/162734040-a43b42fe-f5f1-4245-bbe3-9a619dd2f882.png)

12.	Создать Jenkins pipeline для CI:
•	Jenkinsfile должен браться из репозитория с web-приложением
•	Jenkins должен запускать job для каждого нового коммита в master ветку – для этого нужно включить триггер на SCM Poll и поставить ежеминутную проверку
•	В Jenkinsfile должно быть:
i.	Запуск python тестов
ii.	Сборка docker image
iii.	Аутентификация в docker hub (docker login, логин и пароль должны браться из credentials Jenkins’а)
iv.	Выгрузка image на docker hub (docker push)

> подключаем к нашему созданному `pipeline` систему контроля версий `Git` перед этим создаем `Credential` для подключения  
![image](https://user-images.githubusercontent.com/95025513/163123373-4f60e8e0-09c7-4188-82ce-646a5d7c97f2.png)

>  выставляем `Build Truggers` в `Pol CSM` и маской задаем интеревал  
![image](https://user-images.githubusercontent.com/95025513/163123791-d51f1ffa-7ea4-48ba-967f-f58ee2f7c62a.png)

> Что бы работала аутентификация в `dockerhub` серез `credentials Jenkins’а` нужно его создать
![image](https://user-images.githubusercontent.com/95025513/163124052-58b7d980-39fa-4c68-8abe-ca50be396028.png)
> Затем через переменную в `pipeline` передаём наши данные для входа в `dockerhub`
> `pipeline` -> https://github.com/studentNV/student-exam2/blob/master/Jenkinsfile


