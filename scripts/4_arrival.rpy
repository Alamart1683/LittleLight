init python:
    flag = False

# Сцена прибытия в Город
########################

#-1-#
# Сцена поездки в поезде
label train_moving:
    play sound "sound/train.mp3" # Звук поезда
    if flag == False:
        $ hero = Character(actor.name, color = "#191970")
        scene bg black
        if actor.sex == "male":
            hero "Я очнулся в купе поезда, идущего в город Миддлфилд."
            hero "Судя по времени, до прибытия до пункта назначения осталось не так уж и много..."
        else:
            hero "Я очнулась в купе поезда, идущего в город Миддлфилд."
            hero "Судя по времени, до прибытия до пункта назначения осталось не так уж и много..."
        hide bg black
        scene bg train
        hero "На столике лежит газета, возможно, она содержит полезную информацию."
        call screen train_buttons
    else:
        call screen train_buttons
    return

#-2-#
# Сцена показа газеты
label newspaper:
    # play sound "sound/newspaper.mp3"
    $ flag = True
    call screen newspaper
    return

#-3-#
# Сцена торможения поезда
label train_stopping:
    $ hero = Character(actor.name, color = "#191970")
    scene bg black
    hero "Медленно и невозмутимо поезд прибывал на платформу вокзала Миддлфилда..."
    if actor.sex == "male":
        hero "Я взял свои вещи и направился в сторону выхода из вагона."
    else:
        hero "Я взяла свои вещи и направилась в сторону выхода из вагона."
    play sound "sound/tormoz.mp3" # Звук поезда
    pause(10.0)
    if actor.sex == "male":
        hero "Я покинул вагон и оказался на перроне вокзала."
    else:
        hero "Я покинула вагон и оказалась на перроне вокзала."
    hide bg black
    call station from _call_station
    return

#-4-#
# Сцена появления на воказале
label station:
    $ hero = Character(actor.name, color = "#191970")
    play music "sound/station.mp3"
    scene bg station
    if actor.sex == "male":
        hero "Я оглянулся."
        hero "Здание вокзала. Старое, ему бы определенно не помешал ремонт."
        hero "Я решил пройти внутрь и оттуда начать поиски места, где можно остановиться."
    else:
        hero "Я оглянулась."
        hero "Здание вокзала. Старое, ему бы определенно не помешал ремонт."
        hero "Я решила пройти внутрь и оттуда начать поиски места, где можно остановиться."
    $ flag = False
    hide bg station
    call station_in from _call_station_in
    return

#-5-#
# Сцена внутри вокзала
label station_in:
    $ hero = Character(actor.name, color = "#191970")
    window hide
    scene bg zhd_station
    if actor.sex == "male":
        hero "Высокий потолок вокзала давил на меня."
        hero "Я покинул вокзал и отправился исследовать город."
    else:
        hero "Высокий потолок вокзала давил на меня."
        hero "Я покинула вокзал и отправилась исследовать город."
    stop music
    call city_map from _call_city_map
    return

###################
# Локальные менюшки

# Меню кнопок поезда
screen train_buttons:
    window:
        xysize(1920,1080)
        xalign(0.0)
        yalign(0.0)
        background("images/bg/prozrachniy.png")
        pos(0,0)
        imagebutton id"newspaper":
            idle("gui/custom_buttons/newspaper/newspaper_1.png")
            hover("gui/custom_buttons/newspaper/newspaper_2.png")
            pos(1352, 920)
            action Jump("newspaper")

        imagebutton id"train_window":
            idle("gui/custom_buttons/train_window/train_window_1.png")
            hover("gui/custom_buttons/train_window/train_window_2.png")
            pos(350, 0)
            action Jump("train_stopping")

# Меню чтения газеты
screen newspaper:
    window:
        xysize(1920,1080)
        xalign(0.0)
        yalign(0.0)
        background("images/bg/newspaper.png")
        pos(0,0)
        imagebutton id"newspaper_close":
            idle("gui/custom_buttons/newspaper_close/newspaper_button_1.png")
            hover("gui/custom_buttons/newspaper_close/newspaper_button_2.png")
            pos(1874, 1)
            action Jump("train_moving")
