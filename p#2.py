numbers = [5,3,10,100,200,300,400,500,600,700,800,900,50]

max_num=numbers[0]
min_num=numbers[0]
for i in range(1,len(numbers)):
    if numbers[i]>max_num:
     max_num=numbers[i]
    if numbers[i]<min_num:
     min_num=numbers[i]

print(max_num)
print(min_num)


