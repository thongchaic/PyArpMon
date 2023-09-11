from pylibpcap.pcap import sniff
import binascii
from arp import ARP 
from pylibpcap import get_first_iface

class ARPMon:
    def __init__(self, dev):
        self.dev = dev
    
    def start(self):
        for plen, t, buf in sniff(self.dev, count=-1, promisc=1, filters="arp"):
            arp = ARP(buf)
            arp.pretty()

if __name__ == '__main__':
    dev=get_first_iface()
    print(dev)
    mon = ARPMon(dev)
