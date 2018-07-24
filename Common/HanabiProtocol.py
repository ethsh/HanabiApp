from enum import Enum
import struct

PacketType = Enum('PacketType', 'Registration')
PacketDirection = Enum('PacketDirection', 'Client2Server Server2Client')

class HanabiProtocol:

    @staticmethod
    def create_registration_packet(direction, name=""):
        ret_pkt = struct.pack('bb', PacketType.Registration.value, direction.value)
        if direction == PacketDirection.Client2Server:
            struct_fmt_pkt = "{}s".format(len(ret_pkt))
            struct_fmt_name = "{}s".format(len(name))
            ret_pkt = struct.pack(struct_fmt_pkt + struct_fmt_name, ret_pkt, name)
        return ret_pkt

    @staticmethod
    def parse_registration_packet(direction, pkt):
        # packet is
        # client -> server : | Type | Direction | Name (0-terminated) |
        # server -> client : | Type | Direction |
        if direction == PacketDirection.Client2Server:
            return pkt[2:]
        return

    parse_callbacks = [parse_registration_packet]

    def __init__(self):
        pass

    @staticmethod
    def parse_message(pkt):
        pkt_type, direction = struct.unpack('bb', pkt[0:2])
        res = HanabiProtocol.parse_callbacks[pkt_type - 1].__func__(PacketDirection(direction), pkt)
        return PacketType(pkt_type), PacketDirection(direction), res


