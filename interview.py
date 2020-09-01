#!/usr/bin/python3

def timeInside(firstTime=str, secondTime=str) -> str:
    """This function takes two strings with a format "hh:mm" and finds the time inside this two times.

    Args:
        firstTime (string, optional): First time to use in the hour range. Defaults to str.
        secondTime (string, optional): Is the second time in the hour range. Defaults to str.

    Returns:
        str: Is the time lapse inside the first time and the second time.
    """
    firstTime = hourToNumber(firstTime)
    secondTime = hourToNumber(secondTime)
    
    if secondTime-firstTime <= 0:
        return '00:00'
    return numberToHour(secondTime-firstTime)


def freeTime(calendar=list, workTime=list) -> list:
    """Takes two lists, the first is the person calendar with the meetings inside and the second is the time
    when the person starts to work and end the work day. The calendar hours has to be inside the work time.

    Args:
        calendar (list, optional): This list have in each iteration a pair of hours with the start and
        end hours for each meeting. the format of every hour have to be "hh:mm". Defaults to list.
        workTime (list, optional): This has to be a list with a pair of hours in the format "hh:mm". 
        Defaults to list.

    Returns:
        list: Returns a list with the free time between the meetings in the calendar, including the
        first and last hours in the work time if is available. Every item in the list is a pair of strings,
        with the start time first, and the duration free time after.
    """
    startWorking = workTime[0]
    endWorking = workTime[1]
    currentMeetingStart = None
    previousMeetingEnd = None
    freeTimeList = []

    for meeting in calendar:  # create free time
        currentMeetingStart = meeting[0]

        if previousMeetingEnd == None:
            freeTimeList.append([startWorking, timeInside(startWorking, currentMeetingStart)])

        elif previousMeetingEnd != None:  # anado la hora libre inicial y el tiempo libre
            freeTimeList.append([previousMeetingEnd, timeInside(previousMeetingEnd, currentMeetingStart)])
        # for next iteration
        previousMeetingEnd = meeting[1]

    #last free time
    freeTimeList.append([previousMeetingEnd, timeInside(previousMeetingEnd, endWorking)])
    return freeTimeList


def hourToNumber(hour=str) -> float:
    """Change a string in the format "hh:mm" to a float value that can be used to do math
    operations with hours and minutes.

    Args:
        hour (string, optional): This has to be a string argument in format "hh:mm". Defaults to str.

    Returns:
        float: Returns a float value with the hour as the integer value, and the minutes as decimals values.
    """
    hourMinute = hour.split(':')
    hour = int(hourMinute[0])
    minute = int(hourMinute[1])
    return hour + minute/60


def numberToHour(number=float) -> str:
    """Use a float value as argument, to make a string time value, in the format "hh:mm"

    Args:
        number (float, optional): This argument has to be a float with the hour as an integer
        and minutes as decimals. Defaults to float.

    Returns:
        str: Returns a string value in the format "hh:mm"
    """ 
    hour = int(number)
    minutes = int((number - int(number))*60)
    if hour >= 10 and minutes < 10:
        return f"{hour}:0{minutes}"
    elif hour < 10 and minutes >= 10:
        return f"0{hour}:{minutes}"
    elif hour < 10 and minutes < 10:
        return f"0{hour}:0{minutes}"
    return f"{hour}:{minutes}"


def possibleMeetings(calendar1=list, workTime1=list, calendar2=list, workTime2=list, meetingDuration=str) -> list:
    """Returns a list of times available for possible meetings in two calendars and two worktimes, in a defined work duration.

    Args:
        calendar1 (list, optional): first person calendar in string pairs. Defaults to list.
        workTime1 (list, optional): start and end time to work for the first person. Defaults to list.
        calendar2 (list, optional): second person calendar in string pairs. Defaults to list.
        workTime2 (list, optional): start and end time to work for the first person. Defaults to list.
        meetingDuration (string, optional): hours and minutes of the meeting in string. Defaults to str.

    Returns:
        list: Hours in string for possible meetings in pairs. [[init1, end1], [init2, end2], ..., [initn, endn]]
    """
    possibleMeetingSpace1 = []
    possibleMeetingSpace2 = []
    meetingDuration = hourToNumber(meetingDuration)
    spaces1 = freeTime(calendar1, workTime1)
    spaces2 = freeTime(calendar2, workTime2)
    finalSpaces = []

    existingTime = None
    for time in spaces1:
        existingTime = hourToNumber(time[1])
        if existingTime >= meetingDuration:
            possibleMeetingSpace1.append(time)
    for time in spaces2:
        existingTime = hourToNumber(time[1])
        if existingTime >= meetingDuration:
            possibleMeetingSpace2.append(time)
    
    # verify if time 1 is inside time 2 or viceversa
    # grafica de como debe ser: i1  i2  f1  f2
    # verifico cual es mayor entre 
    for time in possibleMeetingSpace1:
        initTime1, finishTime1 = hourToNumber(time[0]), hourToNumber(time[0])+hourToNumber(time[1])
        for time2 in possibleMeetingSpace2:
            initTime2, finishTime2 = hourToNumber(time2[0]), hourToNumber(time2[0])+hourToNumber(time2[1])

            if initTime1 > initTime2:
                ti = initTime1
            else:
                ti = initTime2
            if finishTime1 < finishTime2:
                tf = finishTime1
            else:
                tf = finishTime2
            dt = tf - ti
            if dt >= 0:
                finalSpaces.append([numberToHour(ti),numberToHour(tf)])
    
    return finalSpaces
        

def main():
    meetings1 = [
        ['09:00', '10:30'],
        ['12:00', '13:00'],
        ['16:00', '18:00']
    ]
    workTime1 = ['09:00', '20:00']

    meetings2 = [
        ['10:00', '11:30'],
        ['12:30', '14:30'],
        ['14:30', '15:00'],
        ['16:00', '17:00'],
    ]
    workTime2 = ['10:00', '18:30']

    meetingTime = 30

    # here I start...
    meetingTime /= 60
    meetingTime = numberToHour(meetingTime)

    spaces = possibleMeetings(meetings1, workTime1, meetings2, workTime2, meetingTime)
    print(spaces)


if __name__ == "__main__":
    main()
