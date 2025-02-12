from datetime import datetime, timedelta

# 1
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Текущая дата:", current_date)
print("Дата пять дней назад:", new_date)

# 2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("\nВчера:", yesterday.date())
print("Сегодня:", today.date())
print("Завтра:", tomorrow.date())

# 3
date_without_microseconds = current_date.replace(microsecond=0)
print("\nС микросекундами:", current_date)
print("Без микросекунд:", date_without_microseconds)

# 4
date1 = datetime(2025, 2, 1, 12, 0, 0)
date2 = datetime(2025, 2, 12, 18, 30, 0)
difference = date2 - date1
difference_in_seconds = difference.total_seconds()
print("\nРазница между датами:", difference)
print("Разница в секундах:", difference_in_seconds)
