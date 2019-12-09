# Заставка
label splashscreen:
    $LLpos = Position(ypos = 0.8, yanchor ='center')
    $RPpos = Position(ypos = 0.6, yanchor ='center')
    $RPTpos = Position(ypos = 0.6, yanchor='center')
    scene bg splash
    # play sound "sound/dydlya.mp3" fadein(2.0) # Плавный запуск музыки
    with Pause(1)

    show text "{color=#ffd700} {b}{size=+20} LittleLight \n Представляет {/size}{/b} {/color}" at LLpos with dissolve  # Плавно показать текст
    with Pause(2)
    hide text with dissolve # Плавно спрятать текст
    with Pause(1)

    scene bg black with dissolve
    show ren at RPpos with dissolve
    show text "{color=#ffffff} {b}{size=+20} Powered by \n RenPy {/size}{/b} {/color}" at RPTpos with dissolve
    stop sound fadeout(2.5) # Плавное торможение музыки
    with Pause(1)
    hide text with dissolve
    hide ren with dissolve
    with Pause(1)
    return
