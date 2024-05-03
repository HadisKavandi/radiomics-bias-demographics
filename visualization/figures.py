import numpy as np
import matplotlib.pyplot as plt

age_nih = np.load('TSNE_NIH_AGE.npy',allow_pickle=True).item()
age_mimic = np.load('TSNE_mimic_AGE.npy',allow_pickle=True).item()
age_che = np.load('TSNE_Chexpert_AGE.npy',allow_pickle=True).item()



fig, axes = plt.subplots(nrows=1, ncols=3,figsize=(15,5))
# Make the font bold
plt.rcParams['font.weight'] = 'bold'
img1=axes[0].scatter(age_nih['comp'][:,0],age_nih['comp'][:,1],c=age_nih['c'],vmin=age_nih['c'].min(), vmax=age_nih['c'].max())
axes[0].grid(which='both')
plt.colorbar(img1, ax=axes[0])
axes[0].set_xlabel('Component 1',weight='bold')
axes[0].set_ylabel('Component 2',weight='bold')
axes[0].set_title('TSNE Plot of the Distribution of \n Age from NIH-14 Dataset',weight='bold')
axes[0].spines[['right', 'top']].set_visible(False)
axes[0].spines[['bottom','left']].set_linewidth(3)


# ax2 = plt.subplot(1,3,2)
img2=axes[1].scatter(age_mimic['comp'][:,0],age_mimic['comp'][:,1],c=age_mimic['c'],vmin=age_mimic['c'].min(), vmax=age_mimic['c'].max())
axes[1].grid(which='both')
plt.colorbar(img2, ax=axes[1])
axes[1].set_xlabel('Component 1',weight='bold')
axes[1].set_ylabel('Component 2',weight='bold')
axes[1].set_title('TSNE Plot of the Distribution of \n Age from MIMIC Dataset',weight='bold')
axes[1].spines[['right', 'top']].set_visible(False)
axes[1].spines[['bottom','left']].set_linewidth(3)


# ax3 = plt.subplot(1,3,3)
img3=axes[2].scatter(age_che['comp'][:,0],age_che['comp'][:,1],c=age_che['c'],vmin=age_che['c'].min(), vmax=age_che['c'].max())
axes[2].grid(which='both')
plt.colorbar(img3, ax=axes[2])
axes[2].set_xlabel('Component 1',weight='bold')
axes[2].set_ylabel('Component 2',weight='bold')
axes[2].set_title('TSNE Plot of the Distribution of \n Age from CheXpert Dataset', weight='bold')
axes[2].spines[['right', 'top']].set_visible(False)
axes[2].spines[['bottom','left']].set_linewidth(3)
plt.tight_layout()
plt.show()

sex_nih = np.load('TSNE_nih_sex.npy',allow_pickle=True).item()
sex_mimic = np.load('TSNE_MIMIC_sex.npy',allow_pickle=True).item()
sex_che = np.load('TSNE_chexpert_sex.npy',allow_pickle=True).item()


sex_nih_label =[]
for i in range(len(sex_nih['c'])):
    if i==0:
        sex_nih_label.append('Female')
    else:
        sex_nih_label.append('Male')




fig, axes = plt.subplots(nrows=1, ncols=3,figsize=(15,5))
# Make the font bold
plt.rcParams['font.weight'] = 'bold'
axes[0].scatter(np.arange(len(sex_nih['comp']))[sex_nih['c']==0],sex_nih['comp'][sex_nih['c']==0],label='Female')
axes[0].scatter(np.arange(len(sex_nih['comp']))[sex_nih['c']==1],sex_nih['comp'][sex_nih['c']==1],label='Male')
axes[0].legend()
axes[0].grid(which='both')
axes[0].set_xlabel('Sample Number',weight='bold')
axes[0].set_ylabel('First Component',weight='bold')
axes[0].set_title('Cross Decomposition Plot of the Distribution \n Sex of from NIH-14 Dataset',weight='bold')
axes[0].spines[['right', 'top']].set_visible(False)
axes[0].spines[['bottom','left']].set_linewidth(3)


