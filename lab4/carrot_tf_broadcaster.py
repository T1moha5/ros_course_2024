#!/usr/bin/env python
#!/usr/bin/env python
import rospy
import tf
import math
from turtlesim.msg import Pose

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    current_time = rospy.Time.now()

    # Радиус вращения и угловая скорость
    radius = 0.2 # Расстояние от черепахи до морковки
    frequency = 1.0 # Частота вращения в Гц
    angular_speed = 2 * math.pi * frequency # Угловая скорость

    # Вычисление текущего угла для вращения
    elapsed_time = current_time.to_sec()
    angle = angular_speed * elapsed_time

    # Координаты морковки относительно черепахи
    x_offset = radius * math.cos(angle)
    y_offset = radius * math.sin(angle)

    # Публикация трансформации морковки относительно черепахи
    br.sendTransform(
    (x_offset, y_offset, 0), # Смещение морковки в локальных координатах черепахи
    tf.transformations.quaternion_from_euler(0, 0, 0), # Без вращения
    current_time,
    turtlename + "_carrot", # Имя фрейма морковки
    turtlename # Фрейм черепахи (родительский фрейм)
    )

if __name__ == '__main__':
    rospy.init_node('carrot_tf_broadcaster')

# Получение имени черепахи из параметра
turtle_name = rospy.get_param('~turtle_tf_name', 'turtle1')

# Подписка на топик позиций черепахи
rospy.Subscriber(f'/{turtle_name}/pose', Pose, handle_turtle_pose, turtle_name)

# Запуск цикла обработки сообщений
rospy.spin()