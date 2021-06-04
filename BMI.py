height = float(input("Enter your height in m: \n"))
weight = float(input("Enter your weight in kg: \n"))

bmi_index = weight / (height ** 2)
#convert to whole number
int_bmi_index = int(bmi_index)

print("Your BODY MASS INDEX is: " + str(bmi_index))
print("Your BODY MASS INDEX is:(whole number) " + str(int_bmi_index))