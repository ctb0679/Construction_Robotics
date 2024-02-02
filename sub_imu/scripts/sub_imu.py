import rospy
from sensor_msgs.msg import Imu

def sub_imu():
	imu_sub = rospy.Subscriber('midog1/imu/data', Imu, callback)
	rospy.init_node('sub_imu', anonymous=True)
	rospy.spin()

def callback(imu_msg):
	print(imu_msg)


if __name__ == '__main__':
	try:
		sub_imu()
	except rospy.ROSInterruptException:
		pass
