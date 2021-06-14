# phonebook
# python phonebook module 

#!/usr/bin/env python3

phones = {}

def menu():
    print("1. Add a record")
    print("2. Lookup a record")
    print("3. Update a record")
    print("4. Remove a record")
    print("5. List all records")
    print("6. Quit")
    selection = input("Please make your selection from the options above: ")
    if(selection == '1'):
        addRecord()
        menu()
    if(selection == '2'):
        lookupRecord()
        menu()
    if(selection == '3'):
        updateRecord()
        menu()
    if(selection == '4'):
        removeRecord()
        menu()
    if(selection == '5'):
        listRecords()
        menu()
    if(selection == '6'):
        exit(0) 

def addRecord():
    name=input("Who would you like to add?")
    phone = input("What is their phone number?")
    phones[name] = phone
    print("Thanks", name, "has been added successfully to the phonebook")

def lookupRecord():
    name = input("Who do want to look up?")
    if name in phones.keys():
            print("This is", name,"'s number:", phones[name])
    else:
        print(name,"does not exist.")


def removeRecord():
    name = input("Enter name you'd like to remove:")
    if name in phones:
        del phones[name]
    print(name,"has been removed successfully")

def updateRecord():
    name = input("Enter name you'd like to update:")
    phone = input("Enter their phone number to update:")
    if name in phones:
        phones[name] = phone
        print("Thanks", name, "'s has been updated", phones[name])

def listRecords():
    record = phones.items()
    print("Here is your phonebook list:",record)
    

def main():
    print("== Welcome to the Phonebook App ==")
    menu()

if __name__ == "__main__":
    main()
    
