
# Import libraries
import socket
import netifaces
import psutil
  


import pyshark









cap = pyshark.FileCapture('test.pcapng')



for pkt in cap:
	print (pkt)




















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