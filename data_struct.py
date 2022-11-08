#Dictionaries are key value pairs, sets are not.
#How do you remove duplicated values? Pass it through sets
#sets do not allow modification
#the only difference between sets and tuples is the type of brackets use
#Tuples can be used to setup a choice list
#enumeratot values

eits = ["Olamide", "Richard", "Emmanuel Odero", "Ahmed", "Sirri"]
eits[1] = "Clinton" 
print(eits [1]) #print(eits [1], eits[-1])

#this is how you make it start from one instead of zero
#remember, index is just a chosen name to represent the function
for index in range (len(eits)):
    print (f"{index + 1} - {eits[index]}")
