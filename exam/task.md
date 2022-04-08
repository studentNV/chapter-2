## Задача:
1.	Форкнуть GitHub репозиторий (web-приложение) по адресу https://github.com/merovigen/student-exam2 в личный GitHub репозиторий.
> Переходим в нужный рипозиторий и справа сверху жмём кнопку `Fork`. Далее идём в свой личный репозиторий и проверяем рузультат `https://github.com/studentNV/student-exam2`
2.	Ознакомиться с документацией к проекту и с кодом приложения. Разобраться как запускать тесты приложения и само приложение. Работающее приложение должно выводить страницу в браузере с калькулятором на JS и хостнеймом сервера, на котором оно запущено.
> Для запуска приложения были выполненны следующие задачи
```bash
sudo yum update -y
sudo yum install git -y
cd cd student-exam2/
git clone https://github.com/studentNV/student-exam2.git
cd student-exam2
sudo yum install python3 -y
python3 -m venv venv
. venv/bin/activate
pip install -e .
export FLASK_APP=js_example
flask run --host=0.0.0.0
```
3.	Написать Dockerfile для web-приложения. Образ, собранный из этого Dockerfile, должен содержать все файлы/утилиты/библиотеки, необходимые для работы web-приложения, а также само приложение. При запуске контейнера на основе данного образа, должно запускаться web-приложение внутри контейнера с экспортированным на host-машину портом, то есть команда `curl 127.0.0.1:[PORT]`, выполненная с host-машины (centos) должна возвращать такой же результат, как и в п.2.
> ========Install Docker=========   
> sudo yum update   
> sudo yum install yum-utils devicemapper-persistent-data -y    
> sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo    
> sudo yum install -y docker-ce   
> sudo systemctl start docker && sudo systemctl enable docker   
> sudo systemctl status docker    
> ========Start Docker========= 
> sudo docker build -t docker_exam2_web_app:1.6 .   
> sudo docker run -p 5000:5000 -d docker_exam2_web_app:1.6    
```bash
FROM centos:7
RUN	yum update -y && \
	yum install git -y && \
	git clone https://github.com/studentNV/student-exam2.git && \
	yum install python3 -y && \
	python3 -m venv student-exam2/venv && \
	student-exam2/venv/bin/pip install --upgrade pip && \
	student-exam2/venv/bin/pip install --upgrade pip && \
	student-exam2/venv/bin/pip install -e student-exam2 && \
RUN pip3 install flask
ENV  FLASK_APP=student-exam2/js_example
ENV  LC_ALL=en_US.utf-8
RUN touch /student-exam2/start-web.sh && \
	echo "#!/bin/bash" >> /student-exam2/start-web.sh && \
	echo "/usr/bin/python3 -m flask run --host=0.0.0.0" >> /student-exam2/start-web.sh && \
	echo "while :" >> /student-exam2/start-web.sh && \
	echo "do" >> /student-exam2/start-web.sh && \
	echo "sleep 10" >> /student-exam2/start-web.sh && \
	echo "done" >> /student-exam2/start-web.sh
ENTRYPOINT ["/bin/bash", "/student-exam2/start-web.sh"]
```
