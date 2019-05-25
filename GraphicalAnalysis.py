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
def club():
    my_data = pd.read_csv('season-1718_csv.csv', delimiter=',')
    clubs = my_data[:39]['HomeTeam'].drop_duplicates().tolist()
    return clubs
def TeamShotsnGoals():
    team = input('Enter the Team to See Shots/Goals Data\n')
    my_data = pd.read_csv('season-1718_csv.csv', delimiter=',')
    juveH = my_data.loc[(my_data.HomeTeam == team)]
    juveA = my_data.loc[my_data.AwayTeam == team]
    juveH.boxplot(by='FTHG', column='HS')
    juveA.boxplot(by='FTAG', column='AS')
    plt.show()
def TeamYCardConceede():
    team = input('Enter the Team to See Cards/Conceded Goals Data\n')
    my_data = pd.read_csv('season-1718_csv.csv', delimiter=',')
    juveH = my_data.loc[(my_data.HomeTeam == team)]
    juveA = my_data.loc[my_data.AwayTeam == team]
    plt.scatter(juveH['FTAG'],juveH['HY'])
    plt.scatter(juveA['FTHG'],juveA['AY'])
    plt.show()
def GoalsByYellow(team):
    my_data = pd.read_csv('season-1718_csv.csv', delimiter=',')
    juveH = my_data.loc[(my_data.HomeTeam == team)]
    juveA = my_data.loc[my_data.AwayTeam == team]
    x = sum(juveH['HY'])
    y = sum(juveA['AY'])
    g = sum(juveH['FTAG'])+sum(juveA['FTHG'])
    return g/(x+y)
def GoalsConceedebyYellow():
    clubs = club()
    a = []
    for team in clubs:
        a.append(GoalsByYellow(team))
    data = pd.DataFrame({'Team':clubs,'Goals/ Yellow Cards':a})
    data.sort_values(by = 'Goals/ Yellow Cards')
    plt.bar(data['Team'],data['Goals/ Yellow Cards'])
    plt.show()
