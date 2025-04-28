#!/usr/bin/env python3
import rospy

def main():
    # Инициализация узла
    rospy.init_node('primer')

    # Установка параметров
    rospy.set_param('~ros_priv_param', 'Hi, I am private =)')
    rospy.set_param('ros_loc_param', 'Hi, I am local =)')
    rospy.set_param('/ros_glob_param', 'Hi, I am global =)')

    # Получение параметров
    try:
        global_param = rospy.get_param('/rosdistro')
        rospy.loginfo("Global parameter '/rosdistro': %s", global_param)
    except rospy.ROSException:
        rospy.logwarn("Global parameter '/rosdistro' not found.")

    try:
        local_param = rospy.get_param('ros_loc_param')
        rospy.loginfo("Local parameter 'ros_loc_param': %s", local_param)
    except rospy.ROSException:
        rospy.logwarn("Local parameter 'ros_loc_param' not found.")

    try:
        private_param = rospy.get_param('~ros_priv_param')
        rospy.loginfo("Private parameter '~ros_priv_param': %s", private_param)
    except rospy.ROSException:
        rospy.logwarn("Private parameter '~ros_priv_param' not found.")

    try:
        custom_global_param = rospy.get_param('/ros_glob_param')
        rospy.loginfo("Custom global parameter '/ros_glob_param': %s", custom_global_param)
    except rospy.ROSException:
        rospy.logwarn("Custom global parameter '/ros_glob_param' not found.")

    # (1) Пример обработки исключения через try-except
    try:
        not_exist_param = rospy.get_param('i_do_not_exist')
    except:
        not_exist_param = "Okay, now it's default time =)"
    rospy.loginfo("Value of 'i_do_not_exist' after try-except: %s", not_exist_param)

    # (2) Пример с установкой значения по умолчанию прямо в get_param
    not_exist_param_default = rospy.get_param('i_do_not_exist', 'default_value')
    rospy.loginfo("Value of 'i_do_not_exist' with default: %s", not_exist_param_default)

    # (3) Работа со списком параметров и удалением параметра
    param_name_2_delete = '/ros_glob_param'

    # Получаем список всех параметров
    param_list = rospy.get_param_names()
    rospy.loginfo("Current parameter list: %s", param_list)

    # Проверяем наличие параметра
    if rospy.has_param(param_name_2_delete):
        rospy.loginfo('[ROSWay] Parameter exists')
    else:
        rospy.loginfo('[ROSWay] Parameter does not exist')

    # Удаляем параметр при наличии
    if rospy.has_param(param_name_2_delete):
        rospy.delete_param(param_name_2_delete)
        rospy.loginfo("[ROSWay] Parameter '%s' deleted.", param_name_2_delete)

    # Проверяем снова после удаления
    if rospy.has_param(param_name_2_delete):
        rospy.loginfo('[ROSWay] Parameter exists')
    else:
        rospy.loginfo('[ROSWay] Parameter does not exist')

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
