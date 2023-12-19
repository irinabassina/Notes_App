import datetime
import json


file_path = 'notes.json'


def load_notes(file_path):
    with open(file_path, 'r+') as file:
        notes = json.load(file)
        return notes

notes = load_notes(file_path)
    

def add_note(notes, new_note):            
    max_id = max(note['id'] for note in notes) if notes else 0 
    new_note['id'] = max_id +1
    notes.append(new_note)

    return notes
    
    
def save_notes(notes, file_path):   
    with open(file_path, 'w+') as file:
        json.dump(notes, file, indent=4)
    
def edit_note(notes, note_id, new_date, new_title=None, new_text=None): 
    for note in notes:
        if note['id'] == note_id:
            if new_title:
                note['title'] = new_title
            if new_text: 
                note['text'] = new_text
            if new_date: 
                note['date'] = new_date
            break
    return notes
                
def delete_note(notes, note_id):
    notes[:] = [note for note in notes if note['id'] != note_id]               
    return notes

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%Y-%H:%M:%S")

def main():

    while True:
        
        print("\n    Записная книжка    ")
        print("1. Вывести все заметки")
        print("2. Вывести заметки по дате")
        print("3. Добавить новую заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            print("\n Заметки: ")
            for note in notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['text']}")
                print(f"Дата: {note['date']}")
                print()
                
        elif choice == '2':
            note_date = input("Введите дату для фильтрации заметок в формате dd/mm/yyyy: ")
            note_date = note_date.strip()
            print("\n Заметки: ")
            for note in  [note for note in notes if note_date in note['date']]:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['text']}")
                print(f"Дата: {note['date']}")
                
                print()
            
        elif choice == '3':
            title = input("Введите заголовок заметки: ")
            text = input("Введите текст заметки: ")
            
            new_note = {
            'title' : title,
            'text' : text,
            'date' : get_date()
            }
            add_note(notes, new_note)
            save_notes(notes, file_path)

        elif choice == '4':
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки или оставьте пустым: ")
            new_text = input("Введите новый текст заметки или оставьте пустым: ")
            
            edit_note(notes, note_id, get_date(), new_title, new_text)
            save_notes(notes, file_path)

        elif choice == '5':
            note_id = int(input("Введите ID заметки для удаления: "))
            
            delete_note(notes, note_id)
            save_notes(notes, file_path)
            
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующий вариант.")


if __name__ == "__main__":
    main()
