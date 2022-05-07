# Lesson 2.5

## Home work 2.5

### Задание 1. Настройка Jenkins
> Вы просили все в архив кинуть, мне показалось что так более удобно, если что архив тут -> https://github.com/studentNV/chapter-2/blob/lesson39-40/39-40esson/screen.7z
1. Развернуть контроллер Jenkins, произведя его базовую настройку.
![image](https://user-images.githubusercontent.com/95025513/162426354-938eea60-bc15-4827-8877-39cab306c51e.png)

2. Проверить наличие, а при отсутствии произвести установку следующих плагинов:
    - GitHub Branch Source Plugin
    - Matrix Authorization Strategy Plugin

![image](https://user-images.githubusercontent.com/95025513/162426404-e7e862aa-0931-4551-9c80-50594b8662e8.png)
![image](https://user-images.githubusercontent.com/95025513/162426411-8d2bf1c8-b2d9-4069-9cc8-df0079e444c7.png)

3. Создать пользователя developer и, используя Project-based Matrix Authorization Strategy, настроить ему права доступа для запуска новых билдов. Для пользователя, созданного на этапе начальной настройки предоставить полные права.

![image](https://user-images.githubusercontent.com/95025513/162426460-64755363-161a-491e-b438-4d71b5990000.png)
![image](https://user-images.githubusercontent.com/95025513/162426471-e5d3a88b-f65f-414b-90d4-4909b59d09df.png)

4. Создать Pipeline и напиcать скрипт непосредственно в Jenkins, который будет выводить дату на контроллере Jenkins.

![image](https://user-images.githubusercontent.com/95025513/162426504-8bf0e77d-ebbf-48ce-9ee4-56846eef53b5.png)

5. Предоставить доступ пользователю developer права для конфигурирования только для этого пайплайна (проекта) и, войдя под пользователем developer, заменить вывод даты на вывод версии bash на контроллере. Проверить работу пайплайна.

![image](https://user-images.githubusercontent.com/95025513/162426530-e0b67025-fe96-40ed-b295-f5124cacb51b.png)
![image](https://user-images.githubusercontent.com/95025513/162426547-f318c2a8-5191-456e-bbaa-de8ab83ae669.png)
![image](https://user-images.githubusercontent.com/95025513/162426557-dde78da0-a325-4f08-ab0a-e9a6418c4a53.png)
![image](https://user-images.githubusercontent.com/95025513/162426567-de817610-b0fa-4826-b323-e18ab770ac06.png)
![image](https://user-images.githubusercontent.com/95025513/162426576-61c53b4e-ca5e-417b-8f3b-cda638083cd6.png)
![image](https://user-images.githubusercontent.com/95025513/162426582-99ee102c-6601-4a8f-8262-b45657e9ffca.png)


6. Развернуть агент Jenkins, настроить подключение к нему через ssh и назначить ему метки unittest и build.

![image](https://user-images.githubusercontent.com/95025513/162426637-4d22c045-8567-464d-b91f-c56a8beb13b4.png)
![image](https://user-images.githubusercontent.com/95025513/162426652-e5ee69ed-736c-479e-8739-21dcb43cbcd2.png)

7. Убрать все экзекьюторы с контроллера Jenkins.
> Не оверен что понял но экзекьют это вроде исполнять так что мы ведь pipelin исполняем

![image](https://user-images.githubusercontent.com/95025513/162426741-7c18ae67-6ee0-43aa-9803-5be0ccbfc10a.png)
![image](https://user-images.githubusercontent.com/95025513/162426758-88790e7f-dbaf-493e-9c7a-be9bffd02b52.png)


### Задание 2. Jenkinsfile
1. Форкнуть репозиторий https://github.com/vauboy/jenkins-lesson.
> форкнутый репозиторий -> https://github.com/studentNV/jenkins-lesson
2. В ветке feat1-add-jenkinsfile находится Jenkinsfile, который нужно переписать с использованием декларативного синтаксиса. Сделать так, чтобы имена, создаваемых docker образов не пересекались в случае одновременного запуска билдов для разных веток.
3. Создать multi-branch pipeline с именем jenkins-lesson. В качестве источника добавить полученный после форка GitHub репозиторий из п.1. Настроить триггер для сканирование репозитория и установить периодичность в 1 минуту.

![image](https://user-images.githubusercontent.com/95025513/162427036-f80e09ae-b61a-4e13-a8f1-aab609726bc3.png)
![image](https://user-images.githubusercontent.com/95025513/162427048-4d1549a7-54fb-453b-8220-3e457dae41c0.png)

4. Создать Pull-Request для внесения изменений из feat1-add-jenkinsfile в main ветку, добавить vauboy ревьювером. Проверить, что в проекте jenkins-lesson в Jenkins появилась новая задача в Pull Requests
> Вот пул реквест -> https://github.com/vauboy/jenkins-lesson/pull/2
> Добавить в ревьюеры я не могу ни кого. У меня просто нет такой возможности.
