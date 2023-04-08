# -*- coding: utf-8 -*-
import os

from myfile import make_dir_if_not_exists
from top.starp.logger import Logger
# port=8888
# port="8889"
# port="8890"
# 阿里云打开

def remove(lst, what=""):
    ret = []
    for val in lst:
        if val == what:
            continue
        ret.append(val)
    return ret


def get_father_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))
################ config #####################
# 配置 html 静态文件的位置
# root_path="/home/mqp/wx-sorting_build"
# root_path="/home/mqp/gitCacheVue/dist/dist"
# root_path="/home/mqp/imFront/dist"

"""
zip_file_path="/home/app/exam-vue/dist.zip"
father_dir= get_father_dir(zip_file_path)
root_path=f'{father_dir}/dist'
"""
# /home/mqp/animals-web

# root_path=f'{father_dir}/dist'
# root_path=f'/home/mqp/animals-web'
# root_path=f'/home/app/exam/student-exam-nginx'
root_path=f'/home/bishe/exam-vue-admin'
# /home/app/exam/student-exam-nginx
# unzip   -o  dist.zip  -d 	 dist/
#/home/mqp/wx-sorting_build_web_desktop
# do_unzip=False
do_unzip=True
# do_unzip=True
# root_path="/home/mqp/wx-sorting_build_web_desktop"

#/home/mqp/wx-sorting_build_web_desktop

class Config():
    def __init__(self):
        # self.jar_name = "demo-0.0.1-SNAPSHOT.jar"
        # # self.jar_name = "sys-writer-web-0.0.1-SNAPSHOT.jar"
        # self.log_file_name_templete = "log_{}.log"
        # # self.port="80"
        # # self.port = "8088"
        # self.port = "8080"
        # # self.sudo = "sudo "
        # self.sudo=" "
        # # sudo 后面最好有个空格

        # self.jar_name = "/home/mqp/whatRubbish-0.0.1-SNAPSHOT.jar"
        # self.log_file_name_templete = "log_{}.log"
        # self.port = "8889"

        # self.jar_name = "/home/mqp/iot/mqp-iot-db-0.0.1-SNAPSHOT.jar"
        self.log_file_name_templete = "log_{}.log"
        # self.port = "8899"
        # self.port="8890"
        # self.jar_name = "pz-blog-1.0.jar"
        # self.log_file_name_templete = "log_{}.log"
        # self.port = "8085"
        self.sudo=" "
        self.kill_app_name="nginx"
        # self.port="8086"
        # im 前端
        # self.port="8087"
        # self.port="8088"
        # self.port="8089"
        self.port="8090"

# lsof -i:8088
################ config #####################

import time_util

now_time_str= time_util.get_now_time_str()

def move_dist():
    os.system(f"mv   dist    dist_{now_time_str}/")
    os.system(f"unzip  -o   /home/pi/writer/dist_admin_this.zip   -d  dist/")
    

def kill_app_line(line, config):
    print("kill_app_line")
    # sps=line.split(" ")
    # pid=sps[1]
    sps = line.split(" ")
    # sps.remove("")
    sps = remove(sps, "")
    # print(sps)
    pid = sps[1]
    # os.system('kill '+pid)
    kill_pid = config.sudo + ' kill ' + pid
    print("kill_pid: ", kill_pid)
    out = os.popen(kill_pid)

def kill_app(config):
    # port = "80"
    port = config.port

    # command = 'ping www.baidu.com' #可以直接在命令行中执行的命令
    r = os.popen(config.sudo + ' lsof -i:' + port)
    # r = os.popen(command) #执行该命令
    info = r.readlines()  # 读取命令行的输出到一个list
    have_java = False
    for line in info:  # 按行遍历
        line = line.strip('\r\n')
        # print(line)
        # if line.startswith("java"):
        if line.startswith(config.kill_app_name):
            kill_app_line(line, config)
            return False
    # java 杀完了
    return True

import time 

logger = Logger(f'make_nginx_conf.py_{now_time_str}.log', level='debug')

