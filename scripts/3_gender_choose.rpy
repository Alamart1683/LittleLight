# Выбор пола главного героя:
label gender_choose:
    scene bg aframe
    window hide # Спрячем диалоговое окно
    # Создаем активные области
    $ result = renpy.imagemap("gui/custom_buttons/gender/img_mp_1.png", "gui/custom_buttons/gender/img_mp_2.png",
    [(300, 0, 962, 1080, "male"), (963, 0, 1580, 1080, "female")]
    )
    # Обрабатываем выбор
    scene bg aframe # Установление фона интро
    window show # Покажем диалоговое окно
    u"..." "Выбранный вами пол персонажа: "
    if result == "female":
        show girl
        $ actor.img = "cg/Girl_Full.png"
    elif result == "male":
        show boy
        $ actor.img = "cg/Boy_Full.png"
    u"..." "Это я называю прогресс"
    $ actor.sex = result
    hide boy with dissolve
    hide girl with dissolve
    hide bg actor creator
    window hide # Спрячем диалогове окно
    scene bg black # Показать черный фон
    return
