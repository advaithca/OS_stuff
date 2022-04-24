#!/bin/bash
# Program to print fibonacci series

read -p "Enter number of terms of Fibonacci series to be printed : " N 

if [ $N -le 0 ]
then
	echo "Non-positive limit detected, terminating...."
else
	i=$N
	first=0
	second=1
	temp=0
	
	echo -n "$first "
	
	while [ $i -gt 1 ]
	do
		echo -n "$second "
		temp=$second
		second=$[$first+$second]
		first=$temp
		i=$[$i-1]
	done
	echo ""
fi
