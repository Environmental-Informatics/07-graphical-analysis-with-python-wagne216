#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:19:18 2020
ABE 651 Assignment 7: graphical Analysis with Python
@author: wagne216
"""

# modules:
import numpy as n
import matplotlib.pyplot as m
import pylab as p
import pandas as d
import seaborn as sns # for the KDE plot
import sys as s # to get command line arg
import scipy as sp
import statsmodels.api as sm # for QQ plot

# 1.) OPEN DATA
col_names =['time','latitude','longitude','depth','mag','magType','nst','gap',\
             'dmin','rms','net','ID','update,''place','Type','horizontalError',\
             'depthError','magError','magNst','status','locationSource','magSource']
# can use read_table for more general or read_csv
# quakes = d.read_table('all_month.csv', header=None,names=col_names) 
# read_csv is easier to automatically get header names
quakes = d.read_csv('all_month.csv', header=0)
normal = d.read_csv('normaldata.csv')

# does it look ok?
print()
print('check data headers: ',quakes.columns )

#%% 2.) GRAPHICAL ANLAYSIS

# 1. histogram - magnitudes
# change mag series to DataFrame 
x = d.DataFrame(quakes['mag'])
#print('x:',x)
#print('xmax:',x.max())
m.hist(x,density=True,bins=10)
#n.histogram(x,bins = 10,range=[0,10])

# format
xt = [-1.6,3, 6.3]
#xt = n.linspace(n.min(x),n.max(x),10) 
m.xticks(xt) # not going where expected
m.xlabel('Earthquake Magnitudes')
m.ylabel('Magnitude Frequency')
m.title('Histogram of Earthquake Observed Earthquake Magnitudes')
#banana = m.xticks() # shows xtick positions are in [-1.63 411 514]!?

p.show()


#%% 2. KDE of magnitudes
# change mag series to DataFrame 
x = d.DataFrame(quakes['mag'])
kdeplot = sns.distplot(x, kde = True, hist=False, rug=True)

# label:
m.xlabel('Earthquake Magnitudes')
m.ylabel('Kernel Density')
m.title('KDE of Earthquake Observed Earthquake Magnitudes')
p.show()

#%% 3. lat v long
# change lat and long series to DataFrames 
y = d.DataFrame(quakes['latitude'])
x = d.DataFrame(quakes['longitude'])

#label:
m.xlabel('Degrees Longitiude')
m.ylabel('Degrees Longitude')
m.title('Spatial Distribution of Earthquake Observations')
m.xticks(n.linspace(-150,150,4))
m.yticks(n.linspace(-65,65,4))

m.plot(x,y,c='black',marker='o',markersize = 1,linestyle='none')
p.show() # to essentially wrap up this  plot

# %% 4. normalized CDF of depths
# change depth series to DataFrames
df_x = d.DataFrame(quakes['depth'])
#x_cdf = n.cumsum(x) # total CDF
#x_cdf_norm = x_cdf/x_cdf.max() # normalized when sums to 1

#label:
m.xlabel('Earthquake Depths (km)')
m.ylabel('F(x)')
m.title('Normalized CDF of Observated Earthquake  Depths')

# using a histogram: (not correct)
#n_bins = 50
# m.hist(x,n_bins,density=True,histtype='step',cumulative=True,label='Empirical')

# plot from scratch: 
x = n.sort(df_x, axis=0) # put depth data in order (must specify axis in this case)
y = n.arange(1,len(x)+1)/len(x) # create y that will be 
m.plot(x,y, marker = '.',color='green', linestyle='none')
p.show()

# %% 5. scatter plot of magnitude v depth
# change depth series to DataFrames
y = d.DataFrame(quakes['depth'])
x = d.DataFrame(quakes['mag'])

#label:
m.xlabel('Earthquake Magnitudes')
m.ylabel('Earthquake Depths (km)')
m.title('Scatterplot of Earthquake Depths versus Magnitudes')

# set plot
m.ylim((-5,700))
m.xlim((-2,7))

# plot using markers instead of scatterplot beacuse there is something I do 
# wrong with scatterplots that i don't understand
m.plot(x,y,'.', color='purple',markersize = 1.5)
p.show()

# %% 6. quantile/Q-Q of magnitudes
 
# change mag series to DataFrames then to array
x = d.DataFrame(quakes['mag'])
xa = n.array(x)
 
# qq plot 
sm.qqplot(xa) 
m.title('QQ Plot of Earthquake Magnitudes') # this doesn't show up

p.show() 

# %% testing qq plot- something is off
#sm.qqplot(normal)
#p.show() 


