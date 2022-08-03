import socket
import struct
import binascii

class Sniffer():

    def ethernet_frame(self, data):
        proto = ""
        IpHeader = struct.unpack("!6s6sH",data[0:14])
        dstMac = binascii.hexlify(IpHeader[0]) 
        srcMac = binascii.hexlify(IpHeader[1]) 
        protoType = IpHeader[2] 
        nextProto = hex(protoType) 

        if (nextProto == '0x800'): 
            proto = 'IPV4'
        elif (nextProto == '0x86dd'): 
            proto = 'IPV6'

        data = data[14:]

        return dstMac, srcMac, proto, data

    def collect_packets(self):
        sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        while True:
            raw_data, addr = sock.recvfrom(65565)
            dest_mac, src_mac, protoType, data = self.ethernet_frame(raw_data)
            if dest_mac != b'000000000000':
                print(dest_mac)
                print(src_mac)
                print("Protocol: " + str(protoType))
                print(data)
                print("\n")
            
    
    def decode_packet(self, raw_data):
         pass
    
    
        
if __name__ == "__main__":
    s = Sniffer()
    s.collect_packets()
    