while getopts "n:p:" arg
#    if [ $arg = "" ]; then
#       show_usage
#       exit 0
#    fi
do
  case ${arg} in
      n) model_name=${OPTARG};;
      p) model_path=${OPTARG};;
    esac
done

cmd="rsync -vzrtopg --progress $model_path 10.77.29.68::backup/data/$model_name"
echo $cmd
$cmd

