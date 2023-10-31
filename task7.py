import calendar

# Проверка, является ли 2027 год високосным
is_leap = calendar.isleap(2027)
print(f"2027 год является високосным: {is_leap}")

# Определение дня недели для 25 июня 1995 года
day_of_week = calendar.weekday(1995, 6, 25)
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
print(f"25 июня 1995 года был {days[day_of_week]}")

# Вывод календаря на 2023 год
cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatyear(2023))
