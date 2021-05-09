import statistics as sts
import numpy as np
import random 
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import pylab
from scipy import stats
from scipy.stats import kstest


class proj2:
    def __init__(self, data):
        self.data = data
        self.data = (self.data - np.mean(self.data))/np.std(self.data)
        self.mean = np.mean(data)
        self.mode = sts.mode(data)
        self.var = np.var(data)
        self.std = np.std(data)
        self.min = np.min(data)
        self.max = np.max(data)
        self.median = sts.median(data)
        self.per25= np.percentile(data,25)
        self.per75 = np.percentile(data,75)
        self.des = stats.describe(data)
        print('-'*50)
    

                
    def quantile(self, s):
        quantile = np.quantile(self.data,s)
        print('-'*50)
        
    def hist(self):
        plt.figure()
        ax = sns.distplot(self.data)
        plt.axvline(np.mean(self.data), color="r", linestyle="dashed", linewidth=5)
        _, max_ = plt.ylim()
        plt.text(
            self.data.mean() + self.data.mean() / 10,
            max_ - max_ / 10,
            "Mean: {:.2f}".format(self.data.mean()),
        )
        plt.title("data")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show();
        print('-'*50)
    
    def qq(self):
        sm.qqplot(self.data, line='45')
        plt.show()
        a = [0.25,0.5,0.75]
        b = self.data.quantile(a)
        c = pd.DataFrame(b,a)
        print(c)
        print('-'*50)

    
    def shapiro(self):
        print('kiểm định shapiro:')
        stat,p = stats.shapiro(self.data)
        print('stat-%.3f, p-%.3f' % (stat,p))
        if p> 0.05:
            print('Không thể bác bỏ H0: Phân phối dữ liệu là chuẩn')
        else:
            print('Dữ liệu không tuân theo luật phân phối chuẩn')
        print('-'*50)    
            
    def kstest(self):
        print('kiểm định kstest:')
        stat, p = kstest(self.data,'norm')
        print('stat-%.3f, p-%.3f' % (stat,p))
        if p>0.05:
            print('Không đủ bằng chứng để bác bỏ: Đây là dữ liệu phân phối chuẩn')
        else:
            print('Đấy không phải dữ liệu phân phối chuẩn')
        print('-'*50)
     
#     def standardize(self):
#          self.data = (self.data - np.mean(self.data))/np.std(self.data)
        

    


def levene(a,b,c):
    
    print(" Levene's Test: ")
    stat,p_value = stats.levene(a,b,c)
    print('statistic by Levene  = ',stat)
    print('pvalue by Levene = ',p_value)
    if (p_value<0.05) and (stat>0):
        print('các Features có tính thuần nhất')
    else:
        print('các Features không có tính thuần nhất')
    print('-'*50)
        
        
def bartlett(a,b,c):
    print(' Bartlett’s Test: ')
    stat, p_value = stats.bartlett(a,b,c)
    print('statistic by Bartlett = ',stat)
    print('pvalue by Bartlett = ',p_value)
    if (p_value<0.05) and (stat>0):
        print('Phương sai các nhóm bằng nhau.')
    else:
        print('Phương sai các nhóm không bằng nhau.')
    print('-'*50)
    
    
    

   
