import sys
import os
from subprocess import Popen, PIPE, STDOUT
# Test cases for the Shadows of the Knight Episode one

class TestCase:
    def __init__(self, building, turns, position, bomb):
        self.building = building
        self.turns = turns
        self.position = position
        self.bomb = bomb 
        self.bomb_dir = self.bombDir()

    def bombDir(self):
        hero_x, hero_y = map(int, self.position.split())
        bomb_x, bomb_y = map(int, self.bomb.split())
        bomb_location = str()
        if hero_y > bomb_y:
            bomb_location = "U"
        elif hero_y < bomb_y:
            bomb_location = "D"
        if hero_x > bomb_x:
            bomb_location += "L"
        elif hero_x < bomb_x:
            bomb_location += "R"
        return bomb_location + '\n'

    def debug(self):
        print(f"building x={self.bomb.split()[0]} y={self.bomb.split()[1]}\
                turns left: {self.turns}\
                batman position: x={self.position.split()[0]} y{self.position.split()[1]}\
                bomb direction: {self.bomb_dir}\
                ", file=sys.stderr)


if __name__ == "__main__":
    
    solution_dir = "../../codingame/shadows_of_the_knight_ep_1/"
    filename = sys.argv[1]      # file to test
    test_case = sys.argv[2:]    # tescase(s) to run against the file
    
    a_lot_of_jumps = TestCase("4 8", '40', '2 3', '3 7')
    less_jumps = TestCase("25 33", '49', '2 29', '24 2')
    lesser_jumps = TestCase("40 60", "32", "6 6", "38 38")
    tower = TestCase("1 80", "6", "0 1", "0 36")
    correct_cutting = TestCase("50 50", "6", "0 0", "22 22")
    evasive = TestCase("100 100", "7", "5 98", "0 1")
    not_there = TestCase("9999 9999", "14", "54 77", "9754 2531")
    
    building = str.encode(a_lot_of_jumps.building+'\n')
    turns = str.encode(a_lot_of_jumps.turns+'\n')
    position = str.encode(a_lot_of_jumps.position+'\n')
    bomb_location = str.encode(a_lot_of_jumps.bombDir()+'\n')
    bomb = str.encode(a_lot_of_jumps.bomb+'\n')

    p = Popen([f"{solution_dir}{filename}"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    # initial inputs
    p.stdin.write(building)
    p.stdin.flush()
    p.stdin.write(turns)
    p.stdin.flush()
    p.stdin.write(position)
    p.stdin.flush()
    p.stdin.write(bomb_location)
    p.stdin.flush()
    
    # first output
    turns = int(turns)
    while turns > 0:
        msg = p.stdout.readline()
        print(f"Batman jumped to {str(msg)} position")
        a_lot_of_jumps.postion = msg
        p.stdin.write(str.encode(a_lot_of_jumps.bombDir()))
        print(f"the bomb is {a_lot_of_jumps.bombDir()} ({a_lot_of_jumps.bomb})")
        p.stdin.flush()
        turns -= 1
        print(f'turns left: {turns}\n')
        if str(msg) == str(bomb):
            print("Congratulations! Batman defused the bomb.")
            break



