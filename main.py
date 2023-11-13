
# створення декоратора обробки помилок

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner

contacts = {}

# функції обробки відповідних команд

@input_error
def handle_hello():
    return "How can I help you?"

@input_error
def handle_add(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Contact {name} added, phone number {phone}"

@input_error
def handle_change(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Phone number for {name} updated. New phone number is {phone}"

@input_error
def handle_phone(command):
    _, name = command.split()
    phone = contacts.get(name, "Contact not found")
    return f"Phone number for {name}: {phone}"

@input_error
def handle_show_all():
    if not contacts:
        return "No contacts added"
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

# основна функція вводу-виводу

def main():
    while True:
        user_input = input("Enter a command: ").lower()
        
        if user_input in ["good bye", "close", "exit", "."]:
            print("Good bye!")
            break

        if user_input == "hello":
            print(handle_hello())

        elif user_input.startswith("add"):
            print(handle_add(user_input))

        elif user_input.startswith("change"):
            print(handle_change(user_input))

        elif user_input.startswith("phone"):
            print(handle_phone(user_input))

        elif user_input == "show all":
            print(handle_show_all())

        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()