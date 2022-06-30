def add_time(start: str, duration: str, wkday=''):
    # split start into list with 3 items: start hour, start min, am/pm
    lststart = start.split()
    ampm = lststart[1]
    lststart = lststart[0].split(':')
    lststart.append(ampm)
    start_hr = int(lststart[0])
    start_min = int(lststart[1])

    # translate 12 hour time format into 24 hour time format
    if ampm == 'PM': start_hr = start_hr + 12
    elif ampm != 'AM':
        new_time = 'Invalid time'
        quit()

    # split duration into list with 2 items: duration hour, duration min
    lstduration = duration.split(':')
    duration_hr = int(lstduration[0])
    duration_min = int(lstduration[1])

    # if any minute is > 60, stop the program
    if start_min > 60 or duration_min > 60:
        new_time = 'invalid minutes'
        quit()

    # adding duration to old time
    newtime_hr = start_hr + duration_hr
    newtime_min = start_min + duration_min
    newtime_day = 0

    # if new time min is > 60, add new hour into newtime
    if newtime_min > 60:
        newtime_hr += newtime_min // 60
        newtime_min = newtime_min % 60
        # newtime_min = f'{newtime_min:02d}'
        # newtime_min = '{:02d}'.format(newtime_min)
    
    # if new time hour is >= 24, add new day number
    if newtime_hr >= 24:
        newtime_day = newtime_hr // 24
        newtime_hr = newtime_hr % 24

    # construct new time in 12 hour format, there's no 00:00 but 12:00 AM
    if newtime_hr > 12:
        newtime_hr -= 12
        ampm = 'PM'
    elif newtime_hr == 12:
        ampm = 'PM'
    elif newtime_hr == 0:
        newtime_hr += 12
        ampm = 'AM'
    else:
        ampm = 'AM'
    new_time = str(newtime_hr) + ':' + str(newtime_min).zfill(2) + ' ' + ampm

    # if the optional starting day of the week has value, add the newtime weekday in
    # defines weekday list
    lstwkday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', \
        'Friday', 'Saturday'] 
    # if optional parameter has value
    if len(wkday) > 0:
        # correct title case
        wkday = wkday.title()
        # get the weekday number from list based on weekday input
        wkday_num = lstwkday.index(wkday)
        # find the residual weekday number 
        newtime_wkday_num = ( wkday_num + newtime_day ) % 7
        # use list to find the correct newtime weekday 
        newtime_wkday = lstwkday[newtime_wkday_num]
        # add weekday into new_time
        new_time += ', ' + newtime_wkday
        # end of if statement for optional parameter

    # add next day or x days later in ()
    if newtime_day == 1:
        new_time = new_time + ' (next day)'
    elif newtime_day > 1:
        new_time = new_time + ' (' + str(newtime_day) + ' days later)'

    return new_time