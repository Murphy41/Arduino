#!/usr/bin/env python3

import rospy
import serial
from std_msgs.msg import Bool, Int32

ser = serial.Serial('/dev/ttyUSB0',115200, timeout=1)

def timer_callback(event):
    if ser.in_waiting>0:
        incoming_byte = ser.read(1)
        if incoming_byte:
            number = int.from_bytes(incoming_byte, byteorder='little')
            rospy.loginfo("Received:{number}")
            UI_pub.publish(number)


def button_callback(msg):
    """
    Callback function for the 'button_pressed' topic.
    Logs the button state.
    """
    if msg.data:
        rospy.loginfo("Button has been pressed!")
        ser.write(bytes[3])

    else:
        rospy.loginfo("Button state is false.")

def listener():
    """
    Publishes to the 'led' topic every 10 seconds to toggle the LED state.
    """
    # rospy.init_node('led_toggle_node', anonymous=True)
    rospy.init_node('ui_comm_node', anonymous=True)

    # led_pub = rospy.Publisher('led', Bool, queue_size=10)
    global UI_pub
    UI_pub = rospy.Publisher('UI', Int32, queue_size=10)

    button_sub = rospy.Subscriber('button', Bool, button_callback)
    timer = rospy.Timer(rospy.Duration(1), timer_callback)
    # rate = rospy.Rate(0.1)  # 0.1 Hz = every 10 seconds
    # led_state = False

    rospy.spin

    # rospy.loginfo("LED toggle publisher is running.")

    # while not rospy.is_shutdown():
    #     led_state = not led_state  # Toggle LED state
    #     led_pub.publish(led_state)
    #     rospy.loginfo(f"Published LED state: {'ON' if led_state else 'OFF'}")
    #     rate.sleep()

if __name__ == "__main__":
    listener()
