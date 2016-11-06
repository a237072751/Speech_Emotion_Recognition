import pandas as pd
path1 = '/home/chang/my/speech/f/angry.csv'
path2 = '/home/chang/my/speech/f/fear.csv'
path3 = '/home/chang/my/speech/f/happy.csv'
path4 = '/home/chang/my/speech/f/neutral.csv'
path5 = '/home/chang/my/speech/f/sad.csv'
path6 = '/home/chang/my/speech/f/suprise.csv'

data1 = pd.read_csv(path1,skiprows=[i for i in xrange(390)])
data2 = pd.read_csv(path2,skiprows=[i for i in xrange(390)])
data3 = pd.read_csv(path3,skiprows=[i for i in xrange(390)])
data4 = pd.read_csv(path4,skiprows=[i for i in xrange(390)])
data5 = pd.read_csv(path5,skiprows=[i for i in xrange(390)])
data6 = pd.read_csv(path6,skiprows=[i for i in xrange(390)])

data1.to_csv('/home/chang/my/speech/data/feature1.csv',sep="\t",na_rep='0',header=False)
data2.to_csv('/home/chang/my/speech/data/feature2.csv',sep="\t",na_rep='0',header=False)
data3.to_csv('/home/chang/my/speech/data/feature3.csv',sep="\t",na_rep='0',header=False)
data4.to_csv('/home/chang/my/speech/data/feature4.csv',sep="\t",na_rep='0',header=False)
data5.to_csv('/home/chang/my/speech/data/feature5.csv',sep="\t",na_rep='0',header=False)
data6.to_csv('/home/chang/my/speech/data/feature6.csv',sep="\t",na_rep='0',header=False)

print 'successful'
