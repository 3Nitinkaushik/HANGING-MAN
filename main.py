import pygame
import random
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
pygame.display.set_caption("Hanging man")
icon = pygame.image.load("hangman (1).png")
pygame.display.set_icon(icon)
img = pygame.image.load("man-silhouette.png")
rimg = pygame.image.load("gallows.png")
ze = pygame.image.load("0.png")
on = pygame.image.load("1.png")
tw = pygame.image.load("2.png")
th = pygame.image.load("3.png")
fr = pygame.image.load("4.png")
fi = pygame.image.load("5.png")
si = pygame.image.load("6.png")
se = pygame.image.load("7.png")
ei = pygame.image.load("8.png")
ni = pygame.image.load("9.png")
tab = pygame.image.load("table.png")
bg=pygame.image.load("1280x720-horror-pumpkins-halloween_1574941038.jpg")







def man(x,y):
    screen.blit(img,(x,y))
def rope():
    screen.blit(rimg,(271,94))
def printnum(numbers) :
    try:
        screen.blit(numbers[0], (20+10, 500))
        screen.blit(numbers[1], (10+50, 500))
        screen.blit(numbers[2], (10+80, 500))
        screen.blit(numbers[3], (10+110, 500))
        screen.blit(numbers[4], (10+140, 500))
        screen.blit(numbers[5], (10+170, 500))
        screen.blit(numbers[6], (10+200, 500))
        screen.blit(numbers[7], (10+230, 500))
        screen.blit(numbers[8], (10+260, 500))
        screen.blit(numbers[9], (10+290, 500))
    except IndexError:
        pass
def table(m,n):
    screen.blit(tab, (m, n))
def confirm():
    answer = askyesno(title='RESTART THE GAME',
                    message='DO YOU WANT TO PLAY AGAIN?')
    return answer

def lose(ns):
    if ns=="K_0":
        return(pygame.K_0)
    if ns=="K_1":
        return(pygame.K_1)
    if ns=="K_2":
        return(pygame.K_2)
    if ns=="K_2":
        return(pygame.K_2)
    if ns=="K_3":
        return(pygame.K_3)
    if ns=="K_4":
        return(pygame.K_4)
    if ns=="K_5":
        return(pygame.K_5)
    if ns=="K_6":
        return(pygame.K_6)
    if ns=="K_7":
        return(pygame.K_7)
    if ns=="K_8":
        return(pygame.K_8)
    if ns=="K_9":
        return(pygame.K_9)

rep=True

while running:
    if rep == True:
        k=[48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
        l = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
        np = random.randint(0, 9)

        ns = "K" + "_" + str(np)
        l.remove(lose(ns))
        numbers = [ze, on, tw, th, fr, fi, si, se, ei, ni]
        rep=False

        m=390
        n=300
        x=390
        y=200


    screen.fill((102, 255, 102))
    screen.blit(bg,(0,0))
    man(x,y)
    rope()
    printnum(numbers)
    table(m,n)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key not in range(48,58):

                Tk().wm_withdraw()
                messagebox.showinfo("", 'out of option key is pressed')

            elif event.key == lose(ns):
                y=y+100
                m+=100
                screen.fill((102, 255, 102))
                screen.blit(bg, (0, 0))
                man(x, y)
                rope()
                table(m,n)
                printnum(numbers)

                pygame.display.update()
                Tk().wm_withdraw()
                messagebox.showinfo("", 'you lost')
                rep = confirm()

                if rep:
                    __name__ == "__main__"
                else:
                    running=False


            elif len(l)==1:
                ki = k.index(event.key)
                k.pop(ki)
                numbers.pop(ki)
                screen.fill((102, 255, 102))
                screen.blit(bg, (0, 0))
                man(x, y)
                rope()
                table(m, n)
                printnum(numbers)


                pygame.display.update()
                Tk().wm_withdraw()  # to hide the main window
                messagebox.showinfo("", 'congratulations, you have saved the man')
                rep=confirm()
                print(rep)
                if rep:
                    __name__=="__main__"

                else:
                    running=False

            elif event.key in l:
                l.remove(event.key)
                ki=k.index(event.key)
                k.pop(ki)
                numbers.pop(ki)
