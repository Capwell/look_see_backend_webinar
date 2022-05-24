# Задача - создать сделать сайт
https://practicum.yandex.ru/

# фреймворк
https://www.djangoproject.com/

# Win терминал Ctrl+Shift + P --  Select Default Profile  - bash
# Создаём виртуальное окружение (в терминале)
python -m venv venv

# Активируем
# lin/mac
source venv/bin/activate
# windows
source venv/Scripts/activate

# Ставим Джанго в окружение
pip install Django==3.2.*

# Создаём проект
django-admin startproject look_see

# Уже можем запустить 
# (Перейти по папкам - cd или открыть содержащую manage.py)
python manage.py runserver
CTRL + C

# Создание приложений
python manage.py startapp catalog

# регистриуем приложение в списке look_see/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog',
]


# прописываем путь. Возми из файла views функцию index
# look_see/urls.py
from catalog import views


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
]

# функция сама
# catalog/views.py
from django.http import HttpResponse


def index(request):
    course_list = ['Бэкенд', 'Фронтенд']
    return HttpResponse(course_list)

# catalog/models.py
from django.db import models


class Course(models.Model):
    name = models.TextField()

# Применим все чтом ы написали - к БД терминал из папки содержащей manage.py)
python manage.py makemigrations
python manage.py migrate


#  создадим админа в коносоли ( с файлом manage.py)
python manage.py createsuperuser
admin


# админка catalog/admin.py
from django.contrib import admin

from .models import Course

admin.site.register(Course)
# делаем удобнее
# catalog/models.py
from django.db import models


class Course(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


course_list = Course.objects.all()