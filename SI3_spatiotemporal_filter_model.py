import SM3_stimuliGeneration as stim
import numpy as np
from scipy import stats,ndimage
from tqdm import tqdm

def DOGfilter(s=(5,5),SDs=(0.2,0.3),g=(1,2)):
    x,y=np.meshgrid(np.linspace(-1,1,s[0]),np.linspace(-1,1,s[1]))
    r=np.sqrt(x**2+y**2)
    g0=stats.norm.pdf(r,SDs[0])
    g1=stats.norm.pdf(r,SDs[1])
    g=g[0]*g0-g[1]*g1
    g=g-np.mean(g)
    return g

def timeIR(noframes=7):
    x=np.linspace(0,np.pi,noframes)
    t=np.cos(x)
    return t

def spreadDOGbyIR(f,t):
    m0=np.tile(np.expand_dims(f,0),(len(t),1,1))
    m1=np.tile(np.expand_dims(np.expand_dims(t,1),2),(1,f.shape[0],f.shape[1]))
    return m0*m1

# SET UP FILTERS
f=DOGfilter()
t=timeIR()
feven=spreadDOGbyIR(f,t)
# NORMALIZE FRONT-END FILTER TO RMS=1
feven=feven/np.sqrt(np.mean(feven**2))

no_stims_totest = 9
labels = ['Black', 'White', 'Gray', 'Second Order', 'Alternating Flip', 'Black Flash', 'White Flash', 'Random Flash', 'Blank']

threshold = 1.8 #i went through different iterations, this combination seems best

plot_actual_output=False
repeat_simulation=True

if repeat_simulation:
    no_iterations=90
    no_trials=tuple(np.ones(no_stims_totest-1)*10)+(80,)
    no_frames_to_consider=15
    results_iter=[]
    output2=[]
    for iteration_no in tqdm(range(no_iterations)):
        results=[]
        output1=[]
        for selectedStim in range(9):
            output0=[]
            for trial_no in range(int(no_trials[selectedStim])): #90 spiders
                x=np.float64(stim.generate(selectedStim,50)) # GENERATE STIMULUS
                # RELEVANT FRAMES EXTRACTED HERE TO REDUCE COMPUTE-TIME FOR CONVOLUTION
                x=x[0:no_frames_to_consider,:,:]
                x+=1
                x/=2 #map 0-1
                x=x**2
                # CONVOLUTION WITH FILTER
                y=ndimage.convolve(x,feven)**2 # SQUARE VALUE TO REMOVE DIRECT LINEARITY
                output=np.mean(y)
                output0.append(output)
                # ADD INTERNAL NOISE THAT SCALES SUPRALINEARLY WITH OUTPUT, WITH
                # AN ADDED 'DARK NOISE' IN THE BACKGROUND (THE +1.2)
                output+=np.random.randn()*(output**2+1.2)
                responded=(output>threshold)
                results.append((iteration_no,selectedStim,responded))
            output1.append(output0)
        output2.append(output1)
        results=np.array(results)
        results_iter.append(results)
    np.save('sim_results_rootnonlin2',results_iter)
else:
    results_iter=np.load('sim_results2.npy',allow_pickle=True)
    #results_iter=np.load('sim_results_rootnonlin2.npy',allow_pickle=True)
#results_iter=np.array(results_iter)

# output averaged over the non-blank stimuli is 1.055

prob_r_iter=[]
for iteration_no in range(len(results_iter)):
    results=results_iter[iteration_no]
    prob_r=[]
    for selectedStim in range(9):
        index=np.where(results[:,1]==selectedStim)[0]
        p=np.mean(results[index,2])
        prob_r.append(p)
    prob_r_iter.append(prob_r)
prob_r_iter=np.array(prob_r_iter)
# plt.plot(np.percentile(prob_r_iter,25,axis=0),'r--')
# plt.plot(np.percentile(prob_r_iter,50,axis=0),'r-')
# plt.plot(np.percentile(prob_r_iter,75,axis=0),'r--')
y=np.mean(prob_r_iter,0)
y_std=np.std(prob_r_iter,0)
ybaseline=y[8]
ybaseline_std=y_std[8]

labels=np.array(labels)
data = np.concatenate((np.expand_dims(y,1),np.expand_dims(y_std,1)),1)  # Numerical 2D array
np.savetxt('modelOutput.csv', data, delimiter=',', header='Mean,STD', comments='')