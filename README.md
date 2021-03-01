# My environment
 Ubuntu18.04   
 Opencv3.4 - [Refer](https://j-remind.tistory.com/57)

# catkin_ws_ov
## catkin_ws_ov : How to run program
    roslaunch ov_msckf your_launch_file (ex)ros_uzhfpv.launch)

Just you need only one Terminal   
You must run the ```source devel/setup.bash``` before starting the program on a new terminal
## How to use open_vins
### catkin_ws_ov : Getting Started
 [Getting Started](https://docs.openvins.com/getting-started.html)
### catkin_ws_ov : How do i change the .bag file?
 Edit your bag_name part of launch file   
```/home/usr_name/datasets/something.bag```

## catkin_ws_ov : Error
- not yet

***

# catkin_stereo
## How to use VINS-Stereo
### catkin_stereo : Getting Started
 ```catkin/src```에 [VINS-Mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono)와 [VINS-Stereo](https://github.com/rising-turtle/VINS-Stereo)를 ```git clone```해줍니다.   
 그 다음에, VINS-Stereo와 VINS-Mono에서 서로 겹치는 폴더를 VINS-Mono에서 지워줍니다.   
 다 지워준 뒤, 알맞은 자리에 옮겨줍니다.   
 그 다음에, ```catkin_make```하세요.

### catkin_stereo : How to run program
    roslaunch vins_estimator_stereo your_launch_file (fpv.launch)
    rosbag play ~/your_datasets_space/somefile.bag

Just you need two Terminals   
You must run the ```source devel/setup.bash``` before starting the program on a new terminal

### catkin_stereo : How can i get the dataset_output
Go to ```src/VINS-Mono/config/fpv```   
And open fpv_forward.yaml   
And edit output_path: "The_path_you_want"

### catkin_stereo : Error
- RLException: while processing vins_rviz.launch:
Invalid roslaunch XML syntax: \[Errno 2] No such file or directory: u'vins_rviz.launch'
The traceback for the exception was written to the log file   
-> 런치파일 맨밑 주소 홈부터 : ```home/.../.../vins_rviz.launch```



***
***
***

# How to change 'avoidance_sitl_mavros.launch' value
Websites for resolution - [WebSite](https://github.com/PX4/PX4-Avoidance/issues/485)

	~/catkin_ws/src/avoidance/avoidance/launch/
에서 avoidance_sitl_mavros.launch파일 gedit -> gui부분 -> ture

## RLException: [local_planner_stereo.launch] is neither a launch file in package [local_planner] nor is [local_planner] a launch file name...

Websites for resolution - [WebSite](https://answers.ros.org/question/143496/roslaunch-is-neither-a-launch-file-in-package-nor-is-a-launch-file-name/)

## command 'make install' error : 
CMake Error at cmake_install.cmake:41 (file):
file cannot create directory: /usr/local/include/ceres.  Maybe need
  administrative privileges.

Makefile:128: recipe for target 'install' failed
make: *** [install] Error 1


try ```sudo make install```

# How to write 'README.md'

recommand website - [blog](https://gist.github.com/ihoneymon/652be052a0727ad59601)


