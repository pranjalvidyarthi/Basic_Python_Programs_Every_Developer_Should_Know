from datetime import datetime #importing datetime from datetime module
# current time display
current_time = datetime.now().strftime('%H:%M:%S')

print(f'Current Time : {current_time}')