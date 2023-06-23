# 2023 Estimated Canadian Income Tax for Individuals - High-level calculation - Project created by Sonia Li

# Mounting Google Drive to Colab
from google.colab import drive
drive.mount('/content/gdrive')  # importing google drive

import sys   # system - specific functions
sys.path.append('/content/gdrive/MyDrive/Colab Notebooks')  # your folder path in Google Drive

import os   # user interactions with operation systems
os.chdir('/content/gdrive/MyDrive/Colab Notebooks')   # currently working path in Google Drive

# Import modules/libraries
import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

# Federal tax rates and income thresholds for 2023:
federal_income_thresholds = [53359, 106717, 165430, 235675]
federal_rates = [0.15, 0.205, 0.26, 0.29, 0.33]
federal_acc_tax = [8003.85, 18942.24, 34207.62, 54578.67]

# Ontario tax rates and income thresholds for 2023:
ontario_income_thresholds = [49231, 98463, 150000, 220000]
ontario_rates = [0.0505, 0.0915, 0.1116, 0.1216, 0.1316]
ontario_acc_tax = [2486.17, 6990.89, 12742.42, 21254.42]

# Federal and Ontario's Basic Personal Amount for 2023:
federal_BPA = int(15000)
ontario_BPA = int(11865)

# Function to calculate (simplified formula) the Federal tax payment for 2023 based on the given income:
def federal_tax(income):
    if income < federal_BPA:
        return int(0)
    elif income <= federal_income_thresholds[0]:
        return float((income * federal_rates[0]) - (federal_BPA * federal_rates[0]))
    elif income <= federal_income_thresholds[1]:
        return float(((income - federal_income_thresholds[0]) * federal_rates[1] + federal_acc_tax[0]) - (federal_BPA * federal_rates[0]))
    elif income <= federal_income_thresholds[2]:
        return float(((income - federal_income_thresholds[1]) * federal_rates[2] + federal_acc_tax[1]) - (federal_BPA * federal_rates[0]))
    elif income <= federal_income_thresholds[3]:
        return float(((income - federal_income_thresholds[2]) * federal_rates[3] + federal_acc_tax[2]) - (federal_BPA * federal_rates[0]))
    else:
        return float(((income - federal_income_thresholds[3]) * federal_rates[4] + federal_acc_tax[3]) - (federal_BPA * federal_rates[0]))

# Function to calculate (simplified formula) the Ontario tax payment for 2023 based on the given income:
def ontario_tax(income):
    if income < ontario_BPA:
        return int(0)
    elif income <= ontario_income_thresholds[0]:
        return float((income * ontario_rates[0]) - (ontario_BPA * ontario_rates[0]))
    elif income <= ontario_income_thresholds[1]:
        return float(((income - ontario_income_thresholds[0]) * ontario_rates[1] + ontario_acc_tax[0]) - (ontario_BPA * ontario_rates[0]))
    elif income <= ontario_income_thresholds[2]:
        return float(((income - ontario_income_thresholds[1]) * ontario_rates[2] + ontario_acc_tax[1]) - (ontario_BPA * ontario_rates[0]))
    elif income <= ontario_income_thresholds[3]:
        return float(((income - ontario_income_thresholds[2]) * ontario_rates[3] + ontario_acc_tax[2]) - (ontario_BPA * ontario_rates[0]))
    else:
        return float(((income - ontario_income_thresholds[3]) * ontario_rates[4] + ontario_acc_tax[3]) - (ontario_BPA * ontario_rates[0]))

# Function to calculate the Canada Pension Plan (CPP) contributions for 2023 based on the given income:
def cpp(income):
    cpp_rate = 0.0595                   # 2023 CPP contribution rate is 5.95%
    cpp_max_pensionable = int(66600)
    cpp_basic_exemption_amt = int(3500)

    if income < cpp_basic_exemption_amt:
        return int(0)
    elif income <= cpp_max_pensionable:
        return float((income - cpp_basic_exemption_amt) * cpp_rate)
    else:
        return float((cpp_max_pensionable - cpp_basic_exemption_amt) * cpp_rate)  # 2023 CPP max contribution is $3,754.45

# Function to calculate the Employment Insurance (EI) premiums for 2023 based on the given income:
def ei(income):
    ei_rate = 0.0163                    # 2023 EI premium rate is 1.63%
    ei_max_insurable = int(61500)

    if income <= ei_max_insurable:
        return float(income * ei_rate)
    else:
        return float(ei_max_insurable * ei_rate)   # 2023 EI max premium is $1,002.45

