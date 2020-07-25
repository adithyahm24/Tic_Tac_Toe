import os
from tkinter import *
from tkinter.messagebox import showinfo


class tic_tac_toe(Tk):
    def __init__(self):
        super().__init__()
        self.y = ''
        self.x = 2
        self.player_1 = []
        self.player_2 = []
        self.tttFrame = Frame(self)
        self.tttFrame.pack()
        self.list = []
        l1 = Label(self.tttFrame, text="player 1 : X", font="times 15")
        l1.grid(row=0, column=1)
        l2 = Label(self.tttFrame, text="player 2 : O", font="times 15")
        l2.grid(row=0, column=2)
        Button(self.tttFrame, text="Restart", command=self.restart_program).grid(row=0,column=3)
        self.b1 = Button(self.tttFrame,font="times 15", width=16, height=8, command=lambda: self.sign(1))
        self.b1.grid(row=1, column=1)

        self.b2 = Button(self.tttFrame,font="times 15", width=16, height=8, command=lambda: self.sign(2))
        self.b2.grid(row=1, column=2)

        self.b3 = Button(self.tttFrame,font="times 15", width=16, height=8, command=lambda: self.sign(3))
        self.b3.grid(row=1, column=3)

        self.b4 = Button(self.tttFrame,font="times 15", width=16, height=8, command=lambda: self.sign(4))
        self.b4.grid(row=4, column=1)

        self.b5 = Button(self.tttFrame,font="times 15", width=16, height=8, command=lambda: self.sign(5))
        self.b5.grid(row=4, column=2)

        self.b6 = Button(self.tttFrame,font="times 15", width=16, height=8, command=lambda: self.sign(6))
        self.b6.grid(row=4, column=3)

        self.b7 = Button(self.tttFrame,font="times 15", width=16, height=8, command=lambda: self.sign(7))
        self.b7.grid(row=8, column=1)

        self.b8 = Button(self.tttFrame,font="times 15", width=16, height=8, command=lambda: self.sign(8))
        self.b8.grid(row=8, column=2)

        self.b9 = Button(self.tttFrame,font="times 15", width=16, height=8, command=lambda: self.sign(9))
        self.b9.grid(row=8, column=3)

    def eval(self):
        sets = {}
        sets[1] = [1, 2, 3]
        sets[2] = [3, 5, 7]
        sets[3] = [1, 5, 9]
        sets[4] = [4, 5, 6]
        sets[5] = [7, 8, 9]
        sets[6] = [1, 4, 7]
        sets[7] = [2, 5, 8]
        sets[8] = [3, 6, 9]
        self.player_1.sort()
        self.player_2.sort()
        for i in sets:
            print(sets[i], self.player_1)
            #for j in sets[i]:
            if all(elem in self.player_1 for elem in sets[i]):
                print(sets[i], self.player_1)
                showinfo('Game Results ', "Player 1 Won!!!")
                return True
            if all(elem in self.player_2 for elem in sets[i]):
                showinfo('Game Results ', "Player 2 Won!!!")
                return True
        return False

    def sign(self, num):

        if num == 1:
            if self.x % 2 == 0:
                self.y = "X"
                self.player_1.append(num)
                print(self.player_1)

            else:
                self.y = 'O'
                self.player_2.append(num)
                print(self.player_2)
            self.b1.config(text=self.y)
            if self.y =='X':
                self.b1.config(bg="#ffc400")
            else:
                self.b1.config(bg="#0084ff")
            self.x = self.x + 1

        if num == 2:
            if self.x % 2 == 0:
                self.y = "X"
                self.player_1.append(num)
                print(self.player_1)

            else:
                self.y = 'O'
                self.player_2.append(num)
                print(self.player_2)
            self.b2.config(text=self.y)
            if self.y =='X':
                self.b2.config(bg="#ffc400")
            else:
                self.b2.config(bg="#0084ff")
            self.x = self.x + 1

        if num == 3:
            if self.x % 2 == 0:
                self.y = "X"
                self.player_1.append(num)
                print(self.player_1)

            else:
                self.y = 'O'
                self.player_2.append(num)
                print(self.player_2)
            self.b3.config(text=self.y)
            if self.y =='X':
                self.b3.config(bg="#ffc400")
            else:
                self.b3.config(bg="#0084ff")
            self.x = self.x + 1

        if num == 4:
            if self.x % 2 == 0:
                self.y = "X"
                self.player_1.append(num)
                print(self.player_1)

            else:
                self.y = 'O'
                self.player_2.append(num)
                print(self.player_2)
            self.b4.config(text=self.y)
            if self.y =='X':
                self.b4.config(bg="#ffc400")
            else:
                self.b4.config(bg="#0084ff")
            self.x = self.x + 1

        if num == 5:
            if self.x % 2 == 0:
                self.y = "X"
                self.player_1.append(num)
                print(self.player_1)

            else:
                self.y = 'O'
                self.player_2.append(num)
                print(self.player_2)
            self.b5.config(text=self.y)
            if self.y =='X':
                self.b5.config(bg="#ffc400")
            else:
                self.b5.config(bg="#0084ff")
            self.x = self.x + 1

        if num == 6:
            if self.x % 2 == 0:
                self.y = "X"
                self.player_1.append(num)
                print(self.player_1)

            else:
                self.y = 'O'
                self.player_2.append(num)
                print(self.player_2)
            self.b6.config(text=self.y)
            if self.y =='X':
                self.b6.config(bg="#ffc400")
            else:
                self.b6.config(bg="#0084ff")
            self.x = self.x + 1

        if num == 7:
            if self.x % 2 == 0:
                self.y = "X"
                self.player_1.append(num)
                print(self.player_1)

            else:
                self.y = 'O'
                self.player_2.append(num)
                print(self.player_2)
            self.b7.config(text=self.y)
            if self.y =='X':
                self.b7.config(bg="#ffc400")
            else:
                self.b7.config(bg="#0084ff")
            self.x = self.x + 1

        if num == 8:
            if self.x % 2 == 0:
                self.y = "X"
                self.player_1.append(num)
                print(self.player_1)

            else:
                self.y = 'O'
                self.player_2.append(num)
                print(self.player_2)
            self.b8.config(text=self.y)
            if self.y =='X':
                self.b8.config(bg="#ffc400")
            else:
                self.b8.config(bg="#0084ff")
            self.x = self.x + 1

        if num == 9:
            if self.x % 2 == 0:
                self.y = "X"
                self.player_1.append(num)
                print(self.player_1)

            else:
                self.y = 'O'
                self.player_2.append(num)
                print(self.player_2)
            self.b9.config(text=self.y)
            if self.y =='X':
                self.b9.config(bg="#ffc400")
            else:
                self.b9.config(bg="#0084ff")
            self.x = self.x + 1

        self.eval()

    def restart_program(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, *sys.argv)


app = tic_tac_toe()
app.mainloop()
