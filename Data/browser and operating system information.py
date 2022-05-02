user_agent = 
        [('User-agent',
        'Mozilla/5.0 (X11;U;Linux 2.4.2.-2 i586; en-us;m18) Gecko/200010131 Netscape6/6.01'
        )]

        #Program to change the user agent
#Verify the UserAgent with wireshark tool

import mechanize

#function to browse the web page
def change_user_agent(url, user_agent):
        try:
                #Create browser object
                browser=mechanize.Browser()
                browser.set_handle_robots(False)
                #add user agent
                browser.addheaders=user_agent
                
                #open web url
                page=browser.open(url)
                
                #read page source code
                source_code = page.read()
        
                #print source code
                print source_code
        except:
                print "Error in browsing....."

url = str(raw_input("Enter the website name: "))

#user agent details
user_agent=[('User-agent','Mozilla/5.0 (X11;U;Linux 2.4.2.-2 i586; en-us;m18) Gecko/200010131 Netscape6/6.01')]

change_user_agent(url,user_agent)