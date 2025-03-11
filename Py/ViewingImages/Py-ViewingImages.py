import tkinter as tk
from PIL import Image, ImageTk
from resizeimage import resizeimage
win=tk.Tk()
win.title("Image Viewer")
win.geometry("300x300")
path=r'/home/user/Документы/.Git/Py/Py-ViewingImages/img/test.jpg'
resized_image=resizeimage.resize_cover(Image.open(path), [300, 300])
render_pic=ImageTk.PhotoImage(resized_image)
img=tk.Label(win,image=render_pic)
img.pack()
win.mainloop()
'''
Make a program for viewing images
# Разработка viewing images.
Decision:
tuser@kvmubuntu:~$ mkdir Py-ViewingImages
tuser@kvmubuntu:~$ cd Py-ViewingImages
tuser@kvmubuntu:~$ python3 -m venv Py-Env
tuser@kvmubuntu:~$ source Py-Env/bin/activate
tuser@kvmubuntu:~$ sudo apt-get install python3-tk
tuser@kvmubuntu:~$ pip install Pillow
tuser@kvmubuntu:~$ pip install python-resize-image
tuser@kvmubuntu:~$ python Py-ViewingImages.py
tuser@kvmubuntu:~$ deactivate
'''