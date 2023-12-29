#Importing the python math module
import math

#informing the user of what is expected of them
print("Choose either 'investment' or 'bond' from the menu below to proceed:")

#printing an empty line
print()

#Explaining to the user what their choice means
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

#printing an empty line
print()

#Giving the user the option to enter their choice
calculation_choice = input("Enter your choice as investment or bond: ")

#Converting the users choice to lower case to avoid case sensitivity
calculation_choice = calculation_choice.lower()

#in the case where the user enters investment
if calculation_choice == 'investment':
    
    #Asking the user to enter the amount they would like to invest and ensuring it is upto 2 decimals
    deposit_amount = round(float(input("Enter the amount you would like to deposit: ")))

    #Asking the user for the interest rate
    interest_rate = float(input("Enter the interest rate as a percentage (no % sign, just a number between 0 and 100): "))

    #Asking the user for the number of investment years
    years_of_investment = int(input("Enter the number of years you would like to invest the deposit: "))

    #Asking the user if they would like simple or compound interest
    interest = input("Would you like simple or compound interest?, please enter simple or compound: ")

    #converting interest to lower case
    interest = interest.lower()

    #calculating the amount that the user will get after the given period at simple interest upto 2 decimals
    if interest == 'simple':
        total_amount = round(deposit_amount*(1+(interest_rate/100)*years_of_investment),2)
        print("Your investment in {} years at an interest rate of {}% will be R{}.".format(years_of_investment,interest_rate,total_amount))

    #calculating the amount that the user will get after the given period at compound interest upto 2 decimals
    elif interest == 'compound':
        total_amount = round(deposit_amount*math.pow(1+interest_rate/100,years_of_investment),2)
        print("Your investment in {} years at an interest rate of {}% will be R{}.".format(years_of_investment,interest_rate,total_amount))

    #When the user does not enter the expected interest type the following message will be displayed
    else:
        print("You haven't entered the correct interest type, please enter simple or compound.")

#in the case where the user enters bond
elif calculation_choice == 'bond':
    #Asking the user to enter the present amount of the house upto 2 decimals
    present_value_of_house = round(float(input("Enter the present value of the house: ")),2)

    #Asking the user for the annual interest rate
    annual_interest_rate = float(input("Enter annual interest rate for repayment (no % sign, just a number between 0 and 100): "))

    #Calculating the monthly interest rate
    monthly_interest_rate = (annual_interest_rate/12)/100
    
    #Asking the user for the number of months they will be repaying the house
    months_of_repayment = int(input("Enter the number of months for the repayment of the house: "))

    #Calculating the monthly repayment for the house
    monthly_repayment = round((monthly_interest_rate*present_value_of_house)/(1-math.pow(1+monthly_interest_rate,-months_of_repayment)),2)

    #Displaying the monthly repayment of the house
    print("Your monthly repayment for a house costing R{} at a monthly interest rate of {}% paid over {} months will be R{}.".format(present_value_of_house,round(monthly_interest_rate*100,4),months_of_repayment,monthly_repayment))
    
#in the case where the user does not enter bond or investment
else:
    print("You have entered an incorrect input, please enter investment or bond.")
