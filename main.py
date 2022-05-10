import building as bl








print(len(bl.infile("C:/Users/HP/Desktop/test.pcapng")))



def IP_sorting(ip):
	global l
	ipl=[]
	for x in xrange(0,len(l)):
		if l[x].src_ip == ip:
			ipl.append(l[x])
		else:
			pass
	return ipl


def only_web(paks):
	webl
	for x in xrange(0,len(paks)):
		if paks.dns_name != "":
			webl.append(paks[x])

	return webl

		


		
	














