import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
#show='*'顯示成密碼樣子
#show='1'全變成1
e = tk.Entry(window,show=None)
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)
def insert_end():
    var = e.get()
    #t.insert('end',var)
    t.insert('end',var)
    
b1 = tk.Button(window,text='insert point',width=15,height=2,
               command=insert_point)
b1.pack()
b2 = tk.Button(window,text='insert end',command=insert_end)
b2.pack()

#默認框
t = tk.Text(window,height=2)
t.pack()

window.mainloop()
