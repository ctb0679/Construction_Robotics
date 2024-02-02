# Instructions to run the code:

## 1. Download and Install ROS web video server

**Install:**
```bash
cd ~/catkin/src
git clone https://github.com/sfalexrog/async_web_server_cpp.git
cd async_web_server
git checkout noetic-devel
```
```bash
cd ~/catkin/src
git clone https://github.com/RobotWebTools/web_video_server.git
```
```bash
catkin_make
```
**Run:**
```bash
rosrun web_video_server web_video_server
```

**2. Install rosbridge:**
```bash
sudo apt-get install ros-<rosdistro>-rosbridge-server
```
**Run:**
```bash
roslaunch rosbridge_server rosbridge_websocket.launch
```

**3.**
```bash
rosrun pub_movement movements.py
```
**4. To run with pc camera:** 
```bash
rosrun pub_movements human_following_laptop.py
```

**5. To run with the robot camera:**
```bash
rosrun pub_movements robot_detect_midpoint.py
```
