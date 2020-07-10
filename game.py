import pygame

given_board1 = [[7,2,3,0,0,0,1,5,9],
               [6,0,0,3,0,2,0,0,8],
               [8,0,0,0,1,0,0,0,2],
               [0,7,0,6,5,4,0,2,0],
               [0,0,4,2,0,7,3,0,0],
               [0,5,0,9,3,1,0,4,0],
               [5,0,0,0,7,0,0,0,3],
               [4,0,0,1,0,3,0,0,6],
               [9,3,2,0,0,0,7,1,4]]
current_board = [[0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0]]
test_board = [[0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0]]
solved_board = [[0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0]]

#to display screen 1
def screen_1():
    screen1 = pygame.display.set_mode((600, 700))
    running = True
    while running:
        screen1.fill((0, 0, 0))
        img1 = pygame.image.load('screen1.png')
        screen.blit(img1,(0,0))
        for event in pygame.event.get():
            # quit if cross is pressed
            if event.type == pygame.QUIT:
                running = False
                quit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    board_input()

                elif event.key == pygame.K_2:
                    screen_2(given_board1)

        pygame.display.update()


#to display screen 2
def screen_2(given_board):
    screen2 = pygame.display.set_mode((600, 700))
    running = True
    while running:
        screen2.fill((0, 0, 0))
        img2 = pygame.image.load('screen2.png')
        screen.blit(img2,(0,0))
        for event in pygame.event.get():
            # quit if cross is pressed
            if event.type == pygame.QUIT:
                running = False
                quit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    screen_3(given_board)

                elif event.key == pygame.K_2:
                    screen_4(given_board)

        pygame.display.update()



#to display screen 3 (game screen)
def screen_3(given_board):

    #to copy given table onto solved table and then solve solved table
    for i in range(9):
        for j in range(9):
            solved_board[i][j] = given_board[i][j]
    solve(solved_board)

    print(given_board)
    print(solved_board)
    print(current_board)
    running = True
    x = 20
    y = 20
    # k and l are index of the highlighted square
    k = 0
    l = 0
    #flag=0 means show rules, flag=1 means show congratulations, flag=2 means H is pressed
    flag = 0

    while running:

        #fill background color
        screen.fill((255, 255, 255))

        # draw background grid
        screen.blit(background, (0, 0))

        # draw highlight square
        movehighlight(x, y)

        # draw given table
        for i in range(9):
            for j in range(9):
                drawnumbers(i, j, given_board[j][i], 0)

        # draw current table
        for i in range(9):
            for j in range(9):
                drawnumbers(i, j, current_board[j][i], 1)

        # draw congratulations/wrong answer
        if flag == 0:
            # draw rules
            pygame.font.init()
            myfont = pygame.font.SysFont('AERIAL', 30)
            textsurface = myfont.render("Press 'ESC' key to check the answer.", False, (0, 0, 0))
            screen.blit(textsurface, (10, 610))
            textsurface = myfont.render("Press 'H' key to fill 1 block correctly.", False, (0, 0, 0))
            screen.blit(textsurface, (10, 635))



        elif flag == 1:
            for i in range(9):
                for j in range(9):
                    if given_board[i][j] == 0:
                        test_board[i][j] = current_board[i][j]
                    else:
                        test_board[i][j] = given_board[i][j]

            print(test_board)
            print(solved_board)

            trigger = 0
            for i in range(9):
                for j in range(9):
                    if test_board[i][j] != solved_board[i][j]:
                        trigger += 1

            if trigger == 0:
                pygame.font.init()
                myfont = pygame.font.SysFont('AERIAL', 40)
                textsurface = myfont.render('CONGRATULATIONS!', False, (255, 0, 0))
                screen.blit(textsurface, (150, 610))
                textsurface = myfont.render('YOU SOLVED THE SUDOKU CORRECTLY!', False, (255, 0, 0))
                screen.blit(textsurface, (20, 650))

            else:
                pygame.font.init()
                myfont = pygame.font.SysFont('Comic Sans MS', 45)
                textsurface = myfont.render('WRONG ANSWER', False, (255, 0, 0))
                screen.blit(textsurface, (100, 600))
            flag = 0

        elif flag == 2:
            current_board[k][l] = solved_board[k][l]
            flag = 0



        # check the keystrokes
        for event in pygame.event.get():
            x_change = 0
            y_change = 0

            # quit if cross is pressed
            if event.type == pygame.QUIT:
                running = False
                quit()
            # other key presses
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -1
                    l -= 1
                    print(k, l)

                elif event.key == pygame.K_RIGHT:
                    x_change = +1
                    l += 1
                    print(k, l)

                elif event.key == pygame.K_UP:
                    y_change = -1
                    k -= 1
                    print(k, l)

                elif event.key == pygame.K_DOWN:
                    y_change = 1
                    k += 1
                    print(k, l)

                elif event.key == pygame.K_1:
                    if given_board[k][l] == 0:
                        print(current_board[k][l], k, l)
                        current_board[k][l] = 1

                elif event.key == pygame.K_2:
                    print(given_board)
                    print(current_board)
                    if given_board[k][l] == 0:
                        print(current_board[k][l], l, k)
                        current_board[k][l] = 2

                elif event.key == pygame.K_3:
                    if given_board[k][l] == 0:
                        print(current_board[k][l], k, l)
                        current_board[k][l] = 3

                elif event.key == pygame.K_4:
                    if given_board[k][l] == 0:
                        print(current_board[k][l], k, l)
                        current_board[k][l] = 4

                elif event.key == pygame.K_5:
                    if given_board[k][l] == 0:
                        print(current_board[k][l], k, l)
                        current_board[k][l] = 5

                elif event.key == pygame.K_6:
                    if given_board[k][l] == 0:
                        print(current_board[k][l], k, l)
                        current_board[k][l] = 6

                elif event.key == pygame.K_7:
                    if given_board[k][l] == 0:
                        print(current_board[k][l], k, l)
                        current_board[k][l] = 7

                elif event.key == pygame.K_8:
                    if given_board[k][l] == 0:
                        print(current_board[k][l], k, l)
                        current_board[k][l] = 8

                elif event.key == pygame.K_9:
                    if given_board[k][l] == 0:
                        print(current_board[k][l], k, l)
                        current_board[k][l] = 9

                elif event.key == pygame.K_ESCAPE:
                    flag = 1
                    print("escape was pressed")

                elif event.key == pygame.K_h:
                    flag = 2
                    print("Help was pressed")

            # x and y are new cordinates for highlight in pixels
            x = x + x_change * 61.5
            y = y + y_change * 61.5

            # to maintain grid boundary for highlight
            if x < 20:
                x = 20
            if y < 20:
                y = 20
            if x > 512:
                x = 512
            if y > 512:
                y = 512

            # to maintain grid boundary for index of highlighted element
            if k < 0:
                k = 0
            if k > 8:
                k = 8
            if l < 0:
                l = 0
            if l > 8:
                l = 8

        pygame.display.update()


