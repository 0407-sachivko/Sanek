#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("In a galaxy far far away %s", msg.data)

def listener():
    rospy.init_node('listener')
    rospy.Subscriber('my_chat_topic', String, callback, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        rospy.logerr("Listener node terminated.")
