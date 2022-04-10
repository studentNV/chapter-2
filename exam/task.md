
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
sudo docker build -t docker_exam2_centos_web:1.6 .
sudo docker run -p 5000:5000 -d docker_exam2_centos_web:1.6
sudo docker build -t docker_exam2_slim_web:1.6 .
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
sudo docker run -p 5050:5000 -d docker_exam2_slim_web:1.6
```
5.	Создать пользователей admin и developer, включить matrix access и настроить права доступа:      
•	admin – полные права на все     
•	developer:      
i.	Overall: read       
ii.	Job: build, cancel, discover, read, workspace       
iii.	Agent: build  

![image](https://user-images.githubusercontent.com/95025513/162625705-7f6626c0-c8aa-4359-96e1-78db47dd85b5.png)

