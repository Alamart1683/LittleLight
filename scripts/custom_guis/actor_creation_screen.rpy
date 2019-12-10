# Пул локальных переменных и функций в контексте создания персонажей
init python:
    inv_count = 0 # Выбор базового наполнения инвентаря
    abil_count = 0 # Выбор абилок
    name = "Игрок" # Выбор имени из пула имен

    def input_name_control(inp_name):
        actor.name = inp_name

# GUI создания персонажа:
screen actor_creation_screen:
    modal True # Непропускаемый экран меню
    # Параметры фрейма
    frame:
        xalign 0.0
        yalign 0.0
        xysize(1920, 1080)
        background("images/bg/black.png")

        # Рамка воруг имени
        add "gui/borders/border1.png":
            pos(772, 890)

        # Ввод имени
        input id "input_name":
            changed input_name_control
            default name
            exclude "\\*/-+1234567890-=!@#$%^&()_ "
            pixel_width(250)
            pos(840, 920)

        # Сгенерировать имя
        imagebutton id "name_generator":
            idle ("gui/custom_buttons/cube/cube.png")
            hover ("gui/custom_buttons/cube/cube_hover.png")
            pos(1070, 890)
            action Jump("random_name_choose")

        # Показать персонажа
        if actor.sex == "male":
            add "gui/custom_buttons/gender/boy_05.png":
                pos(0, 0)
        elif actor.sex == "female":
            add "gui/custom_buttons/gender/girl_05.png":
                pos(0, 0)

        # Выбор начальных предметов для инвентаря справа

        # Выбор абилки

        # Кнопка начала игры
        imagebutton id "thomas_revenge":
            idle("gui/custom_buttons/thomas/thomas1.png")
            hover("gui/custom_buttons/thomas/thomas2.png")
            pos(1550, 800)
            action Jump("train_moving")

        # Запрет на ввод по энтеру
        key "K_RETURN" action Jump("random_name_choose")

# Выбор рандомного имени из пула
label random_name_choose:
    $ name = get_name(actor.sex)
    $ actor.name = name
    call screen actor_creation_screen
