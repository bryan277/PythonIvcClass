def firstName(my_contacts, number):
    # for key in arr:
    #     print(key)
    nameList = []
    for name in my_contacts:
        if my_contacts[name] == number
            nameList.append(name)
        return nameList

def printAll(contacts):
    # for key in arr:
    #     print(key, arr[key])
    print('All names numbers:')
    for key in sorted(contacts):
        print(key, contacts[key])

def main():
    my_contacts = {
    "Fred" : 733243,
    "Marry" : 423423,
    "Bob" : 323432,
    "Robby" : 234323
    }
    nameList = firstName(my_contacts)
    print(nameList)
    nameAllList = printAll(my_contacts)
    print(nameAllList)

for name in nameList:
    print(name, end= '')
# nameList = firstName(my_contacts)
# print(nameList)
main()
