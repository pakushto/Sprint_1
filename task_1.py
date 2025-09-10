string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_time = 0

for i in string.replace(' ', ',').split(','):
    if 'h' in i:
        total_time += int(i.replace('h', '')) * 60
    elif 'm' in i:
        total_time += int(i.replace('m', ''))
    elif 's' in i:
        total_time += int(i.replace('s', '')) // 60

print(total_time)
