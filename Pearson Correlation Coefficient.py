import math
import matplotlib as plt

# calculates the mean
def mean(x):
    sum = 0.0
    for i in x:
         sum += i
    return sum / len(x) 

# calculates the sample standard deviation
def sampleStandardDeviation(x):
    sumv = 0.0
    for i in x:
         sumv += (i - mean(x))**2
    return math.sqrt(sumv/(len(x)-1))

# calculates the PCC using both the 2 functions above
def pearson(x,y):
    scorex = []
    scorey = []

    for i in x: 
        scorex.append((i - mean(x))/sampleStandardDeviation(x)) 

    for j in y:
        scorey.append((j - mean(y))/sampleStandardDeviation(y))

# multiplies both lists together into 1 list (hence zip) and sums the whole list   
    return (sum([i*j for i,j in zip(scorex,scorey)]))/(len(x)-1)
    
print("\n-----Pearson Correlations for the given inputs-----\n")
print ("\nPearson Correlation for [1,1,3,-1] and [2,2,1,-2] : ",pearson([1,1,3,-1],[2,2,1,-2]))
print ("\nPearson Correlation for [2,2,1,-2] and [3,3,8,-1] : ",pearson([2,2,1,-2],[3,3,8,-1]))
print ("\nPearson Correlation for [1,1,3,-1] and [3,3,8,-1] : ",pearson([1,1,3,-1],[3,3,8,-1]))

