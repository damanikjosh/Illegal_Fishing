#!/bin/bash
PWD=$(pwd)
echo $PWD
export GAZEBO_MODEL_PATH=$PWD/models/
gazebo smooth.world