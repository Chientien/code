# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
read the BC points' coordinate, and give the ployfit line of the boundary.
"""

import numpy as np
import pandas as pd
import pylab as pl
import scipy.optimize as so


def getPoints(fpath,fname):
    file = fpath + fname
    # delete the string in the file
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as f:
        for line in lines:
            line = line.strip() + '\n'
            if line[0].isdigit():
                f.write(line)
    # read points coordinates
    data = np.loadtxt(file)
    x_list = data[:,1]
    y_list = data[:,2]
    return (x_list, y_list)


def sorted_x(x, y, order=1):
    ''' sorted the two list by the selected one.'''
    if order == 1:
        y = y[x.argsort()]
        x = sorted(x)
    else:
        x = x[y.argsort()]
        y = y.sort()
    return (x, y)

def linefunc(x, y, n=3):
    ''' get the representation of the BC. '''
    z = np.polyfit(x, y, n)
    print(z)
    f = np.poly1d(z)
    sumnum = 0.0
    maxnum = 0.0
    for i in range(len(x)):
        sumnum += (f(x[i])-y[i])**2
        if maxnum < np.abs(f(x[i])-y[i]):
            maxnum = np.abs(f(x[i])-y[i])
    print('maxnum is :', maxnum)
    print('sum is :', sumnum)
    return f

def showfig(x, y, f, *args):
    ''' show the fig of origin shape and the fitting shape in one picture. '''
    pl.figure()
    pl.plot(x, y,'*', label='origin shape')
    pl.plot(x, f(x), '-', label='fitting shape')
    pl.legend()
    pl.show()


if __name__ == '__main__':
    fpath = r''
    fname = r'bcPoints.txt'
    (X, Y) = getPoints(fpath, fname)
    (X, Y) = sorted_x(X, Y)
    f = linefunc(X, Y, 30)
    showfig(X, Y, f)




