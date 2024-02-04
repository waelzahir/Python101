from time import time
from datetime import datetime

current = time()
print("Seconds since January 1, 1970: " + f"{current:,}"  + " or " + f"{current:e}" + " in scientific notation")
print(datetime.utcfromtimestamp(current).strftime('%B %d %Y'))
