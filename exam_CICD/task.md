![image](https://user-images.githubusercontent.com/95025513/201987660-187deacb-18fd-4b9c-98a1-fb1badb71b37.png)

## Задача:
### 1.	Форкнуть GitHub репозиторий (web-приложение) по адресу https://github.com/merovigen/student-exam2 в личный GitHub репозиторий.
> Переходим в нужный рипозиторий и справа сверху жмём кнопку `Fork`. Далее идём в свой личный репозиторий и проверяем рузультат `https://github.com/studentNV/student-exam2`

![image](https://user-images.githubusercontent.com/95025513/164936436-28956ccf-1778-4cca-9e3c-589090110f1e.png)

> После этого репозиторий `student-exam2` появляется у нас в списке.

![image](https://user-images.githubusercontent.com/95025513/164936467-bca5a0c9-bf02-4106-ad35-217a530f2955.png)

### 2.	Ознакомиться с документацией к проекту и с кодом приложения. Разобраться как запускать тесты приложения и само приложение. Работающее приложение должно выводить страницу в браузере с калькулятором на JS и хостнеймом сервера, на котором оно запущено.
> В тестовом режиме (пробном) запустил приложения по инструкции из репозитория с помощью следующих команд.
```bash
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
```
> Зашел на `web` интерфейс и протестировал правильность работы программы. Далее запустил `unit` тесты по инструкции из того же репозитория.

```bash
cd student-exam2
. venv/bin/activate
pip install -e '.[test]'
coverage run -m pytest
coverage report
```
> Все заявленные функции работают корректно. `Web` приложение отображается правильно, юнит тесты отрабатывают.

### 3.	Написать Dockerfile для web-приложения. Образ, собранный из этого Dockerfile, должен содержать все файлы/утилиты/библиотеки, необходимые для работы web-приложения, а также само приложение. При запуске контейнера на основе данного образа, должно запускаться web-приложение внутри контейнера с экспортированным на host-машину портом, то есть команда `curl 127.0.0.1:[PORT]`, выполненная с host-машины (centos) должна возвращать такой же результат, как и в п.2.

> Для начала необходимо установить и запустить докер перед написанием докер файла.
```bash
sudo yum update
sudo yum install yum-utils devicemapper-persistent-data -y
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker-ce
sudo systemctl start docker && sudo systemctl enable docker
sudo systemctl status docker
```
> `Dockerfile` ->  https://github.com/studentNV/chapter-2/blob/main/exam/dockerfile_centos_web/Dockerfile  
> Для сборки и запуска докер файла были использованы следующие команды:
```bash
sudo docker build -t centos_web:web_app .
sudo docker run --name centos_web -p 5050:5000 -d centos_web:web_
```

### 4.	Запустить и выполнить первоначальную настройку Jenkins, работающего внутри docker-контейнера. Для выполнения данного пункта можно воспользоваться официальным docker образом Jenkins.

> Для запуска `Jenkins` используем следующую команду.
```bash
sudo docker run -d -p 8080:8080 -p 50000:50000 --name jenkins_exam jenkins/jenkins:latest
```
> После не продолжительного ожидания видим окно с полем, в которое необходимо ввести пароль администратора. С помощью команды представленной ниже получаем пароль и вводим в поле `Administrator password`.
```bash
sudo docker exec -it jenkins_exam cat /var/jenkins_home/secrets/initialAdminPassword
```
![image](https://user-images.githubusercontent.com/95025513/164937897-ba4dee83-99d0-492c-a6a9-30e3febe3602.png)
> Далее выбираем стандартную установку с предложенными плагинами и ждем окончания.  

![image](https://user-images.githubusercontent.com/95025513/164938408-fc99f0b7-c18a-4c0b-9680-b1858e63124c.png) 
> После успешной установки всех предложенных плагинов создаем первого пользователя с правами администратора.  

![image](https://user-images.githubusercontent.com/95025513/164938641-e6311f4a-0c24-42d7-8c9b-4f2919b97824.png)
> На этом первоначальная настройка заканчивается.

### 5.	Создать пользователей admin и developer, включить matrix access и настроить права доступа:      
•	admin – полные права на все     
•	developer:      
i.	Overall: read       
ii.	Job: build, cancel, discover, read, workspace       
iii.	Agent: build  
> Создаем пользователей и предоставляем им права по заданию.

![image](https://user-images.githubusercontent.com/95025513/162625705-7f6626c0-c8aa-4359-96e1-78db47dd85b5.png)

### 6.	Установить плагин Ansible и настроить в Global Tool Configuration путь до директории с ansible который установлен на агенте (подробнее в п.7).
> Устанавливаем плагин `Ansible` и после перезагрузки `Jenkins` указываем путь в глобальных настройках.

![image](https://user-images.githubusercontent.com/95025513/164938834-4f8f3217-2a74-467e-9500-7c9c0fc731cd.png)

### 7.	Для сборки и тестирования web-приложения нужно использовать не Jenkins-мастер, установленный и настроенный ранее, а специальный Jenkins-агент, работающий в отдельном docker-контейнере. Для начала нужно подготовить образ этого агента. Для этого требуется написать Dockerfile для Jenkins-агента. В образе должны присутствовать: java8, ansible, python3, пользователь Jenkins и SSH-ключ для авторизации Jenkins-мастера. Способ подключения агента – SSH.
> `Dockerfile` -> https://github.com/studentNV/chapter-2/blob/main/exam/jenkins_agent_ansible/Dockerfile  
> Для сборки и запуска докер файла были использованы следующие команды:
```bash
sudo docker build -t studentnv/exam2:jenkins_agent .
sudo docker run --privileged=true --name jenkins_agent -v /var/run/docker.sock:/var/run/docker.sock  -d studentnv/exam2:jenkins_agent
```
### 8.	Зарегистрировать аккаунт на https://hub.docker.com/ и создать приватный репозиторий, в котором должны храниться созданные в п.3 и п.7 образы.
> После успешной регистрации необходимо войти на хосте под своей учетной записью `Docker hub`.
```bash
sudo docker login
```
> После этого выполняем следующие команды что бы запушить наши образы.
```bash
sudo docker tag dfbe216edce3 studentnv/exam2:web_app
sudo docker push studentnv/exam2:web_app
sudo docker tag c97aa7d15813 studentnv/exam2:jenkins_agent
sudo docker push studentnv/exam2:jenkins_agent
```
> Далее проверяем результат.  

![image](https://user-images.githubusercontent.com/95025513/164939988-04b7797f-1eb9-48c9-9b61-416df7f4ba88.png)

### 9.	Добавить Jenkins credentials (SSH Username with private key) для авторизации на агенте.
> Для того что бы добавить `Jenkins credentials` нужно получить приватный ключ на агенте воспользуемся командой.
```bash
sudo docker exec -it jenkins_agent cat /var/lib/Jenkins/.ssh/id_rsa
```
> Теперь ничего не мешает добавить credential на Jenkins.

![image](https://user-images.githubusercontent.com/95025513/164940486-bffca888-1496-41fe-9c49-656dd064a461.png)

### 10.	Запустить контейнер для Jenkins агента и подключить агента к мастеру Jenkins.
> В настройках `Jenkins` добавляем `agent` выбирая `credential` который создавали выше.

![image](https://user-images.githubusercontent.com/95025513/164940738-4f6c6052-74e7-431b-9300-2962c99cb4e6.png)
> Агент добавился корректно.

![image](https://user-images.githubusercontent.com/95025513/164941098-24b19ec2-f295-4fc5-a7ee-9ed9dbbccaec.png)

### 11.	Запретить сборки на мастере Jenkins (настроить число executors на мастере равным 0)
> Заходим в настройки мастера `Jenkins` и меняем колличество `executors`

![image](https://user-images.githubusercontent.com/95025513/164941198-1a44a73b-3554-4a31-a5f8-e8afcf3b5520.png)

### 12.	Создать Jenkins pipeline для CI:  
•	Jenkinsfile должен браться из репозитория с web-приложением   
•	Jenkins должен запускать job для каждого нового коммита в master ветку – для этого нужно включить триггер на SCM Poll и поставить ежеминутную проверку    
•	В Jenkinsfile должно быть:    
i.	Запуск python тестов  
ii.	Сборка docker image   
iii.	Аутентификация в docker hub (docker login, логин и пароль должны браться из credentials Jenkins’а)    
iv.	Выгрузка image на docker hub (docker push)    

> Создаем `credential` для `GitHub`.

![image](https://user-images.githubusercontent.com/95025513/164941459-194e9606-7b56-4fd9-a5be-c1a9916334d9.png)
![image](https://user-images.githubusercontent.com/95025513/164941947-5a3f99d9-e157-4ed0-a833-27161d778253.png)
> Создаем `credential` для `DockerHub`.

![image](https://user-images.githubusercontent.com/95025513/164941815-7380b4b2-4c43-45f3-a91b-3f26a53f4fd4.png)
> Создаем `pipeline` и настраиваем его по заданию.

![image](https://user-images.githubusercontent.com/95025513/164942079-9d37f179-256a-4f4c-bd3f-42bbdb7f4c33.png)
> При выборе репозитария используем наш созданный `credential`.

![image](https://user-images.githubusercontent.com/95025513/164942171-d32a7d96-0380-46c8-901f-d5f4bf30c77d.png)
![image](https://user-images.githubusercontent.com/95025513/164942198-8f3eec4e-9320-4e4e-95c5-aeb4b9cf7ffa.png)
> `Pipeline` ->  https://github.com/studentNV/student-exam2/blob/master/Jenkinsfile

### 13. Создать Git репозиторий с Ansible. Добавить в него список используемых серверов в inventory, роль для установки вашего web-приложение и роль для установки балансировщика на базе Nginx.
•	Роль для web-приложения должна устанавливать docker, скачивать образ web-приложения и запускать контейнер на определенном порту.  
•	Роль для Nginx должна устанавливать docker, скачивать образ Nginx, генерировать конфигурационный файл Nginx из Jinja2 шаблона для балансировки ваших web-приложений.  
> Было принято решение использовать отдельную виртуальную машину для `CD`. На ней был создать пользователь `Jenkins` и закинут ключ для работы `Ansible`, так же она была обновлена и на ней был установлен `Docker`. Для настройки виртульаной машины для CD выполняем следующие команды.
```bash
sudo docker exec -u root -it jenkins_agent sudo su -l Jenkins -c "ssh-keyscan 192.168.100.72 >> ~/.ssh/known_hosts"
sudo docker exec -u Jenkins -it jenkins_agent  ansible all -i '192.168.100.72,' -k -u root -m ansible.builtin.user -a "name=Jenkins"
sudo docker exec -u Jenkins -it jenkins_agent ansible all -i '192.168.100.72,' -k -u root -m file -a "path=/home/Jenkins/.ssh owner=Jenkins group=Jenkins state=directory"
sudo docker exec -u Jenkins -it jenkins_agent ansible all -i '192.168.100.72,' -k -u root -m copy -a "src=/var/lib/Jenkins/.ssh/id_rsa.pub mode=400 owner=Jenkins group=Jenkins dest=/home/Jenkins/.ssh/authorized_keys"
sudo docker exec -u Jenkins -it jenkins_agent ansible all -i '192.168.100.72,' -k -u root -m user -a "name=Jenkins group=wheel createhome=yes"
```
> `Ansible` -> https://github.com/studentNV/ansible-exam2

### 14. Создать Jenkins pipeline для CD:
•	Jenkinsfile должен браться из репозитория с ansible 
•	В Jenkinsfile должно быть 
i.	Запуск плейбука ansible для деплоя  
ii.	Запуск интеграционных тестов (достаточно обычного http реквеста до web сервера и проверка что он возвращает статус 200) 
> Создаем новый pipeline и настраиваем его так же, как и в пункте `12`. Единственные изменения, меняем ссылку на репозиторий и название основной ветки.

![image](https://user-images.githubusercontent.com/95025513/164942585-e1d4b169-7130-46a2-be82-a4318784d440.png)
> Так как наш файл с переменными для `web` приложения зашифрован, нужно будет его расшифровывать для этого создаем ещё один `credential`.

![image](https://user-images.githubusercontent.com/95025513/164942589-91991d2b-d823-4070-9e34-d6cc2e33c46f.png)
![image](https://user-images.githubusercontent.com/95025513/164942591-a18d521c-9349-4ef2-8967-365d36b9a8bd.png)
> Для проверки работы URL адреса устанавливаем на Jenkins плагин http Request.   
> `Pipeline` -> https://github.com/studentNV/ansible-exam2/blob/main/Jenkinsfile

### 15. Проверить работоспособность pipeline для CI и CD. Проверить работоспособность приложения и балансировщика.
> Изменяем файл `Jenkinsfile` в репозитории с ждем пока наш piptline для `CI` начнет работать!

![image](https://user-images.githubusercontent.com/95025513/164942624-1c65dc0d-40f4-4ed6-8c17-5f8342e40e02.png)
> Смотрим что тесты прошли корректно.

![image](https://user-images.githubusercontent.com/95025513/164942628-22cdd290-2a2a-4a64-8e13-8299ab2de3b9.png)
> Заходим на `Docker Hub` и смотрим как запушился наш образ.

![image](https://user-images.githubusercontent.com/95025513/164942635-468f0b72-76a9-4ed3-8148-d48422ed9d7e.png)
> Теперь смотрим что там с `CI`.

![image](https://user-images.githubusercontent.com/95025513/164942642-87f9ccd9-927a-495a-ba1d-53c76698f16b.png)

> Тут тоже все отлично! Заходим на адрес http://192.168.100.72:8080/ и проверяем результат.

![image](https://user-images.githubusercontent.com/95025513/164942651-7f6d2118-7476-4e84-a785-20b98bbbb6b3.png)

> Обновляя страницу видим разный `hostname` так как наши приложения запущены в докерах, мы видим `Dokcer ID` запущенных докеров.

![image](https://user-images.githubusercontent.com/95025513/164942658-0d987966-58ea-4750-ac41-34acca2bb9e7.png)
![image](https://user-images.githubusercontent.com/95025513/164942659-1dcdc8e1-41bf-4642-8303-c839cd387085.png)

> Заходим на хост и проверяем.

![image](https://user-images.githubusercontent.com/95025513/164942665-e5b5901e-c36f-4cf3-8614-3e14783d1d0b.png)

Всё отрабатывает без проблем
# Недостатки реализации
> В контейнере для агента `Jenkins` в конечном итоге намешено много всего, но идея была в том что бы сделать образ как можно более готовым к рабочему для поставленной задачи.
