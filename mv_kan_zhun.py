
# "D:\download\KanZhunCompanyLink_杭州国电电力科技发展有限公司.json"
import os 

from_dir=rf"D:\download"
# D:\kanZhunDoc

import shutil
to_dir='D:\\kanZhunDoc'
for file_name in os.listdir(from_dir):
    if file_name.startswith('KanZhunCompanyLink_'):
        # print(file_name)
        abs_path=os.path.join(from_dir,file_name)
        abs_to_path=os.path.join(to_dir,file_name)
        # print("abs_to_path")
        # print(abs_to_path)
        print(f"move {abs_path} to {abs_to_path}")
        shutil.move(abs_path,abs_to_path)
        
    # abs_path=os.path.join(from_dir,file_name)