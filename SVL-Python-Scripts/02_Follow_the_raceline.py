#!/usr/bin/env python3
#
# Copyright (c) 2019-2021 LG Electronics, Inc.
#
# This software contains code licensed as described in LICENSE.
#

from environs import Env
import lgsvl
import time
from datetime import datetime

# Create the environment variable
env = Env()

# Create the sim instance and connect to the SVL Simulator
sim = lgsvl.Simulator(env.str("LGSVL__SIMULATOR_HOST", lgsvl.wise.SimulatorSettings.simulator_host), env.int("LGSVL__SIMULATOR_PORT", lgsvl.wise.SimulatorSettings.simulator_port))

# Load the Racetrack and create the scene/environment
sim.load(scene = "781b04c8-43b4-431e-af55-1ae2b2efc873", seed = 650387)         # Create the Red Bull Racetrack
sim.reset()
spawns = sim.get_spawn()

# Load the vehicle and spawn it on the track
state = lgsvl.AgentState()
state.transform = spawns[0]
ego = sim.add_agent(name = "3bb4c2eb-82d3-4ee3-8ebb-2bdbcf6e88ea", agent_type = lgsvl.AgentType.EGO, state = None)

# Set a new daytime for the simulator, Time of day can be set from 0 ... 24
print("Current time:", sim.time_of_day)
sim.set_time_of_day(19.8)
print(sim.time_of_day)



# Create Steps for running the simulation step by step
step_time = 0.1
duration = 30
c = lgsvl.VehicleControl()

step_rate = int(1.0 / step_time)
steps = duration * step_rate
print("Stepping forward for {} steps of {}s per step" .format(steps, step_time))

# The simulator can be run for a set amount of time.
# time_limit is optional and if omitted or set to 0, then the simulator will run indefinitely
t0 = time.time()

# Initial Ego Position - needs to be special because of our coordinate system
s = ego.state
s.position.x = -0.044086    # equals original x in our raceline data
s.position.z = 0.8491629    # equals original -y in our raceline data
s.rotation.y = 270-195      # 270 =- original value from raceline heading, if statement for pi and -pi
ego.state = s

for i in range(steps):

    sim.run(time_limit=step_time)

    state = ego.state
    pos = state.position
    rot= state.rotation
    speed = state.speed

    # Drive in a circle

    c.throttle = 1.0
    c.steering = 0.001
    # a True in apply_control means the control will be continuously applied ("sticky"). False means the control will be applied for 1 frame
    ego.apply_control(c, True)


    print("Speed = {:4.1f}; Position: x={:5.3f},y={:5.3f},z={:5.3f}".format(speed, pos.x, pos.y, pos.z))
    print("Speed = {:4.1f}; Rotation: x={:5.3f},y={:5.3f},z={:5.3f}".format(speed, rot.x, rot.y, rot.z))
t3 = time.time()

# Final statistics
print("Total real time elapsed = {:5.3f}".format(t3 - t0))
print("Simulation time = {:5.1f}".format(sim.current_time))
print("Simulation frames =", sim.current_frame)