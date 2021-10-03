import pytest
import turtle
def read_pulse():
    pass

def measure_pulse(pulse_1,pulse_2,pulse_3):
    sum_pulse = pulse_1 + pulse_2 + pulse_3
    avg_pulse = sum_pulse / 3
    return avg_pulse

def abnormal(avg_pulse1, avg_pulse2, avg_pulse3, avg_pulse4):
    min_level = 90
    max_level = 126
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
    screen = turtle.getscreen()
    t = turtle.Turtle
    turtle.done()


def test_measure_pulse():
    pass

draw_chart(10,50,40,80)