# Homework 8 - Problem 2
# Loan Amortization Schedule

P = float(input("Enter the loan amount: "))
r = float(input("Enter the annual interest rate (%): "))
k = int(input("Enter payments per year: "))
N = int(input("Enter number of years: "))

rate = r / 100 / k
total_payments = k * N

if rate == 0:
    payment = P / total_payments
else:
    payment = P * rate / (1 - (1 + rate) ** -total_payments)

balance = P

print("\nLoan Amortization Schedule")
print(f"{'No.':<6}{'Payment':>12}{'Interest':>12}{'Principal':>12}{'Balance':>14}")
print("-" * 56)

for number in range(1, total_payments + 1):
    interest = balance * rate
    principal = payment - interest

    if principal > balance:
        principal = balance
        payment_amount = principal + interest
    else:
        payment_amount = payment

    balance = balance - principal

    print(f"{number:<6}{payment_amount:>12,.2f}{interest:>12,.2f}{principal:>12,.2f}{balance:>14,.2f}")

print("\nLoan paid off!")
