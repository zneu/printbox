import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

class Box:
    def setup_box(self):
        S = ["+ ", "- ", "+",
             "| ", "  ", "|"
        ]

        self.top = ((S[0] + S[1] * self.x)) + S[2]
        self.side = ((S[3] + S[4] * self.x)) + S[5]
        self.bottom = ((S[0] + S[1] * self.x)) + S[2]

    def print_box(self):
        print(self.top)
        while self.x > 0:
            print(self.side)
            self.x -= 1
        print(self.bottom)

    def __init__(self):
        self.setup_box()
        self.print_box()

if __name__ == "__main__":
    while True:
        x = input("Number or [Q]uit \n").lower()
        clear()
        try:
            Box.x = int(x)
        except ValueError:
            clear()
            quit()
        Box()
