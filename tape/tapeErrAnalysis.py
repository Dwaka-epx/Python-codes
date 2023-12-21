import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob as glob

typeOfTest=['peeling','shearing']
csv_files = sorted(glob.glob(typeOfTest[1]+'Table_*.csv'))

numerator=[0]
denominator=[0]
for itemp,file in enumerate(csv_files):
	df = pd.read_csv(file,sep="\t")
	df_weight = df.iloc[:,1:]
	print("df = ",df)
	#print("df_weight = ",df_weight)
	nsampleArray = df_weight.count(axis=1).to_numpy()
	print("nsampleArray = ",nsampleArray)
	weightMean=df_weight.mean(axis='columns').to_numpy()
	weightVariance=df_weight.var(axis='columns',ddof=1).to_numpy()
	weightVarianceRate = weightVariance/weightMean
	print("weightMean = ",weightMean)
	print("weightVariance = ",weightVariance)
	print("weightVarianceRate= ",weightVarianceRate)

	numerator += ((nsampleArray-1)/(2*weightVarianceRate)).sum()
	denominator += ((nsampleArray-1)/(2*np.square(weightVarianceRate))).sum()
print(numerator/denominator)