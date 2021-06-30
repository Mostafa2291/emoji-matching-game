import os
from random import shuffle, randint 
from guizero import App, Picture, Box, PushButton, Text, warn, info

def decrease():
    timer.value = int(timer.value) - 1
    if int(timer.value) == 0:
        timer.cancel(decrease)
        result.value = "game over"
        
        over = warn("Game over", "You have ran out of time :(")
        timer.value = time
        played.value = "0"
        result.value = ""
        points.value = "0"
        bpoint.value = "0"
        setup_round()
        timer.repeat(1000, decrease)

         
def match_emoji(matched):
    if matched:
        result.value = "correct" #shows the word correct if you got the emoji correctly
        played.value = int(played.value) + 1 #gives you the amount of rounds played
        points.value = int(points.value) + 1 #gives you the score 
        bpoint.value = int(bpoint.value) + 1 #shows you the bonus counter
        timer.value  = int(timer.value)  + 3 #gives you bonus time everytime you get something correct
    else:
        result.value= "incorrect"
        played.value = int(played.value) + 1 #shows rounds played
        points.value = int(points.value) - 1 #reduces the amount of points u have by one everytime u make a mistake
        bpoint.value = 0                     #resets the bonus counter to 0 if u make a mistake

    if int(bpoint.value) == 3:               
        points.value = int(points.value) + 1 #if the bonus counter reaches 3 u get an extra point
        timer.value = int(timer.value) + 5   #adds 5 seconds to the extra point
        congrat = info("Congratulations", "You got 1 bonus point, you can try reach 7 in a row for 3 bonus points!!!") #informs you that u can still get more bonus points if you get 7 in a row
        
    elif int(bpoint.value) == 7:
         points.value = int(points.value) + 3#adds 3 points if u reach 7 in a row
         timer.value = int(timer.value) + 20 #adds 20 extra seconds if u reach 7 in a row
         congrat1 = info("Congratulations", "You got 3 bonus points!! your bonus counter will reset now")
    elif int(bpoint.value) >=7: #resets the bonus counter after you reach 7 in a row
        bpoint.value = 0
    setup_round()
    
# assigns the random pictures to to the buttons     
def setup_round():
    for picture in pictures:
        picture.image = emojis.pop()
    for button in buttons:
        button.image = emojis.pop()
        button.update_command(match_emoji, [False])
    
    matched_emoji = emojis.pop()
    random_picture = randint(0,15)
    pictures[random_picture].image = matched_emoji
    random_button = randint(0, 15)
    buttons[random_button].image = matched_emoji
    buttons[random_button].update_command(match_emoji, [True])
    
# widgets are made
app = App("emoji game", width = 750 ,height= 500)
time = app.question("Hello!", "What do you want your time to be?", initial_value = 50)

result = Text(app)
timer = Text(app, text = time , align = 'bottom')
count = Text(app, text = "Timer: ", align = 'bottom')
points = Text(app, text = "0",align = "bottom")
score = Text(app, text= "Score: ", align =  "bottom")
rounds = Text(app, text = "Rounds Played: ", align = "top")
played = Text(app, text = 0, align = "top")
bpoint = Text(app, text = 0, align = "right")
Bonus = Text(app, text = "Bonus counter: ", align = "right")

emojis_dir = "emojis"
emojis = [os.path.join(emojis_dir, f)for f in os.listdir(emojis_dir)if os.path.isfile(os.path.join(emojis_dir, f))]
shuffle(emojis)
timer.repeat(1000, decrease)



                               
pbox = Box(app,layout = 'grid',align = 'left')#the pictures box which is not interactable
bbox = Box(app,layout = 'grid', align ='right')# the button box which is interactable

pictures = []
for x in range(0,4):
    for y in range(0,4):
        picture = Picture(pbox, grid = [x,y] )
        pictures.append(picture)


buttons = []
for x in range(0,4):
    for y in range(0,4):
        button=PushButton(bbox ,grid = [x,y] )
        buttons.append(button)


    
setup_round()

app.display()
 
