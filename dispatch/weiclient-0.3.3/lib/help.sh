客户端启动命令：
  sh ./lib/client.sh -f ./conf/weiclient.conf.template 
其中 
client.sh为客户端核心脚本，置于客户端路径lib目录下；
weiclient.conf.template为客户端配置文件路径，默认置于客户端conf目录下。
weiclient.conf内容示例与注释：
data_path=./lib/client.sh # 数据目录，可为空，为数据传输需求提供
job_name=control_center # 作业名
user_name=enzhao # 用户名
cluster_type=spark # 任务所处集群类型
cluster_version=2.0.2 # 集群版本
src_dir=../weiclient # 客户端目录相对路径，也是控制中心任务隔离后工作目录

