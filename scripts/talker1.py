#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32, String

def even_publisher():
    rospy.init_node('talker1', anonymous=True)

    pub_numbers = rospy.Publisher('my_chat_topic1', Int32, queue_size=10)
    pub_a = rospy.Publisher('overflow', String, queue_size=10)
    rate = rospy.Rate(10)  # Частота публикации 10 Гц

    number = 0
    while not rospy.is_shutdown():
        rospy.loginfo(f"Chislo: {number}")
        pub_numbers.publish(number)
        number += 2

        if number > 100:
            rospy.logwarn("Достигнуто 100! Сброс счётчика.")
            pub_a.publish("Счётчик достиг 100, сброс")
            number = 0

        rate.sleep()

if __name__ == '__main__':
    try:
        even_publisher()
    except (rospy.ROSInterruptException, KeyboardInterrupt):
        rospy.logerr("Node interrupted.") 
