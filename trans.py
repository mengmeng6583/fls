import pickle
from PIL import Image


# 显示加载的图像

f = open('D:\Prototype_Completion_for_FSL-main\data\MiniImagenet\miniImageNet_category_split_train_phase_train.pickle','rb')   #pickle_data_path为.pickle文件的路径；
#info = pickle.load(f)
with open('D:\Prototype_Completion_for_FSL-main\data\MiniImagenet\miniImageNet_category_split_train_phase_train.pickle', 'rb') as f:
    info = pickle.load(f, encoding='latin1')
print(info)
f.close()  #别忘记close pickle文件