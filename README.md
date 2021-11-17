# F1TENTH_SVL-Simulator
This repository contains all information for working with F1TENTH and the SVL Simulator


# Maps
This folder contains the asset files for the 3D Unity Maps that can be used in the SVL Simulator together with the F1TENTH vehicle. The corresponding 2D racetrack information, centerline of the racetracks and optimal racelines can be found in the [F1TENTH Racetrack Repository](https://github.com/f1tenth/f1tenth_racetracks/)

Currently the following maps are available:
* **Red Bull Racetrack - Austria**: The Red Bull Ring is located in Spielberg, Styria, Austria and is hosting Formula 1, Formula 2, Moto Gp and DTM competitions.


# Sensor Configurations
This folder contains the sensor configuration files for the F1TENTH car in the SVL Simulator.
Those sensor configurations mainly differ in the types of sensors that are incoperated in those.
All sensor publish corresponding ROS2 messages and can therefore displayed over the LGSVL-ROS2 bridge.
Currently the following configurations are available:
* **F1TENTH**: This an original replica of the F1TENTH's vehicle real sensor configuration hardware.
* **F1TENTH Big Vehicle**: This the F1TENTH vehicle with equipped with 3D Lidar, GPS

# Python Scripts
This folder contains Python scripts that connects to the SVL Python API. This basic scripts give an idea on how to run basic functionalities e.g. spawn vehicles and change the daytime. In addition we integrated basic autonomous racing path planners and controllers to run the car fast around the racetrack in the SVL simulator.
* **01_Spawn_and_drive.py**: This script gives a basic explanation on how to connect to the SVL Simulator, load a specific map and then spawn the F1TENTH vehicle.
* **02_Pure_Pursuit.py**: This script is running the Pure Pursuit control algorithm to follow an optimal raceline around the racetrack.
* **03_Multi_Ego.py**: This script is showing on how to spawn two F1TENTH vehicles as ego vehicles and sent control commands to the simulator
* **04_Camera_Access.py**: This script is accessing the sensors on the F1TENTH vehicle and is saving the image afterwards.

# ROS2 Packages
This folder contains ROS2 packages that connects to the SVL ROS2 bridge. This basic RO2 packages include basic autonomous functionalities like object detection, localization, path planning and control to run the car fast around the racetrack in the SVL simulator.


# References
For this repository we are using the theoretical foundations, images and code from the following papers. If you find our work useful in your research, please consider citing:

* J. Betz, A. Wischnewski, A. Heilmeier, F. Nobis, T. Stahl, L. Hermansdorfer, B. Lohmann, M. Lienkamp "What we can learn from autonomous racing",2018, Springer [(PDF)](https://www.researchgate.net/publication/327892743_What_can_we_learn_from_autonomous_level-5_motorsport_chassistech_plus)

* T. Stahl, A. Wischnewski, J. Betz, and M. Lienkamp,
“Multilayer Graph-Based Trajectory Planning for Race Vehicles in Dynamic Scenarios,”
in 2019 IEEE Intelligent Transportation Systems Conference (ITSC), Oct. 2019, pp. 3149–3154. [(PDF)](https://arxiv.org/pdf/2005.08664>`)

* A. Heilmeier, A. Wischnewski, L. Hermansdorfer, J. Betz, M. Lienkamp, B. Lohmann\
"Minimum Curvature Trajectory Planning and Control for an Autonomous Racecar" Vehicle System Dynamics, vol. 58, no. 10, pp. 1497–1527, Jun. 2019,
[(PDF)](https://www.tandfonline.com/doi/abs/10.1080/00423114.2019.1631455?journalCode=nvsd20)
