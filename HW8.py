def import_contacts(filename):
    contacts = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                contacts.append({
                    'last_name': data[0],
                    'first_name': data[1],
                    'middle_name': data[2],
                    'phone_number': data[3]
                })
        print("Контакты успешно импортированы.")
    except FileNotFoundError:
        print("Файл не найден.")
    return contacts


def write_contacts_to_file(contacts, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for contact in contacts:
                file.write(
                    f"{contact['last_name']},{contact['first_name']},{contact['middle_name']},{contact['phone_number']}\n")
        print("Контакты успешно записаны в файл.")
    except IOError:
        print("Ошибка при записи контактов в файл.")


def copy_contact_from_file(source_filename, destination_filename, line_number):
    try:
        with open(source_filename, 'r', encoding='utf-8') as source_file:
            lines = source_file.readlines()
            if 0 < line_number <= len(lines):
                contact_data = lines[line_number - 1].strip().split(',')
                new_contact = {
                    'last_name': contact_data[0],
                    'first_name': contact_data[1],
                    'middle_name': contact_data[2],
                    'phone_number': contact_data[3]
                }
                with open(destination_filename, 'a', encoding='utf-8') as destination_file:
                    destination_file.write(
                        f"{new_contact['last_name']},{new_contact['first_name']},{new_contact['middle_name']},{new_contact['phone_number']}\n")
                print("Контакт успешно скопирован в другой файл.")
                return True
            else:
                print("Указанная строка не существует в файле.")
    except FileNotFoundError:
        print("Файл не найден.")
    except IndexError:
        print("Указанная строка не существует в файле.")
    return False


def delete_contact(contacts, last_name, first_name, middle_name):
    deleted = False
    for contact in contacts:
        if contact['last_name'] == last_name and contact['first_name'] == first_name and contact[
            'middle_name'] == middle_name:
            contacts.remove(contact)
            deleted = True
            print("Контакт успешно удален.")
            break
    if not deleted:
        print("Контакт не найден.")
    else:
        write_contacts_to_file(contacts, "contacts.txt")


def search_contact(contacts, keyword):
    results = []
    for contact in contacts:
        if keyword.lower() in contact['last_name'].lower() or \
                keyword.lower() in contact['first_name'].lower() or \
                keyword.lower() in contact['middle_name'].lower():
            results.append(contact)
    return results


def display_contacts(contacts):
    if not contacts:
        print("Нет контактов для отображения.")
    else:
        print("Список контактов:")
        for i, contact in enumerate(contacts, start=1):
            print(
                f"{i}. Фамилия: {contact['last_name']}, Имя: {contact['first_name']}, Отчество: {contact['middle_name']}, Телефон: {contact['phone_number']}")


def main():
    filename = "contacts.txt"
    contacts = import_contacts(filename)

    while True:
        print("\nМеню:")
        print("1. Вывести все контакты")
        print("2. Добавить новый контакт")
        print("3. Поиск контакта")

        print("4. Копировать контакт из другого файла")
        print("5. Удалить контакт")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            contacts = import_contacts(filename)  # Перечитываем контакты перед отображением
            display_contacts(contacts)
        elif choice == '2':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            contacts.append({
                'last_name': last_name,
                'first_name': first_name,
                'middle_name': middle_name,
                'phone_number': phone_number
            })
            write_contacts_to_file(contacts, filename)
            print("Контакт успешно добавлен.")
        elif choice == '3':
            keyword = input("Введите фамилию, имя или отчество для поиска: ")
            search_results = search_contact(contacts, keyword)
            display_contacts(search_results)

        elif choice == '4':
            source_filename = input("Введите имя файла, из которого нужно скопировать контакт: ")
            line_number = int(input("Введите номер строки контакта для копирования: "))
            if copy_contact_from_file(source_filename, filename, line_number):
                contacts = import_contacts(filename)  # Перечитываем контакты после копирования
        elif choice == '5':
            last_name = input("Введите фамилию контакта для удаления: ")
            first_name = input("Введите имя контакта для удаления: ")
            middle_name = input("Введите отчество контакта для удаления: ")
            delete_contact(contacts, last_name, first_name, middle_name)
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
