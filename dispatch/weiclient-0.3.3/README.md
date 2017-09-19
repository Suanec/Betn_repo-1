.
./conf								weiclient配置目录。
./conf/weiclient.conf				weiclient配置文件。weiclient.sh可由参数指定也可由配置文件指定，指定配置文件应与之相对应。
./conf/weiflow-config.xml			weiflow任务中依赖的xml配置文件。weiflow.sh中指定配置文件应与之相对应。
./lib								weiclient依赖文件，以及控制中心启动依赖所在目录。
./lib/client.sh						weiclient工作脚本,weiclient核心脚本。
./README.md							README说明文件。
./user_custom_run_job.sh			用户自定义工作入口脚本，控制中心对作业进行调度后，由weiflow通过启动该脚本进行任务提交相关工作。
./weiclient.sh						weiclient启动入口脚本。客户端提交至控制中心。
./weiflow.sh						weiflow启动脚本。
