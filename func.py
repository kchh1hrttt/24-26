from tkinter import messagebox
import design
import random
import sys
import os


artifacts = ['Sword', 'Stick', 'Magic Ball', 'Ring of Power', 'Amulet of Wisdom',
             'Cloak of Invisibility', 'Wand of Lightning', 'Scroll of Knowledge']

races = {
    'first_dict': {
        1: 'Elf',
        2: 'Human',
        3: 'Dwarf',
        4: 'Gnome',
        5: 'Orc'
    },
    'second_dict': {
        1: 'Elf',
        2: 'Human',
        3: 'Half-elf',
        4: 'Angel',
        5: 'Demon'
    },
    'third_dict': {
        1: 'Leonal',
        2: 'Centaur',
        3: 'Phoenix',
        4: 'Cyborg',
        5: 'Extraterrestrial'
    },
    'fourth_dict': {
        1: 'Orc',
        2: 'Vampire',
        3: 'Werewolf',
        4: 'Anthropomorphic_animal',
        5: 'Mutant'
    },
    'fifth_dict': {
        1: 'Undead',
        2: 'Celestial',
        3: 'Angel',
        4: 'Forest_spirit',
        5: 'Half-orc'
    }
}

names = {
    'first_dict': {
        1: 'Argo',
        2: 'Bronislav',
        3: 'Velena',
        4: 'Thunder',
        5: 'Darina'
    },
    'second_dict': {
        1: 'Astra',
        2: 'Golden_Eagle',
        3: 'Vesta',
        4: 'Gavin',
        5: 'Daria'
    },
    'third_dict': {
        1: 'Alice',
        2: 'Boris',
        3: 'Victoria',
        4: 'Gregory',
        5: 'Dina'
    },
    'fourth_dict': {
        1: 'Ayla',
        2: 'Bogdan',
        3: 'Barbara',
        4: 'George',
        5: 'Elizabeth'
    },
    'fifth_dict': {
        1: 'Aurora',
        2: 'Vlad',
        3: 'Zlata',
        4: 'Daniel',
        5: 'Jeanne'
    }
}


# переменным присвоены случайные словари с именами/расами из другого словаря
race_dict = races[random.choice(list(races.keys()))]
name_dict = names[random.choice(list(names.keys()))]

# нумерация имён из словаря
name_options = "\n".join(f"{name}" for index, name in enumerate(name_dict.values()))
race_options = "\n".join(f"{race}" for index, race in enumerate(race_dict.values()))


def new_players():
    artifact = design.artefact_cbox.get()
    sex = design.sex_cbox.get()
    name = design.name_cbox.get()
    race = design.race_cbox.get()

    spirit = int(design.spirit_cbox.get())
    exp = int(design.spirit_cbox.get())
    knowledge = int(design.spirit_cbox.get())
    attack = int(design.attack_cbox.get())
    defense = int(design.defense_cbox.get())
    magic_power = int(design.magic_cbox.get())
    luck = int(design.luck_cbox.get())
    character_parameters = [artifact, attack, defense, exp, knowledge,
                            luck, magic_power, name, race, sex, spirit]

    data = format_data(character_parameters)

    ready = messagebox.askyesno('Проверка', f'Всё ли верно?\n{data}')

    if ready:
        formatted_data = format_data(character_parameters, octal=True)
        write_to_data_f(formatted_data)
        num = design.characters_num_lbl.cget('text')
        design.characters_num_lbl.configure(text=num - 1)
        if num == 1:
            messagebox.showinfo('Готово', 'Все персонажи успешно добавлены в файл. Программа автоматически завершит работу')
            os.startfile('data.all')
            sys.exit()


def format_data(c_parameters, octal=False):
    """
    :param c_parameters: параметры персонажа
    :param octal: в зависимости от состояния параметра, характеристики персонажа преобразовываются в восьмеричный формат
    :return: возвращает параметры персонажа, в том, или ином формате
    """

    # проверяется тип данных каждой хар-ки персонажа, int преобразовывается
    if octal:
        c_parameters = [oct(param) if isinstance(param, int) else param for param in c_parameters]

    # случайный номер персонажа
    random_num = random.randint(0, 99999999)

    formatted_data = f'''Person#{random_num}:
artifact: {c_parameters[0]}
attack: {c_parameters[1]}
defense: {c_parameters[2]}
exp: {c_parameters[3]}
knowledge: {c_parameters[4]}
luck: {c_parameters[5]}
magic_power: {c_parameters[6]}
name: {c_parameters[7]}
race: {c_parameters[8]}
sex: {c_parameters[9]}
spirit: {c_parameters[10]}'''

    return formatted_data


def write_to_data_f(data):
    with open('data.all', 'a', encoding='ASCII') as f:
        formatted_data = data.format('f')
        f.write(formatted_data + '\n\n')
