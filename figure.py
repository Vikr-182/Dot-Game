import pygame
import random
pygame.init()

done = False

size = (500,500)
screen = pygame.display.set_mode(size)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


# Create an empty array
snow_list = []
 
for i in range(100):        
    x = random.randrange(0, 500)
    y = random.randrange(0, 500)
    snow_list.append([x, y]) 
     
 
speed = 0
change = 1
size = 5

f = open("A.txt","a")

if f is None:
    f = open("A.txt","x")
        

def draw_stick_figure(x,y):
    # Left most points of the figure
    
    #       0,0             0,5             0,10
    #       5,0             O 
    #                      \|/ 
    #                     _/ \_              
    #                       

    pair = (x,y)
    pygame.draw.circle(screen,WHITE,(x+5,y+5),5)            # head 
    pygame.draw.line(screen,BLACK,(x+5,y+10),(x+5,y+20))    # torso
    pygame.draw.line(screen,BLACK,(x+5,y+15),(x-15,y+6))    # left-arm
    pygame.draw.line(screen,BLACK,(x+5,y+15),(x+25,y+6))    # right-arm
    pygame.draw.line(screen,BLACK,(x+5,y+15),(x+5,y+20))    # below-the-belt 
    pygame.draw.line(screen,BLACK,(x+5,y+20),(x+1,y+35))    # left-leg
    pygame.draw.line(screen,BLACK,(x+5,y+20),(x+9,y+35))    # right-leg

clock = pygame.time.Clock()

count = 0

oldx = 0
oldy = 0

while not done:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            done  = True
    screen.fill(WHITE)
    pair = pygame.mouse.get_pos()
    x = pair[0]
    y = pair[1]
   # draw_stick_figure(x,y) s
    pygame.draw.circle(screen,RED,(x,y),5)        
    
    count += 1
    
   # print("score is",end=" ")
   # print(count)
    for d in snow_list:
   #     print(d[0],end=" ")
    #    print(d[1])
    #    print(x,end=" ")
    #   print(y)
        if x >= d[0]-size and x <= d[0]+size and y >= d[1]-size and y <= d[1]+size:
            done = True
            print("You lose")
            print(x,end=" ")
            print(y)
  #      print("done")
   
    
    if count%100 is 0:
        speed += 1
# Loop 50 times and add a snow flake in a random x,y position
    
#        size += change
        # Process each snow flake in the list
        #if size > 3 or size < 1:
         #   change *= -1

       
   
    for i in range(len(snow_list)):

            # Draw the snow flake            
        pygame.draw.circle(screen,BLACK, snow_list[i], size)
    
            # Move the snow flake down one pixel
        snow_list[i][1] += (speed)
    
    
            # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 500:
                # Reset it just above the top
            y = random.randrange(-10, -5 )
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 500)
            snow_list[i][0] = x
   
 
       
    pygame.mouse.set_visible(False)
    pygame.display.flip()
    clock.tick(60)
    
maxscore = 0
print("Your score is ",count)
f.write(str(count))
f.write('\n')

g = open("A.txt","r")
key = 1
maxscore = count
for line in g:
    if(int(line)>=maxscore):
        key = 0
        maxscore = int(line)      

if key is 1:
    print("You crossed the high score yay ")
    print("New high score is ",end=" ")
    print(maxscore)
else:
    print("Keep trying harder")
    print("High score is ",end=" ")
    print(maxscore)
pygame.quit()
