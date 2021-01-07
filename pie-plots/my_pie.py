import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys




plt.rcParams['font.family']="sans-serif"
plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.size'] = 9

sns.set_style()
files = sys.argv[1:]




method = 1
for item in files:
    with open(item,'r') as rf:
        data=rf.read().split("\n\n\n")
        print(data[0],file=open(f'own_basis{method}.csv',"w"),end="")
        print(data[1],file=open(f'all_basis{method}.csv',"w"),end="")
        method += 1

file_list = ["own_basis1.csv","all_basis1.csv","own_basis2.csv","all_basis2.csv"]



fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(7,7))

item_no = 0
for  i in list(range(0,2)):
    for j in list(range(0,2)):
        df = pd.read_fwf(file_list[item_no],header=None,skiprows=3,skipfooter=1,usecols=[0,5])
        df.columns=["Type","Energy"]
        df["Type"]=df["Type"].apply(lambda x: x.lower())
        df["Energy"]=df["Energy"].round(1)
        total=(df["Energy"].sum()).round(1)
        ax[i][j].pie(df["Energy"].abs(), labels=df["Energy"], labeldistance=1.03,shadow=False, autopct='%1.1f%%')
        ax[i][j].set_title(f'Total binding energy= {total} kcal/mol')
        item_no +=1


ax[0][1].legend(df["Type"], loc=(0.5,1.1),frameon=False)
plt.tight_layout()
plt.savefig("fig1.tiff",dpi=600)
plt.show()

