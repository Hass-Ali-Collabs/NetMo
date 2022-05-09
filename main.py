
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
        print(src_addr )
        l.append(p)
    except AttributeError as e:
        #ignore packets that aren't TCP/UDP or IPv4
        pass


count=0

def add_DNS(pkt):
	try:
		if pkt.dns.qry_name:
			l[count].dns_name=pkt.dms.qry_name
			count+=1
	except AttributeError as e:
		count+=1
        #ignore packets that aren't DNS Request
		pass
	try:
		if pkt.dns.resp_name:
			l[count].dns_name=pkt.dms.qry_name
			count+=1
	except AttributeError as e:
		count+=1
        #ignore packets that aren't DNS Response
		pass





C.apply_on_packets(creat, timeout=100)
C.apply_on_packets(add_DNS, timeout=100)

for x in range(0,len(l)):
	print(l[x].dns_name)





















# #print(socket.if_nameindex())
# #{40006E13-22EC-4E2B-99BC-B7F27F5EB7FA}', '{6DE9F7FB-BFB4-40D8-87BA-7DD580E097FC}', '{5A6E7CCA-312E-4E2E-A04D-EB8A817AF603}', '{8DC31D1C-DDC1-11E7-B15C-806E6F6E6963}']

# print(pyshark.tshark.tshark.get_tshark_interfaces())
# cap = pyshark.LiveCapture(interface='40006E13-22EC-4E2B-99BC-B7F27F5EB7FA')
# cap.sniff(timeout=3)
# print(cap[0])
# #<LiveCapture (5 packets)>

# # for pkt in cap:
# # 	print (pkt)

# # print("test")


# # # Showing gateway list
# # print(netifaces.interfaces())





# # addrs = psutil.net_if_addrs()
# # print(addrs)




# # import netifaces as ni
# # import winreg as wr
# # from pprint import pprint

# # def get_connection_name_from_guid(iface_guids):
# #     iface_names = ['(unknown)' for i in range(len(iface_guids))]
# #     reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
# #     reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
# #     for i in range(len(iface_guids)):
# #         try:
# #             reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'\Connection')
# #             iface_names[i] = wr.QueryValueEx(reg_subkey, 'Name')[0]
# #         except FileNotFoundError:
# #             pass
# #     return iface_names

# # x = ni.interfaces()
# # pprint(get_connection_name_from_guid(x))






# def capture_live_packets(network_interface):
#     capture = pyshark.LiveCapture(interface=network_interface)
#     for raw_packet in capture.sniff_continuously():
#         print(filter_all_tcp_traffic_file(raw_packet))

# def get_packet_details(packet):
#     """
#     This function is designed to parse specific details from an individual packet.
#     :param packet: raw packet from either a pcap file or via live capture using TShark
#     :return: specific packet details
#     """
#     protocol = packet.transport_layer
#     source_address = packet.ip.src
#     source_port = packet[packet.transport_layer].srcport
#     destination_address = packet.ip.dst
#     destination_port = packet[packet.transport_layer].dstport
#     packet_time = packet.sniff_time
#     return f'Packet Timestamp: {packet_time}' \
#            f'\nProtocol type: {protocol}' \
#            f'\nSource address: {source_address}' \
#            f'\nSource port: {source_port}' \
#            f'\nDestination address: {destination_address}' \
#            f'\nDestination port: {destination_port}\n'


# def filter_all_tcp_traffic_file(packet):
#     """
#     This function is designed to parse all the Transmission Control Protocol(TCP) packets
#     :param packet: raw packet
#     :return: specific packet details
#     """
#     if hasattr(packet, 'tcp'):
#        results = get_packet_details(packet)
#        return results

# capture_live_packets('40006E13-22EC-4E2B-99BC-B7F27F5EB7FA')