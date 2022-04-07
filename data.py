import csv

#cricketers=[]
cricketers_file="cricketers_data.csv"

#[{"name":'sachin',"country":'india'},{"name":'gayle',"country":'west indies'}]

def create_cricketers_file():# Note: create the database
    with open(cricketers_file,"a") as fs:
        pass

def add_cricketers(name,country):
    #cricketers.append({"name":name,"country":country})
    with open(cricketers_file,"a",newline="") as fs:
        data=csv.writer(fs)
        data.writerow([name,country])

def delete_cricketers(name):
    #for player in cricketers:
        #if player["name"]==name:
            #cricketers.remove(player)
    cricketers=list_all_cricketers()
    with open(cricketers_file,"w") as fs:
        cricketers=[ player for player in cricketers if player["name"]!=name ]
        for player in cricketers:
            fs.write(f"{player['name']},{player['country']}\n")

def list_all_cricketers():
    #return cricketers
    with open(cricketers_file, "r") as fs:
        all_rows=csv.reader(fs)
        return [{"name":each_list[0],"country":each_list[1]} for each_list in all_rows]



