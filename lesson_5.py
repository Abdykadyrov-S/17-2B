"""
Команды пишутся только один раз когда вы делаете первый пуш


git --version

git config --global user.name "YOUR USERNAME ON GITHUB"

git config --global user.email "YOUR EMAIL ON GITHUB"

"""


"""

Команды для пуша на новый репозиторий (первый пуш в новом репохитории)

git init 

git add .
# git add test.py

git commit -m "first commit"
# git commit -m "Код с урока группу 17-2B"

git branch -M main

git remote add origin <HTTPS link.git>
# git remote add origin https://github.com/Abdykadyrov-S/17-2B.git


git push -u origin main

"""


"""
Команды для пуша на существующий репозиторий с коммитом

git add .

git commit -m "Обновили файлы = Lesson_5.py, test.py"

git push

"""
