from tkinter import *
import tkinter as tk
import time
import os.path

kvs1 = 99.0
kvs2 = 99.0
prev = 0.0
best1 = 99.0
best2 = 99.0
data5 = 0.0
kvs1s = 0.0
kvs1e = 0.0
flag = 0
flag2 = 0
test = 0
flag_b1 = 0
flag_b2 = 0

from pathlib import Path
filename1 = "ENG_OIL_TEMP.tmp"
filename2 = "ENG_OIL_PRESS.tmp"
filename3 = "ENG_COOL_TEMP.tmp"
filename4 = "INTK_AIR_TEMP.tmp"
filename5 = "VEH_SPEED.tmp"
filename6 = "BOOST_PRESS.tmp"
filename7 = "SUP_BAT.tmp"
filename8 = "TANK_LVL.tmp"
file_best1 = "best1.txt"
file_best2 = "best2.txt"

file1 = Path("/home/pi/ENG_OIL_TEMP.tmp")
file2 = Path("/home/pi/ENG_OIL_PRESS.tmp")
file3 = Path("/home/pi/ENG_COOL_TEMP.tmp")
file4 = Path("/home/pi/INTK_AIR_TEMP.tmp")
file5 = Path("/home/pi/VEH_SPEED.tmp")
file6 = Path("/home/pi/BOOST_PRESS.tmp")
file7 = Path("/home/pi/SUP_BAT.tmp")
file8 = Path("/home/pi/TANK_LVL.tmp")

def raise_frame(frame):
    frame.tkraise()
    
def reset1():
    fp = open("best1.txt", 'w')
    fp.write(str(0.0))
    fp.close()
	
def flg_r1():
    global flag_b1
    if(flag_b1 == 0):
        flag_b1 = 1
		
def flg_rr1():
    global flag_b1
    if(flag_b1 == 1):
        flag_b1 = 0
        
def flg_r2():
    global flag_b2
    if(flag_b2 == 0):
        flag_b2 = 1
        
def flg_rr2():
    global flag_b2
    if(flag_b2 == 1):
        flag_b2 = 0
    
def reset2():
    fp = open("best2.txt", 'w')
    fp.write(str(0.0))
    fp.close()
    
