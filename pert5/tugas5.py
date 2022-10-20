#Contoh Program Perulangan

#looping with range
for i in range(1,6):
    print(i)

#looping python with break
for i in range(1,11):
    print(i,"x",i,"=", i*i)
    if i == 10:
        break

#looping python with continue
for i in range(1,11):
    if i == 10:
        continue
    print(i,"x",i,"=", i*i)

#nested loop
listCity = ['Kalimantan', 'Sumatra', 'Sulawesi']
listPlace = ['Barat', 'Utara', 'Selatan']
for city in listCity:
    for place in listPlace:
        print(city, place)

#Penambahan terkait break/continue
for val in "hansen":
    if val == "n":
        continue
    
    print(val)
print ("done")


