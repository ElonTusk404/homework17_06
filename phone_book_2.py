import json
try:
    with open('contacts.json', 'r') as file:
        db = json.load(file)
except FileNotFoundError:
    db = {}

print('Phone Book Program')
print('------------------')
print('1. Add a new contact\n2. Search for a contact\n3. List all contacts\n4. Exit')
while True:
    try:
        from_user = int(input('Enter your choice:\n'))
    except ValueError:
        print('Invalid input. Please enter a number.')
        continue

    if from_user == 4:
        with open('contacts.json', 'w') as file:
            json.dump(db, file)
        print('Goodbye!')
        break
    if from_user == 1:
        new_name = input('Enter name: ').lower()
        new_number = input('Enter phone number: ')

        if new_name in db:
            print('This contact already exists.')
        elif not new_number.isdigit():
            print('Enter only number.')
        else:
            db[new_name] = new_number
            print('A new contact has been created.')
            with open('contacts.json', 'w') as file:
                json.dump(db, file)
    if from_user == 2:
        key_search = input('Enter name: ').lower()

        if key_search in db:
            print(f'Phone number: {db[key_search]}')
        else:
            print('Contact not found.')
    if from_user == 3:
        if not db:
            print('No contacts found.')
        else:
            print('Contacts:')
            for key, value in db.items():
                print(f'{key} : {value}')
