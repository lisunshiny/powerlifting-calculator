from percentages import WEEKS, WEEKS_BENCH
from weights import *

SQUAT_1RM = 105
BENCH_1RM = 105
DEADLIFT_1RM = 165
PRESS_1RM = 77.5

def print_for(weight_name, weight_1rm, curr_week, bench=False):
    # print(get_percentage_1rm_plates(weight_1rm, .9))
    percents = WEEKS[curr_week - 1]
    percents_bench = WEEKS_BENCH[curr_week - 1]
    print("" + weight_name + "")
    print("")
    if bench:
        percents = percents_bench
    for percent,amt in percents:
        
        # print(get_percentage_1rm_plates(weight_1rm, percent))
        # print(str("{:.1f}".format(get_percentage_1rm_amt(weight_1rm, percent, amt))) + " lbs per side" )
        get_percentage_1rm_amt(weight_1rm, percent, amt)
        print("")



for week in range(1,7):
    print_for("BACK SQUAT", SQUAT_1RM, week)
    print_for("BENCH", BENCH_1RM, week)    
    print_for("DEADLIFT", DEADLIFT_1RM, week)
    print_for("STRICT PRESS", PRESS_1RM, week)
    print_for("BENCH", BENCH_1RM, week, True)

    print("")
    print("")
# print_for("squat", SQUAT_1RM, 1)