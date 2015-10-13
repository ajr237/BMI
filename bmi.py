def BMI():
    bmi = mass / height **2
    bmi = '%.2f'%bmi
    return bmi

mass = float(input('Mass: '))
height = float(input('Height:'))
print('Your BMI is',BMI())
