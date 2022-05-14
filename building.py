from python_ip_geolocation import AbstractIpGeolocation
import pyshark
import time
import dns.resolver,dns.reversename



class Packet:

	"""A class in order to create a version of a packet that has what our program demands"""
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


#configuring IP geolocation 
IP_GEOLOCATION_API_KEY =  "e8f7044192ae4f8a8d69eb3372297c48";# Get your own API Key from https://app.abstractapi.com/api/ip-geolocation/documentation
AbstractIpGeolocation.configure(IP_GEOLOCATION_API_KEY)


"""a method that takes the drirectory of a capture file and returns a list of objects or type packet according to the class above"""
def infile(s,pb):
	C = pyshark.FileCapture(s)
	l=[]


	def creat(pkt):
		"""puts into the list L the packets from pyshark that the destination ip is a public IP address"""
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

	


	def url():
		"""gets the DNS hostname for every packet"""
		
		for x in l:
			try:
				z= dns.reversename.from_address(x.des_ip)
				x.dns_name=str(dns.resolver.query(z,"PTR")[0])
				print(x.dns_name)		
			except Exception as e:
				pass

 
	def locations(pks,pb):
		"""gets the geographic location of
		 every public ip present in the list of packets""" 
		pb.setValue(0)
		comb_ls=[]
		ls=[]
		i=0
		leng=len(pks)
		Total_pb =100/leng
		try:
			for x in pks:
				if x.des_ip not in comb_ls and x.src_ip!="":
					time.sleep(0.5)
					z=AbstractIpGeolocation.look_up(x.des_ip)
					print([x.des_ip,z.city,z.country,z.longitude,z.latitude])
					comb_ls.append(x.des_ip)
					ls.append([x.des_ip,z.city,z.country,z.longitude,z.latitude])
				i+=Total_pb
				pb.setValue(i)
			pb.setValue(100)
		except  Exception as e:
			pass
		return ls


	def fillinglocs(pks,loc):
		"""fills the packets with the geolocation where
		 the packet has the name destenation adress 
		 as the one that was geolocated"""
		for i in loc:

			for x in pks:
				if i[0]==x.des_ip:
					if(i[1]!=None):
						x.des_city=i[1]
					else:
						x.des_city="X"
					if(i[2]!=None):
						x.des_country=i[2]
					else:
						x.des_country="X"
					if i[3]!=None and i[4]!=None:
						x.long=i[3]
						x.lat=i[4]
					else:
						x.long=None
						x.lat=None
					
						
#puts the list L threw the above methods
	C.apply_on_packets(creat, timeout=100)
	fillinglocs(l,locations(l,pb))
	url()


#returns the list of Packets l
	return l 


