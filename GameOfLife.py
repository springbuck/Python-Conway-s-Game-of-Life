import matplotlib.pyplot as plot
import numpy as np


"""Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

Any live cell with two or three live neighbours survives.
Any dead cell with three live neighbours becomes a live cell.
All other live cells die in the next generation. Similarly, all other dead cells stay dead."""


class GameOfLife():
    def __init__(self, row,col, speed):
        self.row = row
        self.col = col
        self.board = np.zeros((col,row),int)
        self.speed = speed


    def FillCell(self,row,col):
        self.board[row,col]=1

    def SetSpeed(self,speed):
        self.speed = speed

    def RunIterations(self, iterations: int):
        counter = 0
        for i in range(iterations):
            self.DisplayGraph(counter)
            NewBoard = np.zeros((self.col, self.row), int)
            for x in range(1,self.row-1):
                for y in range(1, self.col-1):
                    NewBoard[x,y] = self.CellCheck(x,y)

            self.board = NewBoard.copy()
            self.board[0] = 0
            self.board[-1] = 0
            self.board[:, 0] = 0
            self.board[:, -1] = 0
            counter+=1




    def Run(self):
        cont = True
        counter = 0
        while cont:
            self.DisplayGraph(counter)
            NewBoard = np.zeros((self.col, self.row), int)
            for x in range(1,self.row-1):
                for y in range(1, self.col-1):
                    NewBoard[x,y] = self.CellCheck(x,y)
            if np.array_equal(self.board,NewBoard):
                cont = False
            self.board = NewBoard.copy()
            self.board[0] = 0
            self.board[-1] = 0
            self.board[:, 0] = 0
            self.board[:, -1] = 0
            counter+=1



    def CellCheck(self,x,y):
        #check the cells neighbours
        neighbourAmount = 0
        if self.board[x-1,y-1]>0:
            neighbourAmount+=1
        if self.board[x-1,y]>0:
            neighbourAmount+=1
        if self.board[x-1,y+1]>0:
            neighbourAmount+=1
        if self.board[x,y-1]>0:
            neighbourAmount+=1
        if self.board[x,y+1]>0:
            neighbourAmount+=1
        if self.board[x+1,y-1]>0:
            neighbourAmount+=1
        if self.board[x+1,y]>0:
            neighbourAmount+=1
        if self.board[x+1,y+1]>0:
            neighbourAmount+=1



        if neighbourAmount<2 or neighbourAmount>3:
            return 0
        elif neighbourAmount == 3:
            return 1
        else:
            return self.board[x,y]


    def DisplayGraph(self, iteration):
        plot.axis("off")
        plot.title("Iteration "+ str(iteration),loc='center')
        plot.imshow(self.board)
        plot.draw()
        plot.pause(self.speed)

    def ExampleGlider(self):
        self.FillCell(3,2)
        self.FillCell(4,3)
        self.FillCell(5,3)
        self.FillCell(5,2)
        self.FillCell(5,1)

if __name__=='__main__':
    test = GameOfLife(20,20,0.5)
    test.ExampleGlider()
    test.Run()
