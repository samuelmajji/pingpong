from turtle import Turtle

k = -20

class Box(Turtle):
    def __init__(self):
        super().__init__()
        self.box_1 = []
        self.box_2 = []

    def set_up(self):
        global k
        for i in range(0, 3):
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(-290-300, k)
            self.box_1.append(new_seg)
            k += 20
        k = -20
        for i in range(0, 3):
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(290+300, k)
            self.box_2.append(new_seg)
            k += 20

    def move_up_l(self):
        for seg in self.box_1:
            seg.setheading(90)
            seg.forward(40)

    def move_down_l(self):
        for seg in self.box_1:
            seg.setheading(270)
            seg.forward(40)

    def move_up_r(self):
        for seg in self.box_2:
            seg.setheading(90)
            seg.forward(40)

    def move_down_r(self):
        for seg in self.box_2:
            seg.setheading(270)
            seg.forward(40)

    def draw_ground(self):
        ground = Turtle()
        ground.pencolor("white")
        ground.penup()
        ground.goto(0, 300)
        ground.pendown()
        ground.setheading(180)
        ground.forward(600)
        ground.setheading(270)
        ground.forward(600)
        ground.setheading(0)
        ground.forward(1200)
        ground.setheading(90)
        ground.forward(600)
        ground.setheading(180)
        ground.forward(600)
        ground.setheading(270)
        for i in range(20):
            ground.penup()
            ground.forward(15)
            ground.pendown()
            ground.forward(15)
# from turtle import Turtle
# k = -20
# class Box(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.box_1 = []
#         self.box_2 = []
#
#
#     def set_up(self):
#         global k
#         for i in range(0,3):
#             new_seg = Turtle("square")
#             new_seg.color("white")
#             new_seg.penup()
#             new_seg.goto(-290-300, k)
#             self.box_1.append(new_seg)
#             k = k + 20
#         k = -20
#         for i in range(0,3):
#             new_seg = Turtle("square")
#             new_seg.color("white")
#             new_seg.penup()
#             new_seg.goto(290+300, k)
#             self.box_2.append(new_seg)
#             k = k + 20
#
#     def move_up_l(self):
#         print(len(self.box_1))
#         self.box_1[0].setheading(90)
#         self.box_1[0].forward(20)
#
#     def move_down_l(self):
#         for i in range(1,len(self.box_1)):
#             self.box_1[i].setheading(270)
#             self.box_1[i].forward(20)
#
#
#     def move_up_r(self):
#         for i in range(1, len(self.box_2)):
#             self.box_2[i].setheading(90)
#             self.box_2[i].forward(20)
#
#     def move_down_r(self):
#         for i in range(1, len(self.box_2)):
#             self.box_2[i].setheading(270)
#             self.box_2[i].forward(20)
#
#     def draw_ground(self):
#         ground = Turtle()
#         ground.pencolor("white")
#         ground.penup()
#         ground.goto(0, 300)
#         ground.pendown()
#         ground.setheading(180)
#         ground.forward(600)
#         ground.setheading(270)
#         ground.forward(600)
#         ground.setheading(0)
#         ground.forward(1200)
#         ground.setheading(90)
#         ground.forward(600)
#         ground.setheading(180)
#         ground.forward(600)
#         ground.setheading(270)
#         for i in range (0, 20):
#             ground.penup()
#             ground.forward(15)
#             ground.pendown()
#             ground.forward(15)
#
#
