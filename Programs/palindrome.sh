#!/bin/bash
# Program to find if string is palindrome or not

read -p "Enter a string :: " s
len=${#s}
y=$[$len-1]
reversed=""
for ((i=0;i<$len;i++)) do
	reversed="$reversed${s:$y:1}"
	y=$[$y-1]
done
if [ $s = $reversed ]
then
	echo "$s is a palindrome."
else
	echo "$s is not a palindrome."
fi
