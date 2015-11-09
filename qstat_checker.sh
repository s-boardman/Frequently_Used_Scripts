#!/usr/bin/bash

echo -e "Checking for jobs $1 to $2" ;

for i in $(seq $1 $2); 
do
qstat | grep $i;
if [ "$(qstat | grep $i)" = '' ];
	then
	echo -e "Job $i is NOT running"; 
fi
done;
