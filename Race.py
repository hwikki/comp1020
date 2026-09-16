#A2: Horse Race Assignment by Yoon Ju (u1658382)

import graphics
import Dice

class Horse:
    def __init__(self,speed,y,image,window):
        self.x = 20
        self.y = y
        self.image = image
        self.window = window
        self.dice = Dice(speed)

    def move(self):
        self.x += self.dice.roll()

    def draw(self):
        self.image.draw_at_pos(self.window,self.x, self.y)

    def crossed_finish_line(self, x):
        return x <= self.x

def main():
    window = graphics.GraphWin("Horse",700,350)

    horse1_image = graphics.Image(graphics.Point(0, 50), "horse1.png")
    horse2_image = graphics.Image(graphics.Point(0, 150), "horse2.png")
    horse3_image = graphics.Image(graphics.Point(0, 250), "horse3.png")

    horse1 = Horse(3,50,horse1_image,window)
    horse2 = Horse(5,150,horse2_image,window)
    horse3 = Horse(7,250,horse3_image,window)

    horse1.draw()
    horse2.draw()
    horse3.draw()

    finish_line = graphics.Line( graphics.Point(650,0), graphics.Point(650,350) )
    finish_line.draw(window)

    window.getMouse()

    while not (horse1.crossed_finish_line(650) or horse2.crossed_finish_line(650) or horse3.crossed_finish_line(650)):
        horse1.move()
        horse2.move()
        horse3.move()

        window.clear_win()

        horse1.draw()
        horse2.draw()
        horse3.draw()

        finish_line.draw(window)

        graphics.update()

        horse1_crossed = horse1.crossed_finish_line(650)
        horse2_crossed = horse2.crossed_finish_line(650)
        horse3_crossed = horse3.crossed_finish_line(650)

    if horse1_crossed and horse2_crossed:
        print("Tie Horse 1 with Horse 2")
    elif horse1_crossed and horse3_crossed:
        print("Tie Horse 1 with Horse 3")
    elif horse2_crossed and horse3_crossed:
        print("Tie Horse 2 with Horse 3")
    elif horse1_crossed:
        print("Horse 1 is the winner")
    elif horse2_crossed:
        print("Horse 2 is the winner")
    elif horse3_crossed:
        print("Horse 3 is the winner")

    window.getMouse()

if __name__ == "__main__":
    main()



