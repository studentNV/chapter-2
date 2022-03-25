# Lesson 2.3

## Home work 2.3

1. Создать 3 ВМ
> vm1-ansible   192.168.100.101  
> vm2-ansible   192.168.100.102

2. На одной из них установить ansible и создать отдельного пользователя, из-под которого он будет запускаться
> установка `ansible`
```bash
sudo yum -y update
sudo yum -y install epel-release
sudo yum -y install ansible
ansible --version
```
> создание нового пользователя `nvAnsible` на `vm1`
```bash
sudo useradd nvAnsible
sudo passwd nvAnsible
sudo usermod -aG wheel nvAnsible
sudo su nvAnsible
```

3. Используя ansible ad-hoc:
> содержимое `invetory_ad_hac.yaml` находится тут -> https://github.com/studentNV/chapter-2/blob/lesson33-36/33-36lesson/playbook/invetory_ad_hac.yaml

- создать такого же пользователя на остальных машинах
```bash
ansible all -i invetory_ad_hac.yaml -k -u root -m ansible.builtin.user -a "name=nvAnsible"
```

- подложить ему ssh-ключи
> Создание пары ключей
```bash
[nvAnsible@localhost hw]$ ssh-keygen

```
> перекидаваем публичный ключ
```bash
ansible all -i invetory_ad_hac.yaml -k -u root -m file -a "path=/home/nvAnsible/.ssh owner=nvAnsible group=nvAnsible state=directory" -b
ansible all -i invetory_ad_hac.yaml -k -u root -m copy -a "src=/home/nvAnsible/.ssh/id_rsa.pub mode=400 owner=nvAnsible group=nvAnsible dest=/home/nvAnsible/.ssh/authorized_keys"
```

- дать возможность использовать sudo (помните о том, что редактирование /etc/sudoers не через visudo - плохая идея)
> добавляем пользователя в группу администраторов `wheel`
> не нашел каким образом редактировать файл `/etc/sudoers` через `visudo` с помощью `Ansible`, если подскажите буду благодарен (выкрутился по другому)
```bash
ansible all -i invetory_ad_hac.yaml -k -u root -m user -a "name=nvAnsible group=wheel createhome=yes"
ansible all -i invetory_ad_hac.yaml -k -u root -m shell -a "echo 'nvAnsible  ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/nvAnsible"
```
4. написать плейбук, со ролями, которые позволят:
- создать пользователя из п.2; обновить все пакеты в системе
> ссылка на task -> https://github.com/studentNV/chapter-2/tree/lesson33-36/33-36lesson/playbook/roles/4_1_AddUser_Update
```bash
ansible-playbook site.yaml -i inventory.yaml
```

- установить ntp-сервер и заменить его стандартный конфиг на кастомный (примеры можно поискать в сети)
> ссылка на task -> https://github.com/studentNV/chapter-2/tree/lesson33-36/33-36lesson/playbook/roles/4_2_Install_FTP
```bash
ansible-playbook site.yaml -i inventory.yaml
```
- установить mysql-сервер, создать пользователя БД и саму базу данных
> ссылка на task -> https://github.com/studentNV/chapter-2/tree/lesson33-36/33-36lesson/playbook/roles/4_3_Install_MYSQL
```bash
ansible-playbook site.yaml -i inventory.yaml
```
> Заходим на сервера и смотреим что получилось
```bash
mysql> SELECT user FROM mysql.user;
+-----------+
| user      |
+-----------+
| root      |
| root      |
|           |
| nvAnsible |
| root      |
|           |
| root      |
+-----------+
7 rows in set (0.00 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test_DB            |
+--------------------+
4 rows in set (0.00 sec)

```

- * установить nginx и настроить его так, чтобы он обслуживал сайт example.com; содержимое сайта должно лежать в /var/www-data/example.com и представлять из себя любой валидный html-документ
- * установить docker в соответствии с инструкцией https://docs.docker.com/engine/install/centos/
