
import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("1000x600+500+300")
button1 = 0
button2 = 0
button3 = 0
def up1():
    global button1
    button1 += 1
    labelleft.config(text=button1)
def up2():
    global button2
    button2 += 1
    labelright.config(text=button2)
def down1():
    global button1
    button1 -= 1
    labelleft.config(text=button1)
def down2():
    global button2
    button2 -= 1
    labelright.config(text=button2)
def up3():
    global button3
    button3 = button1 + button2
    labelmiddle.config(text=button3)
def down3():
    global points3
    button3 = button1 - button2
    labelmiddle.config(text=button3)
labelleft = tk.Label(text=0,
                     background="white",
                     foreground="red",
                     padx="20",
                     pady="10",
                     font="30",
                     height="5",
                     width="10"
                     )
labelleft.place(x=240, y=50)
labelright = tk.Label(text=0,
                      background="white",
                      foreground="red",
                      padx="20",
                      pady="10",
                      font="30",
                      height="5",
                      width="10"
                      )
labelright.place(x=600, y=50)
labelmiddle = tk.Label(text=0,
                       background="white",
                       foreground="red",
                       padx="20",
                       pady="10",
                       font="30",
                       height="5",
                       width="20"
                       )
labelmiddle.place(x=400, y=400)
plus1 = tk.Button(
    text="+",
    background="white",
    foreground="blue",
    padx="15",
    pady="5",
    font="25",
    height="1",
    width="5",
    command=up1
)
plus1.place(x=260, y=175)
minus1 = tk.Button(
    text="-",
    background="white",
    foreground="blue",
    padx="15",
    pady="5",
    font="25",
    height="1",
    width="5",
    command=down1
)
minus1.place(x=260, y=225)
plus2 = tk.Button(
    text="+",
    background="white",
    foreground="blue",
    padx="15",
    pady="5",
    font="25",
    height="1",
    width="5",
    command=up2
)
plus2.place(x=625, y=175)
minus2 = tk.Button(
    text="-",
    background="white",
    foreground="blue",
    padx="15",
    pady="5",
    font="25",
    height="1",
    width="5",
    command=down2
)
minus2.place(x=625, y=225)
plus3 = tk.Button(
    text="+",
    background="white",
    foreground="black",
    padx="20",
    pady="10",
    font="30",
    height="5",
    width="10",
    command=up3
)
plus3.place(x=400, y=50)
minus3 = tk.Button(
    text="-",
    background="white",
    foreground="black",
    padx="20",
    pady="10",
    font="30",
    height="5",
    width="10",
    command=down3
)
minus3.place(x=400, y=175)
root.mainloop()
