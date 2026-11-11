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