#to solve the table and show result
def screen_4(given_board):

    #to copy given table onto solved table and then solve solved table
    for i in range(9):
        for j in range(9):
            solved_board[i][j] = given_board[i][j]
    solve(solved_board)

    running = True
    while running:

        #fill background color
        screen.fill((255, 255, 255))

        # draw background grid
        screen.blit(background, (0, 0))

        # draw given table
        for i in range(9):
            for j in range(9):
                drawnumbers(i, j, solved_board[j][i], 0)

        # check the keystrokes
        for event in pygame.event.get():

            # quit if cross is pressed
            if event.type == pygame.QUIT:
                running = False
                quit()
        pygame.display.update()


#to take input of a board
def board_input():
    given_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    running = True
    # x and y are new coordinates for highlight in pixels
    x = 20
    y = 20
    # k and l are index of the highlighted square
    k = 0
    l = 0
    while running:
        # fill background color
        screen.fill((255, 255, 255))

        # draw background grid
        screen.blit(background, (0, 0))

        # draw highlight square
        movehighlight(x, y)

        #draw given board
        for i in range(9):
            for j in range(9):
                drawnumbers(i, j, given_board[j][i], 0)

        #draw rules
        pygame.font.init()
        myfont = pygame.font.SysFont('AERIAL', 30)
        textsurface = myfont.render('Press ENTER / RETURN once you fill the table.', False, (0, 0, 0))
        screen.blit(textsurface, (10, 610))

        for event in pygame.event.get():
            x_change = 0
            y_change = 0

            # quit if cross is pressed
            if event.type == pygame.QUIT:
                running = False
                quit()
            # other key presses
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -1
                    l -= 1
                    print(k, l)

                elif event.key == pygame.K_RIGHT:
                    x_change = +1
                    l += 1
                    print(k, l)

                elif event.key == pygame.K_UP:
                    y_change = -1
                    k -= 1
                    print(k, l)

                elif event.key == pygame.K_DOWN:
                    y_change = 1
                    k += 1
                    print(k, l)

                elif event.key == pygame.K_1:
                    given_board[k][l] = 1

                elif event.key == pygame.K_2:
                    given_board[k][l] = 2

                elif event.key == pygame.K_3:
                    given_board[k][l] = 3

                elif event.key == pygame.K_4:
                    given_board[k][l] = 4

                elif event.key == pygame.K_5:
                    given_board[k][l] = 5

                elif event.key == pygame.K_6:
                    given_board[k][l] = 6

                elif event.key == pygame.K_7:
                    given_board[k][l] = 7

                elif event.key == pygame.K_8:
                    given_board[k][l] = 8

                elif event.key == pygame.K_9:
                    given_board[k][l] = 9

                elif event.key == pygame.K_0:
                    given_board[k][l] = 0

                elif event.key == pygame.K_RETURN:
                    screen_2(given_board)


            x = x + x_change * 61.5
            y = y + y_change * 61.5

            # to maintain grid boundary for highlight
            if x < 20:
                x = 20
            if y < 20:
                y = 20
            if x > 512:
                x = 512
            if y > 512:
                y = 512

            # to maintain grid boundary for index of highlighted element
            if k < 0:
                k = 0
            if k > 8:
                k = 8
            if l < 0:
                l = 0
            if l > 8:
                l = 8

        pygame.display.update()



