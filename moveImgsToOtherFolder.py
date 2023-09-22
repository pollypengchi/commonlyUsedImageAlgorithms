# 執行程式即可將每個資料夾中的影像移至目標資料夾中。程式會檢查原始資料夾下的每個子資料夾，並將該子資料夾中的所有影像檔案移至目標資料夾中。

# SourceDir
#    |- folder1 - |- img1
#                 |- img2
#                 |- ...
#    |- folder2   
#    |- folder3

# TargetDir
#    |- img1
#    |- img2
#    |- ...


import os
import shutil

source_dir = 'D:/E2_brokenImage/folderA'
target_dir = 'D:/E2_brokenImage/folderB'

# 取得原始資料夾中所有子資料夾的清單
subdirectories = [f.path for f in os.scandir(source_dir) if f.is_dir()]

# 逐一處理每個子資料夾
for directory in subdirectories:
    # 取得子資料夾中所有影像檔案的清單
    image_files = [f.path for f in os.scandir(directory) if f.is_file() and f.name.endswith(('.jpg', '.png', '.jpeg'))]
    
    # 將每個影像檔案移至目標資料夾
    for image_file in image_files:
        shutil.move(image_file, target_dir)

print('move Finished!')