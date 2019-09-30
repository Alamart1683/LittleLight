# Заставка
label splashscreen:
    scene bg splash
    play sound "sound/dydlya.mp3" fadein(2.0) # Плавный запуск музыки
    with Pause(1)

    show text "{color=#ffd700} Студия LittleLight \n Представляет {/color}" with dissolve # Плавно показать текст
    with Pause(2)
    hide text with dissolve # Плавно спрятать текст
    with Pause(1)

    show ren at center with dissolve
    show text "{color=#ffd700} Создано на \n Ренпай {/color}" with dissolve
    stop sound fadeout(2.5) # Плавное торможение музыки
    with Pause(1)
    hide text with dissolve
    hide ren with dissolve
    with Pause(1)
    return
