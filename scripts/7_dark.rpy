# Возможность умереть
label death:
    scene bg dark_coridor
    $ hero = Character(actor.name, color = "#191970")

    hero "Ноги сами зачем-то понесли меня в загородный горный лес."

    if actor.sex == "male":
        hero "Долго блуждав в горном лесу, я набрел на огромное заброшенное здание и решил зайти внутрь."
    else:
        hero "Долго блуждая в горном лесу, я набрела на огромное заброшенное здание и решила зайти внутрь."

    if actor.sex == "male":
        hero "Пройдя по длинному пустынному коридору я вдруг услышал шорох за спиной."
    else:
        hero "Пройдя по длинному пустынному коридору я вдруг услышала шорох за спиной."

    hero "Удар."
    hero "Темнота..."
    #"{space=425}К{space=3}О{space=3}Н{space=2}Е{space=1}Ц И{space=2}Г{space=2}Р{space=2}Ы"

    init python:
        renpy.set_return_stack([])
    call f_hospital_death from _call_f_hospital_death
    return
