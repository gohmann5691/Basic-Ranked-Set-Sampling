from MainRSSamplingClass import *
import pandas as pd
import time
import os
#############################################Main Python Script
times=[]
#timer for debugging
#starttime=time.time()
###set csv file path
starttime=time.time()
df=pd.read_csv(r'C:\Users\gohmancm\Desktop\Experiments\R_Source_Code_dummy_2\simulation_60_0.28_2Copy.csv', header=None)
df=df.head(120)
#m=sample subset size
set_m=6
#r=number of cycles
set_r=len(df.index)//set_m
#choose the number of resamples(usually only needs to be 30, but can be set higher)
resamples=30
#create a results list to store the resamples dataframes
results=[]

#loop through the ranked set sampling generator to get results
for i in range(0, resamples):
    
    newGenSamples=RSSamplingMain(df, set_r, set_m)
    newGenSamples.performRSS()
    results.append(newGenSamples.RSSDataFrame)
#set the output file path here
path='C:\\Users\\gohmancm\Desktop\\RankedSetSamplingPython\\PythonRankedSetSamplingProject\\output\\'
#write the results to a csv
count=1
for i in results:
    currFileName="Cycle"+str(count)+".csv"
    i.to_csv(os.path.join(path,currFileName), index=False)
    count+=1
endTime= time.time()
print("total time was: ",str(endTime-starttime))



