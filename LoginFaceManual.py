from tkinter import Tk, PhotoImage, Button, Label, StringVar, Entry
from threading import Thread as Process
import cv2
import time
from face_recognition import face_encodings, compare_faces, load_image_file
import os
from PIL import ImageTk, Image
def pascheck(idt, past):
    if idt == "StartCode@@@" and past == "12121@!#":
        root.after(1000, root.destroy)
        print("yo")
        #################################### Your Code after login ###################################
        sroot = Tk()
        sroot.title("login successfull")
        sroot.geometry("300x200")
        sroot.title("Login")
        sroot.attributes('-alpha', 0.8)
        sroot.configure(background="black")
        idlab = Label(sroot, text="Hello User", fg="white", bg="black", font=("Segoe UI", 18))
        idlab.place(relx=0.2, rely=0.3)
        sroot.mainloop()
        ##############################################################################################
    else:
        print("Unauthorized Access")
def paschecklog(idt, past):
    global auth
    if idt == "ary" and past == "1234":
        auth = True
def loginGui():
    global idv
    global pas
    global root
    global auth
    root = Tk()
    root.geometry("300x200")
    root.title("Login")
    root.attributes('-alpha', 0.8)
    root.configure(background="black")
    root.iconify()
    idv = StringVar()
    pas = StringVar()
    idlab = Label(root, text="Id", fg="white", bg="black", font=("Segoe UI", 12))
    identry = Entry(root, textvariable=idv)
    paslab = Label(root, text="Passcode", fg="white", bg="black", font=("Segoe UI", 12))
    pasentry = Entry(root, textvariable=pas)
    identry.place(relx=0.4, rely=0.3)
    idlab.place(relx=0.2, rely=0.3)
    pasentry.place(relx=0.4, rely=0.5)
    paslab.place(relx=0.1, rely=0.5)
    bg = PhotoImage(file=".\sign_button.png")
    signin = Button(root, image=bg, bg="black", bd=0, command=lambda: paschecklog(idv.get(), pas.get()))
    signin.image = bg
    signin.place(rely=0.7, relx=0.36)
    root.mainloop()
def facelog():
    global auth
    path = "IMGD"
    known_image = load_image_file(path+"/model.png")
    encoding = face_encodings(known_image)[0]
    cap = cv2.VideoCapture(0)
    while not auth:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        try:
            unknown_image = face_encodings(imgS)[0]
            results = compare_faces([encoding], unknown_image, tolerance=0.5)
        except:
            results = [False]
        if results[0]:
            break
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()
    pascheck('StartCode@@@', '12121@!#')
if __name__ == "__main__":
    ad = time.time()
    if not os.path.exists('IMGD'):
        os.makedirs('IMGD')
    if not os.listdir('./IMGD'):
        root = Tk()
        root.geometry("700x600")
        root.title("Create Face Model")
        frame = Label(root)
        frame.place(x=0, y=10, relwidth=1, relheight=1)
        text = StringVar()
        namel = Label(root, textvariable=text)
        namel.place(x=0, rely=0)
        create = Button(root, text="Create Face model", bg="black", fg="white", bd=0,
                        command=lambda: cv2.imwrite(os.getcwd() + "/IMGD/model.png", img1))
        create.place(rely=0.93, relx=0.44)
        cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(img))
            frame['image'] = img
            root.update()
    else:
        pass
    auth = False
    a = Process(target=facelog, args="")
    a.start()
    loginGui()
    print(round(time.time()-ad, 2),"s Taken to login")