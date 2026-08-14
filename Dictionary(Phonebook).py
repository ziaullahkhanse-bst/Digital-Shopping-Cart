phonebook = {
    "Ali": "0300-1234567",
    "Sara": "0301-7654321",
    "Zia": "0302-9876543",
}

name = input("Enter a name: ")

if name in phonebook:
    print(phonebook[name])
else:
    print("Contact not found!")