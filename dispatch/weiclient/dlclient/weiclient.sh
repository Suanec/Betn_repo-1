#!/bin/bash

#weiflow_zip=weiflow.tar.gz
#if [ -e $weiflow_zip ];
#echo "[Warn]Compact zip file already exists!"
#then rm $weiflow_zip;
#echo "[Warn]Compact zip file deleted!"
#fi
#
#echo "Compacting required files..."
#echo ""
#tar -zcvf $weiflow_zip *
#echo ""
#echo "Done compacting required files."
#echo "Result file is: $weiflow_zip , please check it."
#clientDir=$pwd
##rsync -vzrtopg --progress weiflow.tar.gz 10.77.29.68::backup

if [ ! -d $src_dir ];then
	echo "src_dir: just dir allowed!"
	exit 1
fi
cmd="sh client.sh ../dlclient lihan3 tensorflow 1.0.0 tensorflow"
echo $cmd
$cmd
#rsync -vzrtopg --progress $clientDir 10.77.29.68::backup
