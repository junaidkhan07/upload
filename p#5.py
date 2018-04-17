#Changing, Adding, and Removing Elements
subject=[]

subject.append('Data Structure & Algo')
subject.append('Basic Electronics')
subject.append('HRM')
subject.append('EnglishIII')
subject.append('OOAD')
subject.append('Diff.Equation')
print(subject)
#Inserting Elements into a List
subject.insert(6,'calculus')
print('\t\nINSERTING IN ELEMENT')
print(subject)
#Removing an Item Using the del Statement
del subject[6]
print('\t\nDELETING ELEMENT')
print(subject)