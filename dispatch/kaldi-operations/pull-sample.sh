while getopts "n:p:" arg
#    if [ $arg = "" ]; then
#       show_usage
#       exit 0
#    fi
do
  case ${arg} in
      n) sample_name=${OPTARG};;
      p) sample_path=${OPTARG};;
    esac
done

rsync -vzrt --progress 10.77.29.68::backup/data/$sample_name $sample_path
