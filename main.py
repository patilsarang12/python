import data

def user_add_cricketer():
    name=input("Enter cricketer name : ")
    country=input("Enter country: ")
    data.add_cricketers(name,country)

def user_delete_cricketer():
    name=input("Enter cricketer name to delete: ")
    data.delete_cricketers(name)

def show_cricketers():
    players=data.list_all_cricketers()
    print(players)

def user_select_cricketer():
    name=input("Enter cricketer name to display: ")
    for player in data.list_all_cricketers():
        if player["name"]==name:
            print(player)

select_choice="""
1. Add cricketer
2. Delete cricketer
3. Select cricketer
4. Display cricketer
5. Quit
"""

def menu():
    choice=int(input(select_choice))
    while choice!=5:
        if choice==1:
            user_add_cricketer()
        elif choice==2:
            user_delete_cricketer()
        elif choice==3:
            user_select_cricketer()
        elif choice==4:
            show_cricketers()
        else:
            print("Invalid choice")
        choice=int(input(select_choice))

menu()