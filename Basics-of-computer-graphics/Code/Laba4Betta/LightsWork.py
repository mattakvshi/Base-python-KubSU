from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Угол для перемещения источника света
angle = 0.0


def draw():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Установка матрицы моделирования
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Перемещение источника света
    glLightfv(GL_LIGHT0, GL_POSITION, (-1.0 + math.cos(angle), -1.0 + math.sin(angle), 1.0, 0.0))

    # Рисование трёхмерного примитива (например, куб)
    glPushMatrix()
    glColor3f(0.0, 0.0, 1.0)
    glutSolidCube(0.5)
    glPopMatrix()

    glutSwapBuffers()


def update(dt):
    global angle

    # Увеличение угла для перемещения источника света
    angle += 0.01

    glutPostRedisplay()
    glutTimerFunc(int(dt), update, dt)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Moving Light Source")

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

    glClearColor(0.0, 0.0, 0.0, 0.0)

    glutDisplayFunc(draw)
    glutTimerFunc(0, update, 30)

    glutMainLoop()



main()