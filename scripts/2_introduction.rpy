# Вступление
label introduction:
    scene bg first intro # Установление фона интро
    "{i} Онтос обретает сознание... {/i}"
    u"Онтос" "Я - вечное и незыблемое бытие. Я суть двигатель всего происходящего здесь..."
    u"Онтос" "И вам предстоит стать орудием моей космической воли, познав суть истинного детерминизма, смертные."
    u"Онтос" "Сейчас моей всеобъемлющей волей будет устроен смотр готовых на данный момент безвольных вместилищ духов, названных спрайтами:"
    show girl with dissolve

    u"Онтос" "1 - Девушка, целая:"
    hide girl with dissolve
    show h_girl with dissolve

    u"Онтос" "2 - Девушка, половинная:"
    hide h_girl with dissolve
    show boy with dissolve

    u"Онтос" "1 - Парень, целый:"
    hide boy with dissolve
    show h_boy with dissolve

    u"Онтос" "2 - Парень, половинный:"
    hide h_boy with dissolve
    show boy at left with dissolve
    show girl at right with dissolve

    u"Онтос" "А теперь посмотрим на них вместе:"
    u"Онтос" "Правда, неплохо?"
    show boy at left:
        linear 3 rotate 360
    show girl at right:
        linear 5 rotate 360
    u"Онтос" "А теперь давайте их покрутим, хе хе"
    hide girl with dissolve
    hide boy with dissolve
    show h_boy at left with dissolve
    show h_girl at right with dissolve
    u"Онтос" "Давайте теперь взглянем на них вместе вблизи"
    u"Онтос" "Как мне кажется, Марина очень хорошо постаралась... Я доволен."
    u"Онтос" "После окончания заставки следует перейти к созданию персонажа, что логино."
    hide h_girl with dissolve
    hide h_boy with dissolve
    hide bg first intro
    show black
    return
