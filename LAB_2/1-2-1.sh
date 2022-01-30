#! /bin/bash
#A directory is need for which we want to change the premissions

#The address to code is stored in $code_address to keep runing it recursively
code_address=$(pwd)

cd $@

for j in $(ls)
do
	chmod a+rwx $j
done

directories=$(ls -d */)
for i in $directories
do
target_dir=$(pwd)
cd $code_address
./1-2-1.sh $target_dir/$i
cd $target_dir
done
