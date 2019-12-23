# Первое посещение отеля
label first_hotel_visit:
    scene bg hotel_reception
    call hood
    $ hero = Character(actor.name, color = "#191970")
    $ reception_girl = Character("Мэри Сью", color = "#800080")
    $ girl_pos = Position(ypos = 1080, xpos = 1600)

    if actor.sex == "male":
        hero "Совершив достаточно долгую прогулку по городу, я нашел здание столь желанной гостиницы и вошел внутрь."
    else:
        hero "Совершив достаточно долгую прогулку по городу, я нашла здание столь желанной гостиницы и вошла внутрь."

    show reception_girl at girl_pos

    hero "Совершив достаточно долгую прогулку по городу, я нашел здание столь желанной гостиницы и вошел внутрь."
    hero "У ресепшена стояла девушка."
    hero "Заметив мою нерешительность, она подошла ко мне."

    if actor.sex == "male":
        show h_boy at left
    else:
        show h_girl at left

    show reception_girl at girl_pos

    reception_girl "Здравствуйте, меня зовут Мэри Сью. Добро пожаловать в отель \" У погибшего альпиниста \"!"
    reception_girl "Мы всегда рады новым постояльцам!"

    hero "Скажите пожалуйста, есть ли у вас сейчас свободные номера?"

    reception_girl "Город у нас небольшой, да и туристов приезжает совсем мало, так что свободные комнаты вседа найдутся!"

    hero "А цена?"

    reception_girl "50$ в сутки и замечательный номер с видом на историческую часть города ваш!"

    if actor.sex == "male":
        hero "Дорого конечно, но у меня все равно нет выбора, подумала я."
        hero "Хорошо, я согласен - сказал я и отсчитал требуемую сумму."
    else:
        hero "Дорого конечно, но у меня все равно нет выбора, подумала я."
        hero "Хорошо, я согласна - сказала я и отсчитала требуемую сумму."

    $ actor.money = 1000 - 50

    call hood

    reception_girl "Отлично! Я провожу вас в ваш номер."
    reception_girl "А, и ещё. Закрывайте шторы по ночам."

    call home
    return

# Лейбл моего номера в отеле
label home:
    scene bg hotel_room
    call hood
    $ hero = Character(actor.name, color = "#191970")
    hero "На этом пока все!"
    call start
