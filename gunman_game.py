import random

man = ['strong', 'medium', 'weak']
state = [True, True, True]
attack = [0.8, 0.6, 0.4]
final = 0
live = [0, 0, 0]

def judge(pb):
    truth = random.random()
    if pb >= truth:
        return True
    else:
        return False

def kill():
    global state
    num = 0
    for each_item in state:
        state_now = state
        if each_item == True:
            obj = choose(num, state)
            result = judge(attack[each_item])
            if result:
                state_now[obj] = False
        num = num + 1
        state = state_now

def choose(num, state):
    num_ch = 0
    for each_item in state:
        if num_ch != num:
            if each_item == True:
                return num_ch
        num_ch = num_ch + 1

def ifend(state):
    live = 0
    global man
    global final
    live_num = 0
    num = 0
    for each_item in state:
        if each_item == True:
            live = live + 1
            live_num = num
        num = num + 1
    if live == 1:
        final = live_num
        return False
    elif live > 1:
        return True

for i in range (0,100000):
    state = [True, True, True]
    while(ifend(state) == True):
        kill()
    live[final] = live[final] + 1

print(live)