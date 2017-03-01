import csv
import mechanize
import time
  

browser = mechanize.Browser()
surl= 'https://m.facebook.com/search/?refid=46&search=Search&search_source=top_nav&query='
uname=["uname1","uname2","uname3","uname4","uname5"]
upass=["pass1","pass2.","pass3.","pass4.","pass5"]
date=time.strftime("%m/%d/%Y")


f=open("E:\\Projects\\found.csv","a+")



def login(user,userpass):
    
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.set_handle_refresh(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    url = 'http://m.facebook.com/login.php'
    
    browser.open(url)
    browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
    browser.form['email'] = user
    browser.form['pass'] = userpass
    response = browser.submit()
    return;



def process_data(recevied_response,pnumber):
			s_index=recevied_response.find("fref=search")+13 #filtering profile name start
			e_index=s_index
			while 1==1:
				if recevied_response[e_index]=="<" and recevied_response[e_index+1]=="/" and recevied_response[e_index+2]=="a":
					break
				e_index=e_index+1
			#e_index=str_response.find("</a><div class=\"bm bn\">")
			final_name=recevied_response[s_index:e_index]
			if final_name.find("<span class=\"alternate_name\">") !=-1:
				final_name=final_name.replace("<span class=\"alternate_name\">","")
				final_name=final_name.replace("</span>","")
			#print final_name #filtering profile name end
			e_index=recevied_response.find("?refid=") #printing username start
			s_index=e_index
			while recevied_response[s_index]!="/":
				s_index=s_index-1
			#print recevied_response[s_index:e_index] #printing username end end
			towrite="0"+pnumber+","+final_name+",http://facebook.com"+recevied_response[s_index:e_index]+",N/A,N/A,N/A,"+str(date)
			print towrite
			f.write(str(towrite)+'\n')

			return;



with open('E:\\Projects\\data3.csv') as csvfile
	readCSV = csv.reader(csvfile, delimiter=',')
	row=list(readCSV)
	for c in range(5):
		if c%10==0:
			login(uname[c/10],upass[c/10])
		response2 = browser.open(surl+"0"+str(row[c][0]))
		str_response = response2.read()
		if "No results found for" in str_response :
			print "Not Found- 0"+ str(row[c][0])
		else:
			print "Found- " + "0" + str(row[c][0])
			process_data(str_response,row[c][0])

f.close()
	






