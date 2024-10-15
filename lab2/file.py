rospy.init_node('talker')
pub = rospy.Publisher('my_chat_topic', String, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(1) # 1 Hz
def start_talker():
    # Создаем объект сообщения
    msg = String()
    # Бесконечный цикл, пока ROS система работает
    while not rospy.is_shutdown():
        # Сформируем сообщение, которое включает в себя время
        hello_str = "hi =) %s" % rospy.get_time()
        # Вывод в терминал информации (содержание сообщения)
        rospy.loginfo(hello_str)
        # Заполнение сообщения и публикация сообщения в топик
        msg.data = hello_str
        pub.publish(msg)
        # Сон в соответствии с выдерживаемой частотой
        rate.sleep()
try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
