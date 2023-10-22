from math import cos, pi, sin

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_cube(color):
    glColor3fv(color)

    glBegin(GL_QUADS)

    # Front face
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    # Back face
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)

    # Other faces
    # Right face
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)

    # Left Face
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    # Top Face
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)

    # Bottom Face
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)

    glEnd()


def draw_circle(radius, y, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, y, 0)  # center point
    for i in range(num_segments + 1):  # to close the circle
        theta = i / num_segments * 2.0 * pi
        glVertex3f(radius * cos(theta), y, radius * sin(theta))
    glEnd()


def draw_cylinder(radius, height, num_segments):
    # Draw the tube
    glBegin(GL_TRIANGLE_STRIP)

    for i in range(num_segments):
        theta = i / num_segments * 2.0 * pi
        next_theta = (i + 1) / num_segments * 2.0 * pi

        glVertex3f(radius * cos(theta), 0, radius * sin(theta))  # Lower ring vertex
        glVertex3f(radius * cos(next_theta), 0, radius * sin(next_theta))  # Lower ring vertex

        glVertex3f(radius * cos(theta), height, radius * sin(theta))  # Upper ring vertex
        glVertex3f(radius * cos(next_theta), height, radius * sin(next_theta))  # Upper ring vertex

    glEnd()

    # Draw the two ends
    draw_circle(radius, 0, num_segments)
    draw_circle(radius, height, num_segments)


def draw_windows(color):
    glColor3fv(color)

    # Iterable settings for window placements
    # Each entry indicates (xScale, yScale, xOffset, yOffset)
    settings = [
        (0.6, 0.7, 0.1, 0.1),  # Front window
        # (-0.6, -0.7, -0.1, -0.1),  # Rear window
        # (0, 0, 0, 0),  # Left window
        # (0, 0, 0, 0)  # Right window
    ]

    settings1 = [
        (0.6, 0.7, 0.1, 0.1),  # Rear window
        # (0, 0, 0, 0),
        # (0, 0, 0, 0)  # Right window
    ]

    settings2 = [
        (0.5, 0.5, 0.5, 0.5),  # Rear window
        # (0, 0, 0, 0),
        # (0, 0, 0, 0)  # Right window
    ]

    for xScale, yScale, xOffset, yOffset in settings:
        glPushMatrix()
        glScalef(xScale, yScale, 1.0)
        glTranslatef(xOffset, yOffset, 0.5)  # To position at edge of roof
        glBegin(GL_QUADS)
        glVertex3f(-0.8, -0.5, 0.1)
        glVertex3f(0.6, -0.5, 0)
        glVertex3f(0.5, 0.5, 0)
        glVertex3f(-0.5, 0.5, 0)
        glEnd()
        glPopMatrix()

    for xScale, yScale, xOffset, yOffset in settings1:
        glPushMatrix()
        glScalef(xScale, yScale, 1.0)
        glTranslatef(xOffset, yOffset, 0.5)  # To position at edge of roof
        glBegin(GL_QUADS)
        glVertex3f(-0.8, -0.5, -1.1)
        glVertex3f(0.6, -0.5, -1)
        glVertex3f(0.5, 0.5, -1)
        glVertex3f(-0.5, 0.5, -1)
        glEnd()
        glPopMatrix()

    for xScale, yScale, xOffset, yOffset in settings2:
        glPushMatrix()
        glScalef(xScale, yScale, 1.0)
        glTranslatef(xOffset, yOffset, 0.5)  # To position at edge of roof
        glBegin(GL_QUADS)
        glVertex3f(0.51, -0.9, -1)
        glVertex3f(0.51, 0.4, -1)
        glVertex3f(0.51, 0.4, 0)
        glVertex3f(0.51, -0.9, 0)
        glEnd()
        glPopMatrix()

    for xScale, yScale, xOffset, yOffset in settings2:
        glPushMatrix()
        glScalef(xScale, yScale, 1.0)
        glTranslatef(xOffset, yOffset, 0.5)  # To position at edge of roof
        glBegin(GL_QUADS)
        glVertex3f(-1.51, -0.9, -1)
        glVertex3f(-1.51, 0.4, -1)
        glVertex3f(-1.51, 0.4, 0)
        glVertex3f(-1.51, -0.9, 0)
        glEnd()
        glPopMatrix()


def draw_car():
    glPushMatrix()

    # Car body - Main chassis
    glTranslatef(0.0, 0.0, 0.0)
    glScalef(1.0, 0.3, 0.5)
    draw_cube((1.0, 0.3, 0.17))  # Color in RGB, here it's red.

    # Car roof
    glPushMatrix()
    glTranslatef(0.0, 0.7, 0.0)
    glScalef(0.8, 0.5, 0.5)
    draw_cube((1.0, 0.3, 0.17))  # Color in RGB, here it's red.

    # Car windows
    draw_windows((0.20, 0.28, 0.34))  # Color in RGB, here it's cyan.

    glPopMatrix()

    # Wheels
    glColor3fv((0.0, 0.0, 0.0))  # Color in RGB, here it's black
    for x in [-0.35, 0.35]:
        for z in [-0.45, 0.25]:
            glPushMatrix()
            glTranslatef(x, -0.5, z)
            glRotatef(90.0, 1.0, 0.0, 0.0)  # Orient the cylinder's height along the wheel axis
            draw_cylinder(0.12, 0.2, 32)  # radius, height, segments
            glPopMatrix()

    glPopMatrix()


def main():
    pygame.init()
    display = (1200, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)  # Enable depth test

    # Change the background color to grey
    glClearColor(0.82, 0.82, 0.82, 1)

    gluPerspective(20, 1200 / 800, 0.1, 10)

    glTranslatef(0.0, 0.0, -4)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_car()
        pygame.display.flip()
        pygame.time.wait(10)


main()
