import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

class SantaCruz(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Resultados, Resultados2016, Resultados2017, Resultados2018):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Resultados")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Resultados(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = tk.Button(self, text="Resultados 2016",
                            command=lambda: controller.show_frame("Resultados2016"))
        button2 = tk.Button(self, text="Resultados 2017",
                            command=lambda: controller.show_frame("Resultados2017"))
        button3 = tk.Button(self, text='Resultados 2018',
                            command=lambda: controller.show_frame('Resultados2018'))

        button1.pack()
        button2.pack()
        button3.pack()

class Resultados2016(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Resultados 2016", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Voltar",
                           command=lambda: controller.show_frame("Resultados"))
        button.pack()

"""
class Resultados2016(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Resultados 2016", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Voltar",
                           command=lambda: controller.show_frame("Resultados"))
        button.pack()
"""
class Resultados2017(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Resultados 2017", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Voltar",
                           command=lambda: controller.show_frame("Resultados"))
        button.pack()

class Resultados2018(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Resultados 2018", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Voltar",
                           command=lambda: controller.show_frame("Resultados"))
        button.pack()


if __name__ == "__main__":
    app = SantaCruz()
    app.mainloop()


