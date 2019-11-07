# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import turtle as sc
'''import turtle as bomb'''
import leaderboard as lb
#-----game configuration----
shape="turtle"
size=10
color="green"
score=0
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
size_counter=0#change size

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("please enter your name:")
#-----initialize turtle-----
joe=trtl.Turtle(shape = shape)
joe.color(color)
joe.shapesize(size)
joe.speed(0)


sc=trtl.Turtle()
sc.penup()
sc.goto(-370,270)
sc.ht()

font = ("roboto", 50, "bold")
sc.write("score", font=font)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(70,-370)
'''
bomb=trtl.Turtle(shape = shape)
bomb.color("black")
bomb.shapesize(1)
bomb.speed(0)
bombtimer = 0
'''
#-----game functions--------
def turtle_clicked(x,y):
    print("joe was clicked")
    change_position()
    score_counter()
    change_size()#custom
    increase_time()#custom
''' bombtime()'''

def change_position ():
    joe.penup()
    joe.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-400,400)
    joe.goto(new_xpos,new_ypos)
    joe.st()
def score_counter():
    global score
    score += 1
    print(score)
    sc.clear()
    sc.write(score,font=font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.goto(-300,0)
    counter.write("Time's Up Good Job", font=font)
    timer_up = True
    gameover()
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def gameover():
    joe.ht()
    joe.goto(10000,10000)
    wn.bgcolor("red")

def change_size():#custom
    global size
    if size >= 1:
      size -= 1
      joe.shapesize(size)

def increase_time():#custom
    global timer
    timer += 1
'''
def bomb_clicked(x,y):
    bomb.penup()
    global timer,timer_up
    timer == 0

def bomb_pos():
    bomb_xpos = random.randint(-400,400)
    bomb_ypos = random.randint(-400,400)
    if bombtimer == 1:
      bomb.goto(bomb_xpos,bomb_ypos)

def bombtime():
    bombtimer += 1
    bombtimer == 0
'''

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global joe

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, joe, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, joe, score)


#-----events----------------
joe.onclick(turtle_clicked)
'''bomb.onclick(bomb_clicked)'''
wn = trtl.Screen()
wn.bgcolor("blue")#custom, background color is blue
wn.ontimer(countdown, counter_interval) 
wn.mainloop()