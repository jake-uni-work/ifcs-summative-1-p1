
def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        return True
    return False
    

if __name__ == "__main__":
    year = int(input("Please enter a year: "))
    
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is NOT a leap year")