# Function to create the pie chart:
def pie_chart(numbers, labels, colors):
    plt.title("2023 Income Tax Estimation", fontsize=10)

    # Function to display both the value and percentage in the pie chart
    def autopct_format(values): # defines an inner function named autopct_format. This function is used to format the autopct (automatic percentage) labels for each pie slice
        def my_format(pct): # defines an inner function named autopct_format. This function is used to format the autopct (automatic percentage) labels for each pie slice
            total = sum(values) # calculates the sum of all the values in the numbers list
            val = float(pct * total / 100.0)  #calculates the actual value corresponding to the percentage (pct) of the total sum
            return '${v:,.2f} - {:.1f}%'.format(pct, v=val)
            # formats the autopct label by replacing {v:,.2f} with the value (val) in currency format and {:.1f}% with the percentage (pct) formatted with one decimal place
        return my_format

    plt.pie(numbers, autopct=autopct_format(numbers), textprops={'fontsize': 8},
            colors=colors, labels=labels, startangle=70)
    plt.axis("equal")   # ensures that the pie chart is displayed as a circle (with equal aspect ratio)

    # Function to create a donut for a pie chart:
    circle = plt.Circle(xy=(0, 0), radius=0.75, facecolor="white")  # creates a white circle at the center of the pie chart to give it a donut-like appearance
    plt.gca().add_artist(circle)  # adds the created circle as an artist to the current axes
    plt.show()  # displays the pie chart

# Main code:
if __name__ == '__main__':
    print("2023 Federal and Ontario Tax Estimation Calculator")
    print("\033[1m" "DISCLAIMER: THIS CALCULATOR IS FOR ESTIMATION PURPOSES ONLY. DO NOT USE FOR ACTUAL TAX FILING!" "\033[0m")   #'\033[1m' & '\033[1m' = bold
    print()
    
    # Input name and validate name input:
    name = input("Please enter your name: ")    # Get user input
    while not name.strip(): # Checks if the name, after removing any leading or trailing whitespace, is empty or consists only of whitespace characters
        print("Invalid name. Please enter a valid name.")
        name = input("Please enter your name: ")    # Get user input

    # Input income and validate income input by using try-except statement:
    income = None   # initializes the income variable to None
    while income is None:
        income_input = input("Please enter your estimated annual gross salary for 2023: CAD ")  # Get user input

        try:
            income = float(income_input)

            if income <= 0:
                print("Invalid income. Please enter a positive value.")
                income = None

        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    print("**************************************************\n")

    # Load and display an image
    try:
        img = cv2.imread("tax.jpg")  # Load the image file "tax.jpg" using OpenCV's imread function
        img = cv2.resize(img, (280,210))  # Resize the image to a specific width (280) and height (210)
        cv2_imshow(img)  # Display the image using OpenCV's imshow function
    except Exception as e:
        print(f"Error loading or displaying the image: {str(e)}")  # If any exception occurs during image loading or display, print an error message

    # Calculate total tax and net income
    total_tax = float(federal_tax(income) + ontario_tax(income) + cpp(income) + ei(income))
    net_income = float(income-total_tax)

    # Print the results
    print(f"\nHello {name.title()}! Your estimated tax for 2023:\n")
    print('\033[1m' f"\tTotal Tax: ${float(total_tax):,.2f}" '\033[0m')   #'\033[1m' & '\033[0m' = bold
    print(f"\t - Ferderal Tax: ${float(federal_tax(income)):,.2f}")    # f'{float(number):,.2f}' = format the number with a thousand separator and round it up to two decimal places
    print(f"\t - Ontario Tax: ${float(ontario_tax(income)):,.2f}")
    print(f"\t - CPP Contributions: ${float(cpp(income)):,.2f}")
    print(f"\t - EI Premiums: ${float(ei(income)):,.2f}")
    print()
    print('\033[1m' f"\tNet Income: ${float(net_income):,.2f}" '\033[0m')
    print()
    print(f"\tBi-weekly Income: ${float(net_income/52*2):,.2f}")
    print(f"\tMonthly Income: ${float(net_income/12):,.2f}")
    print()
    print(f"\tAverage Tax Rate: {(total_tax/income)*100:,.2f}%")
    print()

    # Call the pie_chart function
    pie_chart([net_income, ei(income), cpp(income), ontario_tax(income), federal_tax(income)],
              ["Net Income", "EI Premiums", "CPP Contributions", "Ontario Tax", "Federal Tax"],
              ["pink", "gold", "skyblue", "coral", "violet"])

    # Assumptions
    print(f"""Assumptions:
    - This calculator provides a \033[1mhigh-level estimation\033[0m for 2023 Canadian taxes based on the information provided.
    - The calculation is based on the \033[1mannual gross salary\033[0m and does \033[1mNOT\033[0m consider other sources of income.
    - The estimated tax amounts are calculated using the \033[1mtax rates and income thresholds\033[0m for Federal and Ontario taxes in 2023.
    - The \033[1mBasic Personal Amount (BPA)\033[0m for Federal and Ontario taxes in 2023 are considered in the calculations.
    - The \033[1mCanada Pension Plan (CPP) contributions\033[0m and \033[1mEmployment Insurance (EI) premiums\033[0m are calculated based on the provided income.
    - The calculated amounts do \033[1mNOT\033[0m include other tax credits, deductions, or expenses that may apply in your specific situation.
    - This estimation is \033[1mNOT\033[0m intended for actual tax filing purposes. Consult with a tax professional for accurate tax calculations.
    - The estimation results are rounded to two decimal places.
    - The assumptions and calculations are based on the information available at the time of coding (\033[1m2023\033[0m).
    """)

    # Load and display an image
    try:
        img = cv2.imread("greeting.jpg")
        img = cv2.resize(img, (280,280))
        cv2_imshow(img)
    except Exception as e:
        print(f"Error loading or displaying the image: {str(e)}")
