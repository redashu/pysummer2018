#!/usr/bin/python2
import time
import webbrowser
option='''
Press  1 :  to  enter any thing - split each word and search on google 
Press  2 :  same  but find URL 
Press  3 :   same  but find  images answer 
Press  4 :   current time and date 
Press  5 :   open default browser 
Press  6 : all Network IP 
Press  7 :  enter domain name and find owner , email , contact 
'''
print  option

ch=raw_input()

if   ch ==  '1'  :
	search_data=raw_input("enter data : ")
	final_data=search_data.strip()
	#  above removing  leading and trailing space 
	done_data=final_data.split()
        #  spliting each word by space 
	for  i  in  done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)

else :

	print  "no chance !!"

