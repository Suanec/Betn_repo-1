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
cmd="sh client.sh ../weiclient enzhao sparkWeiflow 2.0.2"
echo $cmd
$cmd
#rsync -vzrtopg --progress $clientDir 10.77.29.68::backup
