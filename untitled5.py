import turtle
n=int(input("你要幾邊形"))
uu=turtle.Turtle()
ll=turtle.Turtle()
uu.speed(0)
uu.color("gold")
ll.speed(0)
ll.color("silver")
for i in range(n):
    uu.forward(0.1)
    uu.left(360/n)

for i in range(n):
    ll.forward(0.1)
    ll.right(360/n)
