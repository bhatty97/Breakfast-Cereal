import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("BC2.csv")

#  Method that determines the number of every dataset
def function():
    G = 0
    K = 0
    N = 0
    P = 0
    Q = 0
    R = 0
    for row in data.Manufacturer:
        if row == 'General Mills':
            G = G+1
        if row == 'Kelloggs':
            K = K+1
        if row == 'Nabisco':
            N = N+1
        if row == 'Post':
            P = P+1
        if row == 'Quaker Oats':
            Q = Q+1
        if row == 'Ralston Purina':
            R = R+1
    print('The number of General Mills cereal products are: %d' % G)
    print('The number of Kelloggs cereal products are: %d' % K)
    print('The number of Nabisco cereal products are: %d' % N)
    print('The number of Post cereal products are: %d' % P)
    print('The number of Quaker Oats cereal products are: %d' % Q)
    print('The number of Ralston Purina cereal products are: %d' % R)

    plt.bar(['General Mills', 'Kelloggs', 'Nabisco', 'Post', 'Quaker Oats', 'Ralston Purina'], [G, K, N, P, Q, R])
    plt.show()

# General test plot
# data.plot(kind='bar', x='Fiber', y='Manufacturer')
# plt.show()

hist = data.hist(bins=3)
plt.show()