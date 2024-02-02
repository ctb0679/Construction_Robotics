Instructions to run the code:

1. Download and Install ROS web video server

Install:

cd ~/catkin/src
git clone https://github.com/sfalexrog/async_web_server_cpp.git
cd async_web_server
git checkout noetic-devel

cd ~/catkin/src
git clone https://github.com/RobotWebTools/web_video_server.git

catkin_make

Run:

rosrun web_video_server web_video_server


2. Install rosbridge:

sudo apt-get install ros-<rosdistro>-rosbridge-server

Run:

roslaunch rosbridge_server rosbridge_websocket.launch


3. rosrun pub_movement movements.py

4. To run with pc camera: rosrun pub_movements human_following_laptop.py


To run with the robot camera: rosrun pub_movements robot_detect_midpoint.py
