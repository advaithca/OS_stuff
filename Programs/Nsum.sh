#!/bin/bash
# Program to print sum of first N numbers
echo "Enter a number: "
read N
if [ $N -le 0 ]
then
	echo "Non-positive number detected, terminating..."
else
	i=$N
	sum=0

	while [ $i -gt 0 ]
	do
		sum=$[$sum+$i]
		i=$[$i-1]
	done
	echo "Sum of first $N numbers is $sum"
fi
