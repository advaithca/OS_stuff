#!/bin/bash
# Prints sum of N numbers

read -p "Enter limit: " N 

if [ $N -le 0 ]
then
	echo "Non-positive input detected, terminating...."
else
	sum=0
	i=1
	echo "Enter $N numbers"
	while [ $i -le $N ]
	do
		read -p "Num $i. " k
		sum=$[$sum+$k]
		i=$[$i+1]
	done
	echo "Sum of the entered $N numbers is $sum"
fi
