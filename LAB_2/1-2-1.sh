#! /bin/bash
code_address=$(pwd)
cd $@
for j in $(ls)
do
	chmod +sx $j
done
directories=$(ls -d */)
for i in $directories
do
	$code_address/test.sh $(pwd)/$i
done