axes[1].scatter(np.arange(len(sex_mimic['comp']))[sex_mimic['c']==0],sex_mimic['comp'][sex_mimic['c']==0],label='Female')
axes[1].scatter(np.arange(len(sex_mimic['comp']))[sex_mimic['c']==1],sex_mimic['comp'][sex_mimic['c']==1],label='Male')
axes[1].legend()
axes[1].grid(which='both')
axes[1].set_xlabel('Sample Number',weight='bold')
axes[1].set_ylabel('First Component',weight='bold')
axes[1].set_title('Cross Decomposition Plot of the Distribution \n Sex of from MIMIC Dataset',weight='bold')
axes[1].spines[['right', 'top']].set_visible(False)
axes[1].spines[['bottom','left']].set_linewidth(3)

axes[2].scatter(np.arange(len(sex_che['comp']))[sex_che['c']==0],sex_che['comp'][sex_che['c']==0],label='Female')
axes[2].scatter(np.arange(len(sex_che['comp']))[sex_che['c']==1],sex_che['comp'][sex_che['c']==1],label='Male')
axes[2].legend(loc='lower left')
axes[2].grid(which='both')
axes[2].set_xlabel('Sample Number',weight='bold')
axes[2].set_ylabel('First Component',weight='bold')
axes[2].set_title('Cross Decomposition Plot of the Distribution \n Sex of from CheXpert Dataset',weight='bold')
axes[2].spines[['right', 'top']].set_visible(False)
axes[2].spines[['bottom','left']].set_linewidth(3)

plt.tight_layout()
plt.show()


race_mimic = np.load('TSNE_mimic_race.npy',allow_pickle=True).item()
race_che = np.load('TSNE_chexpert_race.npy',allow_pickle=True).item()
fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(15,5))
# Make the font bold
plt.rcParams['font.weight'] = 'bold'
axes[0].scatter(race_mimic['comp'][race_mimic['c']==0,0],race_mimic['comp'][race_mimic['c']==0,1],label='White')
axes[0].scatter(race_mimic['comp'][race_mimic['c']==1,0],race_mimic['comp'][race_mimic['c']==1,1],label='African-American')
axes[0].scatter(race_mimic['comp'][race_mimic['c']==2,0],race_mimic['comp'][race_mimic['c']==2,1],label='Asian')
axes[0].legend()
axes[0].grid(which='both')
axes[0].set_xlabel('Component 1',weight='bold')
axes[0].set_ylabel('Component 2',weight='bold')
axes[0].set_title('Cross Decomposition Plot of the Distribution \n of Races of from MIMIC Dataset',weight='bold')
axes[0].spines[['right', 'top']].set_visible(False)
axes[0].spines[['bottom','left']].set_linewidth(3)


axes[1].scatter(race_che['comp'][race_che['c']==0,0],race_che['comp'][race_che['c']==0,1],label='White')
axes[1].scatter(race_che['comp'][race_che['c']==1,0],race_che['comp'][race_che['c']==1,1],label='African-American')
axes[1].scatter(race_che['comp'][race_che['c']==2,0],race_che['comp'][race_che['c']==2,1],label='Asian')
axes[1].legend()
axes[1].grid(which='both')
axes[1].set_xlabel('Component 1',weight='bold')
axes[1].set_ylabel('Component 2',weight='bold')
axes[1].set_title('Cross Decomposition Plot of the Distribution \n of Races from CheXpert Dataset',weight='bold')
axes[1].spines[['right', 'top']].set_visible(False)
axes[1].spines[['bottom','left']].set_linewidth(3)
plt.tight_layout()
plt.show()

# axes[1].scatter(np.arange(len(sex_mimic['comp']))[sex_mimic['c']==0],sex_mimic['comp'][sex_mimic['c']==0],label='Female')
# axes[1].scatter(np.arange(len(sex_mimic['comp']))[sex_mimic['c']==1],sex_mimic['comp'][sex_mimic['c']==1],label='Male')
# axes[1].legend()
# axes[1].grid(which='both')
# axes[1].set_xlabel('Sample Number',weight='bold')
# axes[1].set_ylabel('First Component',weight='bold')
# axes[1].set_title('Cross Decomposition Plot of the Distribution \n Sex of from MIMIC Dataset',weight='bold')
# axes[1].spines[['right', 'top']].set_visible(False)
# axes[1].spines[['bottom','left']].set_linewidth(3)