# NetMo(Network Monitor)



## Introduction:


In a time where one's life is seamlessly integrated with the internet,
and more of our time is spent browsing the world wide web. 
it is essential to be knowledgeable  of network traffic in one's personal network.



Some of the benefits of monitoring your personal network are:


	*ability to know what parties your or other people's
	 machines are communicating with over the internet

	*the ability as a parent to monitor the internet activity
	 or your children, to better protect them from the wild
	 wasteland that is the internet


	*picking out any unusual activity from your device, 
	 that could be an indication of a compromise in your
	 machine's security




Many tools exist that are focused on network monitoring, and network packet analysis,
 some of them are accusable threw a paywall, others are open source. 
 the one that is by far the most widespread, and ubiquitous is Wireshark.


Wireshark offers to the user near endless capabilities when it comes to network monitoring,
 and packet analysis, at the extremally competitive price of 0$. the main issue with Wireshark
 is the high barrier of entry in terms of expertise.  
 if you are not a person who is well versed in the realm of networking, Wireshark to you is as
 useful as a digital paperweight.


It could be easily argued that people who need the ability to monitor their networks the most,
 are the people who are not able to use Wireshark.

A regular everyday user, someone who only wants to  monitor the internet activity of others in their network,
 or just check-in on their personal machine, dont need the full power of Wireshark,
 and they could be easily overwhelmed.



## Example of Wireshark:

![](ReadMeStuff/ws.png)





## introduction to NetMo:
NetMo(Network Monitor) is a program aiming at bringing the benefits of Wireshark to the regular user, with as little fuss as   possible. it aims to show the user what they need, in simple terms, and in ease of accessibility.

It also builds over what Wireshark offers by having IP Geolocation capabilities, which tells the user the location of the destination of each packet, and plots it on a map for them. it also adds to the packet the DNS response of the destination IP address if one existed.

NeMo takes a file that was captured by Wireshark, and turns it from a hard to understand complicated overload of information, to a simple useful  and easy to understand format, and adds on top of what has already been captured by Wireshark.

![](ReadMeStuff/netmo.gif)



## Live Capture:

currently NetMo is not fully standalone, due to the fact that live capture capabilities have not been added, this was brought about by the incompatibility of pyshark( a module that offers the power of Wireshark in python) with windows, in the future live capture will be added to a version of NetMo that is Linux based, and if pyshark live capture becomes compatible with windows in the future that feature will be added to the Windows version. 






## How to run the program?
This program uses pyshark,Abstract-python-ip-geolocation,Dnspython,pyqt5,PyQtWebEngine,folium,pandas. To install the required dependencies, run:

```
$ pip install -r requirements.txt
```

Then you can run the code using:

```
python main.py
```



## user Manual:


## 1
![](ReadMeStuff/import.png)

click the import button, choose the capture file you want to read and press open



## 2
![](ReadMeStuff/mappath.png)

create a directory for the resulting map to be stored in


## 3
![](ReadMeStuff/run.png)
press run



## 4
![](ReadMeStuff/progress.png)
wait for the progress bar to finish



## 5
![](ReadMeStuff/ipfilter.png)

use dropdown menu to filter with accordance to source IP



## 6
![](ReadMeStuff/reset.png)
reset filtering done by the IP filter



## 7
![](ReadMeStuff/usemap.png)
you can drag around the map, zoom in and zoom out



## 8
![](ReadMeStuff/mapopen.png)
open the map on web browser











