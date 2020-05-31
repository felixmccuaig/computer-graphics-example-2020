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

    
orthogonalProjection = [[1, 0, 0], [0, 1, 0]]

teapotVertices = [];
faceOrder = [];

with open('teapot.obj', 'r') as teapot:
    for line in teapot:
        strippedLine = line.strip()
        components = strippedLine.split()
        if(len(components) > 3):
            if(components[0] == "v"):
                teapotVertices.append((float(components[1]), float(components[2]), float(components[3])))
            else:
                faceOrder.append((int(components[1]), int(components[2]), int(components[3])))
        del components
        del strippedLine
        del line
            
            
        
        





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

def render2(vertices, faces):
    projectedRepresentation = []
    for vertex in vertices:
        projectedRepresentation.append(project(vertex));
    gameDisplay.fill(black)

    for i in range(len(faces)):
        if len(projectedRepresentation) >= i + 1:
            pygame.draw.line(gameDisplay, green, projectedRepresentation[faces[i][0]], projectedRepresentation[faces[i][1]])
            pygame.draw.line(gameDisplay, green, projectedRepresentation[faces[i][1]], projectedRepresentation[faces[i][2]])
            pygame.draw.line(gameDisplay, green, projectedRepresentation[faces[i][0]], projectedRepresentation[faces[i][2]])
    del projectedRepresentation
    pygame.display.update()

vertices = [(-1, 1, 1), (1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, -1), (1, 1, -1), (1, -1, -1), (-1, -1, -1), (0, 0, 2), (0, 0, -2)];
connectionOrder = [[2, 4, 5, 9], [3, 6, 9], [4, 7, 9], [8, 9], [6, 8, 10], [7, 10], [8, 10], [10]];

deltaTime = 0

HZ = 60

timePerFrame = 1 / 60

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

        

    for i in range(len(teapotVertices)):
        teapotVertices[i] = rotateVertexByX(teapotVertices[i], 1 * (math.pi / 180));
        teapotVertices[i] = rotateVertexByY(teapotVertices[i], 1 * (math.pi / 180));
        teapotVertices[i] = rotateVertexByZ(teapotVertices[i], 1 * (math.pi / 180));
    
    render2(teapotVertices, faceOrder)

    finalTime = time.time()
    deltaTime = finalTime - ogTime;
    if(timePerFrame - deltaTime > 0):
        time.sleep(timePerFrame - deltaTime)


    
    







