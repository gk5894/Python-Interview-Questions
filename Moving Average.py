import numpy as np

dataset = [25,27,31,33,38,46,33]

def movaverage(values, window):
	weights = np.repeat(1.0,window)/window
	sma = np.convolve(values, weights, 'valid')
	return sma


def expaverage(values,window):
	weights = np.exp(np.linspace(-1.,0.,window))
	weights /= weights.sum()
	a = np.convolve(values,weights)[:len(values)]
	a[:window] = a[window]
	return a

print("\n ---------Simple Moving Average--------")
print ("\nThe simple moving average with window size 3 : ",movaverage(dataset,3))
print ("\nThe simple moving average with window size 4 : ",movaverage(dataset,4))

print("\n ---------Exponential Moving Average--------")
print ("\nThe exponential moving average with window size 3 : ",expaverage(dataset,3))
print ("\nThe exponential moving average with window size 4 : ",expaverage(dataset,4))
