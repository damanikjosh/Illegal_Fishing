#!/bin/bash
if [ "$#" -lt 1 ]; then
        echo usage: ./run.sh world_name
        exit 1
fi
export GAZEBO_MODEL_PATH=$(pwd)/models/
gazebo worlds/$1.world