#used by solve function
def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return(i,j)
    else:
        return (None)


#used by solve function
def valid(bo,num,pos):
    #row
    for j in range(9):
        if bo[pos[0]][j] == num and j != pos[1]:
            return (False)

    #column
    for i in range(9):
        if bo[i][pos[1]] == num and i!=pos[0] :
            return (False)

    #subgrid
    x_sub = int(pos[0]/3)
    y_sub = int(pos[1]/3)
    for i in range(x_sub * 3 , (x_sub * 3) + 3):
        for j in range(y_sub * 3 , (y_sub*3) + 3):
            if bo[i][j] == num and (i,j)!=pos:
                return(False)

    return (True)


#used to solve
def solve(bo):
    find = find_empty(bo)
    if not find :
        return (True)
    else :
        x,y = find

    for i in range(1,10):
        if valid(bo,i,(x,y)):
            bo[x][y] = i

            if solve(bo):
                return (True)

            bo[x][y] = 0

    return(False)





#initialize pygame
pygame.init()

#create a screen
screen = pygame.display.set_mode((600,700))

#place screen title
pygame.display.set_caption('sudoku-gui')

#place screen icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#place background image (600,600)
background = pygame.image.load('grid.png')

#place highlight image (63,63)
highlight = pygame.image.load('highlight.png')


#draw the highlight
def movehighlight(x,y):
    screen.blit(highlight,(x,y))

#draw the numbers on screen
def drawnumbers(x,y,num,color):
    pygame.font.init()
    #0 for black, 1 for blue
    if color == 0:
        myfont = pygame.font.SysFont('Comic Sans MS', 45)

        if num==1:
            textsurface = myfont.render('1', False, (0, 0, 0))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        elif num==2:
            textsurface = myfont.render('2', False, (0, 0, 0))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==3:
            textsurface = myfont.render('3', False, (0, 0, 0))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==4:
            textsurface = myfont.render('4', False, (0, 0, 0))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==5:
            textsurface = myfont.render('5', False, (0, 0, 0))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==6:
            textsurface = myfont.render('6', False, (0, 0, 0))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==7:
            textsurface = myfont.render('7', False, (0, 0, 0))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==8:
            textsurface = myfont.render('8', False, (0, 0, 0))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==9:
            textsurface = myfont.render('9', False, (0, 0, 0))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))

    elif color == 1:
        myfont = pygame.font.SysFont('Comic Sans MS', 45)

        if num==1:
            textsurface = myfont.render('1', False, (47,86,233))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        elif num==2:
            textsurface = myfont.render('2', False, (47,86,233))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==3:
            textsurface = myfont.render('3', False, (47,86,233))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==4:
            textsurface = myfont.render('4', False, (47,86,233))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==5:
            textsurface = myfont.render('5', False, (47,86,233))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==6:
            textsurface = myfont.render('6', False, (47,86,233))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==7:
            textsurface = myfont.render('7', False, (47,86,233))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==8:
            textsurface = myfont.render('8', False, (47,86,233))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))
        if num==9:
            textsurface = myfont.render('9', False, (47,86,233))
            screen.blit(textsurface, (40+61.5*x, 20+61.5*y))

#run screen 1
screen_1()
