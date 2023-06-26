import time
import locale

second = time.time()

locale.setlocale(locale.LC_ALL, '')

# Format the number with thousands separators
integer_part, decimal_part = str(second).split('.')
integer_part = locale.format_string("%d", float(second), grouping=True)
final_str = integer_part + '.' + decimal_part

scientific_notation = "{:.2e}".format(second)

print("Seconds since January 1, 1970: ", final_str," or ", scientific_notation , " in scientific notation")
# Oct 21 2022$
last_format = time.localtime(second)
print(time.strftime("%b %d %Y", last_format))