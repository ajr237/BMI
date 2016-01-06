def BMI(mass, height):
	"""Calculates an individual's BMI, calculated from height (m) and mass (kg)"""
	bmi = mass / height **2
	bmi = round(bmi,2)
	return bmi
	
def bmi_class(bmi_score):
	"""Classifies a BMI score"""
	if bmi_score <18.5:
		bmi_class = 'Underweight'
	else:
		bmi_class = 'Will finish later'
	return bmi_class

while True:
	if __name__ == '__main__':
		while True:
			try:			
				mass = float(input('Mass (kg): '))
				if mass == '': 
					break   #Exits program when user enters a blank entry.
				height = float(input('Height (m): '))
				if height == '':
					break
			except ValueError:
				print('Value must be a number. Please retry')
				break
			except NameError:
				print('name error')
				break
			except:
				print('An unknown error has occurred')
				
			print('Your BMI is',BMI(mass, height), 'This is classified as', bmi_class(BMI(mass, height)))
