# a121_catch_a_turtle.py
#CAN ONLY RUN IN DEBUG
#-----import statements-----
import turtle as trtl
import random
sq = trtl

#-----game configuration----
sqshape = "square"
sqsize = 1
sqcolor = "purple"
sqpensize = 3
score = 0
font_setup = ("Arial", 20, "normal")
timercount = 5
counter_interval = 1000
timer_up = False
colors = ["red", "yellow", "purple", "blue", "pink"]
sizes = [0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]



#-----initialize turtle------
sq = trtl.Turtle()
sq.shape(sqshape)
sq.shapesize(sqsize)
sq.fillcolor(sqcolor)
sq.pensize(sqpensize)

write = trtl.Turtle() 

timer = trtl.Turtle()


#-----game functions--------
def sq_clicked(x,y):
	change_position()
	

def draw_coord_plane():
	sq.penup()
	sq.setposition(-200,-150)
	sq.pendown()
	sq.left(90)
	for x in range(2):
		sq.forward(300)
		sq.right(90)
		sq.forward(400)
		sq.right(90)

def change_position():
	newcolor = random.choice(colors)
	sq.color(newcolor)
	newsize = random.choice(sizes)
	sq.shapesize(newsize)

	x = random.randint(-200,200)
	y = random.randint(-150,150)
	sq.penup()
	sq.setposition(x,y)
	sq.pendown()
	update_score()
	
	
def update_score():
	global score
	score += 1
	write.clear()
	write.write(score,font=font_setup)

def countdown():
	global timercount, timer_up
	strtimer = str(timercount)
	if timercount == 0:
		timer.clear()
		timer.write("Time's up!", font=font_setup)
		timer_up = True
		sq.hideturtle()
	else:
		timer.clear()
		timer.write("Timer: " + strtimer, font=font_setup)
		timercount = timercount-1
		timer.getscreen().ontimer(countdown, counter_interval)


	
		


#-----events----------------

sq.onclick(sq_clicked)
draw_coord_plane()
write.penup()
write.setposition(0,200)
write.pendown()
timer.penup()
timer.setposition(0,-200)
timer.pendown()

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.bgcolor("green")
wn.mainloop()









