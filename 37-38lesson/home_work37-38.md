# Lesson 2.4

## Home work 2.4

### Задача 1. Работа с локальным репозиторием

1. Создать локальный репозиторий "git-lesson"
```bash
[sitis@localhost git]$ git init git-lesson
Initialized empty Git repository in /home/sitis/git/git-lesson/.git/
```

2. Создать пустой файл README.md и закоммитить изменения.
```bash
[sitis@localhost git-lesson]$ touch README.md
[sitis@localhost git-lesson]$ git add README.md
[sitis@localhost git-lesson]$ git commit -m "Add new file README.md"
[master (root-commit) 04519c3] Add new file README.md
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
```

3. Создать дополнительную ветку "feat1-add-readme", добавить в файл README.md немного текста. Изменения закоммитить.
```bash
[sitis@localhost git-lesson]$ git checkout -b feat1-add-readme
Switched to a new branch 'feat1-add-readme'
[sitis@localhost git-lesson]$ echo "First line" >> README.md
[sitis@localhost git-lesson]$ git add README.md
[sitis@localhost git-lesson]$ git commit -m "Add some text in  README.md  file"
[feat1-add-readme 43db494] Add some text in  README.md  file
[feat1-add-readme 6d34e0b] Add some text in  README.md  file
 1 file changed, 1 insertion(+)
```
4. Переключиться обратно на "master" ветку и так же добавить в README.md немного другого текста
```bash
[sitis@localhost git-lesson]$ git checkout master
Switched to branch 'master'
[sitis@localhost git-lesson]$ echo "Add new line from master branch" >> README.md
[sitis@localhost git-lesson]$ git add README.md
[sitis@localhost git-lesson]$ git commit -m "add some text from master branch"
[master e9a73cd] add some text from master branch
 1 file changed, 1 insertion(+)
```
5. Смержить изменения из "feat1-add-readme" в "master" ветку так, чтобы сохранились изменения только из "feat1-add-readme" ветки
```bash
[sitis@localhost git-lesson]$ git merge feat1-add-readme
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```
> Заходим в файл README.md и устранияем конфликт
```bash
[sitis@localhost git-lesson]$ cat README.md
<<<<<<< HEAD
Add new line from master branch
=======
First line
>>>>>>> feat1-add-readme
[sitis@localhost git-lesson]$ vi README.md
[sitis@localhost git-lesson]$ cat README.md
First line
[sitis@localhost git-lesson]$ git add README.md
[sitis@localhost git-lesson]$ git commit
[master 3c7e1f1] Merge branch 'feat1-add-readme'
[sitis@localhost git-lesson]$ git status
# On branch master
nothing to commit, working directory clean
```
6. Переключиться обратно на "feat1-add-readme" ветку, создать файл temp_file и закоммитить изменения
```bash
[sitis@localhost git-lesson]$ git checkout feat1-add-readme
Switched to branch 'feat1-add-readme'
[sitis@localhost git-lesson]$ touch temp_file
[sitis@localhost git-lesson]$ git add temp_file
[sitis@localhost git-lesson]$ git commit -m "Create a new file with name temp_file"
[feat1-add-readme 0ccf41b] Create a new file with name temp_file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 temp_file
```
7. Отменить изменения, вносимые первым коммитом ветки "feat1-add-readme"
```bash
[sitis@localhost git-lesson]$ git log
commit 0ccf41b33ad8da72ad7681f3e1f057b643c1e79f
Author: Your Name <you@example.com>
Date:   Fri Mar 25 13:53:14 2022 +0300

    Create a new file with name temp_file

commit 6d34e0b83ef81fee4c79bf78500ee99ec0588665
Author: Your Name <you@example.com>
Date:   Fri Mar 25 13:49:20 2022 +0300

    Add some text in  README.md  file

commit 04519c3b413e8841023c8bd25de1812d8b5152f1
Author: Your Name <you@example.com>
Date:   Fri Mar 25 13:48:45 2022 +0300

    Add new file README.md
[sitis@localhost git-lesson]$ git show 6d34e0b83ef81fee4c79bf78500ee99ec0588665
commit 6d34e0b83ef81fee4c79bf78500ee99ec0588665
Author: Your Name <you@example.com>
Date:   Fri Mar 25 13:49:20 2022 +0300

    Add some text in  README.md  file

diff --git a/README.md b/README.md
index e69de29..9649cde 100644
--- a/README.md
+++ b/README.md
@@ -0,0 +1 @@
+First line
[sitis@localhost git-lesson]$ git reset --hard 6d34e0b83ef81fee4c79bf78500ee99ec0588665
HEAD is now at 6d34e0b Add some text in  README.md  file
```

