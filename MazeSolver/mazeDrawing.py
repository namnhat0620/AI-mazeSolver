import os
from turtle import st
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import drawPath

def visualize_maze(fig, matrix, start, end, filename, route=None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    #1. Define walls and array of direction based on the route
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]=='x']

    if route:
        direction=[]
        for i in range(1,len(route)):
            if route[i][0]-route[i-1][0]>0:
                direction.append('v') #^
            elif route[i][0]-route[i-1][0]<0:
                direction.append('^') #v        
            elif route[i][1]-route[i-1][1]>0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    #2. Drawing the map
    #ax=plt.figure(dpi=100).add_subplot(111)

    # for i in ['top','bottom','right','left']:
    #     ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=100,color='black')
    
    #plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
    #            marker='P',s=100,color='green')

    plt.scatter(start[1],-start[0],marker='*',
                s=100,color='gold')

    # if route:
    #     for i in range(len(route)-2):
    #         plt.scatter(route[i+1][1],-route[i+1][0],
    #                     marker=direction[i],color='silver')

    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    #Get output
    # plt.savefig(filename + ".png")
    # file = open(filename + ".txt", "w")
    # file.write(str(len(route)))
    # file.close()
    # artist = []
    # if route:
    #     for i in range(len(route)-2):
    #         plt.scatter(route[i+1][1],-route[i+1][0],
    #             marker=direction[i],color='silver')

    # anim = animation.ArtistAnimation(fig=ax, artists=artist)
    # anim.save('output.gif')
    drawPath.drawRoute(fig, route, direction)
    #Show on screen
    plt.show()
    

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')
    
    # for _, point in enumerate(bonus):
    #   print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')


def read_file(file_name: str = 'maze.txt'):
    f=open(file_name,'r')
    #   n_bonus_points = int(next(f)[:-1])
    #   bonus_points = []
    #   for i in range(n_bonus_points):
    #     x, y, reward = map(int, next(f)[:-1].split(' '))
    #     bonus_points.append((x, y, reward))

    text=f.read()
    matrix=[list(i) for i in text.splitlines()]
    f.close()

    return matrix

# def drawRoute(frame, route):
#     if route:
#         direction=[]
#         for i in range(1,len(route)):
#             if route[i][0]-route[i-1][0]>0:
#                 direction.append('v') #^
#             elif route[i][0]-route[i-1][0]<0:
#                 direction.append('^') #v        
#             elif route[i][1]-route[i-1][1]>0:
#                 direction.append('>')
#             else:
#                 direction.append('<')

#         direction.pop(0)

#     # if route:
#     #     for i in range(len(route)-2):
#     #         plt.scatter(route[i+1][1],-route[i+1][0],
#     #                     marker=direction[i],color='silver')

#     x.append(route[frame][0])
#     y.append(route[frame][1])

#     line.set_data(x,y)
#     return line,