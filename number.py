print('hello editor')
list_number = [3,4,5]
# print(dir(list_number))
list_number.append(20)
list_number.sort(reverse=True)
print(list_number)
sum = 0
for num in list_number:
    sum+=num

print(f"sum = {sum}")