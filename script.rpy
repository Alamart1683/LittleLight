# Определение всех сущностей игры.
init:
    # Объект игрока
    python:
        _actor = Player(img = "", sex = "", name = "Игрок",
        col = "#000000", abils = [], money = 1000)

    $ ontos = Character(u"...")

    # Создание объектов фонов
    image bg splash = "bg/splash.png" # Создание объекта фона заставки
    image bg first intro = "bg/intro1.png" # Создание объектов фона вступления
    image bg actor creator = "bg/creation1.png" # Фон гуи создания персонажа
    image bg black = "bg/black.png" # Просто черный фон
    image bg train = "bg/train_intro.png" # Интро поезд
    image bg station = "bg/station.png" # Интро вокзал
    image bg aframe = "bg/actor_creation_frame.png"
    image bg zhd_station = "bg/zhd_station.png" # Железнодорожная станция
    image bg police_office = "bg/police_office.png" # Полицейский участок
    image bg cathedral = "bg/cathedral.png" # Собор
    image bg hospital = "bg/hospital.png" # Госпиталь
    image bg guildhall = "bg/guildhall.png" # Ратуша
    image bg hotel_reception = "bg/reception.png" # Ресепшен отеля
    image bg hotel_room = "bg/hotel_room.png" # Комната в отеле
    image bg school_coridor = "bg/school_coridor.png" # Школьный коридор
    image bg dark_coridor = "bg/dark_coridor.png" # Темный коридор

    # Создание объектов картинок спрайтов
    image girl = "cg/Girl_Full.png"
    image h_girl = "cg/Girl_Half.png"
    image boy = "cg/Boy_Full.png"
    image h_boy = "cg/Boy_Half.png"
    image ren = "cg/renpy.png"
    image reception_girl = "cg/Receptiongirl.png"
    image policeman = "cg/Policeman.png"

    # Картинка худа
    image hood = "gui/borders/hood.png"

# Игра начинается здесь:
label start:
    $ actor = _actor # объект гг
    # play sound "sound/freedom.mp3" fadein(2.0)
    # call introduction # Вызов вступления
    call gender_choose from _call_gender_choose # Вызов меню выбора пола гг
    call screen actor_creation_screen # Вызов меню создания персонажа
    play sound "sound/train.mp3" # Звук поезда
    return

label ex:
    pass
