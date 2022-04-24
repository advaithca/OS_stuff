#!/bin/bash
# Program to calculate factorial

read -p "Enter number whose factorial is to be calculated :: " f
N=$f
fact=1

if [ $f -eq 0 ]
then
	echo "Factorial of 0 is 1"
else
	if [ $f -lt 0 ]
	then
		echo "Factorial of negative numbers is too complicated."
	else
		while [ $N -ge 1 ]
		do
			fact=$[$fact*$N]
			N=$[$N-1]
		done
		echo "Factorial of $f is $fact."
	fi
fi
