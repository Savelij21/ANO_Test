### Тестовое задание "Реализация сервиса по работе с задачами"

1. Вся функциональность реализована в приложении tasks_app
2. Конфигурация Джанго проекта - в директории src
3. Все необходимые сервисы запускаются через docker-compose одной командой up
4. При первичной инициализации и миграциях БД создаются необходимые 4 статуса для задач (функция в файле миграции)
5. Юнит-тесты реализованы в файле test.py приложения tasks_app
6. Логи создания и обработки задач ведутся в logs/django.log Джанго приложения ano_test_project
7. Документирвоание API ведется с помощью drf_spectacular, swagger схема доступна по пути /api/swagger/