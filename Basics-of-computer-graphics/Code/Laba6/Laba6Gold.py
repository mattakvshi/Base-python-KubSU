from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import time
import numpy as np




# Функция для обновления сцены
def update_scene():
    start_time = time.time()  # Фиксируем время начала

    while True:
        t = time.time() - start_time  # Вычисляем текущее время
        y_offset = np.sin(t)  # Создаем вертикальное смещение, основанное на синусе от времени

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()

        # Применяем смещение по y
        glTranslatef(0, y_offset, 0)

        # Ставим окрашивание
        # color = [0.97, 0.98, 0.99, 1.]
        color = [0.56, 0.22, 0.29, 1.0]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

        # Настройка свойств материала
        ambient = [0.25, 0.25, 0.25, 1.0]
        diffuse = [0.4, 0.4, 0.4, 1.0]
        specular = [0.774597, 0.774597, 0.774597, 1.0]
        shininess = 76.8
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shininess)

        # Создаем цилиндр
        glRotatef(75, 1, 0, 0)
        glutSolidCylinder(1, 2, 32, 32)

        glPopMatrix()
        glRotate(1, 0, 1, 0)
        glutSwapBuffers()

        # Задержка перед следующим кадром
        time.sleep(0.01)

    return


# Функция для настройки освещения
def setup_lighting():
    glEnable(GL_LIGHTING)

    # Первый источник света
    lightZeroPosition = [10., 4., 10., 1.]
    lightZeroColor = [1, 0.84, 0, 0.6]
    #lightZeroColor = [0.8, 1.0, 0.8, 1.]  # Оттенок зеленого
    #lightZeroColor = [0.56, 0.22, 0.29, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)

    # Второй направленный источник света
    lightOnePosition = [-10., 3., -10., 1.]
    lightOneColor = [0.90, 0.78, 0.76, 1.]  # Оттенок синего (цветовое значение #769FCD в формате RGB)
    glLightfv(GL_LIGHT1, GL_POSITION, lightOnePosition)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, lightOneColor)
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 180.0)
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [0.0, 0.0, 0.0])
    glEnable(GL_LIGHT1)

    # # Третий источник света
    # lightTwoPosition = [10., -10., -10., 1.0]  # Положение сзади и внизу справа от цилиндра
    # lightTwoColor = [0.8, 1.0, 0.8, 1.]  # Цвет HEX #903749 в формате RGB
    # glLightfv(GL_LIGHT2, GL_POSITION, lightTwoPosition)
    # glLightfv(GL_LIGHT2, GL_DIFFUSE, lightTwoColor)
    # glEnable(GL_LIGHT2)

    # Четвертый источник света
    lightThreePosition = [0., 10., 0., 1.]  # Положение сверху от цилиндра
    lightThreeColor = [1.0, 1.0, 1.0, 1.0]  # Белый цвет
    glLightfv(GL_LIGHT3, GL_POSITION, lightThreePosition)
    glLightfv(GL_LIGHT3, GL_DIFFUSE, lightThreeColor)
    glEnable(GL_LIGHT3)

    return


# Функция для настройки вида
def setup_view():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40., 1., 1., 40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, 0, 10,
              0, 0, 0,
              0, 1, 0)
    glPushMatrix()

    return


def main():
    # Инициализация и настройка окна
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b'CylinderMetal')

    # glClearColor(0.84, 0.9, 0.95, 1.)
    glClearColor(0.25, 0.24, 0.32, 1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)

    setup_lighting()  # Настраиваем освещение
    glutDisplayFunc(update_scene)  # Устанавливаем функцию обновления сцены
    setup_view()  # Настраиваем вид

    glutMainLoop()

    return


if __name__ == '__main__':
    main()
