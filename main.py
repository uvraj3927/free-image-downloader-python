import requests
import tkinter

def get_image():
    url_of_image=entry1.get()
    img_response=requests.get(url_of_image)
    name=entry2.get()
    with open("name","wb") as f:
        f.write(img_response.content)
    entry1.delete(0,"end")
    entry2.delete(0,"end")

#window creation    
window=tkinter.Tk()
window.title("Free-Image-Downloader")
window.geometry("400x200")
window.config(bg="skyblue")

label1=tkinter.Label(
        window,
        text="Enter URL:",
        bg="skyblue",
        font=("Arial",13))
label1.place(x=10,y=50)

entry1=tkinter.Entry(
        window,
        width=50)
entry1.place(x=100,y=50)

label2=tkinter.Label(
        window,
        text="File name:",
        bg="skyblue",
        font=("Arial",12))
label2.place(x=10,y=100)

entry2=tkinter.Entry(
        window,
        width=30)
entry2.place(x=100,y=100)

button1=tkinter.Button(
        window,
        text="Download",
        bg="lightgreen",
        fg="blue",
        command=get_image)
button1.place(x=320,y=150)

window.mainloop()

 