### Задача 2. Работа с удаленным репозиторием

1. Создать пустой репозиторий в GitHub "git-lesson".
> https://github.com/studentNV/git-lesson
2. Сделать этот репозиторий удаленным для локального репозитория из первой задачи
```bash
[sitis@localhost git-lesson]$ git remote add origin https://github.com/studentNV/git-lesson.git
[sitis@localhost git-lesson]$ git remote
origin
```

3. Отправить изменения из всех веток в "git-lesson" репозиторий
```bash
[sitis@localhost git-lesson]$ git push origin master
Username for 'https://github.com': studentNV
Password for 'https://studentNV@github.com':
Counting objects: 10, done.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (10/10), 931 bytes | 0 bytes/s, done.
Total 10 (delta 0), reused 0 (delta 0)
To https://github.com/studentNV/git-lesson.git
 * [new branch]      master -> master
[sitis@localhost git-lesson]$ git push origin feat1-add-readme
Username for 'https://github.com': studentNV
Password for 'https://studentNV@github.com':
Total 0 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'feat1-add-readme' on GitHub by visiting:
remote:      https://github.com/studentNV/git-lesson/pull/new/feat1-add-readme
remote:
To https://github.com/studentNV/git-lesson.git
 * [new branch]      feat1-add-readme -> feat1-add-readme
[sitis@localhost git-lesson]$

```

4. Заменить содержимое README.md в ветке "feat1-add-readme" строкой "Hello Github", закоммитить и отправить в "git-lesson" репо
```bash
[sitis@localhost git-lesson]$ echo "Hello Github" > README.md
[sitis@localhost git-lesson]$ git commit -am "Change file README.md for Pull-Request"
[feat1-add-readme 4ac0fe2] Change file README.md for Pull-Request
 1 file changed, 1 insertion(+), 1 deletion(-)
[sitis@localhost git-lesson]$ git push origin feat1-add-readme
Username for 'https://github.com': studentNV
Password for 'https://studentNV@github.com':
Counting objects: 5, done.
Writing objects: 100% (3/3), 283 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/studentNV/git-lesson.git
   6d34e0b..4ac0fe2  feat1-add-readme -> feat1-add-readme
```
5. Сделать Pull-Request из ветки "feat1-add-readme" в "master" и добавить меня (@vauboy) ревьювером
> не могу вас добавить ревьювером пока вы не примите приглашение на `collaborates` (в ином случае у меня просто пустой список на добавление в ревьюверы) репозиторий публичный проверил перейдя на пулл реквест с другого акаунта на `git-hub`
> https://github.com/studentNV/git-lesson/pull/1

### Задача 3. Знакомство с GitLab Community Edition

1. Запустить Gitlab CE в докере "gitlab/gitlab-ce:latest"
Необходимо сделать скриншоты на всех последующих этапах и приложить в виде архива
2. Создать группу "devops-course"
3. Создать пользователей: developer1 и developer2
4. Добавить их в группу и назначить следующие пермишены:
developer1 – maintainer
developer2 – developer
5. Создать новый проект
6. Создать все необходимые для GitFlow ветки в проекте (например main, develop, release-v1, feature1)
7. Запретить отправку изменений в "main" ветку для всех пользовате. У maintainer должен остаться возможность для слияния изменений из других веток
8. Защитить релизные ветки с помощью wildcard (например release-*) и разрешить слияние только пользователям с уровнем доступа maintainer
9. Защитить develop ветку и разрешить создавать Merge Requests всем пользователям. Под всеми пользователями имеются ввиду developer+maintainer
10. Разрешить всем вносить любые изменения в "feature-*" ветки
> Тут так же все пользователи если идёт речь о developer+maintainer, то скриншот в архиве. Если всё же `все пользователи`, как я понимаю у них и так есть этот достпун (если не настроено в правиле каких либо ограничений)  
> Все скриншоты -> https://github.com/studentNV/chapter-2/blob/lesson37-38/37-38lesson/git_lab.7z
