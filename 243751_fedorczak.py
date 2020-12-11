#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

def draw_rectangle(x,y,a,b) :

    glBegin(GL_TRIANGLES)
    glColor3f(0.0,0.6,1.0)
    glVertex2f(x+a/2, y+b/2)
    glColor3f(1.0,0.4,0.1)
    glVertex2f(x-a/2, y+b/2)
    glColor3f(0.5,1.0,0.0)
    glVertex2f(x+a/2,y-b/2)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.0,0.6,1.0)
    glVertex2f(x-a/2,y+b/2)
    glColor3f(0.1,0.2,0.5)
    glVertex2f(x+a/2,y-b/2)
    glColor3f(0.6,0.2,0.0)
    glVertex2f(x-a/2,y-b/2)
    glEnd()
    glFlush()
def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    '''
    zad na 3.0
    glColor3f(0.0, 0.0, 12.0)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 11.0, 0.0)
    glVertex2f(-120.0, -70.0)
    glColor3f(3.0, 0.0, 0.0)
    glVertex2f(120.0, -70.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0, 100)
    glEnd()


    glFlush()

    '''
    draw_rectangle(0.0,0.0,150.0,75.0)

    glFlush()


def update_viewport(window, width, height):
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspectRatio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspectRatio, 100.0 / aspectRatio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
