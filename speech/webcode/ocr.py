# -*- coding: UTF-8 -*-
from sklearn.metrics import classification_report
import csv
import numpy as np
from numpy import matrix
from math import pow
from collections import namedtuple
import math
import random
import os
import json
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
class MyModel:
    # 保存神经网络的文件路径
	NN_FILE_PATH = "/home/chang/my/speech/webcode/data/model.m"
	def __init__(self, data_matrix, data_labels, use_file=True):
		# 决定了要不要导入nn.json
		self._use_file = use_file
		# 数据集
		self.data_matrix = data_matrix
		self.data_labels = data_labels
		if (not os.path.isfile(self.NN_FILE_PATH) or not use_file):
            # 初始化神经网络
            # 训练并保存
			self.clf = OneVsOneClassifier(LinearSVC(random_state=0))
			ids = np.arange(len(data_labels))
			np.random.shuffle(ids)
			# shuffle
			X = data_matrix[ids]
			y = data_labels[ids]
			self.train(X,y)

			self.save()
		else:
            # 如果nn.json存在则加载
			self._load()

	def train(self, data_matrix,data_labels):
		self.clf.fit(data_matrix,data_labels)
		print "training..."
		y_pred = self.predict(data_matrix)
		print(classification_report(data_labels, y_pred))

	def predict(self, test):
		return self.clf.predict(test)

	def save(self):
		if not self._use_file:
			return
		joblib.dump(self.clf, self.NN_FILE_PATH)

	def _load(self):
		if not self._use_file:
			return
		self.clf = joblib.load(self.NN_FILE_PATH)


