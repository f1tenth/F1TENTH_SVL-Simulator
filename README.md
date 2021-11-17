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
* **F1TENTH**:

# ROS2 Packages
This folder contains ROS2 packages that connects to the SVL ROS2 bridge. This basic RO2 packages include basic autonomous functionalities like object detection, localization, path planning and control to run the car fast around the racetrack in the SVL simulator.
