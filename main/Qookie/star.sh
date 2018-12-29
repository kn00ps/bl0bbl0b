#!/bin/bash
while :
do
	echo "Press [CTRL+C] to stop.."
	sleep 1
	rm -rf /tmp/*
	python3 IN_.py
	sleep 42230
done

