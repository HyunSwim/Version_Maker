#!/bin/sh
MY_PWD=$PWD
cd $1
if test directory.txt; then
	rm -r directory.txt
fi
touch $1/directory.txt
for i in *
do
	if test -d $i; then
		cd $i
		echo $PWD >> ../directory.txt
		cd ..
	fi
done

cd $MY_PWD

python3 version_maker.py --pwd $1
rm -r directory.txt