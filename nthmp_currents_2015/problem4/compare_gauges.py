
from pylab import *
from clawpack.visclaw.data import ClawPlotData


datadir = '../all_data/4_Seaside_OSU_Model_Lab/comparison_data'

d = loadtxt(datadir+'/Wavegage.txt',skiprows=1)
t = d[:,0]

def plot_wavemaker():
    dt = 0.02
    wm_disp = 0.47*(d[:,1]-d[0,1])
    wm_speed = (wm_disp[2:] - wm_disp[:-2])/(2.*dt)
    t_speed = t[1:-1]
    
    figure()
    
    plot(t_speed,wm_speed)
    
    beta = 0.25 
    t0 = 14.75
    gaussian = 0.51*exp(-beta*(t_speed - t0)**2)
    plot(t_speed,gaussian,'r')
    xlim(0,40)
    legend(['from data','Gaussian'])
    title('speed of wavemaker')

Wmwg = d[:,2]
wg1 = d[:,3]
wg2 = d[:,4]
wg3 = d[:,5]
wg4 = d[:,6]


# ----

b1 = loadtxt(datadir+'/B1.txt',skiprows=1)
b1a = reshape(b1,(9000,4))
b4 = loadtxt(datadir+'/B4.txt',skiprows=1)
b4a = reshape(b4,(9000,4))
b6 = loadtxt(datadir+'/B6.txt',skiprows=1)
b6a = reshape(b6,(9000,4))
b9 = loadtxt(datadir+'/B9.txt',skiprows=1)
b9a = reshape(b9,(9000,4))



plotdata = ClawPlotData()
plotdata.outdir = '_output'

figure(50,figsize=(8,12))
clf()
for gnum,wg in zip([1,2,3,4], [wg1,wg2,wg3,wg4]):
    g = plotdata.getgauge(gnum)
    subplot(4,1,gnum)
    plot(t,wg,'b',label='Measured')
    plot(g.t, g.q[3,:],'r',label='GeoClaw')
    xlim(0,40)
    title('Gauge %s' % gnum)
    ylabel('surface (m)')
legend(loc='upper left')



if 0:
    gauges = {}
    gauges = [0, 1, 2, 3, 4, 5, 101, 102, 103, 104, 105, 106, 107, 108, \
                109, 201, 202, 203, 204, 205, 206, 207, 208, 209]
    for gaugeno in gauges:
        gauges[gaugeno] = plotdata.getgauge(gaugeno)

figure(501); clf()
figure(502); clf()
figure(503); clf()

subp = 0
for bnum,ba in zip([1,4,6,9], [b1a,b4a,b6a,b9a]):
    subp = subp + 1
    g = plotdata.getgauge(200 + bnum)
    figure(200+bnum)
    clf()
    subplot(311)
    plot(ba[:,0],ba[:,1],'b',label='Measured')
    plot(g.t, g.q[1,:],'r',label='GeoClaw')
    xlim(20,40)
    title('Gauge B%s' % bnum)
    ylabel('depth (m)')

    figure(501)
    subplot(4,1,subp)
    plot(ba[:,0],ba[:,1],'b',label='Measured')
    plot(g.t, g.q[1,:],'r',label='GeoClaw')
    xlim(20,40)
    ylabel('depth (m)')
    text(22,.05,'B%s' % bnum, fontsize=15)
    if subp==1: title('Depth')

    figure(200+bnum)
    subplot(312)
    plot(ba[:,0],ba[:,2],'b')
    #g = plotdata.getgauge(201)
    h = g.q[0,:]
    u = where(h > 0.001, g.q[1,:]/h, 0.)
    v = where(h > 0.001, g.q[2,:]/h, 0.)
    s = sqrt(u**2 + v**2)
    #plot(g.t, s, 'r')
    plot(g.t, u, 'r')
    xlim(20,40)
    #ylabel('speed (m/s)')
    ylabel('u-velocity (m/s)')

    figure(502)
    subplot(4,1,subp)
    plot(ba[:,0],ba[:,2],'b')
    #plot(g.t, s, 'r')
    plot(g.t, u, 'r')
    xlim(20,40)
    ylabel('m/s')
    text(22,.5,'B%s' % bnum, fontsize=15)
    #if subp==1: title('Speed')
    if subp==1: title('u-velocity')

    figure(200+bnum)
    subplot(313)
    plot(ba[:,0],ba[:,3],'b',label='Measured')
    #g = plotdata.getgauge(201)
    hss = h*s*s
    plot(g.t, hss, 'r',label='GeoClaw')
    xlim(20,40)
    ylabel('mflux (m^3/s^2)')
    legend(loc='upper left')

    figure(503)
    subplot(4,1,subp)
    plot(ba[:,0],ba[:,3],'b',label='Measured')
    plot(g.t, hss, 'r',label='GeoClaw')
    xlim(20,40)
    ylabel('m^3/s^2')
    text(22,.05,'B%s' % bnum, fontsize=15)
    if subp==1: title('Momentum flux')

if 0:
    figure(50); fname = 'wg1-4.png'; savefig(fname); print "Saved ",fname
    figure(201); fname = 'B1.png'; savefig(fname); print "Saved ",fname
    figure(204); fname = 'B4.png'; savefig(fname); print "Saved ",fname
    figure(206); fname = 'B6.png'; savefig(fname); print "Saved ",fname
    figure(209); fname = 'B9.png'; savefig(fname); print "Saved ",fname
    figure(501); fname = 'B_depth.png'; savefig(fname); print "Saved ",fname
    figure(502); fname = 'B_velocity.png'; savefig(fname); print "Saved ",fname
    figure(503); fname = 'B_mflux.png'; savefig(fname); print "Saved ",fname