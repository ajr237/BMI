def BMI():
    bmi = mass / height **2
    bmi = '%.2f'%bmi
    return bmi

mass = float(input('Mass (kg): '))
height = float(input('Height (m):'))
print('Your BMI is',BMI())
