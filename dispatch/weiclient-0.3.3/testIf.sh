srvIP=10.77.29.68
if [[ $srvIP = '10.77.29.68' ]] ; then
echo true
else 
echo false
fi



IFS=/ read -r -a PARTS <<< $CUR_DIR
echo $PWD
echo $PART

#echo $CUR_DIR | cut -d "/" -f 3-
