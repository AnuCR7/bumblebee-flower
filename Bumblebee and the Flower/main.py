import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE='Bumblebee and the Flower'

score= 0
gameover=False
startscreen=True

Sprite= Actor ('bumblebee')
Sprite1= Actor ('flower')
def draw ():
    if startscreen:
        screen.fill('blue')
        screen.draw.text('You have 1 minute to hit as many flowers as possible',center=(WIDTH/2,HEIGHT/2),fontsize=30,color='white')
        screen.draw.text('Press SPACE to start',center=(WIDTH/2,HEIGHT/2+50),fontsize=25,color='white')
    else:
        #screen.clear()
        screen.blit('background',(0,0))
        Sprite.draw()
        Sprite1.draw()
        screen.draw.text('score= '+str(score),midtop=(WIDTH/2,10),fontsize=40,color='WHITE')
        if gameover==True:
            screen.fill('blue')
            screen.draw.text('time up your final score is '+str(score),midtop=(WIDTH/2,10),fontsize=40,color='WHITE')

def placebumblebee ():
    Sprite.x=randint(50,(WIDTH-50))
    Sprite.y=randint(50,(HEIGHT-50))
placebumblebee()

def placeflower ():
    Sprite1.x=randint(50,(WIDTH-50))
    Sprite1.y=randint(50,(HEIGHT-50))
placeflower()

def timeup():
    global gameover
    gameover=True

def update():
    global score
    global startscreen
    if startscreen:
        if keyboard.space:
            startscreen=False
    if keyboard.left:
        Sprite.x=Sprite.x-5
    if keyboard.right:
        Sprite.x=Sprite.x+5
    if keyboard.up:
        Sprite.y=Sprite.y-5
    if keyboard.down:
        Sprite.y=Sprite.y+5
        
    if Sprite.colliderect(Sprite1):
        placeflower()
        score=score+1
    


clock.schedule(timeup,60.0) 
    

pgzrun.go()