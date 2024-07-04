#!/usr/bin/python3

import rospy
from can2tcp.can2tcp import SocketCANGateway, TCPCanGateway

if __name__ == "__main__":
    rospy.init_node('tcp_can_gateway')
    can_interface = rospy.get_param('~can_interface', 'vcan0')
    gateway_host = rospy.get_param('~gateway_host', '192.168.1.4')
    gateway_port = rospy.get_param('~gateway_port', 20001)
    rospy.loginfo("TCP CAN Gateway starting on interface %s for host %s:%d", can_interface, gateway_host, gateway_port)
    tcp_can_gateway = TCPCanGateway(gateway_host, gateway_port)
    socket_can_gateway = SocketCANGateway(interface=can_interface, bitrate=1000000)
    tcp_can_gateway.set_receive_callback(socket_can_gateway.send)
    socket_can_gateway.set_receive_callback(tcp_can_gateway.send)
    while not rospy.is_shutdown():
        rospy.spin()
