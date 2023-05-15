#1
numbers = [int(input("Enter an item: ")) for _ in range(5)]
print(numbers)

#2
numbers = [1,2,3,4,5]
numbers.pop()
print(numbers)

#3
num = [int(input("Enter an item: ")) for _ in range(10)]
nu_one = int(input("Enter an item: "))
num.count(nu_one)
print(num.count(nu_one))

#4
numbers_one = int(input("Enter an item: "))
numbers_one = [numbers_one]
numbers = [int(input("Enter an item: ")) for _ in range(4)]
num = numbers_one + numbers
rev = num[::-1]
print(rev)

#5

A = []
C = []
for i in range(5):
    number = int(input(f'Enter number #{i}:'))
    C.append(number)
    if number > 5:
        print(number)

#6
numbers_one = int(input("Enter an item: "))
numbers_one = [numbers_one]
numbers_two = [int(input("Enter an item: ")) for _ in range(4)]
numbers = numbers_one + numbers_two
max = numbers[0]
min = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    elif numbers[i] < min:
        min = numbers[i]
print(max,'max numbers')
print(min, 'min numbers')


#7
text = 'eQ_e1+%ew14rgr454gj'
digit_counter = 0
for i in text:
    if i.isdigit():
        digit_counter += 1
if digit_counter == 0:
    print("number not found")
else:
    print(digit_counter)