def clock():
    if file1.exists():
        with open(filename1, 'r') as f1:
            data1 = f1.read()
            eot.config(text = data1 + chr(176) +"C", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))

    if file2.exists():
        with open(filename2, 'r') as f2:
            data2 = f2.read()
            eop.config(text = data2 + " bar", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))

    if file3.exists():
        with open(filename3, 'r') as f3:
            data3 = f3.read()
            ect.config(text = data3 + chr(176) + "C", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
		
    if file4.exists():
        with open(filename4, 'r') as f4:
            data4 = f4.read()
            iat.config(text = data4 + chr(176) + "C", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
		
    if file5.exists():
        with open(filename5, 'r') as f5:
            global data5
            data5 = float(f5.read())
			
            global kvs1
            global kvs2
            global prev
            global best1
            global best2
            global kvs1s
            global kvs1e
            global flag
            global flag2
            global test
            global flag_b1
            global flag_b2
			
            if (prev == 0 and data5 > 0):
                kvs1s = time.time()
                flag=1
                flag2=1 
            if (data5 >= 100 and flag == 1):
                kvs1e = time.time()
                kvs1 = kvs1e - kvs1s
                flag=0
                
            #Button(f2, text='Reset', bg="#1FC6F9", command=lambda:reset(fb1, file_best1)).place(relx=0.78, rely=0.34, anchor='s')
            #Button(f2, text='Reset', bg="#1FC6F9", command=lambda:reset(fb2, file_best2)).place(relx=0.78, rely=0.48, anchor='s')
            #B1["command"]= "reset(fb1, file_best1)"
            
            fb1 = open(file_best1, 'r')
            test = fb1.read()
            fb1.close()
			
            if (test == str(0.0)):
                fb1 = open(file_best1, 'w')
                fb1.write(str(99.0))
                fb1.close()
                float(best1)
				
            if (test == str(99.0)):
                fb1 = open(file_best1, 'w')
                fb1.write(str(best1))
                fb1.close()
                float(best1)
            else:
                fb1 = open(file_best1, 'r')
                best1 = fb1.read()
                fb1.close()
                float(best1)
                
            if (best1 == str(0.0)):
                fb1 = open(file_best1, 'w')
                fb1.write(str(99.0))
                fb1.close() 
				
            if (kvs1 < float(best1)):
                best1 = kvs1
                fb1 = open(file_best1, 'w')
                fb1.write(str(best1))
                fb1.close()
                float(best1)
                
            if(flag_b1 == 1):
                best1 = 99.0
                kvs1 = 99.0
                reset1()
                flg_rr1()
                flag4 = 1
                    
            if(data5 >= 200 and flag2 == 1):
                kvs2e = time.time()
                kvs2 = kvs2e - kvs1s
                flag2 = 0
                
            #B2["command"]= "reset(fb2, file_best2)"
                
            fb2 = open(file_best2, 'r')
            test2 = fb2.read()
            fb2.close()
			
            if (test2 == str(0.0)):
                fb2 = open(file_best2, 'w')
                fb2.write(str(99.0))
                fb2.close()
                float(best2)
				
            if (test2 == str(99.0)):
                fb2 = open(file_best2, 'w')
                fb2.write(str(best2))
                fb2.close()
                float(best2)
            else:
                fb2 = open(file_best2, 'r')
                best2 = fb2.read()
                fb2.close()
                float(best2)
                
            if(kvs2 < float(best2)):
                best2 = kvs2
                fb2 = open(file_best2, 'w')
                fb2.write(str(best2))
                fb2.close()
                float(best2)
                
            if(flag_b2 == 1):
                best2 = 99.0
                kvs2 = 99.0
                reset2()
                flg_rr2()
                flag4 = 1
                    
            prev = data5	
            
            if(float(best1) > 50 or float(best1) == 0.0 ):
                acc1_b.config(text = "- - ", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
                flag4 = 0
            else:
                acc1_b.config(text =  "%.2f" % float(best1) + "s", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
            if(float(best2) > 90 or float(best2) == 0.0):
                acc2_b.config(text = "- - ", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
            else:
                acc2_b.config(text = "%.2f" % float(best2) + "s", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
            
            if(kvs1 > 50 or kvs1 == 0):
                acc1.config(text = "- - ", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
            else:
                acc1.config(text= "%.2f" % kvs1 + "s", foreground='#1FC6F9', font=('arial', 28, 'bold'))
            if(kvs2 > 90 or kvs2 == 0):
                acc2.config(text = "- - ", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
            else:
                acc2.config(text = "%.2f" % kvs2 + "s", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
            vs.config(text = str(data5) + " km/h", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
		
    if file6.exists():
        with open(filename6, 'r') as f6:
            data6 = f6.read()
            bp.config(text = data6 , foreground = '#1FC6F9', font = ('arial', 48, 'bold'))
            if(float(data6) == 0):
			
                w0.tag_raise(wb0)
                w1.tag_raise(wb1)
                w2.tag_raise(wb2)
                w3.tag_raise(wb3)
                w4.tag_raise(wb4)
                w5.tag_raise(wb5)
                w6.tag_raise(wb6)
                w7.tag_raise(wb7)
                w8.tag_raise(wb8)
				
            if(float(data6) > 0 and float(data6) < 0.3):
                
                w0.tag_raise(wf0)
                w1.tag_raise(wb1)
                w2.tag_raise(wb2)
                w3.tag_raise(wb3)
                w4.tag_raise(wb4)
                w5.tag_raise(wb5)
                w6.tag_raise(wb6)
                w7.tag_raise(wb7)
                w8.tag_raise(wb8)
                
            if(float(data6) >= 0.3 and float(data6) < 0.6):
                
                w0.tag_raise(wf0)
                w1.tag_raise(wf1)
                w2.tag_raise(wb2)
                w3.tag_raise(wb3)
                w4.tag_raise(wb4)
                w5.tag_raise(wb5)
                w6.tag_raise(wb6)
                w7.tag_raise(wb7)
                w8.tag_raise(wb8)
                
            if(float(data6) >= 0.6 and float(data6) < 0.9):
                
                w0.tag_raise(wf0)
                w1.tag_raise(wf1)
                w2.tag_raise(wf2)
                w3.tag_raise(wb3)
                w4.tag_raise(wb4)
                w5.tag_raise(wb5)
                w6.tag_raise(wb6)
                w7.tag_raise(wb7)
                w8.tag_raise(wb8)
                
            if(float(data6) >= 0.9 and float(data6) < 1.2):
                
                w0.tag_raise(wf0)
                w1.tag_raise(wf1)
                w2.tag_raise(wf2)
                w3.tag_raise(wf3)
                w4.tag_raise(wb4)
                w5.tag_raise(wb5)
                w6.tag_raise(wb6)
                w7.tag_raise(wb7)
                w8.tag_raise(wb8)
              
            if(float(data6) >= 1.2 and float(data6) < 1.5):
                 
                w0.tag_raise(wf0)
                w1.tag_raise(wf1)
                w2.tag_raise(wf2)
                w3.tag_raise(wf3)
                w4.tag_raise(wf4)
                w5.tag_raise(wb5)
                w6.tag_raise(wb6)
                w7.tag_raise(wb7)
                w8.tag_raise(wb8)
                
            if(float(data6) >= 1.5 and float(data6) < 1.8):
                
                w0.tag_raise(wf0)
                w1.tag_raise(wf1)
                w2.tag_raise(wf2)
                w3.tag_raise(wf3)
                w4.tag_raise(wf4)
                w5.tag_raise(wf5)
                w6.tag_raise(wb6)
                w7.tag_raise(wb7)
                w8.tag_raise(wb8)
               
            if(float(data6) >= 1.8 and float(data6) < 2.0):
                
                w0.tag_raise(wf0)
                w1.tag_raise(wf1)
                w2.tag_raise(wf2)
                w3.tag_raise(wf3)
                w4.tag_raise(wf4)
                w5.tag_raise(wf5)
                w6.tag_raise(wf6)
                w7.tag_raise(wb7)
                w8.tag_raise(wb8)
              
            if(float(data6) >= 2.0 and float(data6) < 2.5):
                
                w0.tag_raise(wf0)
                w1.tag_raise(wf1)
                w2.tag_raise(wf2)
                w3.tag_raise(wf3)
                w4.tag_raise(wf4)
                w5.tag_raise(wf5)
                w6.tag_raise(wf6)
                w7.tag_raise(wf7)
                w8.tag_raise(wb8)
                
            if(float(data6) >= 2.5 and float(data6) <= 3.0):
                
                w0.tag_raise(wf0)
                w1.tag_raise(wf1)
                w2.tag_raise(wf2)
                w3.tag_raise(wf3)
                w4.tag_raise(wf4)
                w5.tag_raise(wf5)
                w6.tag_raise(wf6)
                w7.tag_raise(wf7)
                w8.tag_raise(wf8)
		
    if file7.exists():
        with open(filename7, 'r') as f7:
            data7 = f7.read()
            volt.config(text = data7 + "V", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
		
    if file8.exists():
        with open(filename8, 'r') as f8:
            data8 = f8.read()
            tnk.config(text = data8 + "%", foreground = '#1FC6F9', font = ('arial', 28, 'bold'))
			
    root.attributes('-fullscreen', True)	
    root.after(20, clock)
	
while True:

    root = Tk()
    
    f2 = Frame(root, width=800, height=480)
    f1 = Frame(root, width=800, height=480)
    
    for frame in (f2, f1):
        frame.grid(row=0, column=0, sticky='news')
    
    imag_static2 = tk.PhotoImage(file="bkr2.png")
    st2 = tk.Label(f2, image=imag_static2)
    st2.place(relx=0.5, rely=1.0, anchor='s')
    
    imag_static1 = tk.PhotoImage(file="bkr1.png")
    st1 = tk.Label(f1, image=imag_static1)
    st1.place(relx=0.5, rely=1.0, anchor='s')

    Button(f1, text='->', bg="#1FC6F9", command=lambda:raise_frame(f2)).place(relx=0.1, rely=0.1, anchor='s')
    Button(f2, text='<-', bg="#1FC6F9", command=lambda:raise_frame(f1)).place(relx=0.1, rely=0.1, anchor='s')
    
    Button(f2, text='Reset', bg="#1FC6F9", command=lambda:flg_r1()).place(relx=0.88, rely=0.34, anchor='s')
    Button(f2, text='Reset', bg="#1FC6F9", command=lambda:flg_r2()).place(relx=0.88, rely=0.48, anchor='s')
    
    w0 = Canvas(f1, width=46, height=32, bg="#1FC6F9", highlightbackground= "#000000")
    w1 = Canvas(f1, width=46, height=60, bg="#1FC6F9", highlightbackground= "#000000")
    w2 = Canvas(f1, width=46, height=89, bg="#1FC6F9", highlightbackground= "#000000")
    w3 = Canvas(f1, width=46, height=115, bg="#1FC6F9", highlightbackground= "#000000")
    w4 = Canvas(f1, width=45, height=139, bg="#1FC6F9", highlightbackground= "#000000")
    w5 = Canvas(f1, width=45, height=159, bg="#1FC6F9", highlightbackground= "#000000")
    w6 = Canvas(f1, width=61, height=178, bg="#1FC6F9", highlightbackground= "#000000")
    w7 = Canvas(f1, width=63, height=192, bg="#1FC6F9", highlightbackground= "#000000")
    w8 = Canvas(f1, width=63, height=202, bg="#1FC6F9", highlightbackground= "#000000")
	
    w0.place(relx=0.122, rely=0.715, anchor='s')
    w1.place(relx=0.188, rely=0.715, anchor='s')
    w2.place(relx=0.255, rely=0.715, anchor='s')
    w3.place(relx=0.323, rely=0.715, anchor='s')
    w4.place(relx=0.391, rely=0.715, anchor='s')
    w5.place(relx=0.458, rely=0.715, anchor='s')
    w6.place(relx=0.535, rely=0.715, anchor='s')
    w7.place(relx=0.625, rely=0.715, anchor='s')
    w8.place(relx=0.715, rely=0.715, anchor='s')
	
    wf0 = w0.create_rectangle(0, 0, 73, 68, fill="#1FC6F9")
    wf1 = w1.create_rectangle(0, 0, 73, 128, fill="#1FC6F9")
    wf2 = w2.create_rectangle(0, 0, 73, 190, fill="#1FC6F9")
    wf3 = w3.create_rectangle(0, 0, 73, 249, fill="#1FC6F9")
    wf4 = w4.create_rectangle(0, 0, 72, 295, fill="#1FC6F9")
    wf5 = w5.create_rectangle(0, 0, 72, 340, fill="#1FC6F9")
    wf6 = w6.create_rectangle(0, 0, 97, 380, fill="#1FC6F9")
    wf7 = w7.create_rectangle(0, 0, 100, 410, fill="#1FC6F9")
    wf8 = w8.create_rectangle(0, 0, 100, 430, fill="#1FC6F9")
	
    wb0 = w0.create_rectangle(0, 0, 73, 65, fill="#000000")
    wb1 = w1.create_rectangle(0, 0, 73, 125, fill="#000000")
    wb2 = w2.create_rectangle(0, 0, 73, 190, fill="#000000")
    wb3 = w3.create_rectangle(0, 0, 73, 250, fill="#000000")
    wb4 = w4.create_rectangle(0, 0, 72, 295, fill="#000000")
    wb5 = w5.create_rectangle(0, 0, 72, 340, fill="#000000")
    wb6 = w6.create_rectangle(0, 0, 97, 380, fill="#000000")
    wb7 = w7.create_rectangle(0, 0, 100, 410, fill="#000000")
    wb8 = w8.create_rectangle(0, 0, 100, 430, fill="#000000")
    
    eot = Label(f1, borderwidth=0, relief="solid", bg="#000000")
    eot.place(relx=0.5, rely=0.945, anchor='s')
    
    eop = Label(f1, borderwidth=0, relief="solid", bg="#000000")	
    eop.place(relx=0.9, rely=0.945, anchor='se')

    ect = Label(f2, borderwidth=0, relief="solid", bg="#000000")
    ect.place(relx=0.58, rely=0.945, anchor='se')

    iat = Label(f2, borderwidth=0, relief="solid", bg="#000000")
    iat.place(relx=0.81, rely=0.945, anchor='s')

    vs = Label(f2, borderwidth=0, relief="solid", bg="#000000")
    vs.place(relx=0.28, rely=0.645, anchor='sw')
    
    acc1 = Label(f2, borderwidth=0, relief="solid", bg="#000000")
    acc1.place(relx=0.28, rely=0.34, anchor='sw')
    
    acc2 = Label(f2, borderwidth=0, relief="solid", bg="#000000")
    acc2.place(relx=0.28, rely=0.48, anchor='sw')
    
    acc1_b = Label(f2, borderwidth=0, relief="solid", bg="#000000")
    acc1_b.place(relx=0.68, rely=0.34, anchor='sw')
    
    acc2_b = Label(f2, borderwidth=0, relief="solid", bg="#000000")
    acc2_b.place(relx=0.68, rely=0.48, anchor='sw')

    bp = Label(f1, borderwidth=0, relief="solid", bg="#000000")
    bp.place(relx=0.83, rely=0.43, anchor='sw')

    volt = Label(f1, borderwidth=0, relief="solid", bg="#000000")
    volt.place(relx=0.14, rely=0.945, anchor='sw')

    tnk = Label(f2, borderwidth=0, relief="solid",  bg="#000000")
    tnk.place(relx=0.14, rely=0.945, anchor='sw')
	
    clock()

    root.mainloop()
