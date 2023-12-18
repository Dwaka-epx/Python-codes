#************* *************

import pandas as pd
import matplotlib.pyplot as plt

plotDatasets = [# condition, before, after]
	#['125dC120min','2023-12-06-121748','2023-12-06-200841']
	['125dC120min2','2023-12-08-225841','2023-12-12-125943']
	#,['137dC10min','2023-11-12-182201','2023-11-15-194738']
	,['137dC10min2','2023-12-17-154334','2023-12-17-174653']
	,['131dC20min','2023-11-15-194738','2023-11-19-110826_2023-11-15-224348']
	#,['150dC3min','2023-11-11-211107','2023-11-12-134302']
	,['150dC3min2','2023-12-17-163006','2023-12-18-134743']
]
colors = ['blue','green','red','brown',"orange"]
nMeasureSample = 2 # [before ,after]
listDfs = []
listDfRatios=[]
errRatio = 0.02 # from the connector coupling reproducibility

for iParameter, listRuns in enumerate(plotDatasets):
	parameterLabel = listRuns[0]
	runDate = listRuns[1:]
	
	#************* fill dfs to "listDfs" *************
	for irun,date in enumerate(runDate):
		df = pd.read_csv(f'./{parameterLabel}/output_logger2signal{date}.csv')
		df.index += 1
		listDfs.append(df) #both  before and after are filled.

	dfRatio = listDfs[nMeasureSample*iParameter+1]/listDfs[nMeasureSample*iParameter]
	mean_ratio = dfRatio.mean(numeric_only=True)

	listDfRatios.append(dfRatio)
	#************* plot *************
	fig, ax = plt.subplots()
	x = np.arange(len(dfRatio))+1
	y = dfRatio.values.flatten()
	yErr = y*np.sqrt(2)*errRatio
	ax.errorbar(x, y, yerr=yErr ,fmt='o'
						 , capsize=3, label=parameterLabel)

	ax.set_title(' after signal / before welding')
	ax.set_xlabel('index of fiber (upper <-> lower)')
	ax.set_ylabel('Normalized Signal')
	ax.set_ylim([0, 1])
	ax.legend()
plt.show()

