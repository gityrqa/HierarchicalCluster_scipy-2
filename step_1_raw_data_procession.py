#原始数据处理，加入索引，加入延迟序列
import numpy as np
np.set_printoptions(threshold= 1000000000000)
#
#data 转换
def dataReshape(X, dtw= 10):
    dtwL = np.ones([len(X), dtw+1])
    for i in range(dtw+1):
        dtwL[dtw-i:, i] = X[:len(X)-(dtw-i)]
    return dtwL
def Matrix_merge(X,Y):
    #X,Y行数必须相同，X的列合并后排在前面
    #如果X.shape=(n,)，要先进行X.reshape((X.shape[0],1))
    Z = np.zeros((X.shape[0], X.shape[1]+Y.shape[1]))
    Z[:, 0:X.shape[1]] = X
    Z[:, X.shape[1]:] = Y
    return Z
def main_1(filePath = 'GOLD.txt', usecols = 4, dtw = 10):
    a = np.loadtxt(filePath, usecols=usecols, delimiter=',')
    intex = np.arange(0, a.shape[0], 1)
    intex = intex.reshape((intex.shape[0], 1))
    dtwL = dataReshape(a, dtw)  # dtwL=[10天前的数据，9天前的数据，...,昨天的，今天的]共11列数据，最后一列为预测数据，倒数第二列为真实数据
    intex_dtwL = Matrix_merge(intex, dtwL)  # intex_dtwL=索引列+dtwL,这一步可以用np.hstack代替
    np.savetxt('raw_data_procession/gold_intex_-10_0.txt', intex_dtwL)
    print('step_1:原始数据处理')
    print('原始数据文件：', filePath)
    print('选取原始数据中的第n列(从第0列开始)：', usecols)
    print('选取前n天的数据用于聚类：', dtw)
    print('处理后数据维数：', intex_dtwL.shape)
    print('处理后数据的列向量代表的意义：索引，Bar[-9],...,Bar,预测列')
    print('原始数据已处理完毕，保存在：raw_data_procession/gold_intex_-10_0.txt')
    print('------')
    return intex_dtwL

if __name__=="__main__":
    filePath = 'GOLD.txt'   #载入原始数据表
    usecols = 4     #选择获取的数据：第5列
    dtw = 10        #选取前10天的数据用于分析
    main_1(filePath, usecols, dtw)

