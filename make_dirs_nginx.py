

# error_log /home/nginx/8088/log/error.log;
# pid /home/nginx/8088/nginx.pid;


import os 

# port="8088"
port="8004"
os.makedirs(f"/home/nginx/{port}/log", exist_ok=False)
# os.makedirs(f"/home/nginx/{port}/log", exist_ok=False)

# os.makedirs("/home/nginx/8088/log", exist_ok=False)