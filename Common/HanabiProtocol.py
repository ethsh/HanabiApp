from enum import Enum
import struct
import pickle

PacketType = Enum('PacketType', 'REGISTRATION ENTER_GAME RECEIVE_CARD OPERATION')


class HanabiMessage:
    def __init__(self, msg_type, *args, **kwargs):
        self.msg_type = msg_type
        self.args = args
        self.kwargs = kwargs

    def serialize_message(self):
        return pickle.dumps(self)

    @staticmethod
    def deserialize_msg(serialized_data):
        return pickle.loads(serialized_data)


class HanabiProtocol:
    @staticmethod
    def create_registration_packet(name=""):
        ret_pkt = struct.pack('b', PacketType.Registration.value)
        struct_fmt_pkt = "{}s".format(len(ret_pkt))
        struct_fmt_name = "{}s".format(len(name))
        ret_pkt = struct.pack(struct_fmt_pkt + struct_fmt_name, ret_pkt, name)
        return ret_pkt

    @staticmethod
    def parse_registration_packet(direction, pkt):
        ret = {}
        # packet is
        # client -> server : | Type | Name |
        # server -> client : | Type |
        # if direction == PacketDirection.Client2Server:
        #    ret['name'] = pkt[1:]
        return ret



    parse_callbacks = [parse_registration_packet]

    def __init__(self):
        pass

    @staticmethod
    def parse_message(pkt, direction):
        pkt_type = struct.unpack('b', pkt[0:1])
        res = HanabiProtocol.parse_callbacks[pkt_type - 1].__func__(PacketDirection(direction), pkt)
        return res


