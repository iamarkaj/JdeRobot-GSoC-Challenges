# ROS2 Challenge

# Part 1: Introduction to ROS2


## a. 'Hello! ROS2 is fun'


### Creating workspace
```
mkdir -p ros2_ws/src && cd ros2_ws
source /opt/ros/foxy/setup.bash
colcon build
source install/local_setup.bash && source install/setup.bash
```

### Downloading the packages
Download ROS2 Challenge folder inside ros2_ws/src

### Building packages using colcon
```
colcon build --symlink-install --packages-select <package_name>
. install/setup.bash
```

### Running talker
```
ros2 run pubsub_py talker
```

### Running listener
```
ros2 run pubsub_py listener
```

![pubsub_py](assets/pubsub_py.png)


## b. Launch your robot


### Visualization of the laser scan data using rviz2

![laser_scan](assets/laser_scan.png)

[Click here](https://www.youtube.com/watch?v=DjI-VWtPRd0) to watch the video.

 
 
# Part 2: ROS2 Navigation2


```
echo 'source ~/ros2_ws/install/setup.bash' >> ~/.bashrc
echo 'export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/ros2_ws/src/turtlebot3/turtlebot3_simulations/turtlebot3_gazebo/models' >> ~/.bashrc
export TURTLEBOT3_MODEL=burger
```

## Launching gazebo
```
ros2 launch turtlebot3_gazebo mylaunch.launch.py
```

## Making the map

![map](assets/map.png)

[Click here](https://www.youtube.com/watch?v=FBW4gHa-DPU) to watch the video.

```
ros2 launch turtlebot3_cartographer cartographer.launch.py
```

## Move the robot using keyboard keys
```
ros2 run turtlebot3_teleop teleop_keyboard
```

## Saving the map
```
ros2 run nav2_map_server map_saver_cli --ros-args -p save_map_timeout:=10000
```

## Finally

![final](assets/final.png)

[Click here](https://youtu.be/JV2rbXceeOA) to watch the video.

```
ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=$HOME/<ros2_ws_path>/src/<map_name>.yaml open_rviz:=true use_sim_time:=true
``` 



