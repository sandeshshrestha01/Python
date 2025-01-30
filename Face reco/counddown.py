from datetime import datetime
import  time
new_year = datetime(datetime.now().year
                    +1,1,1)
print("Countdown to Happy New Year 2025!")
while datetime.now()<new_year:
    remaining= new_year-datetime.now()
    print(f"\rTime left: {remaining}",end="")
    time.sleep(1)
print("\n Happy New Year 2025!")