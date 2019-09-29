init python:
    import random
    # Метод выбора случайного имени из пула
    def get_name(sex):
        if sex == "male":
            number = random.randint(0, len(male_names) - 1)
            return male_names[number]
        elif sex == "female":
            number = random.randint(0, len(female_names) - 1)
            return female_names[number]
