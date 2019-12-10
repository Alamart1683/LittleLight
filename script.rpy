# Определение всех сущностей игры. $ для меня
init:
    # Объект игрока
    python:
        _actor = Player(img = "", sex = "", name = "", col = "#000000", abils = [])

    $ ontos = Character(u"...")

    # Создание объектов фонов
    image bg splash = "bg/splash.png" # Создание объекта фона заставки
    image bg first intro = "bg/intro1.png" # Создание объектов фона вступления
    image bg actor creator = "bg/creation1.png" # Фон гуи создания персонажа
    image bg black = "bg/black.png" # Просто черный фон
    image bg train = "bg/train_intro.png" # Интро поезд
    image bg station = "bg/station.png" # Интро вокзал
    image bg aframe = "bg/actor_creation_frame.png"
    image bg zhd_station = "bg/zhd_station.png"

    # Создание объектов картинок спрайтов
    image girl = "cg/Girl_Full.png"
    image h_girl = "cg/Girl_Half.png"
    image boy = "cg/Boy_Full.png"
    image h_boy = "cg/Boy_Half.png"
    image ren = "cg/renpy.png"

# Игра начинается здесь:
label start:
    #play sound "sound/freedom.mp3" fadein(2.0)
    $ actor = _actor # объект гг
    # call introduction # Вызов вступления
    call gender_choose # Вызов меню выбора пола гг
    call screen actor_creation_screen # Вызов меню создания персонажа
    play sound "sound/train.mp3" # Звук поезда
    return
