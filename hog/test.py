from hog import*
def echo_0(s0, s1):
    print('*', s0)
    return echo_0
def echo_1(s0, s1):
    print('**', s1)
    return echo_1

s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=3, say=both(echo_0, echo_1))

