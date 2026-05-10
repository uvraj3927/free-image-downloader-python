import requests
import tkinter

window=tkinter.Tk()
window.title("Free-Image-Downloader")
window.geometry("400x200")

label1=tkinter.Label(window,text="Enter URL:",font=("Arial",13))
label1.pack(side="left",padx=10)

entry1=tkinter.Entry(window,width=50)
entry1.pack(side="left")

def get_image():
    url_of_image=entry1.get()
    img_response=requests.get(url_of_image)
    
    with open("image.jpg","wb") as f:
        f.write(img_response.content) 

button1=tkinter.Button(window,text="Download",bg="skyblue",fg="blue",command=get_image).place(x=320,y=150)

window.mainloop()