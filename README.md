# ROS2-Filecoin

Simple ROS2 package to publish Robonomics datalog data to Filecoin.

## Requirements

1. [ROS2 Foxy](https://docs.ros.org/en/foxy/index.html)
2. python = ">=3.8, <4.0"

## Installation

```
pip3 install robonomics-interface
```
Source ROS2 environment:
```
source /opt/ros/foxy/setup.bash
```
> The exact command depends on where you installed ROS 2. If you’re having problems, ensure the file path leads to your installation.

Create ROS2 workspace & install ros dependencies:

```
mkdir -p dev_ws/src
cd ~/dev_ws/src
git clone https://github.com/tubleronchik/ros2-filecoin.git
rosdep install -i --from-path src --rosdistro foxy -y
```
Build the workspace from the root of the workspace (`dev_ws`) and source the overlay:
```
colcon build --packages-select ros2_filecoin
. install/local_setup.bash
```

## Run

```
ros2 run ros2_filecoin datalog_listener
```



