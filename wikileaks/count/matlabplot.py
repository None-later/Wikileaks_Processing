#import matplotlib
import numpy as np
import matplotlib.pyplot as plt

import pylab
font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }

x=[1966,1980,2005,2008]
print x
y=[0.3,0.5,-0.0,-0.3]


plt.plot(x, y, 'k')
plt.title('Damped exponential decay', fontdict=font)
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
plt.xlabel('time (s)', fontdict=font)
plt.ylabel('voltage (mV)', fontdict=font)

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
#plt.show()
plt.savefig('foo.png')
#pylab.savefig('foo.png',bbox_inches='tight')
#plt.savefig('fafa.png', dpi=None, facecolor='w', edgecolor='w',        orientation='portrait', papertype=None, format=None,       transparent=False,bbox_inches=None, pad_inches=0.1,        frameon=None)
#fig = plt.figure()
#ax = fig.add_subplot(111)
#print ax
#ax.plot(range(100))
#fig.savefig('graph.png')
