import tkinter as tk
import random
import re

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class DieRoller(Page):

    def get_random(self,max):
        return random.randint(1, int(max))

    def die_cast(self, input):
        dice = input.split(" ")
        if len(dice) > 0:
            value = ""
            for die in dice:
                pattern = re.compile("\d+d\d+")
                if pattern.match(die):
                    values = die.split("d")
                    output = ""
                    sum = 0
                    for i in range(int(values[0])):
                        roll = self.get_random(values[1])
                        sum += roll
                        output = output + str(roll) + ", "
                    output = die+': '+output.strip(", ")+'\nSUM: '+str(sum)+'\nAVG: '+str(sum/float(values[0]))+"\n"
                    value = value + output + "\n"
            return value


    def onClick(self, entry, roll_value):
       roll_value.set(self.die_cast(entry.get()))

    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Die Roller")
       label.grid(row=0, column=0)
       e = tk.Entry(self)
       e.grid(row=1, column=0)
       roll_value = tk.StringVar()
       roll_value.set("")
       roll = tk.Label(self, textvariable=roll_value, justify="left")
       roll.grid(row=3, column=0)
       roll_button = tk.Button(self, text="Roll", command=lambda : self.onClick(e, roll_value))
       roll_button.grid(row=2, column=0)

       


class Page2(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = DieRoller(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="both", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Die Roller", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x650")
    root.mainloop()