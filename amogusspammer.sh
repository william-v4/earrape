#!/bin/bash

repeat=0

while true
do
	if [ $repeat -eq 4 ]
	then
		aplay amogussfx.wav
	fi
	aplay amogus.wav &
	repeat=$((repeat+1))
	echo $repeat
	sleep 0.5
done
