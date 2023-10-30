
from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *
from math import cos, sin, pi

# Инициализация Pygame и экрана
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)

camera_distance = 5.0
camera_angle = 0.0

light_angle = 0.0
light_radius = 2.0

# Настройки OpenGL
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (WINDOW_WIDTH / WINDOW_HEIGHT), 0.1, 50.0)
glEnable(GL_DEPTH_TEST)

# Параметры источника света
light_position = [2, 2, 2, 1]

# Включение и настройка источника света
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_POSITION, light_position)

# Создание сферы
radius = 1.0
latitude_slices = 20
longitude_slices = 20

vertices = []
normals = []
for latitude in range(latitude_slices):
    for longitude in range(longitude_slices):
        x = radius * sin(latitude * pi / latitude_slices) * cos(longitude * 2 * pi / longitude_slices)
        y = radius * sin(latitude * pi / latitude_slices) * sin(longitude * 2 * pi / longitude_slices)
        z = radius * cos(latitude * pi / latitude_slices)
        vertices.append((x, y, z))
        normals.append((x, y, z))

# Отрисовка сферы
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    light_position[0] = light_radius * cos(light_angle)
    light_position[1] = light_radius * sin(light_angle)
    light_position[2] = 2.0  # Фиксированная высота источника света
    light_position[3] = 1.0  # Тип источника света
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glClearColor(0.349, 0.357, 0.510, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    cam_x = camera_distance * cos(camera_angle)
    cam_y = camera_distance * sin(camera_angle)
    cam_z = 5.0
    gluLookAt(cam_x, cam_y, cam_z, 0, 0, 0, 0, 1, 0)

    glColor3f(0.023, 0.040, 0.188)
    glBegin(GL_TRIANGLES)
    for latitude in range(latitude_slices - 1):
        for longitude in range(longitude_slices):
            # Верхний треугольник
            glNormal3fv(normals[latitude * longitude_slices + longitude])
            glVertex3fv(vertices[latitude * longitude_slices + longitude])

            glNormal3fv(normals[latitude * longitude_slices + (longitude + 1) % longitude_slices])
            glVertex3fv(vertices[latitude * longitude_slices + (longitude + 1) % longitude_slices])

            glNormal3fv(normals[(latitude + 1) * longitude_slices + longitude])
            glVertex3fv(vertices[(latitude + 1) * longitude_slices + longitude])

            # Нижний треугольник
            glNormal3fv(normals[latitude * longitude_slices + (longitude + 1) % longitude_slices])
            glVertex3fv(vertices[latitude * longitude_slices + (longitude + 1) % longitude_slices])

            glNormal3fv(normals[(latitude + 1) * longitude_slices + (longitude + 1) % longitude_slices])
            glVertex3fv(vertices[(latitude + 1) * longitude_slices + (longitude + 1) % longitude_slices])

            glNormal3fv(normals[(latitude + 1) * longitude_slices + longitude])
            glVertex3fv(vertices[(latitude + 1) * longitude_slices + longitude])
    glEnd()

    light_angle += 0.1

    pygame.display.flip()

pygame.quit()