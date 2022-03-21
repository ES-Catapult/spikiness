# spikiness
Code to calculate spikiness of a pandas data Series. 
The basis of this calculation is the spikiness function:
int( (y''(t))**2 )dt - The integral of the square of the second derivative of the function
Here we calculate the RMS spikiness for evenly spaced data
