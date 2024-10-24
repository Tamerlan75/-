import json

comm = input("Что вы хотите сделать?: ")
# Функция для создания заметки
def create_note(notes):

    with open("notes.json", "w", encoding='utf-8') as file:
        json.dump(notes, file)

# Функция для чтения заметки
def read_notes():
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)
        return notes

# Функция для добавления заметки
def add_note(notes):
    with open("notes.json", "w", encoding='utf-8') as file:
        json.dump(notes, file)

# Функция для удаления заметки
def del_note(id_del, notes):
    for item in notes:
        for value in item.values():
            if value == id_del:
                notes.remove(item)
                create_note(notes)
    #print(notes)

# Функция для редактирования заметки
def edit_note(id_edit, notes, change, ed):
    for item in notes:
        for value in item.values():
            if value == id_edit:
                item.update(dict([(ed, change)]))
                create_note(notes)
    #print(notes)


# Создание заметки
if comm == "Создать заметку":
    notes = []
    note = {}
    i = input("Введите id заметки: ")
    note['id'] = i
    t = input("Введите title заметки: ")
    note['title'] = t
    cont = input("Введите тело заметки: ")
    note['content'] = cont
    d = input("Введите дату создания заметки: ")
    note['date'] = d
    notes.append(note)
    print(notes)
    create_note(notes)
# Чтение заметки
elif comm == 'Прочитать заметки':
    print(read_notes())
# Добавление заметки
elif comm == 'Добавить заметку':
    notes = read_notes()
    note = {}
    i = input("Введите id заметки: ")
    note['id'] = i
    t = input("Введите title заметки: ")
    note['title'] = t
    cont = input("Введите тело заметки: ")
    note['content'] = cont
    d = input("Введите дату добавления заметки: ")
    note['date'] = d
    notes.append(note)
    print(notes)
    add_note(notes)
# Удаление заметки
elif comm == 'Удалить заметку':
    notes = read_notes()
    id_del = input("Введите id удаляемой заметки: ")
    del_note(id_del, notes)
# Редактирование заметки
elif comm == "Редактировать заметку":
    notes = read_notes()
    id_edit = input("Введите id редактиркемой заметки: ")
    ed = input("Что необходимо отредактировать?: ")
    if ed == 'title':
        change = input("Ведите новый заголовок: ")
        edit_note(id_edit, notes, change, ed)
    if ed == 'content':
        change = input("Введите новый контент: ")
        edit_note(id_edit, notes, change, ed)










