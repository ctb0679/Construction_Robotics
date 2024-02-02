#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    try:
        # Convert compressed image to OpenCV format
        bridge = CvBridge()
        image = bridge.compressed_imgmsg_to_cv2(msg, desired_encoding="bgr8")

        # Display the image
        cv2.imshow('Robot Camera', image)
        cv2.waitKey(1)

    except Exception as e:
        rospy.logerr(e)

def main():
    # Initialize the ROS node
    rospy.init_node('robot_camera_viewer', anonymous=True)

    # Subscribe to the compressed image topic
    rospy.Subscriber('/midog3/camera/image_raw/compressed', CompressedImage, image_callback)

    # Keep the script running
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
