import numpy as N
import pylab as P
#-----------------------------------------------------------------------------




DSGspat = N.load('DSG.npy')
rhoprimeSpat = N.load('density_anomaly.npy')
rhoeffAS = N.load('sourceterm.npy')


ntheta, Imax = N.shape(DSGspat)

rad		= N.linspace(0., 1.0, Imax)
th, gauss	= N.polynomial.legendre.leggauss(ntheta)
th		= N.arccos(-th)
lat = th/N.pi*180.-90.

xx,yy = N.meshgrid(lat, rad)

fig = P.figure(figsize=(18,18))
P.subplots_adjust(top=0.98, bottom=0.1, right=0.98, left=0.02, hspace=0.01)
P.rcParams['font.family'] = 'serif'
P.rcParams['font.size'] = '28'

ax	= P.subplot(311)
P.xlim(-90,90)
P.ylim(0.94,1.)
P.title(r'source term $\rho^U$')
P.ylabel(r'radius $r/R$')
P.xlabel(r'$colatitude$')
print('max original ',rhoeffAS.max() )
cmax = rhoeffAS.max()
cmap ='seismic'
cs = N.linspace(-cmax, cmax,100)
cs2 = N.linspace(-cmax, cmax,10)

im = P.contourf(xx,yy,rhoeffAS.T, cs, cmap = cmap)
P.contour(xx,yy,rhoeffAS.T, cs2, colors=['black'])
P.colorbar(im)

ax	= P.subplot(312)
P.xlim(-90,90)
P.ylim(0.94,1.)
P.title(r'true density anomaly $\rho^\prime$')
P.ylabel(r'radius $r/R$')
P.xlabel(r'$colatitude$')
print('max after trafo',rhoprimeSpat.max() )
cmax = rhoprimeSpat.max()
cs = N.linspace(-cmax, cmax,100)
cs2 = N.linspace(-cmax, cmax,10)
im = P.contourf(xx,yy,rhoprimeSpat.T, cs, cmap = cmap)
P.contour(xx,yy,rhoprimeSpat.T, cs2, colors=['black'])
P.colorbar(im)

ax	= P.subplot(313)
P.xlim(-90,90)
P.ylim(0.90,1.)
P.title(r'DSG term')
P.ylabel(r'radius $r/R$')
P.xlabel(r'$colatitude$')
cmax = N.abs(DSGspat).max()
print('max diff',cmax )
cs = N.linspace(-cmax, cmax,100)
cs2 = N.linspace(-cmax, cmax,10)
P.contour(xx,yy,DSGspat.T, cs2, colors=['black'])
im = P.contourf(xx,yy,DSGspat.T, cs, cmap = cmap)
P.colorbar(im)
P.tight_layout()


P.show()
