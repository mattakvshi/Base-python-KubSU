import math

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def init():
    # Инициализация Pygame
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | OPENGLBLIT )

    # this line is important:
    glEnable(GL_DEPTH_TEST)

    # Инициализация OpenGL
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)


def draw_ring(center, color, outer_radius, inner_radius):
    # Здесь мы создаём списки для вершин и нормалей
    vertices = []
    normals = []

    num_segs = 100  # Число сегментов, на которых мы разбиваем кольцо

    for seg in range(num_segs):
        theta = 2.0 * 3.141592 / num_segs * seg
        for side in range(2):
            r = outer_radius - (inner_radius * side)
            x = r * math.sin(theta)  # Обновлено на x
            y = r * math.cos(theta)  # Обновлено на y
            vertices.append(
                (center[0] + x, center[1] + y, center[2]))  # Теперь координаты вершин представляют собой (x, y, 0)
            normals.append((x, y, 0))  # Обновлено на (x, y, 0)

    glBegin(GL_TRIANGLE_STRIP)
    glColor(color)
    for i in range(num_segs * 2):
        glNormal3fv(normals[i])
        glVertex3fv(vertices[i])
    glEnd()
def draw_bear():
    bear_color = (0.4, 0.29, 0.18)
    bear_color_dark = (0.16, 0.09, 0.02)
    eye_color = (0, 0, 0)  # Черный цвет глаз
    mouth_color = (1, 0, 0)  # Красный цвет рот

    sphere = gluNewQuadric()

    # Рисуем голову
    glPushMatrix()
    glColor(bear_color)
    gluSphere(sphere, 0.5, 20, 20)  # Шар для головы

    # Рисуем глаза на голове
    glPushMatrix()
    glColor(eye_color)
    glTranslatef(-0.2, 0.2, 0.4)  # Смещение левого глаза
    gluSphere(sphere, 0.1, 20, 20)  # Шар для левого глаза
    glPopMatrix()

    glPushMatrix()
    glColor(eye_color)
    glTranslatef(0.2, 0.2, 0.4)  # Смещение правого глаза
    gluSphere(sphere, 0.1, 20, 20)  # Шар для правого глаза
    glPopMatrix()

    # Рисуем рот на голове
    glPushMatrix()
    glColor(mouth_color)
    glTranslatef(0, -0.2, 0.4)  # Смещение рта
    gluSphere(sphere, 0.15, 20, 20)  # Шар для рта
    glPopMatrix()

    glPopMatrix()

    # Рисуем левое ухо
    glPushMatrix()
    glColor(bear_color_dark)
    glTranslatef(-0.35, 0.35, 0.1)  # Смещение левого уха
    gluSphere(sphere, 0.2, 20, 20)  # Шар для левого уха
    glPopMatrix()

    # Рисуем правое ухо
    glPushMatrix()
    glColor(bear_color_dark)
    glTranslatef(0.35, 0.35, 0.1)  # Смещение правого уха
    gluSphere(sphere, 0.2, 20, 20)  # Шар для правого уха
    glPopMatrix()

    # Рисуем тело
    glPushMatrix()
    glColor(bear_color)
    glTranslatef(0.0, -0.8, 0.0)  # Смещение тела
    gluSphere(sphere, 0.8, 20, 20)  # Шар для тела
    glPopMatrix()

    ring_color = (1, 0.843, 0)  # Цвет колец - Золото
    ring_outer_radius = 0.15  # Внешний радиус колец
    ring_inner_radius = 0.05  # Внутренний радиус колец
    ring_distance = 0.2  # Расстояние между кольцами
    ring_start_pos = -0.4  # Позиция самого левого кольца

    top_rings_coords = [(-0.4, -0.8, 0.8), (0, -0.8, 0.8), (0.4, -0.8, 0.8)]  # координаты для верхних колец
    bottom_rings_coords = [(-0.2, -1.0, 0.8), (0.2, -1.0, 0.8)]  # координаты для нижних колец

    # Рисуем 3 золотых кольца сверху
    for coord in top_rings_coords:
        draw_ring(coord, ring_color, ring_outer_radius, ring_inner_radius)

    # Рисуем 2 золотых кольца внизу
    for coord in bottom_rings_coords:
        draw_ring(coord, ring_color, ring_outer_radius, ring_inner_radius)

    # Рисуем левую ногу
    glPushMatrix()
    glColor( bear_color_dark)
    glTranslatef(-0.4, -1.5, 0.0)  # Смещение левой ноги
    gluSphere(sphere, 0.3, 20, 20)  # Шар для левой ноги
    glPopMatrix()

    # Рисуем правую ногу
    glPushMatrix()
    glColor( bear_color_dark)
    glTranslatef(0.4, -1.5, 0.0)  # Смещение правой ноги
    gluSphere(sphere, 0.3, 20, 20)  # Шар для правой ноги
    glPopMatrix()

    # Рисуем левую руку
    glPushMatrix()
    glColor( bear_color_dark)
    glTranslatef(-0.8, -0.5, 0.0)  # Смещение левой руки
    gluSphere(sphere, 0.3, 20, 20)  # Шар для левой руки
    glPopMatrix()

    # Рисуем правую руку
    glPushMatrix()
    glColor( bear_color_dark)
    glTranslatef(0.8, -0.5, 0.0)  # Смещение правой руки
    gluSphere(sphere, 0.3, 20, 20)  # Шар для правой руки
    glPopMatrix()

def main(): 
    init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClearColor(0.82, 0.82, 0.82, 1)

        glRotatef(1, 3, 1, 1)  # Поворот медведя в 3D пространстве
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_bear()
        pygame.display.flip()
        pygame.time.wait(10)

main()