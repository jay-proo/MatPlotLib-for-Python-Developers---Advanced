import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

N=100
X,Y=np.mgrid[-3:3:complex(0,N),-2:2:complex(0,N)]
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X-1)**2 - (Y-1)**2)
Z = (Z1-Z2)*2
class MidpointNormalize(colors.Normalize):
    def __init__(self,vmin=None,vmax=None,midpoint=None,clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self,vmin,vmax,clip)

    def __call__(self,value,clip=None):
        x,y=[self.vmin,self.midpoint,self.vmax],[0,0.5,1]
        return np.masked_array(np.interp(value,x,y))

fig,ax=plt.subplots(2,1)
pcm = ax[0].pcolormesh(X,Y,Z,
norm = MidpointNormalize(midpoint=0),
cmap = 'RdBu_r')
fig.colorbar(pcm,ax=ax[0],extend='both')
pcm=ax[1].pcolormesh(X,Y,Z,
cmap='RdBu_r',vmin=-np.max(Z))
fig.colorbar(pcm,ax=ax[1],extend='both')
fig.show()
