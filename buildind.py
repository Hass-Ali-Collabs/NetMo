
import pyshark


class Packet:



	def __init__( self, src_ip,des_ip,src_city,src_country,des_city,des_coutry,src_port,des_port,protocol, dns_name):


		self.src_ip=src_ip
		self.des_ip=des_ip
		self.src_city=src_city
		self.src_country=src_country
		self.des_city=des_city
		self.des_coutry=des_coutry
		self.src_port=src_port
		self.des_port=des_port
		self.protocol=protocol
		self.dns_name=dns_name



C = pyshark.FileCapture('C:/Users/HP/Desktop/test.pcapng')
#self, src_ip,des_ip,src_city,src_country,des_city,des_coutry,port,protocol, dns_name



l=[]



def creat(pkt):
    try:
        protocol =  pkt.transport_layer
        src_addr = pkt.ip.src
        src_port = pkt[pkt.transport_layer].srcport
        dst_addr = pkt.ip.dst
        dst_port = pkt[pkt.transport_layer].dstport
        p = Packet(src_addr,dst_addr,"x","x","x","x",src_port,dst_port,pkt.transport_layer,"")
        l.append(p)
    except AttributeError as e:
        #ignore packets that aren't TCP/UDP or IPv4
        pass


IN=0

def add_DNS(pkt):
	try:
		if pkt.dns.qry_name:
			#l[pkt.no].dns_name=pkt.dms.qry_name
			print(pkt.dms.qry_name)
			#IN+=1
	except AttributeError as e:
		#IN+=1
        #ignore packets that aren't DNS Request
		#print(pkt.no)
		pass
	try:
		if pkt.dns.resp_name:
			#l[pkt.no].dns_name=pkt.dms.qry_name
			print(pkt.dms.resp_name)

			#IN+=1
	except AttributeError as e:
		#IN+=1
        #ignore packets that aren't DNS Response
		pass

C.apply_on_packets(creat, timeout=100)
C.apply_on_packets(add_DNS, timeout=100)
