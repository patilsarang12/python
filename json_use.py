import json

with open("json_test.json","r") as fp:
    """
    data=fp.read()
    print(type(data)) # Note: read() functions return class str obj
    print("using json.loads(str) to read...")
    mydata=json.loads(data) # loads() will take str obj and convert into dict
    print(mydata['myinfo']['technologies']['skills'])  # Parse your dict using for loop and []
    for skills in mydata['myinfo']['technologies']['skills']:
        print(skills,end=" ")
    
    fp.seek(0) # Note: bring file pointer to the beginning as it has reached the end with read()
    """
    print("Using json.load(fp) to read ...")
    mydata=json.load(fp) # load() will take file pointer and read from file directly
    print(mydata['myinfo']['technologies']['skills'])  # Parse your dict using for loop and []
    mydata['myinfo']['technologies']['skills'][0]="java"
    mydata['myinfo']['technologies']['skills'][1]="dotnet"
    mydata['myinfo']['technologies']['skills'][2]="shell scripting"

    for skills in mydata['myinfo']['technologies']['skills']:
        print(skills, end=" ")
    fp.seek(0)
    json_string=json.dumps(mydata)
    print(json_string) # obj of type dict


with open("new_json_file.json","w") as fs:
    json.dump(mydata,fs,indent=4)  #use indent kwarg to format your json file properly
