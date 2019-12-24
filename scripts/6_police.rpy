# Переменная первого посещения
init python:
    police_flag = False

# Первое посещение полиции
label police:
    scene bg police_office
    call hood from _call_hood_4
    hero "Полицейский участок. Думаю, надо изучить стенд, висящий на стене."
    window hide
    $ result = renpy.imagemap (
        "gui/custom_buttons/police/police_office.png", "gui/custom_buttons/police/police_office_highlight.png",
        [
            (850, 280, 1090, 592, "wall"),
            (1570, 275, 1920, 815, "wardrobe"),
        ]
    )
    # Попытка посмотреть на стенд
    if result == "wall":
        call talk_policeman from _call_talk_policeman
    # Попытка открыть штаф
    elif result == "wardrobe":
        window show
        hero "Шкаф закрыт на ключ."
        call police from _call_police_1

    call city_map from _call_city_map_6

# Лейбл первого разговора с полисменом
label talk_policeman:
    scene bg police_office
    call hood from _call_hood_5
    $ hero = Character(actor.name, color = "#191970")
    $ policeman = Character("Шериф Джонсон", color = "#800000")
    $ policeman_pos = Position(ypos = 1080, xpos = 1500)

    if actor.sex == "male":
        hero "Когда я подошел к стенду, мне на встречу вышел полицейский, который находился в глубине помещения."
    else:
        hero "Когда я подошла к стенду, мне на встречу вышел полицейский, который находился в глубине помещения."

    if actor.sex == "male":
        show h_boy at left
    else:
        show h_girl at left

    show policeman at policeman_pos

    # Если визит первый
    if police_flag == False:
        policeman "Здравствуйте, меня зовут Джонсон и я местный шериф. Слежу за порядком в этом городишке."

        if actor.sex == "male":
            hero "Я представился и рассказал о цели своего приезда."
        else:
            hero "Я представилась и рассказала о цели своего приезда."

        policeman "Что ж, будет очень приятно, если мы будем сотрудничать."

        if actor.sex == "male":
            hero "После знакомства с шерифом я покинул полицейский участок."
        else:
            hero "После знакомства с шерифом я покинула полицейский участок."

        $ police_flag = True

    # Иначе
    else:
        policeman "Добрый день, чем могу помочь?"
        hero "Простите, пока ничем."

    call city_map from _call_city_map_7
    return
