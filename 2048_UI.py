from tkinter import Frame, Label, CENTER

import Constants as c
import Logics

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        #self.commands={c.UP:Logics.upMove,c.DOWN:Logics.downMove,c.LEFT:Logics.leftMove,c.RIGHT:Logics.rightMove}
        self.master.bind("<Key>",self.key_down)
        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.mainloop()
        
    def init_grid(self):
        background=Frame(self,bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE,height=c.SIZE)
        background.grid()
        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                cell=Frame(background,bg=c.BACKGROUND_COLOR_CELL_EMPTY,width=c.SIZE/c.GRID_LEN,height=c.SIZE/c.GRID_LEN)
                
                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)
                t=Label(master=cell,text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY,justify=CENTER,font=c.FONT,width=5,height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)
            
    def init_matrix(self):
        self.matrix=Logics.startGame()
        Logics.add_new_2(self.matrix)
        Logics.add_new_2(self.matrix)
        
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                newNumber=self.matrix[i][j]
                if(newNumber==0):
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(newNumber),bg=c.BACKGROUND_COLOR_DICT[newNumber],fg=c.CELL_COLOR_DICT[newNumber])
        self.update_idletasks()
                    


##    def callback(self,event):
##        self.frame.focus_set()
    
    def key_down(self,event):
        key=str(event.char)
        print(key)
        if key in c.COMMANDS:
            self.matrix,changed=c.COMMANDS[key](self.matrix)
            if changed:
                Logics.add_new_2(self.matrix)
                self.update_grid_cells()
                changed=False
                if Logics.Current_state(self.matrix)=="WON":
                    self.grid_cells[1][1].configure(text="YOU",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="WIN!",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if Logics.Current_state(self.matrix)=="LOSS":
                    self.grid_cells[1][1].configure(text="YOU",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="LOSE!",bg=c.BACKGROUND_COLOR_CELL_EMPTY)

                
                
grid=Game2048()
