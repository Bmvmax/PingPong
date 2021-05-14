from pygame import *
window = display.set_mode((700, 500))
run = True
display.set_caption("sdsdsd")
game = True
a = (34, 0, 255)
window.fill(a)
finish = False

FPS = 60
clock = time.Clock()

while game:
   for e in event.get():
        if e.type == QUIT:
            game = False

   if finish != True:
      window.fill(a)



   display.update()
   clock.tick(FPS)