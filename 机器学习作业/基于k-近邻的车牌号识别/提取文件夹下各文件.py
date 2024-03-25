from PIL import Image
import os
import numpy as np
import tqdm
def process_img(directory_path):
    """
    将目录中所有文件转化为size=20*20的numpy矩阵
    :param directory_path: 根目录的路径
    :return: 包含所有图片信息的列表
    """
    # 查找 根目录 下所有文件路径
    def find_all_files(directory_path):
        file_paths = []
        if os.path.isfile(directory_path):
            # 根目录是文件则直接返回该目录
            file_paths.append(directory_path)
            return file_paths
        else:
            # os.walk递归遍历根目录下所有文件
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_paths.append(os.path.join(root, file))
            file_paths_cleaned = [file_path for file_path in file_paths if not file_path.endswith('.DS_Store')]
            return file_paths_cleaned
    
    # 读取图片
    def extract_img(filepath): 
        # 转化为 numpy 矩阵
        def to_array(img):
            pixels = np.array(img) 
            return pixels.reshape(-1)
            return pixels
        
        img = Image.open(filepath)
        pixels = to_array(img)
        img.close()
        return pixels
        
    
    # 将根目录下每一个img文件转化为size=20*20 numpy矩阵
    pixels_list = []
    file_path = find_all_files(directory_path)
    for filepath in tqdm(file_path, desc="Processing images"):
        if os.path.isfile(filepath):
            pixels = extract_img(filepath)
            pixels_list.append(pixels)
    return pixels_list