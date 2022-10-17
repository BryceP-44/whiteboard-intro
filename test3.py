import numpy as np
from math import *
import random
import cv2
import time

path= r'D:\trash\yt\vids\new intro\hatupic.png'
img=cv2.imread(path)

fps=60
h,w,channels=img.shape
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
outvid=cv2.VideoWriter('output.avi',fourcc,fps,(w,h),isColor=True)
frames=240

#make a fram of 0s replace with spiny ones,ones that are 0 still
#find them with np.where and then replace with img2 of whiteboard

b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]
info=[]



print("scanning image...")

for i in range(h):
    for j in range(w):
        b,g,r=img[i,j,:]
        if b<100 and g<100 and r>100:
            Ay=1000*random.uniform(-1,1)
            Ax=1000*random.uniform(-1,1)
            phiy=.1*random.uniform(-1,1)
            wy=(pi+phiy)/frames #phiy/frames
            phix=.1*random.uniform(-1,1)
            wx=(pi+phix)/frames #phix/frames
            info.append([i,j,i,j,wy,wx,phiy,phix,Ay,Ax,b,g,r])


ti=time.time()
print("writing swirley pixels...")
for i in range(frames):
    
    if i%10==0:
        print(round(100*i/frames),"percent done in",round(time.time()-ti),"total seconds")
    
    frame=np.zeros((h,w,3),dtype=np.uint8)
    frame[:,:,:]=[255,255,255]
    #i need w,x,xog,y,yog,phix,phiy
    for j in range(len(info)):
        y,x,yog,xog,wy,wx,phiy,phix,Ay,Ax,b,g,r=info[j]
        
        y=yog+Ay*sin(wy*(i+1)-phiy)
        x=xog+Ax*sin(wx*(i+1)-phix)
            
        if y<1080-1 and y>0:
            if x<1920-1 and x>0:
                frame[round(y),round(x),0]=b
                frame[round(y),round(x),1]=g
                frame[round(y),round(x),2]=r
    if i==0 and j==0:
        for i in range(5):
            outvid.write(frame)
    outvid.write(frame)
    
for i in range(5):
    outvid.write(frame)
    
final=np.copy(frame)
writer=np.copy(img)

print("writing transition...")
tran=150
ti=time.time()
for i in range(tran):
    if i%10==0:
        print(round(100*i/tran),"percent done in",round(time.time()-ti),"total seconds")
    b=(i+1)/tran*img[:,:,0]+(1-((i+1)/tran))*final[:,:,0]
    g=(i+1)/tran*img[:,:,1]+(1-((i+1)/tran))*final[:,:,1]
    r=(i+1)/tran*img[:,:,2]+(1-((i+1)/tran))*final[:,:,2]
    writer[:,:,0]=b
    writer[:,:,1]=g
    writer[:,:,2]=r
    
    outvid.write(writer)
    
for i in range(20):
    outvid.write(img)
    


for i in range(60):
    frame=np.copy(img)
    a=round(h*i/60) #h*percentage
    frame[0:a,:,0]=0
    frame[h-a:h,:,0]=0
    frame[0:a,:,1]=0
    frame[h-a:h,:,1]=0
    frame[0:a,:,2]=0
    frame[h-a:h,:,2]=0
    outvid.write(frame)













