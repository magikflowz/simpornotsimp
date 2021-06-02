def todolist():
    list = []
    while(True):
        items = input("Add an item to your to do list: ")

        print("type quit to leave the program")
        if (items == 'quit'):
            print(todolist)
            break
        else:
            list.append(items)

todolist()