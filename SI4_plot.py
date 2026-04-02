import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib import patches

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble="\n".join([ # plots will use this preamble
        r"\usepackage{stix}",
        r"\usepackage{fdsymbol}"]))
#plt.rcParams['font.family'] = 'Arial'
#matplotlib.verbose.level = 'debug-annoying'
# rcParams['mathtext.fontset'] = 'custom'
# rcParams['mathtext.it'] = 'Arial:italic'
# rcParams['mathtext.rm'] = 'Arial'

data = pd.read_csv('to_plot.csv')

stim_conditions=np.unique(data['stim'])
exp_conditions=np.unique(data['exp'])
eye_conditions=np.unique(data['eyes'])
y=np.float64(data['prob'])
y_sem=np.float64(data['error'])

stim_conditions=stim_conditions[0:-1] # REMOVE none
stim_conditions=stim_conditions.take((1,7,6,2,0,3,5,4)) #   REORDER TO ALIGN WITH FIGURE 1
exp_conditions=exp_conditions.take((3,0,1,2)) # BRING MODEL TO FRONT
eye_conditions=eye_conditions.take((0,2,1))

fig = plt.figure(figsize=(8,8))
column_pointer=(0.5,)
row_pointer=(0.5,)
panel_width=0.6
panel_height=0.4

ax=plt.axes((column_pointer[0]-panel_width/2,
             row_pointer[0]-panel_height/2,
             panel_width,panel_height))

exp_line_style=('-','--',':','-')
for exp_p,exp in enumerate(exp_conditions):
    index=np.where((data['stim']=='none') & (data['exp']==exp))[0]
    if len(index)>0:
        y0=y[index][0]
        y0_sem=y_sem[index][0]
        if exp=='Model':
            r=patches.Rectangle((-1,y0-y0_sem),9,2*y0_sem,
                                edgecolor=None,facecolor='k',alpha=0.1)
            ax.add_patch(r)
        else:
            ax.plot((-1,8),np.ones(2)*y0,exp_line_style[exp_p],color='k',alpha=0.5)

eye_symbol_colours=('k','k','k')
eye_symbol_facecolours=('k','w','k')
exp_symbol_shape=('o','v','^','o')
inter_condition_offset=0.1
for stim_p,stim in enumerate(stim_conditions):
    offset=-1.5
    for exp_p,exp in enumerate(exp_conditions):
        for eye_p,eye in enumerate(eye_conditions):
            index=np.where((data['stim']==stim) & (data['exp']==exp) & (data['eyes']==eye))[0]
            if len(index)>0:
                y0=y[index][0]
                y0_sem=y_sem[index][0]
                x=stim_p+offset*inter_condition_offset
                if exp=='Model':
                    r=patches.Rectangle((stim_p-0.3,y0-y0_sem),0.6,2*y0_sem,
                                        edgecolor=None,facecolor='k',alpha=0.2)
                    ax.add_patch(r)
                else:
                    ax.plot(np.ones(2)*x,(y0-y0_sem,y0+y0_sem),'-',
                            color=eye_symbol_colours[eye_p],linewidth=2,alpha=0.3)
                    ax.plot(x,y0,exp_symbol_shape[exp_p],
                            markeredgecolor=eye_symbol_colours[eye_p],
                            markerfacecolor=eye_symbol_facecolours[eye_p])
                    offset+=1
ax.set_ylim((-0.05,1.05))
ax.set_xlim((-1,8))
ax.set_yticks((0,1))
ax.set_yticklabels(('0','1'))
ax.set_xticks(range(8))
stim_labels=('Black $\lgblksquare$', 'White $\lgwhtsquare$', 'Grey $\lgwhtsquare$', 'Cryptic', 'Alt. Flip', 'Black $\lightning$','White $\lightning$', 'Random $\lightning$')
ax.set_xticklabels(stim_labels, rotation=45, ha='right')
ax.tick_params(axis='both', which='both',left=False,right=True,labelleft=False,labelright=True)

output_y=0.5
spider_icon_x=column_pointer[0]-panel_width*0.61
spider_icon_width=0.12
spider_icon_y_offset=0.17
spider_icon_y=(output_y-spider_icon_y_offset,output_y+spider_icon_y_offset)
spider_icon_filenames=('spider_still.png','spider_rotating.png')
for spider_icon_p in (1,0):
    axspidericon=plt.axes((spider_icon_x-spider_icon_width/2,
                           spider_icon_y[spider_icon_p]-spider_icon_width/2,
                           spider_icon_width,spider_icon_width))
    spicon=plt.imread(spider_icon_filenames[spider_icon_p])
    axspidericon.imshow(spicon)
    axspidericon.set_axis_off()
    
axframe=plt.axes((0,0,1,1))
axframe.text(column_pointer[0]-panel_width*0.61,row_pointer[0],
             'Probability of turning',rotation=90,
                horizontalalignment='center',
                verticalalignment='center')
axframe.set_xlim((0,1))
axframe.set_ylim((0,1))
axframe.set_axis_off()


# =============================================================================
# ax.spines['right'].set_color('white')
# ax.spines['left'].set_color('white')
# ax.spines['top'].set_color('white')
# opacity_level=0.4
# ax.spines['bottom'].set_alpha(opacity_level)
# #ax.xaxis.label.set_color((1,0,0,0.2))
# ax.tick_params(axis='x',color=(0,0,0,opacity_level),labelcolor=(0,0,0,opacity_level))
# =============================================================================
