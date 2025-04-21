#!/usr/bin/env python3
import rospy
from std_msgs.msg import String, Int32

def callback(msg):
    rospy.loginfo("I heard: %d", msg.data)

def listener():
    rospy.init_node('listener1')
    rospy.Subscriber('my_chat_topic1', Int32, callback, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        rospy.logerr("Listener node interrupted.")
