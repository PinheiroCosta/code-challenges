import sys
import os
from subprocess import Popen, PIPE
# Test cases for the Shadows of the Knight Episode one

class TestCase:
    def __init__(self, building, turns, position, bomb):
        self.building = building
        self.turns = int(turns)
        self.position = position
        self.bomb = bomb
        self.bomb_dir = self.bombDir()

    def bombDir(self):
        hero_x, hero_y = self.position.split()
        bomb_x, bomb_y = self.bomb.split()
        bomb_location = str()
        if hero_y > bomb_y:
            bomb_location = "U"
        elif hero_y < bomb_y:
            bomb_location = "D"
        if hero_x > bomb_x:
            bomb_location += "L"
        elif hero_x < bomb_x:
            bomb_location += "R"
        return bomb_location

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
    bomb_dir = str()
    
    a_lot_of_jumps = TestCase("4 8", '40', '2 3', '3 7')
    less_jumps = TestCase("25 33", '49', '2 29', '24 2')
    lesser_jumps = TestCase("40 60", "32", "6 6", "38 38")
    tower = TestCase("1 80", "6", "0 1", "0 36")
    correct_cutting = TestCase("50 50", "6", "0 0", "22 22")
    evasive = TestCase("100 100", "7", "5 98", "0 1")
    not_there = TestCase("9999 9999", "14", "54 77", "9754 2531")

    turns = int(a_lot_of_jumps.turns)

    p = Popen([f"{solution_dir}{filename}"], stdin=PIPE)

    with open(r"./test_case/a_lot_of_jumps.txt", 'r') as case:
        p.stdin.write(case.readlines()[0])
        p.stdin.write(case.readlines()[1])
        p.stdin.write(case.readlines()[2])

    for turn in range(turns):
        p.stdin.write(a_lot_of_jumps.bomb_dir)
        a_lot_of_jumps.debug()
        a_lot_of_jumps.turns -= 1


