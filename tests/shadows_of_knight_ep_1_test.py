import sys

# Test cases for the Shadows of the Knight Episode one

def a_lot_of_jumps():
    print("4 8", file=sys.stdin)
    print("40", file=sys.stdin)
    print("2 3", file=sys.stdin)
    
def less_jumps():
    pass

def lesser_jumps():
    pass

def tower():
    pass

def correct_cutting():
    pass

def evasive():
    pass

def not_there():
    pass


if __name__ == "__main__":
    # list of all arguments
    test_list = [a_lot_of_jumps(), less_jumps(), lesser_jumps(), tower(), correct_cutting(), evasive(), not_there()]
    args = sys.argv[1:]

    if len(args) == 0:
        # if no argument is given
        # print all test cases
        print('no argument given')
        for test in test_list:
            test
    else:
        # print only the selected ones
        print(len(args), "args given")

    

