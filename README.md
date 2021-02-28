# catkin_ws_ov
### catkin_ws_ov : how to run program
    1. roslaunch ov_msckf ros_uzhfpv.launch

### catkin_ws_ov : error
- not yet

# catkin_stereo
### catkin_stereo : how to run program
    1. roslaunch vins_estimator_stereo fpv.launch
    2. rosbag play ~/workspace/dataset/indoor_forward_5_snapdragon_with_gt.bag


### catkin_stereo : error
- RLException: while processing vins_rviz.launch:
Invalid roslaunch XML syntax: \[Errno 2] No such file or directory: u'vins_rviz.launch'
The traceback for the exception was written to the log file
-> 런치파일 맨밑 주소 홈부터/.../vins_rviz.launch

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


try 'sudo make install'
	



## bigbigbig
### bigbig

# How to write 'README.md'

recommand website - [blog](https://gist.github.com/ihoneymon/652be052a0727ad59601)


