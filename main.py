import pytest
import turtle
def read_pulse():
    pulse1 = input("enter first pulse ")
    pulse2 = input("enter second pulse ")
    pulse3 = input("enter third pulse ")
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
    t.left(45)
    t.forward(avg_pulse1)
    t.right(45)
    #pulse2
    if avg_pulse2 < avg_pulse1 :
        t.right(45)
        t.forward(avg_pulse2)
        t.left(45)
    elif avg_pulse2 > avg_pulse1 :
        t.left(45)
        t.forward(avg_pulse2)
        t.right(45)

    #pulse3
    if avg_pulse3 < avg_pulse2 :
        t.right(45)
        t.forward(avg_pulse3)
        t.left(45)
    elif avg_pulse3 > avg_pulse2 :
        t.left(45)
        t.forward(avg_pulse3)
        t.right(45)

    #pulse4
    if avg_pulse4 < avg_pulse3 :
        t.right(45)
        t.forward(avg_pulse4)
        t.left(45)
    elif avg_pulse4 > avg_pulse3 :
        t.left(45)
        t.forward(avg_pulse4)
        t.right(45)


    turtle.mainloop()


def test_measure_pulse():
    pass

draw_chart(60,50,100,80)