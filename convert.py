import sys
print(sys.argv)
if len(sys.argv)!=3:
    print("Please provide only 2 arguments!")
    sys.exit(1)
"""
print("Name of your script is ",sys.argv[0])
print("First argument is ",sys.argv[1])
print("Second argument is ",sys.argv[2])
print("Total number of arguments ",len(sys.argv))
"""
mystring=sys.argv[1]
action=sys.argv[2]
if action=="upper" or action=="UPPER":
    print(mystring.upper())
elif action=="lower" or action=="LOWER":
    print(mystring.lower())
else:
    print("invalid action!")
