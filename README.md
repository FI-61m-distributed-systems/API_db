# users_db_api
# configure.py
Задаёт конфигурацию БД. Создаёт файл conf.ini.
# connection.py
Предостовляет доступ к БД.
# registration.py
Получает логин, пароль, ел.почту пользователя и вносит их в БД.
# authorization.py
Получает логин, пароль, ел.почту и сверяет с данными в БД.
# money.py
Запрос на обновление в БД. Получает логин получателя, отправителя, сумму перевода.
# stub.py
Служебные функции.
# test/test_con
Тестирование основных функций в консоли.
# Get Started
Запустить configure.py : python configure.py -s <host> -p <password> -l <port> 
С консоли запускать  registration.py, authorization.py, money.py в зависимости от потребностей.
