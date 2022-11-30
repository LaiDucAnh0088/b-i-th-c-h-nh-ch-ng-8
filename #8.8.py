#8.8
a= int(input('nhap ma loai phong: '))
b= int(input('nhap so dem ban o: '))
s=0
if(a==1): s= b*1260
if(a==2): s= b*1550
if(a==3): s= b*1830
if(a==4): s= b*1830
if(a==5): s= b*2120
if(a==6): s= b*2120
if(a==7): s= b*2540
if(a==8): s= b*4800
if(b<2): print('so tien phai tra: ',s)
if(2<=b<=3): print('so tien phai tra: ',s- s/4)
if(b>=4): print('so tien phai tra: ',s- s/3)

