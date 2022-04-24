#!/bin/bash
# Program to find if string is palindrome or not

RED="\e[31m"
GREEN="\e[32m"
NORMAL="\e[0m"
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
	echo -e "${GREEN} $s is a palindrome. ${NORMAL}"
else
	echo -e "${RED} $s is not a palindrome. ${NORMAL}"
fi
