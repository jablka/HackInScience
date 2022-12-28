# Today is 2015-09-17 and it is 09:34:35.

import datetime

teraz = datetime.datetime.today()

print(
    f'Today is {teraz.strftime("%Y-%m-%d")} and it is {teraz.strftime("%H:%M:%S")}.'
      ) 
