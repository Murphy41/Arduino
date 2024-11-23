#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool

def button_callback(msg):
    """
    Callback function for the 'button_pressed' topic.
    Logs the button state.
    """
    if msg.data:
        rospy.loginfo("Button has been pressed!")
    else:
        rospy.loginfo("Button state is false.")

def led_toggle_publisher():
    """
    Publishes to the 'led' topic every 10 seconds to toggle the LED state.
    """
    rospy.init_node('led_toggle_node', anonymous=True)
    led_pub = rospy.Publisher('led', Bool, queue_size=10)

    button_sub = rospy.Subscriber('button_pressed', Bool, button_callback)

    rate = rospy.Rate(0.1)  # 0.1 Hz = every 10 seconds
    led_state = False

    rospy.loginfo("LED toggle publisher is running.")

    while not rospy.is_shutdown():
        led_state = not led_state  # Toggle LED state
        led_pub.publish(led_state)
        rospy.loginfo(f"Published LED state: {'ON' if led_state else 'OFF'}")
        rate.sleep()

if __name__ == "__main__":
    try:
        led_toggle_publisher()
    except rospy.ROSInterruptException:
        pass

