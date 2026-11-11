#Tip calculator : work out the tip and each person's share of a bill.

def calculate_tip(bill: float, tip_percent: float) -> float: 
    #Return the tip amount for a bill
    return bill * tip_percent/100

def split_bill(bill: float, tip_percent: float, people: int) -> float:
    #Return what each person pays, tip included, rounded to 2 decimal
    if people < 1:
        raise ValueError("people must be atleast one")
    total = bill + calculate_tip(bill, tip_percent)
    return round(total / people, 2)

def ask_number(prompt : str, cast=float, minimum = 0) :
    #keep asking untill the user types a valid number >= minimum.

    while True:
        raw = input(prompt)
        try: 
            value = cast(raw)
        except ValueError:
            print(f" '{raw}' is not a valid number. Try again.")
            continue
        if value < minimum:
            print(f"Please enter a number of at least {minimum}.")
            continue
        return value

def main() -> None:
    print("== Tip Calculator ==")
    bill = ask_number("Bill amount: ")
    tip_percent = ask_number("Tip % (e.g. 10) : ")
    people = ask_number("Number of people : ", cast = int, minimum=1)

    tip = calculate_tip(bill, tip_percent)
    share = split_bill(bill, tip_percent, people)

    print(f"\nTip :      {tip : .2f}")
    print(f"Total :      {bill + tip: .2f}")
    print(f"Each person : {share : .2f}")



if __name__ == "__main__":
    main()


