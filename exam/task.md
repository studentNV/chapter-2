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
