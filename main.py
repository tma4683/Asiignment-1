import pytest
import turtle
def read_pulse():
    pulse1 = int(input("enter first pulse :"))
    pulse2 = int(input("enter second pulse :"))
    pulse3 = int(input("enter third pulse :"))
    return pulse1, pulse2, pulse3

def measure_pulse(pulse_1,pulse_2,pulse_3):
    sum_pulse = pulse_1 + pulse_2 + pulse_3
    avg_pulse = sum_pulse / 3
    return avg_pulse

def abnormal(avg_pulse1, avg_pulse2, avg_pulse3, avg_pulse4):
    min_level = 60
    max_level = 90
    if avg_pulse1 < min_level or avg_pulse1 > max_level:
        return 1
    elif avg_pulse2 < min_level or avg_pulse2 > max_level:
        return 2
    elif avg_pulse3 < min_level or avg_pulse3 > max_level:
        return 3
    elif avg_pulse4 < min_level or avg_pulse4 > max_level:
        return 4
    else :
        return None

def warning_doctor(abnormal_hour):
    print("this patient has abnormal levels at hour " + str(abnormal_hour))

def draw_chart(avg_pulse1, avg_pulse2, avg_pulse3, avg_pulse4):

    t = turtle.Turtle()
    #pulse1
    t.left(90)
    t.forward(avg_pulse1)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(avg_pulse1)
    t.right(180)
    #pulse2
    t.forward(avg_pulse2)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(avg_pulse2)
    t.right(180)
    #pulse3
    t.forward(avg_pulse3)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(avg_pulse3)
    t.right(180)
    #pulse4
    t.forward(avg_pulse4)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(avg_pulse4)
    t.right(180)
    t.left(90)
    t.forward(120)

    turtle.mainloop()

# these are the TDD functions
def test_measure_pulse():
    pulse1, pulse2, pulse3 = read_pulse()
    measure_pulse(pulse1, pulse2, pulse3)
    assert pulse1 >= 0 and pulse2 >= 0 and pulse3 >= 0

def test_abnormal() :
    print("hour 1")
    pulse1, pulse2, pulse3 = read_pulse()
    avg_hour1 = measure_pulse(pulse1, pulse2, pulse3)
    print("hour 2")
    pulse1, pulse2, pulse3 = read_pulse()
    avg_hour2 = measure_pulse(pulse1, pulse2, pulse3)
    print("hour 3")
    pulse1, pulse2, pulse3 = read_pulse()
    avg_hour3 = measure_pulse(pulse1, pulse2, pulse3)
    print("hour 4")
    pulse1, pulse2, pulse3 = read_pulse()
    avg_hour4 = measure_pulse(pulse1, pulse2, pulse3)

    min_level = 60
    max_level = 90
    hour1 = avg_hour1 >= min_level and avg_hour1 <= max_level
    hour2 = avg_hour2 >= min_level and avg_hour2 <= max_level
    hour3 = avg_hour3 >= min_level and avg_hour3 <= max_level
    hour4 = avg_hour4 >= min_level and avg_hour4 <= max_level

    result = abnormal(avg_hour1,avg_hour2,avg_hour3,avg_hour4)
    if hour1 and hour2 and hour3 and hour4:
        assert result == None

def main() :
    print("hour 1")
    pulse1, pulse2, pulse3 = read_pulse()
    avg_hour1 = measure_pulse(pulse1, pulse2, pulse3)
    print("average for hour 1 is :" + str(avg_hour1))
    print("hour 2")
    pulse1, pulse2, pulse3 = read_pulse()
    avg_hour2 = measure_pulse(pulse1, pulse2, pulse3)
    print("average for hour 2 is :" + str(avg_hour2))
    print("hour 3")
    pulse1, pulse2, pulse3 = read_pulse()
    avg_hour3 = measure_pulse(pulse1, pulse2, pulse3)
    print("average for hour 3 is :" + str(avg_hour3))
    print("hour 4")
    pulse1, pulse2, pulse3 = read_pulse()
    avg_hour4 = measure_pulse(pulse1, pulse2, pulse3)
    print("average for hour 4 is :" + str(avg_hour4))

    result = abnormal(avg_hour1, avg_hour2, avg_hour3, avg_hour4)
    if result != None :
        warning_doctor(result)
    draw_chart(avg_hour1, avg_hour2, avg_hour3, avg_hour4)

main()



