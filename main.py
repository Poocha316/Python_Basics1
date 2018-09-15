

def minutes_to_hours(minutes):
    hours = minutes / 60
    print(hours)

def condition1(a,b):
    if a < b:
        print(str(a) + " lower than " + str(b))
    else:
        print(str(a) + " higher than " + str(b))

def loop1():
    list = ['aba','abb','cba','ccc']

    for i in list:
        if 'c' in i:
            print(i)

loop1()