init python:
    flag = False

# Сцена прибытия в Город
########################

#-1-#
# Сцена поездки в поезде
label train_moving:
    if flag == False:
        scene bg black
        u"..." "Вы проспыпаетесь в плацкартном вагоне от невыносимого запаха носков соседа..."
        hide bg black
        scene bg train
        u"..." "Поезд делает ту-ту и чух-чух!"
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
    u"..." "За окном стали заметны силуэты домов, и вы почувствовали, что поезд начал постепенно сбавлять ход..."
    u"Поезд" "Чучух-чучух... Чучух-чучух... Издает скрипение тормозов... Издает их еще..."
    u"..." "Медленно и невозмутимо поезд прибывал на платформу вокзала уездного города N"
    u"..." "Вы берете свои вещи и направляетесь к выходу из вагона, издавая топающие звуки"
    u"Поезд" "Тем временем я остановился и меня немного тряхнуло."
    u"..." "Вы выходите из вагона и оказываетесь на городском вокзале..."
    hide bg black
    call station

#-4-#
# Сцена появления на воказале
label station:
    scene bg station
    u"..." "Вы оглядываетесь и видите весьма потрепанное здание городского воказала"
    u"..." "Вы решаете последовать в него с целью узнать где здесь можно остановиться..."
    u"..." "Пока конец"
    $ flag = False
    hide bg station
    call start

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
