import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob as glob

typeOfTest=['peeling','shearing']
csv_files = sorted(glob.glob(typeOfTest[1]+'Table_*.csv'))

fig, ax = plt.subplots()
colors = ['black','green','blue','red']
errlist = [0.01394836*np.sqrt(2),0.00691378*np.sqrt(2)]#比の値について誤差の伝播則よりsqrt(2)が必要
Rerr =errlist[0]


for itemp,file in enumerate(csv_files):
	print(itemp,file)

	df = pd.read_csv(file,sep="\t"
									 #,header=None
									 )
	print(df)
	temp_accel=df.columns.values[0]
	print("temp_accel = ",temp_accel)
	t_accel=df.iloc[:,0].to_numpy()
	print("t_accel=",t_accel)
	weightMean=df.iloc[:,1:].mean(axis='columns').to_numpy()
	print("weightMean = ",weightMean)
	normalizedWight = weightMean/weightMean[0]
	print(normalizedWight)
	#break
	ax.errorbar(t_accel
						 ,normalizedWight
						 ,yerr=normalizedWight*Rerr, capsize=3, fmt='s'
				, ecolor=colors[itemp], color=colors[itemp],ms=7, mec='k'
				, label=temp_accel)

ax.set_xlabel('acceleration time [hour]')
ax.set_ylabel('Normalized peeling strength')
#plt.yscale('log')
plt.legend(loc='upper right')
ax.set_title('90° peeling test')
plt.ylim([0,3.5])
plt.show()