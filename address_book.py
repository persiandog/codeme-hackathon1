import sys

action = input("Welcome to your address book.\n" "Enter what you would like to do: print all addresses, add new contact, delete contact, or exit programme: ")

#print the whole file
if action == 'print all addresses':
    with open('contact_list.txt') as f:
        content = f.read()
        print(content)

#add new contact
if action == 'add new contact':
    with open('contact_list.txt', 'a', encoding='utf-8') as f:
        new_contact = input("Enter name, phone number and address: ")
        f.writelines(new_contact)
        f.write("\n")

    print("Thank you. Contact added")

#delete contact
if action == 'delete contact':
    contact_to_delete = input("What's the contact name to delete? ")
    with open("contact_list.txt") as f:
        lines = f.readlines()
    with open("contact_list.txt", "w") as f:
        for line in lines:
            if line.strip("\n") not in contact_to_delete:
                f.write(line)
                print("Thank you. Contact deleted.")
            else:
                print("Sorry, no such contact in the file.")

#exit programme
if action == 'exit programme':
    print("Good bye!")
    sys.exit('Closed by user')
