import time
import os

stop = ["gz model -m aws_robomaker_racetrack_RaceStartLight_01_00 -d", "gz model -m aws_robomaker_racetrack_RaceStartLight_01_01 -d", "gz model -m aws_robomaker_racetrack_RaceStartLight_01_02 -d", "gz model -m aws_robomaker_racetrack_RaceStartLight_01_03 -d"]

start = ["gz model --spawn-file=/home/deep/catkin_ws/src/autoz_task/aws-robomaker-racetrack-world/models/aws_robomaker_racetrack_RaceStopLight_01/model.sdf --model-name=lightGreen2 -x 4.780034 -y -12.566224 -z 5.328665 -R 0 -P 0.000 -Y 0", "gz model --spawn-file=/home/deep/catkin_ws/src/autoz_task/aws-robomaker-racetrack-world/models/aws_robomaker_racetrack_RaceStopLight_01/model.sdf --model-name=lightGreen2 -x 4.780034 -y -17.566224 -z 5.328665 -R 0 -P 0.000 -Y 0"]

time.sleep(5)
for cmd in stop:
    os.system(cmd)

for cmd in start:
    os.system(cmd)




