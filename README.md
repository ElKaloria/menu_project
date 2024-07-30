<h2> Тестовое задание - древовидное меню на Django </h2>
<p>Текст задания можно прочитать здесь:</p>
<p>https://docs.google.com/document/d/1XTnbcXhejyGB-I2cHRiiSZqI3ElHzqDJeetwHkJbTa8/edit</p>
<h3>Запуск на Windows</h3>
<code>git clone git@github.com:ElKaloria/menu_project.git
cd menuProject
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
</code>
<p> При работе в Pycharm создавать виртуальное окружение не обязательно, если оно создается по умолчанию при создании проекта</p>
<h3>Для изменения и создания меню через админ-панель потребуестя создать суперпользователя</h3>
<p>Это можно сдлеать командой</p>
<code>python manage.py createsuperuser</code>
