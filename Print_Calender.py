from calendar import TextCalendar

year = int(input('Enter Year:'))  # Nhập năm
cal = TextCalendar()              # Tạo đối tượng lịch dạng text
print(cal.formatyear(year, 2, 1, 8, 3))  