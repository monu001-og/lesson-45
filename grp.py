import tkinter as tk 

window =tk.Tk()

for i in range(3):
    for j in range(3):
        frame= tk.frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=1,column=j,madx=5,pady=5)
        lavel=tk.Label(master=frame,text=f"Row {i}\ncolumn {j}")
        label.pack()
window.mainloop()
        