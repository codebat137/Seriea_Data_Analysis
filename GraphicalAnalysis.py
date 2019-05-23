import csv
import pandas as pd
import numpy as np
from pandas import DataFrame
from scipy import stats
from datetime import datetime
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
def TeamShotsnGoals():
    team = input('Enter the Team to See Shots/Goals Data\n')
    my_data = pd.read_csv('season-1718_csv.csv', delimiter=',')
    juveH = my_data.loc[(my_data.HomeTeam == team)]
    juveA = my_data.loc[my_data.AwayTeam == team]
    juveH.boxplot(by='FTHG', column='HS')
    juveA.boxplot(by='FTAG', column='AS')
    plt.show()
TeamShotsnGoals()