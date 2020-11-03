import sys
import tkinter
from PIL import Image, ImageTk
import threading
import time
 
def show_image():

    global item, canvas
 
    root = tkinter.Tk()
    root.attributes('-fullscreen', True)
    # root.bind('', lambda e: root.destroy())
    root.title('Status')
    root.geometry("1920x1080")
    img = Image.open('image/display_locked_qr.jpeg')
    img = ImageTk.PhotoImage(img)
    canvas = tkinter.Canvas(bg = "black", width=1920, height=1080)
    canvas.place(x=0, y=0)
    item = canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
    root.mainloop()
 

thread1 = threading.Thread(target=show_image)
thread1.start()
 
while(True):
    img2 = Image.open('image/display_unlocked_qr.jpeg')
    img2 = ImageTk.PhotoImage(img2)
    time.sleep(3) 
    

    canvas.itemconfig(item,image=img2)
    time.sleep(3)

    img = Image.open('image/display_locked_qr.jpeg')
    img = ImageTk.PhotoImage(img)
    canvas.itemconfig(item,image=img)   