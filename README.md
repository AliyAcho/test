# test

## Инструкции по запуску

1. В файле env.dev вам нужно поменять CHAT_ID в телеграм на свой. Также вы должны написать этому боту http://t.me/test_order_notifications_bot или использовать своего бота поменяв BOT_TOKEN.

2. Выполните `docker-compose up -d --build`.

3. Перейдите на http://localhost:8000. Если результатов нет, можно перезагрузить страницу через некоторое время. Обычно это занимает не более 10 секунд.

## ...

Скрипт запускается автоматически после `docker-compose up -d --build`. Основные функции скрипта находятся в папке приложения core(upDB.py). В этой же папке находятся функция получения курса доллара(dollar.py) и функции для получения данных из таблицы(sheets.py).


