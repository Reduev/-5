import random
from datetime import datetime, timedelta
from array import array

current_year = datetime.now().year
start_date = datetime(current_year - 5, 1, 1)
end_date = datetime(current_year, 12, 31)

dates = []
for _ in range(10):
    random_date = start_date + timedelta(
        days=random.randint(0, (end_date - start_date).days)
    )
    dates.append(random_date)

dates.sort()

date_array = array('d', [date.timestamp() for date in dates])

print("Разница между датами:")
for i in range(len(date_array) - 1):
    date1 = datetime.fromtimestamp(date_array[i])
    date2 = datetime.fromtimestamp(date_array[i + 1])
    delta = (date2 - date1).days
    print(f"Разница между {date1.strftime('%Y-%m-%d')} и {date2.strftime('%Y-%m-%d')}: {delta} дней")