init python:
    flag = False

# Сцена прибытия в Город
########################

#-1-#
# Сцена поездки в поезде
label train_moving:
    play sound "sound/train.mp3" # Звук поезда
    if flag == False:
        scene bg black
        if actor.sex == "male":
            actor.name "Я очнулся в купе поезда, идущего в город Миддлфилд."
            actor.name "Судя по времени, до прибытия до пункта назначения осталось не так уж и много..."
        else:
            actor.name "Я очнулась в купе поезда, идущего в город Миддлфилд."
            actor.name "Судя по времени, до прибытия до пункта назначения осталось не так уж и много..."
        hide bg black
        scene bg train
        actor.name "На столике лежит газета, возможно, она содержит полезную информацию."
        call screen train_buttons
    else:
        call screen train_buttons

#-2-#
# Сцена показа газеты
label newspaper:
    $ flag = True
    call screen newspaper

#-3-#
# Сцена торможения поезда
label train_stopping:
    scene bg black
    actor.name "Медленно и невозмутимо поезд прибывал на платформу вокзала Миддлфилда..."
    if actor.sex == "male":
        actor.name "Я взял свои вещи и направился в сторону выхода из вагона."
    else:
        actor.name "Я взяла свои вещи и направилась в сторону выхода из вагона."
    play sound "sound/tormoz.mp3" # Звук поезда
    pause(10.0)
    if actor.sex == "male":
        actor.name "Я покинул вагон и оказался на перроне вокзала."
    else:
        actor.name "Я покинула вагон и оказалась на перроне вокзала."
    hide bg black
    call station

#-4-#
# Сцена появления на воказале
label station:
    play music "sound/station.mp3"
    scene bg station
    if actor.sex == "male":
        actor.name "Я оглянулся."
        actor.name "Здание вокзала. Старое, ему бы определенно не помешал ремонт."
        actor.name "Я решил пройти внутрь и оттуда начать поиски места, где можно остановиться."
    else:
        actor.name "Я оглянулась."
        actor.name "Здание вокзала. Старое, ему бы определенно не помешал ремонт."
        actor.name "Я решила пройти внутрь и оттуда начать поиски места, где можно остановиться."
    $ flag = False
    hide bg station
    call station_in

#-5-#
# Сцена внутри вокзала
label station_in:
    window hide
    scene bg zhd_station
    if actor.sex == "male":
        actor.name "Высокий потолок вокзала давил на меня."
        actor.name "Я покинул вокзал и отправился исследовать город."
    else:
        actor.name "Высокий потолок вокзала давил на меня."
        actor.name "Я покинула вокзал и отправилась исследовать город."
    stop music
    call city_map


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
