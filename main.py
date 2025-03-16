# Logical operator
# and
age = 20
is_student = True
if age < 18 and is_student:
    print('You can go to picnic')
else:
    print('You can not go to picnic')

# # or
age=65
if age < 18 or age > 60:
    print('you can get a discount')
else:
    print('you can not get a discount')

# # not

is_teacher = False
if not is_teacher:
    print('You are a teacher')
else:
    print('You are not a teacher')


# # If statement

name='hania'
if name:'hania'
print('hi my name is hania')

# # else statement

name='rohan'
if name=='hania':
    print('hi my name is hania')
else:
    print('hi my name is rohan')

# # # elif statement

name = 'saima'

if name == 'hania':
    print('hi im hania')

elif name == 'saima':
    print('im saima')

elif name == 'rohan': 
    print('hi my self rohan')

else:
    print('Unknown name')

# # same same but different (name)

name = 'robina'

if name == 'hania':
    print('hi im hania')

elif name == 'saima':
    print('im saima')

elif name == 'rohan': 
    print('hi my self rohan')

else:
    print('Unknown name')


 # Nested if statement

invite=True
age=20

if invite:
    if invite:
        print('you can join the party')
        if age >= 20:
            print('your age is correct')

        else:print('your young')
    else:print('your not invited')

