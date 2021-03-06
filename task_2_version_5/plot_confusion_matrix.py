import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
#default

import pickle

save_path="D:\\LAB\\lab\\task_2_version_4\\confusion_matrix.txt"
#save_path="/Users/Mata/Documents/lab/task_2_version_3/features.txt"
f = open(save_path,'rb')
confusion_matrix=pickle.load(f)
f.close()

print(confusion_matrix.shape)
num_samples=confusion_matrix.shape[0]
#confusion_matrix[0,100]+=10
conf_mat=pd.DataFrame(confusion_matrix/10)#,index=[i for i in range(num_samples)],columns=[i for i in range(num_samples)])
plt.figure(figsize=(18,10))
sn.heatmap(conf_mat,cmap="YlGnBu",annot=False,linewidth=0.1,vmax=1.0,xticklabels=False, yticklabels=False)
plt.ylabel("test utterance",fontsize=20)
plt.xlabel("identified ID",fontsize=20)
plt.show()