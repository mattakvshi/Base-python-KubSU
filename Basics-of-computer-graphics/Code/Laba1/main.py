import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# vertices = ((-50, 30),
#             (50, 30),
#             (50, -30),
#             (24, -18))
#
# edge = ((0, 1),
#         (1, 2),
#         (2, 3),
#         (3, 0))

#
# def draw():
#     glBegin(GL_QUADS)
#     for e in edge:
#         for vertex in e:
#             glVertex2f(vertices[vertex])
#     glEnd()


def draw():

    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-50, 30)
    glVertex2f(50, 30)
    glVertex2f(50, -30)
    glVertex2f(-50, -30)
    glEnd()

    glColor3f(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-45, 29)
    glVertex2f(-41, 26)
    glVertex2f(-43, 25)
    glVertex2f(-42, 21)
    glVertex2f(-45, 24)
    glVertex2f(-48, 21)
    glVertex2f(-47, 25)
    glVertex2f(-49, 26)
    glEnd()


    glColor3f(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-45, 18)
    glVertex2f(-43, 16)
    glVertex2f(-44, 15)
    glVertex2f(-44, 13)
    glVertex2f(-45, 15)
    glVertex2f(-46, 13)
    glVertex2f(-46, 15)
    glVertex2f(-47, 16)
    glEnd()

    glColor3f(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-39, 19)
    glVertex2f(-37, 17)
    glVertex2f(-38, 16)
    glVertex2f(-38, 14)
    glVertex2f(-39, 16)
    glVertex2f(-40, 14)
    glVertex2f(-40, 16)
    glVertex2f(-41, 17)
    glEnd()

    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-34, 22)
    glVertex2f(-33.5, 20.5)
    glVertex2f(-32, 20)
    glVertex2f(-33, 19)
    glVertex2f(-33, 17)
    glVertex2f(-34, 19)
    glVertex2f(-35, 17)
    glVertex2f(-35, 19)
    glVertex2f(-36, 20)
    glVertex2f(-34.5, 20.5)
    glEnd()

    glColor3f(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-33, 29)
    glVertex2f(-31, 27)
    glVertex2f(-32, 26)
    glVertex2f(-32, 24)
    glVertex2f(-33, 26)
    glVertex2f(-34, 24)
    glVertex2f(-34, 26)
    glVertex2f(-35, 27)
    glEnd()



# def draw():
#     glColor3f(1, 0, 0)
#     glBegin(GL_QUADS)
#     glVertex2f(-6, 3)
#     glVertex2f(6, 3)
#     glVertex2f(6, 2)
#     glVertex2f(-6, 2)
#     glEnd()
#     glColor3f(1, 1, 0)
#     glBegin(GL_QUADS)
#     glVertex2f(-6, 2)
#     glVertex2f(6, 2)
#     glVertex2f(6, 1)
#     glVertex2f(-6, 1)
#     glEnd()
#     glColor3f(0, 0, 1)
#     glBegin(GL_QUADS)
#     glVertex2f(6, 1)
#     glVertex2f(-6, 1)
#     glVertex2f(-6, 0)
#     glVertex2f(6, 0)
#     glEnd()
#     glColor3f(1, 1, 1)
#     glBegin(GL_QUADS)
#     glVertex2f(-6, 0)
#     glVertex2f(6, 0)
#     glVertex2f(6, -1)
#     glVertex2f(-6, -1)
#     glEnd()
#     glColor3f(0, 0, 0)
#     glBegin(GL_QUADS)
#     glVertex2f(6, -1)
#     glVertex2f(-6, -1)
#     glVertex2f(-6, -2)
#     glVertex2f(6, -2)
#     glEnd()
#     glColor3f(0, 1, 0)
#     glBegin(GL_LINE_LOOP)
#     glVertex2f(-6, 3)
#     glVertex2f(6, 3)
#     glVertex2f(6, -2)
#     glVertex2f(-6, -2)
#     glEnd()




def main():
    pygame.init()
    display = (1800, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(80, display[0] / display[1], 1, 40)
    glTranslatef(0.0, 0.0, -40)
    # gluPerspective(80, display[0] / display[1], 1, 10)
    # glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # square()
        draw()
        pygame.display.flip()


main()
