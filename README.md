# test work
---
## Start:
* Должен быть установлен интерпретатор python версии 3.8 и выше
* В корневой папке создать виртуальное окружение ``python3 -m venv venv`` 
* Активировать виртуальное окружение ``source ./venv/bin/activate`` 
* Установить зависимости ``pip install -r requirements.txt``
* Инициализировать базу ``python manage.py migrate``
* Создать админа ``python manage.py createsuperuser``
* Запустить сервер ``python manage.py runserver``

## Start in docker:
* В корневой папке выполнить ``docker-compose build && docker-compose up``
* После запуска контейнера выплнить ``docker exec -it <container_id> python manage.py createsuperuser`` , чтобы создать админа

## Swagger:
* Swagger будет доступен по адресу localhost/api/swagger-ui/
* Админка будет доступна по адреcу localhost/admin/