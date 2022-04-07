import csv

fs=open("c:\\Users\\Shree\\airports.csv","r",encoding='utf-8')
line=fs.readline()
count=0
count_small_airports=0
while line:
    if 'small_airport' in line:
        #print(f"small airport at {count_small_airports}")
        count_small_airports+=1
    count+=1
    line=fs.readline()
print("Count of small airports are ",count_small_airports)
print("Total number of airports are ",count)




"""
fs=open("c:\\users\\shree\\data.csv","r")
data=csv.reader(fs)
print(list(data)) # Note: generator will be consumed!
fs.seek(0) # bring the file pointer to start
print("Total number of records in my csv file ",len(list(data)))
fs.seek(0) # bring the file pointer to start
for record in data: #  Here data is list of lists
    print("Jersey number is ",record[0]) # record is first list
    print("Player name is ", record[1])
    print("country is ", record[2])
fs.close()
"""
