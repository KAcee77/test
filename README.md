# test work
---
## Start:
* В корневой папке создать виртуальное окружение ``python3 -m venv venv`` 
* Активировать виртуальное окружение ``source ./venv/bin/activate`` 
* Установить зависимости ``pip install -r requirements.txt``
* Инициализировать базу ``python manage.py migrate``
* Создать админа ``python manage.py createsuperuser``
* Запустить сервер ``python manage.py runserver``

## Swagger:
* Swagger будет доступен по адресу localhost/project/api/swagger-ui/
* Админка будет доступна по адреcу localhost/admin/