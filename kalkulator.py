

num1= int(input('1- raqamni kiriting:'))
num2= int(input('2-raqamni kiriting:'))

print("Choose calculation: \n",
       "Add \n",
       "Subtract \n",
       "Multiply \n",
       "Divide")

calc = input()

if calc == 'Add':
    ans = num1 + num2
elif calc == 'Subtract':
    ans = num1 -num2
elif calc == 'Multiply':
    ans = num1 * num2
elif calc == 'Divide':
    ans == num1 /num2

print(ans)
