# Игра "Заливка" 🎮

---

### Описание проекта 📝

Данная работа выполнялась в рамках полуфинала олимпиады DevOps на сайте [траетория будущего](https://tbolimpiada.ru/).

В игре есть два игрокаю От их стартовых позиций можно проложить маршрут друг к другу, каждая клетка поля имеет один из 10 цветов, заданных случайным образом:

Игроки начинают игру в противоположных углах. Первый игрок начинает игру в левом нижнем углу. Второй игрок - в правом верхнем. Игроки выбирают цвет по очереди, начиная с первого игрока. Для выбора цвета разрешены те цвета, с которыми есть соприкосновения. Нельзя выбрать цвет соперника. При выборе нового цвета к пространству игрока добавляются клетки, соприкасающиеся с полем игрока, в которых указан данный цвет (т.е. при заливке цветом поле постепенно растет не менее, чем на 1 клетку).

Игра останавливается в тот момент, когда игрок не может выбрать цвет и совершить ход.

Побеждает тот игрок, у которого в момент окончания игры больше занятых клеток.

### Установка проекта

#### 1. Используя Docker 🐋 (Linux Ubuntu)

**Для установки проекта сначала установите Docker:**

`sudo apt-get update`
`sudo apt-get install docker.io`
`sudo apt-get install docker-compose`

**Выполните клонирование репозитория:**

`git clone https://github.com/Tminww/devops-game.git`

**Перейдите в дирректорию проекта:**

`cd devops-game`

**Создайте необходимые файлы и дирректорию:**

`mkdir /backend/src/log`
`touch /backend/src/.env`

**Теперь нужно указать в файле `.env` путь к базе данных SQLite:**

`echo 'DB_PATH="<path_to_database>"' > ./backend/src/.env`

**Запустите docker-compose:**

`sudo docker-compose up -d --build`

**Проверить работу контейнеров можно следующей командой:**

`sudo docker ps -a`

**Если все прошло успешно, то по следующим URI будут доступны:**

`localhost:8000` **- backend**
`localhost:8080` **- frontend**

### Как пользоваться

После выполнения всех действий по установке проекта откройте браузер.

Вбейте в адресной строке `localhost:8080` и перейдите на главный экран веб-приложения.

1. Нажмите кнопку **Играть** и у вас отрисуется поле.
2. Нажмите кнопку **Результаты** и у вас отобразятся результаты последних 10 игр

### Примечание

- Документация для `backend` была сгенерирована библиотекой `lezydocs` и `swagger`

- Модульное тестирование реализовано с помощью библиотеки `pytest`

- Для backend на `Python` использовался форматтер `Black`
- Для frontend на `JS` использовался форматтер `Prettier`
- Использалась база данных `Sqlite`
- Для взаимодействия `клиента и сервера` было выбрано `REST API`
- Логгирование сохраняется в папке `backend/src/log`
-
