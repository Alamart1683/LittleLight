# Карта города
label city_map:
    $ hero = Character(actor.name, color = "#191970")
    # $ money = "{color=#FFFF00}Деньги: " + str(actor.money) + "$"
    # $ MoneyPos = Position(ypos = 30, xpos = 1780)
    scene bg black
    call hood
    # show hood at top
    # show text money at MoneyPos
    window hide # Спрячем диалоговое окно
    # Создаем активные области
    $ result = renpy.imagemap (
        "gui/custom_buttons/map/townmap.png", "gui/custom_buttons/map/townmap_highlight.png",
        [
            (50, 720, 400, 1060, "hotel"),
            (966, 372, 1364, 674, "church"),
            (225, 492, 504, 624, "school"),
            (820, 217, 1260, 308, "station"),
            (1676, 502, 1920, 710, "hospital"),
            (485, 348, 898, 744, "guildhall"),
            (243, 406, 378, 494, "police")
        ]
    )

    # Обрабатываем выбор:

    # Переход в отель в первый раз
    if result == "hotel":
        call first_hotel_visit
    # Переход в собор в первый раз
    elif result == "church":
        call f_church
    # Переход в школу в первый раз
    elif result == "school":
        call f_school
    # Переход на вокзал в первый раз
    elif result == "station":
        call f_station
    # Переход в больницу в первый раз
    elif result == "hospital":
        call f_hospital
    # Переход в ратушу в первый раз
    elif result == "guildhall":
        call f_guildhall
    # Переход в отделение полиции в первый раз
    elif result == "police":
        call f_police

    label f_church:
        scene bg cathedral
        hero "Городской собор. Сейчас мне здесь нечего делать."
        call city_map

    label f_school:
        hero "Школа. Сейчас мне здесь нечего делать."
        call city_map

    label f_station:
        scene bg zhd_station
        hero "Старый вокзал. Кажется я начинаю ходить кругами."
        call city_map

    label f_hospital:
        scene bg hospital
        hero "Местный госпиталь. Сейчас мне здесь нечего делать."
        call city_map

    label f_guildhall:
        scene bg guildhall
        hero "Старинная ратуша, центр города. Сейчас мне здесь нечего делать."
        call city_map

    label f_police:
        scene bg police_office
        hero "Полицейский участок. Сейчас мне здесь нечего делать."
        call city_map

    return
