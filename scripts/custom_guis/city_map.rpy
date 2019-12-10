# Карта города
label city_map:
    scene bg black
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
        call f_hotel
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

    label f_hotel:
        actor.name "Наконец-то я отыскал то, что нужно!"

    label f_church:
        actor.name "Городской собор. Сейчас мне здесь нечего делать."
        call city_map

    label f_school:
        actor.name "Школа. Сейчас мне здесь нечего делать"
        call city_map

    label f_station:
        actor.name "Вокзал. Кажется я начинаю ходить кругами"
        call city_map

    label f_hospital:
        actor.name "Местный госпиталь. Сейчас мне здесь нечего делать"
        call city_map

    label f_guildhall:
        actor.name "Старинная ратуша, центр города. Сейчас мне здесь нечего делать"
        call city_map

    label f_police:
        actor.name "Полицейский участок. Сейчас мне здесь нечего делать"
        call city_map





    scene bg black # Показать черный фон
    return
