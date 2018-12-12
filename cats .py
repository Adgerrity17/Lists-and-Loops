#All of my cats page 84 of automate the boring stuff
#Working with lists
#Generating inputs to put into the list
#print("Enter the name of cat 1: ")
#cat1 = input()
#print("Enter the name of cat 2: ")
#cat2 = input()
#print("Enter the name of cat 3: ")
#cat3 = input()
#print("Enter the name of cat 4: ")
#cat4 = input()
#print("Enter the name of cat 5: ")
#cat5 = input()
#print("Enter the name of cat 6: ")
#cat6 = input()



#However you can simplify this process below

catNames = []
while True:
    print(('Enter the name of cat ' + str(len(catNames) + 1)) + '(Or enter nothing to stop.): ')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatination
print('The cat names are:')
for name in catNames:
    print('  ' + name)