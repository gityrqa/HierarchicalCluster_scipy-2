import os
def del_file(path='scipy_hierarchical_clustering/'):
    for i in os.listdir(path):
        path_file = os.path.join(path, i) # 取文件绝对路径
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)


del_file(path='scipy_hierarchical_clustering/')


#-*-coding:utf-8-*-  
#文件名: ch.py  
def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体  
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
