#getting the interface name as a list with netaface 

import netifaces
netifaces.interfaces()
#['lo0', 'gif0', 'stf0', 'en0', 'en1', 'fw0']



import netifaces as ni
import winreg as wr
from pprint import pprint

def get_connection_name_from_guid(iface_guids):
    iface_names = ['(unknown)' for i in range(len(iface_guids))]
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
    for i in range(len(iface_guids)):
        try:
            reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'\Connection')
            iface_names[i] = wr.QueryValueEx(reg_subkey, 'Name')[0]
        except FileNotFoundError:
            pass
    return iface_names

x = ni.interfaces()
pprint(get_connection_name_from_guid(x))



"""['Local Area Connection* 12',
 'Bluetooth Network Connection',
 'Wi-Fi',
 'Ethernet',
 'VirtualBox Host-Only Network',
 '(unknown)',
 'isatap.{4E4150B0-643B-42EA-AEEA-A14FBD6B1844}',
 'isatap.{BB05D283-4CBF-4514-B76C-7B7EBB2FC85B}']"""