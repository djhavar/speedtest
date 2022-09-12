from tkinter import *
import speedtest

root=Tk()
root.config(bg="#25f555")
root.title("Internet Speed Test")
root.geometry("500x500")

label = Label(root, text="internet Speed Check",font=("lucinda Sans unicode",18,"bold","italic"), fg="#2d13f0", bg="#25f555")
label.place(relx=0.5,rely=0.1,anchor=CENTER)

label_download = Label(root, text="download ",font=("lucinda Sans unicode",18,"bold","italic"), fg="#2d13f0", bg="#25f555")
label_download.place(relx=0.25,rely=0.5,anchor=CENTER)

label_upload = Label(root, text="upload speed",font=("lucinda Sans unicode",18,"bold","italic"), fg="#2d13f0", bg="#25f555")
label_upload.place(relx=0.75,rely=0.5,anchor=CENTER)

label_download_speed = Label(root,font=("Yu Gothic Light",14,"bold","italic"), fg="#2d13f0", bg="#25f555")
label_download_speed.place(relx=0.25,rely=0.6,anchor=CENTER)

label_upload_speed = Label(root,font=("Yu Gothic Light",14,"bold","italic"), fg="#2d13f0", bg="#25f555")
label_upload_speed.place(relx=0.75,rely=0.6,anchor=CENTER)

def speedCheck():
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000,2)
    label_download_speed['text'] = str(download_speed) + "mbps"
    upload_speed = round(st.download()/1000000,2)
    label_upload_speed['text'] = str(upload_speed) + "mbps"
    
btn_check = Button(root,text="Check Speed",command=speedCheck(),bg='#dba718',fg="#fc0317")
btn_check.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()

