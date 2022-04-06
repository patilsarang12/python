cricketers=[]


def add_cricketers(name,country):
    cricketers.append({"name":name,"country":country})

def delete_cricketers(name):
    for player in cricketers:
        if player["name"]==name:
            cricketers.remove(player)

def list_all_cricketers():
    return cricketers
