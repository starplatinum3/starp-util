from zipfile import ZipFile
import os
import list_util


def get_all_file_paths(directory):
    # 初始化文件路径列表
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            #连接字符串形成完整的路径
            #  "school_24" in filename:
            if filename.endswith(".json") and filename.startswith("school_24"):
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
            # filepath = os.path.join(root, filename)
            # file_paths.append(filepath)

    # 返回所有文件路径
    return file_paths

def main():
    print('start  download zip ')
    # list_util. 
    # 要压缩的文件夹名
    # directory = '齐普夫定律'
    directory = rf'D:\download'
    file_paths = get_all_file_paths(directory)
    # 打印所有要压缩的文件列表
    # for file_name in file_paths:
    #     print(file_name)

    # 生成压缩文件
    # zip_file_name=rf"d:/jobSch24.zip"
    idx=0
    tmp_file_paths=[]
    part=0
    print("len(file_paths)")
    print(len(file_paths))
    # job_24_zips2
    for file_path in file_paths:
        idx+=1
        tmp_file_paths.append(file_path)
        if idx%2000==0:
            # D:\job_24_zips
            # zip_file_name=rf"D:\jobZips\jobSch24_part_{part}.zip"
            # zip_file_name=rf"D:\job_24_zips\jobSch24_part_{part}.zip"
            zip_file_name=rf"D:\job_24_zips2\jobSch24_part_{part}.zip"
            part+=1
            print(f"zip  {zip_file_name} ")
            with ZipFile(zip_file_name, 'w') as zip:
                #遍历写入文件
                for file in tmp_file_paths:
                    zip.write(file)
            tmp_file_paths=[]
            print(f"zip  {zip_file_name}  end ")

    # 'my_python_files.zip'
    # with ZipFile(zip_file_name, 'w') as zip:
    #     #遍历写入文件
    #     for file in file_paths:
    #         zip.write(file)

    print('successfully!')


def zip_dir_files():
    """
    [Running] D:/software/anaconda/envs/visual/python -u "d:\proj\pythonProj\my_util_py_pub\zip_file.py"
successfully!

[Done] exited with code=0 in 1212.196 seconds
"""
    # list_util. 
    # 要压缩的文件夹名
    # directory = '齐普夫定律'
    directory = rf'D:\download'
    file_paths = get_all_file_paths(directory)
    # 打印所有要压缩的文件列表
    # for file_name in file_paths:
    #     print(file_name)

    # 生成压缩文件
    # zip_file_name=rf"d:/jobSch24.zip"
    idx=0
    tmp_file_paths=[]
    part=0
    # D:\job_zip
    zip_file_name=rf"D:\job_zip\jobSch24.zip"
    with ZipFile(zip_file_name, 'w') as zip:
        #遍历写入文件
        for file in file_paths:
            zip.write(file)
    # for file_path in file_paths:
    #     idx+=1
    #     tmp_file_paths.append(file_path)
    #     if idx%2000==0:
    #         # D:\job_24_zips
    #         # zip_file_name=rf"D:\jobZips\jobSch24_part_{part}.zip"
    #         # zip_file_name=rf"D:\job_24_zips\jobSch24_part_{part}.zip"
    #         zip_file_name=rf"D:\job_zip\jobSch24.zip"
    #         part+=1
    #         with ZipFile(zip_file_name, 'w') as zip:
    #             #遍历写入文件
    #             for file in tmp_file_paths:
    #                 zip.write(file)
    #         tmp_file_paths=[]

    # 'my_python_files.zip'
    # with ZipFile(zip_file_name, 'w') as zip:
    #     #遍历写入文件
    #     for file in file_paths:
    #         zip.write(file)

    print('successfully!')

# D:\proj\pythonProj\my_util_py_pub\zip_file.py
# python3 zip_file.py
if __name__ == "__main__":
    main()
    # zip_dir_files()
