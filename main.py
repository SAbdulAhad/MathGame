import random

# number
num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
# operator
operators = ['+', '-', '*']
operator = random.choice(operators)

computer = f'{num1} {operator} {num2}'
print(computer)
ans = ''
if '+' in computer:
    ans = num1 + num2
elif '-' in computer:
    ans = num1 - num2
else:
    ans = num1 * num2

player = int(input('Answer:'))

# statements
gd_stmnts = ['You win!', 'Right answer']
gd_stmnt = random.choice(gd_stmnts)

bd_stmnts = ['You loss!', 'Wrong answer']
bd_stmnt = random.choice(bd_stmnts)

if player == ans:
    print(gd_stmnt)
else:
    print(bd_stmnt)