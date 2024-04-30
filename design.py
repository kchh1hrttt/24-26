#!/usr/bin/env python3

from tkinter import messagebox
from random import randint
from tkinter import ttk
import tkinter as tk
import func


root = tk.Tk()
root.title('Герої меча та магії: Генератор параметров для игры')
root.geometry('1100x195')
root.minsize(1100, 195)
root.maxsize(1100, 195)
root.option_add('*Font', 'Roboto 14')
# root.configure(background='red')
icon = tk.PhotoImage(file='window-icon.png')
root.wm_iconphoto(False, icon)

name_lbl = tk.Label(root, text='Имя:')
name_lbl.grid(row=0, column=0)

name_cbox = ttk.Combobox(root)
name_cbox['values'] = func.name_options
name_cbox.state(('readonly',))
name_cbox.current(randint(0, 4))
name_cbox.grid(row=0, column=1)

race_lbl = tk.Label(root, text='Раса:')
race_lbl.grid(row=0, column=2)

race_cbox = ttk.Combobox(root)
race_cbox['values'] = func.race_options
race_cbox.state(('readonly',))
race_cbox.current(randint(0, 4))
race_cbox.grid(row=0, column=3)

sex_lbl = tk.Label(root, text='Пол:')
sex_lbl.grid(row=0, column=4)

sex_cbox = ttk.Combobox(root)
sex_cbox['values'] = ('Male', 'Female', 'Other')
sex_cbox.state(('readonly',))
sex_cbox.current(2)
sex_cbox.grid(row=0, column=5)

attack_lbl = tk.Label(root, text='Атака:')
attack_lbl.grid(row=1, column=0)

attack_cbox = ttk.Combobox(root)
attack_cbox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
attack_cbox.state(('readonly',))
attack_cbox.current(randint(0, 9))
attack_cbox.grid(row=1, column=1)

defense_lbl = tk.Label(root, text='Защита:')
defense_lbl.grid(row=1, column=2)

defense_cbox = ttk.Combobox(root)
defense_cbox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
defense_cbox.state(('readonly',))
defense_cbox.current(randint(0, 9))
defense_cbox.grid(row=1, column=3)

magic_lbl = tk.Label(root, text='Магическая сила:')
magic_lbl.grid(row=1, column=4)

magic_cbox = ttk.Combobox(root)
magic_cbox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
magic_cbox.state(('readonly',))
magic_cbox.current(randint(0, 9))
magic_cbox.grid(row=1, column=5)

knowledge_lbl = tk.Label(root, text='Знания:')
knowledge_lbl.grid(row=2, column=0)

knowledge_cbox = ttk.Combobox(root)
knowledge_cbox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
knowledge_cbox.state(('readonly',))
knowledge_cbox.current(randint(0, 9))
knowledge_cbox.grid(row=2, column=1)

luck_lbl = tk.Label(root, text='Удача:')
luck_lbl.grid(row=2, column=2)

luck_cbox = ttk.Combobox(root)
luck_cbox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
luck_cbox.state(('readonly',))
luck_cbox.current(randint(0, 9))
luck_cbox.grid(row=2, column=3)

spirit_lbl = tk.Label(root, text='Боевой дух:')
spirit_lbl.grid(row=2, column=4)

spirit_cbox = ttk.Combobox(root)
spirit_cbox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
spirit_cbox.state(('readonly',))
spirit_cbox.current(randint(0, 9))
spirit_cbox.grid(row=2, column=5)

exp_lbl = tk.Label(root, text='Опыт:')
exp_lbl.grid(row=3, column=0)

exp_cbox = ttk.Combobox(root)
exp_cbox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
exp_cbox.state(('readonly',))
exp_cbox.current(randint(0, 9))
exp_cbox.grid(row=3, column=1)

artefact_lbl = tk.Label(root, text='Артефакт:')
artefact_lbl.grid(row=3, column=2)

artefact_cbox = ttk.Combobox(root)
artefact_cbox['values'] = func.artifacts
artefact_cbox.state(('readonly',))
artefact_cbox.current(randint(0, 4))
artefact_cbox.grid(row=3, column=3)

characters_lbl = tk.Label(root, text='Осталось персонажей:')
characters_lbl.grid(row=3, column=4)

characters_num_lbl = tk.Label(root, text=randint(5, 20), font='Roboto 14')
characters_num_lbl.grid(row=3, column=5)

ready_btn = tk.Button(root, text='Далее', command=func.new_players,
                      width=5, height=2)
ready_btn.grid(row=4, column=3)
