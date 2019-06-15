import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, auc

fpr1=np.load('fpr_replay.npy')
tpr1=np.load('tpr_replay.npy')
auc1=auc(fpr1,tpr1)

fpr2=np.load('fpr_morph.npy')
tpr2=np.load('tpr_morph.npy')
auc2=auc(fpr2,tpr2)

fpr3=np.load('fpr_stea.npy')
tpr3=np.load('tpr_stea.npy')
auc3=auc(fpr3,tpr3)



plt.figure(121,figsize=(4,3))
#plt.plot([0,1],[0,1],'k--')
#plt.plot([-0.01,0.3],[0.75,0.75],':',color='red')
#plt.plot([0.3, 0.3],[0.75,1.05],':',color='red')



plt.xlim([-0.01,0.6])
plt.ylim([0.6,1.01])
plt.plot(fpr1,tpr1,color='black',lw=3, label='Replay Attack')

plt.plot(fpr2,tpr2,color='r',lw=3, linestyle=':', label='Morphing Attack')

plt.plot(fpr3,tpr3,color='blue',lw=3, linestyle='--',label='Stealthy Attack')


plt.xlabel('False positive rate',fontsize=12)
plt.ylabel('True positive rate',fontsize=12)
#plt.title('ROC Curve (zoomed in at top left)')
plt.legend(loc='lower right')
plt.tight_layout()

plt.show()
