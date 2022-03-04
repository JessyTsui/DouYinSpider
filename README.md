config.py是配置文件

save_data.py是第一段根据Excel的需求URL去抖音接口里抓到真实视频URL，然后存到./data/指定csv下

down_to_path.py是第二段根据data/指定csv来下载视频到本地，暂时简单的单个视频流式下载，

upload2cos.py是第三段根据把本地视频上传到cos上，做了多线程上传处理