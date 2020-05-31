import pygame
import math
import time

WIDTH = 1280
HEIGHT = 720

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
gameDisplay.fill(black)

# Define center at (0,0)

def rotateVertexByX(vertex, theta):
    return (vertex[0], (math.cos(theta) * vertex[1]) - (math.sin(theta) * vertex[2]), (math.cos(theta) * vertex[2]) + (math.sin(theta) * vertex[1]))

def rotateVertexByY(vertex, theta):
    return ((math.cos(theta) * vertex[0]) + (math.sin(theta) * vertex[2]), vertex[1], (math.cos(theta) * vertex[2]) - (math.sin(theta) * vertex[0]))

def rotateVertexByZ(vertex, theta):
    return ((math.cos(theta) * vertex[0]) - (math.sin(theta) * vertex[1]), (math.cos(theta) * vertex[1]) + (math.sin(theta) * vertex[0]), vertex[2])

def scaleVertex(vertex, scaleFactor):
    return (vertex[0] * scaleFactor, vertex[1] * scaleFactor, vertex[2] * scaleFactor)

def scaleVertexByX(vertex, scaleFactor):
    return (vertex[0] * scaleFactor, vertex[1], vertex[2])

def scaleVertexByY(vertex, scaleFactor):
    return (vertex[0], vertex[1] * scaleFactor, vertex[2])

def scaleVertexByZ(vertex, scaleFactor):
    return (vertex[0], vertex[1], vertex[2] * scaleFactor)

def translate(vertex, vector):
    return (vertex[0] + vector[0], vertex[1] + vector[1], vertex[2] + vector[2])

def project(vertex):
    return (int(vertex[0] * 50 + (WIDTH / 2)), int(vertex[1] * 50 + (HEIGHT / 2)))

def render(vertices, connectionOrder, scaleFactor):
    projectedRepresentation = []
    for vertex in vertices:
        vertex = scaleVertex(vertex, abs(scaleFactor))
        projectedRepresentation.append(project(vertex));
        del vertex
    gameDisplay.fill(black)

    for i in range(len(connectionOrder)):
        for j in range(len(connectionOrder[i])):
            pygame.draw.line(gameDisplay, green, projectedRepresentation[i], projectedRepresentation[connectionOrder[i][j] - 1])
    del projectedRepresentation
    pygame.display.update()

vertices = [(-1, 1, 1), (1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, -1), (1, 1, -1), (1, -1, -1), (-1, -1, -1), (0, 0, 2), (0, 0, -2)];
connectionOrder = [[2, 4, 5, 9], [3, 6, 9], [4, 7, 9], [8, 9], [6, 8, 10], [7, 10], [8, 10], [10]];

deltaTime = 0

HZ = 60

timePerFrame = 1 / HZ

scaleFactor = 1
increasing = True

upperScaleBound = 2
lowerScaleBound = -2

for i in range(len(vertices)):
        vertices[i] = scaleVertexByX(vertices[i], 3);
        vertices[i] = scaleVertexByY(vertices[i], 3);

while True:
    ogTime = time.time()

    if(increasing and scaleFactor < upperScaleBound):
       scaleFactor += 0.005
    else:
       increasing = False

    if(not increasing and scaleFactor > lowerScaleBound):
       scaleFactor -= 0.005
    else:
       increasing = True

    for i in range(len(vertices)):
        vertices[i] = rotateVertexByX(vertices[i], 1 * (math.pi / 180));
        vertices[i] = rotateVertexByY(vertices[i], 1 * (math.pi / 180));
        vertices[i] = rotateVertexByZ(vertices[i], 1 * (math.pi / 180));
    
    render(vertices, connectionOrder, scaleFactor)

    finalTime = time.time()
    deltaTime = finalTime - ogTime;
    if(timePerFrame - deltaTime > 0):
        time.sleep(timePerFrame - deltaTime)


    
    







