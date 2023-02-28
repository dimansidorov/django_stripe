# Django Stripe Test Project
Реализация Django + Stripe API бэкенд со следующим функционалом и
условиями:
- Django Модель Item с полями (name, description, price)
- API GET /buy/{id}, c помощью которого можно получить Stripe Session
Id для оплаты выбранного Item. При выполнении этого метода c
бэкенда с помощью python библиотеки stripe должен выполняться
запрос stripe.checkout.Session.create(...) и полученный session.id
выдаваться в результате запроса
- API GET /item/{id}, c помощью которого можно получить простейшую
HTML страницу, на которой будет информация о выбранном Item
и кнопка Buy. По нажатию на кнопку Buy должен происходить
запрос на /buy/{id}, получение session_id и далее с помощью JS
библиотеки Stripe происходить редирект на Checkout форму
stripe.redirectToCheckout(sessionId=session_id)

## Лицензия

MIT


## Запуск проекта

Все команды расчитаны на OC Linux. Необходимо, чтобы на рабочей машине были установлены python и pip. 
Инструкции по установке python и pip можно найти в данной статье: https://habr.com/ru/post/491916/

1. Для начала рекомендуется создать отдельную папку, в который вы будете размещать проект. Удобно воспользоваться командой в терминале:

`mkdir test`

2. Перейти в папку test. Удобно воспользоваться командой в терминале:

`cd test`

3. Установите virtualenv, если ранее он не был у вас установлен. Удобно воспользоваться командой в терминале:
 
`pip install virtualenv`

Документация: https://virtualenv.pypa.io/en/latest/installation.html

3. Создание виртуального окружения. Удобно воспользоваться командой в терминале:

`virtualenv -p python3 mytest`

4. Активация виртуального окружения. Удобно воспользоваться командой в терминале:

`source mytest/bin/activate`

5. Клонируйте репозиторий. Удобно воспользоваться командой в терминале:

`git clone git@github.com:dimansidorov/django_stripe.git`

6. Перейдите в клонированный репозиторий. Установите все необходимые пакеты из requirements.txt. Необходимо воспользоваться командой в терминале:

`cd django_stripe && pip install -r requirements.txt`

7. Создайте и сделайте миграции. Необходимо воспользоваться командой в терминале:

`python manage.py makemigrations && python manage.py migrate`

8. Если есть необходимость работы с админ-панелью django - создайте суперпользователя. Необходимо воспользоваться командой в терминале:

`python manage.py createsuperuser`

9. Добавление товара в БД можно сделать при помощи команды:

`python manage.py additem`

или через админ-панелью django.

10. Запуск на тестовом веб-сервере:

`python manage.py runserver`



