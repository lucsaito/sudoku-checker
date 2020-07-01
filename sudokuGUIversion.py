import tkinter as tk


def center_window(frame):  #Takes a tk.Frame as input and return its centralized geomtry
    window_height = int(frame.winfo_screenheight() * 0.47)
    window_width = int(frame.winfo_screenwidth() * 0.3)
    screen_width = frame.winfo_screenwidth()
    screen_height = frame.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int(
        (screen_height / 2) - (window_height / 2))
    geometry = "{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)
    return geometry


class Navigation(tk.Frame):  #Titulo
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.Text = tk.Label(self, text="Fill the blanks with the numbers")
        self.Text.pack(side=tk.TOP)


class Main(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.configure(padx=80)

        self.Board = tk.Frame(self, width = 200, height = 200)
        self.Board.pack()



        self.rows = self.entry_boxes(self.Board)
        self.place_boxes(self.rows)
        self.columns = self.columns_set(self.rows)

        self.Result = tk.Label(self, text="", width=3, height=2)
        self.CheckBut = tk.Button(self, text="Check", width=10, height=2,
                                  command = lambda: self.check(self.rows, self.columns))
        self.Reset = tk.Button(self, text="Reset", width=10, height=2,
                               command= lambda: self.reset_but(self.rows))

        self.Reset.pack(side=tk.LEFT, padx=2)
        self.Result.pack(side=tk.LEFT, padx=20)
        self.CheckBut.pack(side=tk.RIGHT, padx=2)


    def entry_boxes(self, board):
        boxes = []
        for i in range(9):
            row = []
            for i in range(9):
                row.append(tk.Entry(board, width=2))
            boxes.append(row)
        return boxes
    def place_boxes(self, boxes):
        for row in boxes:
            for box in row:
                box.grid(row = boxes.index(row), column = row.index(box))
    def columns_set(self, boxes):
        columns = []
        for i in range(9):
            columns.append([
                boxes[0][i],
                boxes[1][i],
                boxes[2][i],
                boxes[3][i],
                boxes[4][i],
                boxes[5][i],
                boxes[6][i],
                boxes[7][i],
                boxes[8][i]
            ])
        return columns
    def reset_but(self, rows):
        #print("teste")
        for row in rows:
            for element in row:
                element.delete(0, tk.END)
                element.insert(0, "")
    def get_row_values(self, rows):
        _rows = []
        for row in rows:
            _elements = []
            for element in row:
                _elements.append(element.get())
            _rows.append(_elements)
        return _rows
    def get_column_values(self, columns):
        _columns = []
        for column in columns:
            _elements = []
            for element in column:
                _elements.append(element.get())
            _columns.append(_elements)
        return _columns

    def squares_create(self, rows):
        _rows = self.get_row_values(rows)
        squares = []
        bigcol1 = []
        bigcol2 = []
        bigcol3 = []
        for i in range(9):
            for j in range(3):
                bigcol1.append(_rows[i][j])
        for k in range(9):
            for j in range(3, 6):
                bigcol2.append(_rows[k][j])
        for l in range(9):
            for j in range(6, 9):
                bigcol3.append(_rows[l][j])
        squares.append(bigcol1[0:9])
        squares.append(bigcol1[9:18])
        squares.append(bigcol1[18:27])

        squares.append(bigcol2[0:9])
        squares.append(bigcol2[9:18])
        squares.append(bigcol2[18:27])

        squares.append(bigcol3[0:9])
        squares.append(bigcol3[9:18])
        squares.append(bigcol3[18:27])
        return squares
    def condition1(self, rows):
        _rows = self.get_row_values(rows)
        if all(len(set(row)) == 9 for row in _rows):
            return True
        else:
            print("False, row")
    def condition2(self, columns):
        _columns = self.get_column_values(columns)
        if all(len(set(column)) == 9 for column in _columns):
            return True
        else:
            print("False, column")

    def condition3(self, rows):
        _squares = self.squares_create(rows)
        if all(len(set(square)) == 9 for square in _squares):
            return True
        else:
            print("False, square")



    def check(self, rows, columns):
        if self.condition1(rows) and self.condition2(columns) and self.squares_create(rows):
            return self.Result.config(text="Correct")
        else:
            return self.Result.config(text="False")


class Bottom(tk.Frame):  #Botao de check e resultado
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master


class MainApplication(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title("Sudoku checker:")
        self.master.geometry(center_window(self))
        self.master.resizable(False, False)


        self.Navigation = Navigation(self).pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.Main = Main(self).pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.Bottom = Bottom(self).pack(side = tk.BOTTOM, fill = tk.BOTH, expand = True)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side=tk.TOP, fill = tk.BOTH, expand = True)
    root.mainloop()
