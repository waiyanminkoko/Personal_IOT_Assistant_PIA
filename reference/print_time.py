# Print Time
import time
print(time.strftime("%H:%M:%S"))
print(time.strftime("%d/%m/%Y"))

# Collect Time
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
