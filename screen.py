import time 
import random
ascii_number_art = {0: """\
 .d88b.  
.8P  88. 
88  d'88 
88 d' 88 
`88  d8' 
 `Y88P'  
""", 1: """\
 db 
o88 
 88 
 88 
 88 
 VP 
""", 2: """\
.d888b. 
VP  `8D 
   odD' 
 .88'   
j88.    
888888D 
""", 3: """\
d8888b. 
VP  `8D 
  oooY' 
  ~~~b. 
db   8D 
Y8888P' 
""", 4: """\
  j88D  
 j8~88  
j8' 88  
V88888D 
    88  
    VP  
""", 5: """\
  ooooo 
 8P~~~~ 
dP      
V8888b. 
    `8D 
88oobY' 
        
""", 6: """\
   dD   
  d8'   
 d8'    
d8888b. 
88' `8D 
`8888P 
""", 7: """\
d88888D 
VP  d8' 
   d8'  
  d8'   
 d8'    
d8'     
"""}


class screen:
    player_1_score = 0
    player_2_score = 0
    def run(self):
        self.start()

    def __init__(self, screen_x, screen_y) -> None:
        self.screen_x = screen_x
        self.screen_y = screen_y

    def start(self):
        self.looped = 0
        self.player_1_y = (self.screen_y - 2) // 2
        self.player_1_x = 2
        self.player_2_y = (self.screen_y - 2) // 2
        self.player_2_x = self.screen_x - 3
        self.ball_x = (self.screen_x - 2) // 2
        self.ball_y = (self.screen_y - 2) // 2
        self.screen = []
        self.delta_x = random.choice([-2, 2])
        self.delta_y = random.choice([-1, 1])
        self.make_screen()
        self.display()
        time.sleep(1)
        self.loop_board()

    def make_screen(self):
        for y in range(self.screen_y):
            temp_screen = []
            for x in range(self.screen_x):
                if (y == 0 or y == self.screen_y - 1) and (x != 0 or x != self.screen_x - 1):
                    temp_screen.append("▬")
                elif (x == 0 or x == self.screen_x - 1) and (y > 22 or y < 8):
                    temp_screen.append("❚")
                else:
                    temp_screen.append(" ")
            self.screen.append(temp_screen)
    
    def display(self):
        print(ascii_number_art[self.player_1_score])
        for y in range(self.screen_y):
            for x in range(self.screen_x):
                if self.screen[y][x] == "|":
                    self.screen[y][x] = " "
                self.screen[self.player_1_y][self.player_1_x] = "|"
                self.screen[self.player_1_y - 1][self.player_1_x] = "|"
                self.screen[self.player_1_y + 1][self.player_1_x] = "|"

                self.screen[self.player_2_y - 1][self.player_2_x] = "|"
                self.screen[self.player_2_y + 1][self.player_2_x] = "|"
                self.screen[self.player_2_y][self.player_2_x] = "|"
                if self.screen[y][x] == "●":
                    self.screen[y][x] = " "
                self.screen[self.ball_y][self.ball_x] = "●"
            print(str(self.screen[y])[1:-1].replace(',', '').replace('\'', ''))
        print(ascii_number_art[self.player_2_score])
        self.looped += 1

    def loop_board(self):
        while True:
            self.ball_x += self.delta_x
            self.ball_y += self.delta_y
            self.check_collision()
            self.display()
            time.sleep(.1)
            print("\033[H\033[2J")

    def check_collision(self):
        
        if (self.ball_y < 22 and self.ball_y > 8) and (self.ball_x >= self.screen_x - 1):
            if self.player_1_score == 6:
                print("\033[H\033[2J")
                print("""\
                                            
    db   d8b   db d888888b d8b   db d8b   db d88888b d8888b.                  d8888b. db       .d8b.  db    db d88888b d8888b.       db 
    88   I8I   88   `88'   888o  88 888o  88 88'     88  `8D                  88  `8D 88      d8' `8b `8b  d8' 88'     88  `8D      o88 
    88   I8I   88    88    88V8o 88 88V8o 88 88ooooo 88oobY'                  88oodD' 88      88ooo88  `8bd8'  88ooooo 88oobY'       88 
    Y8   I8I   88    88    88 V8o88 88 V8o88 88~~~~~ 88`8b        C8888D      88~~~   88      88~~~88    88    88~~~~~ 88`8b         88 
    `8b d8'8b d8'   .88.   88  V888 88  V888 88.     88 `88.                  88      88booo. 88   88    88    88.     88 `88.       88 
    `8b8' `8d8'  Y888888P VP   V8P VP   V8P Y88888P 88   YD                  88      Y88888P YP   YP    YP    Y88888P 88   YD       VP 
                                            
                                            
                    """)
                exit()
            else:
                self.player_1_score += 1
                self.start()

        if (self.ball_y < 22 and self.ball_y > 8) and (self.ball_x <= 1):
            if self.player_2_score == 6:
                print("\033[H\033[2J")
                print("""\
                                            
    db   d8b   db d888888b d8b   db d8b   db d88888b d8888b.                  d8888b. db       .d8b.  db    db d88888b d8888b.      .d888b. 
    88   I8I   88   `88'   888o  88 888o  88 88'     88  `8D                  88  `8D 88      d8' `8b `8b  d8' 88'     88  `8D      VP  `8D 
    88   I8I   88    88    88V8o 88 88V8o 88 88ooooo 88oobY'                  88oodD' 88      88ooo88  `8bd8'  88ooooo 88oobY'         odD' 
    Y8   I8I   88    88    88 V8o88 88 V8o88 88~~~~~ 88`8b        C8888D      88~~~   88      88~~~88    88    88~~~~~ 88`8b         .88'   
    `8b d8'8b d8'   .88.   88  V888 88  V888 88.     88 `88.                  88      88booo. 88   88    88    88.     88 `88.      j88.    
    `8b8' `8d8'  Y888888P VP   V8P VP   V8P Y88888P 88   YD                  88      Y88888P YP   YP    YP    Y88888P 88   YD      888888D
                                            
                                            
                    """)
                exit()
            else:
                self.player_2_score += 1
                self.start()
        if ((self.ball_x <= self.player_1_x + 1 and self.ball_x >= self.player_1_x - 1) and (self.ball_y <= self.player_1_y + 1 and self.ball_y >= self.player_1_y - 1)):
            self.delta_x *= -1
            if (self.ball_y == self.player_1_y - 1):
                self.delta_y = abs(self.delta_y) * -1
            elif (self.ball_y == self.player_1_y + 1):
                self.delta_y = abs(self.delta_y)
        if ((self.ball_x <= self.player_2_x + 1 and self.ball_x >= self.player_2_x - 1) and (self.ball_y <= self.player_2_y + 1 and self.ball_y >= self.player_2_y - 1)):
            self.delta_x *= -1
            if (self.ball_y == self.player_2_y - 1):
                self.delta_y = abs(self.delta_y) * -1
            elif (self.ball_y == self.player_2_y + 1):
                self.delta_y = abs(self.delta_y)

        if self.ball_x >= self.screen_x - 1 or self.ball_x <= 0:
            self.ball_x = self.ball_x - self.delta_x 
            self.delta_x *= -1
        if self.ball_y >= self.screen_y - 1 or self.ball_y <= 0:
            self.ball_y = self.ball_y - self.delta_y
            self.delta_y *= -1

        if self.looped >= 150:
            if self.delta_x < 0 and self.delta_x < 5:
                self.delta_x -= 1
            elif self.delta_x > 0 and self.delta_x > -5:
                self.delta_x += 1
            if self.delta_y < 0 and self.delta_y < 3:
                self.delta_y -= 1
            elif self.delta_y > 0 and self.delta_y > -3:
                self.delta_y += 1
            self.looped -= 50
