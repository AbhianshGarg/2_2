# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
t = trtl.Turtle()
timekeeper = trtl.Turtle()
s = trtl.Turtle()
wn = trtl.Screen()
import random as rnd
import time

import leaderboard as lb

t.speed(0)

#-----game configuration----
spot_color = 'pink'
t.shape('circle')
wn.setup(400, 400)

timekeeper.penup()
timekeeper.hideturtle()
timekeeper.goto(-170, 150)

s.penup()
s.hideturtle()
s.goto(50, -150)

score = 0

font_setup = ("Arial", 20, "normal")
timer = 2
counter_interval = 1000   #1000 represents 1 second
timer_up = False
play = True

leaderboard_file_name = 'a122_txt_file.txt'




#-----Lists--------

colors = ['green', 'blue', 'orange', 'red', 'yellow']
leader_names_list = []
leader_scores_list = []

#-----game functions--------
def start_game():

  global player_name
  player_name = wn.textinput('Menu','What is your name?:')

  print("""
  Welcome to this game. Try to click the moving circle as many times as possible!

  Game starts in 3 seconds!
  """)
  
  for i in range(3, 0, -1):
    timekeeper.clear()
    timekeeper.write(i, font=font_setup)
    time.sleep(1)


def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global t

  # load all the leaderboard records into the lists
  lb.load_leaderboard('a122_txt_file.txt', leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard('a122_txt_file.txt', leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, t, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, t, score)

def move(x, y):
  if play == True:
    t.penup()
    x_move = rnd.randint(-180, 180)
    y_move = rnd.randint(-180, 180)
    t.goto(x_move, y_move)
    t.stamp
    s.clear()
    global score
    score += 1
    w_score = 'Score: ' + str(score)
    s.write(w_score, font=font_setup)
    randomize()

def randomize():
  size = rnd.randint(1, 3)
  t.turtlesize(size)
  wn.bgcolor(rnd.choice(colors))
    
def countdown():
  global timer, timer_up
  global play
  timekeeper.clear()
  if timer <= 0:
    timekeeper.write("Time's Up", font=font_setup)
    global timer_up
    timer_up = True
    play = False
    manage_leaderboard()
  else:
    timekeeper.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    timekeeper.getscreen().ontimer(countdown, counter_interval)



#-----events----------------
start_game()

wn.ontimer(countdown, counter_interval) 
while play == True:
  t.onclick(move)

  

wn.mainloop()