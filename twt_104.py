_,*A=open(0)
while A:
 _,a,*A=A;r=b=0;a=*map(int,a.split()),
 for v in a:b+=v;b=[b,0][b<0];r=[b,r][b<r]
 print(r)