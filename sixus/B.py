from three.A import Turtle
from three.B import draw_object
from functools import partial
from math import sqrt

def rewrite(axiom, rules, iterations):
    states = axiom
    for i in range(iterations):
        chars = ''
        for char in states:
            chars += rules.get(char,char)
        states = chars
    return states

def draw(turtle_func, axiom, rules, iterations):
    rules = rewrite(axiom, rules, iterations)
    for rule in rules:
        try:
            turtle_func[rule]()
        except KeyError:
            pass

'''http://www-user.uni-bremen.de/schmuhl/fractals/fractal_curves.html
'''

def koch(turtle):
    angle = 60
    step = 1/3
    turtle_func = {'F': partial(turtle.forward, step), '+':partial(turtle.right, angle), '-':partial(turtle.left, angle)}
    draw(turtle_func, axiom='F--F--F', rules={'F':'F+F--F+F'}, iterations=5)

def sierpinski_arrowhead(turtle):
    angle = 60
    step = 1.5849
    turtle_func = {'A': partial(turtle.forward, step),'B': partial(turtle.forward, step),  '+':partial(turtle.right, angle), '-':partial(turtle.left, angle)}
    draw(turtle_func, axiom='A', rules={'A':'B-A-B', 'B':'A+B+A'}, iterations=6)

def hilbert(turtle):
    angle = 93
    step = 2
    turtle_func = {'F': partial(turtle.forward, step), '+':partial(turtle.right, angle), '-':partial(turtle.left, angle)}
    draw(turtle_func, axiom='L', rules={'L':'+RF-LFL-FR+', 'R':'-LF+RFR+FL-'}, iterations=6)

stack = []

def push(turtle):
    global stack
    stack.append(((turtle.x, turtle.y), turtle.angle))

def pop(turtle):
    global stack
    ((turtle.x, turtle.y), turtle.angle) = stack.pop()
    
def pythagoras_plant(turtle):
    global stack
    angle = 25
    step = 2
    stack = []
    turtle_func = {'F': partial(turtle.forward, step), '+':partial(turtle.right, angle), '-':partial(turtle.left, angle), '[': partial(push, turtle), ']': partial(pop, turtle)}
    draw(turtle_func, axiom='X', rules={'X':'F[+X]-X', 'F':'FF'}, iterations=6)
  
def plant(turtle):
    global stack
    angle = 25
    step = 1
    stack = []
    turtle_func = {'F': partial(turtle.forward, step), '+':partial(turtle.right, angle), '-':partial(turtle.left, angle), '[': partial(push, turtle), ']': partial(pop, turtle)}
    draw(turtle_func, axiom='X', rules={'X':'F-[[X]+X]+F[+FX]-X', 'F':'FF'}, iterations=6)

def quadratic_koch_island(turtle):
    angle = 90
    step = 1/4
    turtle_func = {'F': partial(turtle.forward, step), '+':partial(turtle.right, angle), '-':partial(turtle.left, angle)}
    draw(turtle_func, axiom='F+F+F+F', rules={'F':'F+F-F-FF+F+F-F'}, iterations=4)

def dragon_curve(turtle):
    angle = 45
    step = 1
    turtle_func = {'F': partial(turtle.forward, step), '+':partial(turtle.right, angle), '-':partial(turtle.left, angle)}
    draw(turtle_func, axiom='FX', rules={'F':'Z', 'X':'+FX--FY+', 'Y':'-FX++FY-'}, iterations=12)

def terdragon(turtle):
    angle = 120
    step = 2
    turtle_func = {'F': partial(turtle.forward, step), '+':partial(turtle.right, angle), '-':partial(turtle.left, angle)}
    draw(turtle_func, axiom='F', rules={'F':'F-F+F'}, iterations=7)

#draw_object(koch, start_x=5, start_y=85)
#draw_object(sierpinski_arrowhead, start_x=5, start_y=5)
draw_object(hilbert, start_x=5, start_y=5)
#draw_object(plant, start_x=5, start_y=55)
#draw_object(pythagoras_plant, start_x=5, start_y=45)
#draw_object(quadratic_koch_island, start_x=25, start_y=25)
#draw_object(dragon_curve, start_x=25, start_y=25)
#draw_object(terdragon, start_x=85, start_y=20)