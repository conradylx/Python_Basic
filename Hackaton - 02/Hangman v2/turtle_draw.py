import time
import turtle


def print_hangman(counter: int, final: bool):
    hangman = turtle.Turtle()
    hangman.hideturtle()
    hangman.speed(0)

    if final:
        hangman.clear()
        hangman.pencolor("red")

    for count in range(counter):
        if count == 0:
            hangman.lt(180)
            hangman.fd(200)
            hangman.rt(180)

        elif count == 1:
            hangman.fd(100)
            hangman.lt(90)
            hangman.fd(240)

        elif count == 2:
            hangman.rt(90)
            hangman.fd(150)

        elif count == 3:
            hangman.rt(90)
            hangman.fd(50)

        elif count == 4:
            hangman.rt(85)
            hangman.circle(10)
            hangman.lt(85)
            hangman.penup()
            hangman.fd(20)
            hangman.pendown()

        elif count == 5:
            hangman.fd(50)
            hangman.rt(35)
            hangman.fd(50)
            hangman.lt(180)
            hangman.fd(50)

            hangman.rt(115)
            hangman.fd(50)
            hangman.lt(180)
            hangman.fd(50)

        elif count == 6:
            hangman.rt(30)
            hangman.fd(40)
            hangman.lt(90)
            hangman.fd(40)
            hangman.lt(180)
            hangman.fd(80)

        elif count:
            if not final:
                print_hangman(counter, True)
                time.sleep(7)
                turtle.done()


if __name__ == '__main__':
    print_hangman(9, False)