# 先把这个端口的nginx 杀掉
config = Config()
# kill_app(config)
time.sleep(1)
# python time.sleep(1)
port=config.port

with open("nginx_template.conf","r",encoding="utf-8") as f:
    nginx_template= f.read()

nginx_template:str

out_str=nginx_template.replace("$port$", port)
out_str=out_str.replace("$root_path$", root_path)


# if do_unzip:
# # unzip   -o  dist.zip  -d 	 dist/
#     os.system(f"unzip   -o  {zip_file_path}  -d 	{father_dir}/dist/")

nginx_root_dir=f"/home/nginx/{port}"
# makrdir 
make_dir_if_not_exists(nginx_root_dir)
# out_path=f"/home/nginx/nginx_{port}.conf"
out_path=f"{nginx_root_dir}/nginx_{port}.conf"
# 这里要写入 但是还没有创建目录
# out_path=f"nginx_{port}.conf"
with open(out_path,"w",encoding="utf-8") as f:
    # nginx_template= f.read()
    f.write(out_str)

print("config write here",out_path)
print(f"nginx_root_dir {nginx_root_dir}")
print(f"port {port}")

logger.logger.info(f"config write here {out_path}")
logger.logger.info(f"nginx_root_dir {nginx_root_dir}")
logger.logger.info(f"port {port}")
# 加入log 
logger.logger.info(f"start at starplatinumora.top:{port}")

# os.system(f"mkdir {nginx_root_dir}")
# make_dir_if_not_exists(nginx_root_dir)
os.system(f"cp /usr/sbin/nginx  {nginx_root_dir}/nginx")

# os.system(f"mkdir /home/nginx/{port}")
# os.system(f"mkdir /home/nginx/{port}/log")
os.system(f"mkdir {nginx_root_dir}/log")
os.system(f"{nginx_root_dir}/nginx -c {nginx_root_dir}/nginx_{port}.conf")
print("查看nginx 有没有启动")
os.system(f"lsof -i :{port}")
# os.system(f"/home/nginx/{port}/nginx -c /home/nginx/{port}/nginx_{port}.conf")
# if father_dir:
#     print ("father_dir",father_dir)
print("root_path",root_path)

os.system(f"firewall-cmd --zone=public --add-port={port}/tcp   --permanent")
time.sleep(1)
os.system(f"firewall-cmd --reload")

# firewall-cmd --reload

"""
[root@iZuf61itscfjc6o9pu5l8hZ my_util_py_pub]# python3 make_nginx_conf.py 
创建目录  /home/nginx/8088
config write here /home/nginx/8088/nginx_8088.conf
nginx_root_dir /home/nginx/8088
port 8088
2022-12-04 13:49:50,337 - make_nginx_conf.py[line:155] - INFO: config write here /home/nginx/8088/nginx_8088.conf
2022-12-04 13:49:50,337 - make_nginx_conf.py[line:156] - INFO: nginx_root_dir /home/nginx/8088
2022-12-04 13:49:50,337 - make_nginx_conf.py[line:157] - INFO: port 8088
2022-12-04 13:49:50,337 - make_nginx_conf.py[line:159] - INFO: start at starplatinumora.top:8088
查看nginx 有没有启动
COMMAND   PID USER   FD   TYPE    DEVICE SIZE/OFF NODE NAME
nginx   25341 root    6u  IPv4 579110971      0t0  TCP *:radan-http (LISTEN)
nginx   25341 root    7u  IPv6 579110972      0t0  TCP *:radan-http (LISTEN)
nginx   25342 root    6u  IPv4 579110971      0t0  TCP *:radan-http (LISTEN)
nginx   25342 root    7u  IPv6 579110972      0t0  TCP *:radan-http (LISTEN)
nginx   25343 root    6u  IPv4 579110971      0t0  TCP *:radan-http (LISTEN)
nginx   25343 root    7u  IPv6 579110972      0t0  TCP *:radan-http (LISTEN)
root_path /home/mqp/animals-web
"""