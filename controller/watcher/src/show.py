import sys
import tkinter
from PIL import Image, ImageTk
import threading
import time
import urllib.request
import io
import requests
import json
 
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
    url = "http://192.168.10.15:8080/api/products"

    products_get = requests.get(url)

    product_dict = products_get.json()[-1] #最新のレコードを辞書型で取得
    image_url = product_dict['image'] #imageのURLを取得
    img_read = urllib.request.urlopen(image_url).read()
    img_bin = io.BytesIO(img_read)

    img2 = Image.open(img_bin)  # PILで開く

    # img2 = Image.open('image/display_unlocked_qr.jpeg')
    img2 = ImageTk.PhotoImage(img2)
    time.sleep(3) 
    

    canvas.itemconfig(item,image=img2)
    time.sleep(3)

    img = Image.open('image/display_locked_qr.jpeg')
    img = ImageTk.PhotoImage(img)
    canvas.itemconfig(item,image=img)   