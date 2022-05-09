
# Import libraries
import socket
import netifaces
import psutil
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



C = pyshark.FileCapture('test.pcapng')
#self, src_ip,des_ip,src_city,src_country,des_city,des_coutry,port,protocol, dns_name



l=[]



def print_conversation_header(pkt):
    try:
        protocol =  pkt.transport_layer
        src_addr = pkt.ip.src
        src_port = pkt[pkt.transport_layer].srcport
        dst_addr = pkt.ip.dst
        dst_port = pkt[pkt.transport_layer].dstport
        p = Packet(src_addr,dst_addr,"x","x","x","x",src_port,dst_port,pkt.transport_layer,"")
        print(src_addr )
        l.append(p)
    except AttributeError as e:
        #ignore packets that aren't TCP/UDP or IPv4
        pass

C.apply_on_packets(print_conversation_header, timeout=100)



print(len(l))
# try:
# 	p = Packet(C[0].ip.src,C[0].ip.dst,"x","x","x","x",C[0][C[0].transport_layer].srcport,C[0][C[0].transport_layer].dstport,C[0].transport_layer,C[0].dns.qry_name)
# except AttributeError as e:
#         #ignore packets that aren't TCP/UDP or IPv4
#         pass

# print(p.src_ip+" "+p.des_ip+" "+p.src_city+" "+p.src_country+" "+p.des_city+" "+p.des_coutry+" "+p.port,protocol+" "+p.dns_name)





















