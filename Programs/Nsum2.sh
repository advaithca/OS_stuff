#!/bin/bash
# Program to print sum of N numbers

read -p "Enter limit : " N
ArrayNums=(0)
i=0
echo "Enter $N numbers :"
while [ $i -lt $N ]
do
	read -p "Num $i. " x
	ArrayNums+=( $x )
	i=$[$i+1]
done

sum=0

for i in ${ArrayNames[@]}; do
	sum=$[$sum+$i]
done
echo "Sum of given $N numbers is $sum"
