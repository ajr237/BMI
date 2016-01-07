def BMI(mass, height):
	"""Calculates an individual's BMI, calculated from height (m) and mass (kg)"""
	bmi = mass / height **2
	bmi = round(bmi,2)
	return bmi
	
def bmi_class(bmi_score):
	"""Classifies a BMI score"""
	if bmi_score <18.5:
		bmi_class = 'Underweight'
	elif bmi_score >=18.5 and bmi_score <25:
		bmi_class = 'Healthy Weight'
	else:
		bmi_class = 'Will finish later'
	return bmi_class

while True:
	if __name__ == '__main__':
		while True:
			try:			
				mass = input('Mass (kg): ')
				if mass == '': 
					break   #restarts program when user enters a blank entry.
				mass = float(mass)
				
				height = input('Height (m): ')
				if height == '':
					break	#restarts program when user enters a blank entry.
				height = float(height)
				
				if BMI(mass, height) <220:					
					print('Your BMI is',BMI(mass, height), 'This is classified as', bmi_class(BMI(mass, height)))
				else:
					print('values entered have resulted in a BMI far too large for any human being. this is not designed for elephants.'.title())
			except ValueError:
				print('value must be a number. please retry'.title())	#restarts when any value other than a number is entered.
			except:
				print('an unknown error has occurred'.title())	#catches any other unknown exception.
				
