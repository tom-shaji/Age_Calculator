import datetime

def get_valid_date():
    while True:
        date_str = input("Enter date of birth (YYYY-MM-DD): ").strip()
        try:
            dob = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            if dob > datetime.date.today():
                print("Error: Date of birth cannot be in the future. Please try again.")
            else:
                return dob
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD format (e.g., 1990-05-15).")

def calculate_age(dob):
    today = datetime.date.today()
    
    # Calculate age in years
    years = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        years -= 1
        
    # Calculate age in total months
    months = (today.year - dob.year) * 12 + (today.month - dob.month)
    if today.day < dob.day:
        months -= 1
        
    # Calculate age in total days
    days = (today - dob).days
    
    return years, months, days

def calculate_next_birthday(dob):
    today = datetime.date.today()
    
    # Try to set the birthday to the current year
    try:
        next_bday = dob.replace(year=today.year)
    except ValueError:
        # Handle leap year babies (Feb 29) in non-leap years (set to March 1st)
        next_bday = datetime.date(today.year, 3, 1)
        
    # If the birthday has already passed this year, it's next year
    if next_bday < today:
        try:
            next_bday = dob.replace(year=today.year + 1)
        except ValueError:
            next_bday = datetime.date(today.year + 1, 3, 1)
            
    days_remaining = (next_bday - today).days
    return next_bday, days_remaining

def main():
    print("===================================")
    print("      Python Age Calculator        ")
    print("===================================")
    
    while True:
        print("\n")
        dob = get_valid_date()
        
        years, months, days = calculate_age(dob)
        next_bday, days_remaining = calculate_next_birthday(dob)
        
        print("\n--- Age Details ---")
        print(f"Current age in years : {years} years")
        print(f"Age in months        : {months} months")
        print(f"Age in days          : {days} days")
        
        print("\n--- Next Birthday ---")
        print(f"Next birthday date   : {next_bday.strftime('%Y-%m-%d')}")
        if days_remaining == 0:
            print("Days remaining       : 0 (Happy Birthday! 🎉)")
        else:
            print(f"Days remaining       : {days_remaining} days")
            
        print("-----------------------------------")
        
        choice = input("\nCalculate another person's age? (y/n): ").strip().lower()
        if choice != 'y' and choice != 'yes':
            print("\nThank you for using the Age Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
