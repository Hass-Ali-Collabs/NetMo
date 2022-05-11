from python_ip_geolocation import AbstractIpGeolocation
import pyshark
import socket
import time



class Packet:



	def __init__( self, src_ip,des_ip,src_city,src_country,des_city,des_country,src_port,des_port,protocol, dns_name,prity):


		self.src_ip=src_ip
		self.des_ip=des_ip
		self.src_city=src_city
		self.src_country=src_country
		self.des_city=des_city
		self.des_country=des_country
		self.src_port=src_port
		self.des_port=des_port
		self.protocol=protocol
		self.dns_name=dns_name
		self.prity=prity
		self.long=""
		self.lat=""

	def __call__(self):
		if self.src_ip!="":
			if self.dns_name!="":
				return "Sender IP: "+self.src_ip+" Riciver IP: "+self.des_ip+" Sender location: "+self.city+"-"+self.src_country+" URL: "+self.dns_name
			else:
				return "Sender IP: "+self.src_ip+" Riciver IP: "+self.des_ip+" Sender location: "+self.city+"-"+self.src_country



IP_GEOLOCATION_API_KEY =  "e8f7044192ae4f8a8d69eb3372297c48";# Get your API Key from https://app.abstractapi.com/api/ip-geolocation/documentation
AbstractIpGeolocation.configure(IP_GEOLOCATION_API_KEY)

def infile(s):
	

	C = pyshark.FileCapture(s)#if error /U008.. put path between "" and r befor it

	l=[]

	def creat(pkt):
		try:

			protocol =  pkt.transport_layer
			src_addr = pkt.ip.src
			src_port = pkt[pkt.transport_layer].srcport
			dst_addr = pkt.ip.dst
			dst_port = pkt[pkt.transport_layer].dstport
			if dst_addr[0:3]!="192" and dst_addr[0:3]!="172" and dst_addr[0:3]!="10." :
				p = Packet(src_addr,dst_addr,"x","x","x","x",src_port,dst_port,pkt.transport_layer,"",pkt.pretty_print)
				l.append(p)
		except AttributeError as e:


	        #ignore packets that aren't TCP/UDP or IPv4
			pass

	


	def url(ls):
		for x in range(0,len(ls)):
			try:
				ls[x].dns_name=socket.gethostbyaddr(ls[x].des_ip)[0]
			except Exception as e:
				pass


	def ips(pks):
		comb_ls=[]
		ls=[]
		try:
			for x in pks:
				if x.des_ip not in comb_ls and x.src_ip!="":
					time.sleep(0.3)
					z=AbstractIpGeolocation.look_up(x.des_ip)
					print([x.des_ip,z.city,z.country,z.longitude,z.latitude])
					comb_ls.append(x.des_ip)
					ls.append([x.des_ip,z.city,z.country,z.longitude,z.latitude])
		except  Exception as e:
			pass
		return ls

			
		











	# def add_DNS(pkt):
	# 	global IN
	# 	# #if(IN==len(l)):
	# 	# 	return none
		
	# 	try:
	# 		if pkt.dns.qry_name:
	# 			l[IN].dns_name=pkt.dms.qry_name
	# 			print(pkt.dms.qry_name)
	# 	except AttributeError as e:
	# 		l[IN].dns_name=""
	#         #ignore packets that aren't DNS Request
	# 		pass
	# 	try:
	# 		if pkt.dns.resp_name:
	# 			l[IN].dns_name=pkt.dms.qry_name
	# 			print(pkt.dms.resp_name)

	# 	except AttributeError as e:
	# 		l[IN].dns_name=""
	#         #ignore packets that aren't DNS Response
	# 		pass
	# 	IN +=1
		#print(IN) 

	C.apply_on_packets(creat, timeout=100)
	#C.apply_on_packets(add_DNS, timeout=100)
	ips(l)
	url(l)





	return l 


