from arp_mon import ARPMon
from pylibpcap import get_iface_list, get_first_iface
import ifcfg


if __name__ == '__main__':
    #signal.signal(signal.SIGINT, sigint_handler)
    default = ifcfg.default_interface()
    device = str(default['device'])
    arp = ARPMon(device)
    arp.send()

