import datetime
import calendar

def friday_the_13th():

    datum = datetime.date.today()

    # či je dnes?
    if datum.day == 13 and datum.weekday() == 4:
        # print(datum)
        return str(datum)
    
    # či je v tomto mesiaci
    elif datum.day < 13:
        day = 13
        month = datum.month
        year = datum.year
        
        future_day = calendar.weekday(year, month, day)
        if future_day == 4:
            vysledok = datetime.date(year, month, day)
            # print(vysledok)        
            return str(vysledok)

    # postupujeme v iterácii mesiacov / rokov
    day = 13
    month = datum.month
    year = datum.year

    vysledok = None
    while not vysledok:
                  
        if month == 12:
            month = 1
            year += 1
        else:
            month +=1

        future_day = calendar.weekday(year, month, day)
        if future_day == 4:
            vysledok = datetime.date(year, month, day)
            # print(vysledok)

    return str(vysledok)