salary = float(input("Enter your monthly salary: "))
loan_amount = float(input("Kindly enter the loan amount you are requesting: "))
month = int(input("How many months you are going to pay for the loan? "))

loan_interest = loan_amount * 0.10
monthly_payment = loan_interest * month + loan_amount
loanable_amount = monthly_payment / month

print(f"Your loan interest is: {loan_interest:.2f}")
print(f"Your monthly payment for the loan is: {loanable_amount:.2f}")

if salary >= 30000 and loan_amount <= salary * 10:
    print("You are eligible to avail the loan!")
elif salary < 30000:
    print("Sorry, you are not eligible since your monthly salary is too low.")
elif loan_amount > salary * 10:
    print("Sorry, you are not eligible since your loan amount you are requesting is too high.")