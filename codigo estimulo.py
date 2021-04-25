import turtle
import time


# Tiempo:
def advance(angulo, sentido, distancia, pasos, espera):
    if sentido == "horario":
        ball.right(angulo)
    if sentido == "antihorario":
        ball.left(angulo)
    distanciaPorPaso = distancia / pasos #cuanta distancia recorre por pasos
    x = 0 #empiezo con 0 pasos recorridos
    while x < pasos: #mientras no termine la cantidad de pasos sigo recorriendo
        ball.forward(distanciaPorPaso) #recorre z pasos
        time.sleep(espera)
        x += 1


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Eyeball Exercise")
print(wn.window_height())
print(wn.window_width())

#Fullscreen window:
wn.screensize()
wn.setup(width = 1.0, height = 1.0)


#Texto Introductorio:

t = turtle.Turtle(visible=False)
t.color("SeaGreen")
t.write("A continuación, se le presentará seis diferentes ejercicios de movimientos oculares de seguimiento.", False, "center", font=("Arial", 20, "bold"))
time.sleep(5)
t.hideturtle()
t.clear()

t = turtle.Turtle(visible=False)
t.color("SeaGreen")
t.write("Siga con sus ojos, y sin mover la cabeza, los distintos movimientos que realice la pelota.", False, "center", font=("Arial", 20, "bold"))
time.sleep(5)
t.hideturtle()
t.clear()

t = turtle.Turtle(visible=False)
t.color("SeaGreen")
t.write("Por favor, haga su mejor esfuerzo.", False, "center", font=("Arial", 20, "bold"))
time.sleep(5)
t.hideturtle()
t.clear()

#Pelota 1 Movimiento laberinto
ball = turtle.Turtle()
ball.penup()
ball.setpos(-300,150)
ball.shape("circle")
ball.color("firebrick")
advance(0,"horario",600,100,0.030) 
advance(90,"horario",150,25,0.030) 
advance(90,"horario",600,100,0.030) 
advance(90,"horario",-150,25,0.030) 
advance(90,"horario",600,100,0.030) 
ball.hideturtle()

time.sleep(3) #Segundos entre cada pelota

#Pelota 2
ball = turtle.Turtle()
ball.penup()
ball.setpos(-300,150)
ball.shape("circle")
ball.color("firebrick")
advance(150,"antihorario",-600,100,0.030) 
advance(60,"horario",300,50,0.030) 
advance(150,"antihorario",0,0.1,0) 
advance(150,"antihorario",-600,100,0.030) 
advance(60,"antihorario",300,50,0.030) 
ball.hideturtle()

time.sleep(3) #Segundos entre cada pelota

#Pelota 3 Movimiento Zigzag 
ball = turtle.Turtle()
ball.penup()
ball.setpos(-250,-250)
ball.shape("circle")
ball.color("firebrick")
advance(90,"antihorario",500,100,0.030) 
advance(10,"antihorario",-500,100,0.030) #HASTA ACA ES 1ER ZIGZAG
advance(10,"horario",500,100,0.030) 
advance(170,"horario",500,100,0.030)  #HASTA ACA ES 2DO ZIGZAG
advance(10,"horario",-500,100,0.030)
advance(170,"horario",-500,100,0.030)  #HASTA ACA ES 3ER ZIGZAG
advance(10,"horario",500,100,0.030)
advance(170,"horario",500,100,0.030)  #HASTA ACA ES 4TO ZIGZAG
advance(10,"horario",-500,100,0.030)
advance(170,"horario",-500,100,0.030) #HASTA ACA ES 5TO ZIGZAG
advance(10,"horario",500,100,0.030)
advance(170,"horario",500,100,0.030)
ball.hideturtle()

time.sleep(3) #Segundos entre cada pelota

#Pelota 4 Movimiento Estrellade5Puntas
ball = turtle.Turtle()
ball.penup()
ball.setpos(-200,-200)
ball.shape("circle")
ball.color("firebrick")
advance(60,"antihorario",500,83,0.030) #ball.goto(0,250)
advance(120,"horario",500,83,0.030) #ball.goto(200,-200)
advance(210,"antihorario",600,100,0.030) #ball.goto(-300,150)
advance(150,"horario",550,100,0.030) #ball.goto(300,150)
advance(30,"antihorario",-600,91,0.030) #ball.goto(-200,-200)
ball.hideturtle()

time.sleep(3) #Segundos entre cada pelota

#Pelota 5 Movimiento Estrella8Puntas 
ball = turtle.Turtle()
ball.penup()
ball.setpos(0,0)
ball.shape("circle")
ball.color("firebrick")
advance(90,"antihorario",200,33,0.030) 
advance(180,"horario",200,33,0.030)
advance(0,"horario",200,33,0.030) 
advance(180,"horario",200,33,0.030)
advance(145,"antihorario",200,33,0.030) 
advance(180,"horario",200,33,0.030) 
advance(360,"horario",200,33,0.030)
advance(180,"horario",200,33,0.030)
advance(235,"horario",200,33,0.030) 
advance(180,"horario",200,33,0.030) 
advance(360,"horario",200,33,0.030) 
advance(180,"horario",200,33,0.030) 
advance(130,"antihorario",200,33,0.030)
advance(180,"horario",200,33,0.030) 
advance(360,"antihorario",200,33,0.030)
advance(180,"horario",200,33,0.030)
ball.hideturtle()

time.sleep(3) #Segundos entre cada pelota


#Pelota 6 Movimiento horario y antihorario #NO PUDE HACERLO
ball = turtle.Turtle()
#ball.penup()
ball.setpos(0,90)
ball.shape("circle")
ball.color("firebrick")

advance(0,"horario",40,10,0.030)
for i in range(5, 15):
    advance(i,"horario",40,10,0.030)
    advance(0,"horario",1,1,0.030)

advance(0,"horario",20,10,0.030)

for i in range(5, 20):
    advance(i,"horario",40,10,0.030)
    advance(0,"horario",1,1,0.030)

advance(0,"horario",40,10,0.030)

for i in range(5, 15):
    advance(i,"horario",40,10,0.030)
    advance(0,"horario",1,1,0.030)

advance(0,"horario",20,10,0.030)

for i in range(15, 20):
    advance(i,"horario",40,10,0.030)
    advance(0,"horario",1,1,0.030)

advance(0,"horario",10,10,0.030)

for i in range(5, 20):
    advance(i,"horario",40,10,0.030)
    advance(0,"horario",1,1,0.030)
advance(0,"horario",40,10,0.030)
for i in range(5, 15):
    advance(i,"horario",40,10,0.030)
    advance(0,"horario",1,1,0.030)
for i in range(15, 20):
    advance(i,"horario",40,10,0.030)
    advance(0,"horario",1,1,0.030)
advance(0,"horario",10,10,0.030)

ball.hideturtle()


#Texto: 
t = turtle.Turtle(visible=False)
t.color("SeaGreen")
t.write("¡Gracias por su participación!", False, "center", font=("Arial", 20, "bold"))


wn.mainloop()

