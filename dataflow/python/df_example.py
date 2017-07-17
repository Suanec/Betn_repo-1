import dataflow as df

params = ""

# 所有函数的一个参数，表示依赖关系
# 将params初始化为text所需参数列表
input1 = df.input.spark.text(None, params)

# 将params初始化为数据采样模块所需参数列表
sampler = df.process.spark.dataSampler(input1, params)

# 将params初始化为数据提取模块所需参数列表
extractor = df.process.spark.dataExtract(sampler, params)

# 将params初始化为数据清洗模块所需参数列表
cleaner = df.process.spark.dataClean(extractor, params)

# 将params初始化为特征映射模块所需参数列表
f_map = df.process.spark.featureMapping(cleaner, params)

# 将params初始化为libsvm数据格式输出模块所需参数列表
output1 = df.output.spark.libsvm(f_map, params)

# 第一个参数None表示node1不依赖其他node
# 第二个参数表示node1需要从output1回溯执行该node内部的DAG逻辑
node1 = df.node.spark(None, output1)

# 绑定node执行相关信息，如Spark的spark-submit执行路径
# 以及spark-submit所需的资源参数，都通过bind函数绑定
node1.bind(params)

# =======================================================
# 到这里为止完成DAG的定义阶段，后面通过Session来实际执行这里定义的DAG

# 定义类似Tensorflow的Session环境，调用run函数执行上述DAG定义。
with df.Session() as session:
    session.run(node1)
    print "Running %s" % node1