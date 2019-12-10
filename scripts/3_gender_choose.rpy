# Выбор пола главного героя:
label gender_choose:
    scene bg black
    window hide # Спрячем диалоговое окно
    # Создаем активные области
    $ result = renpy.imagemap("gui/custom_buttons/gender/img_mp_1.png", "gui/custom_buttons/gender/img_mp_2.png",
    [(300, 0, 962, 1080, "male"), (963, 0, 1580, 1080, "female")]
    )
    # Обрабатываем выбор
    # ontos "Выбранный вами пол персонажа: "
    if result == "female":
        # show girl
        $ actor.img = "cg/Girl_Full.png"
    elif result == "male":
        # show boy
        $ actor.img = "cg/Boy_Full.png"
    $ actor.sex = result
    # hide boy with dissolve
    # hide girl with dissolve
    scene bg black # Показать черный фон
    return
