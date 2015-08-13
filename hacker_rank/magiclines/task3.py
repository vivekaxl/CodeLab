


inp=raw_input().split()
l=int(inp[0])
r=int(inp[1])

res=0
for i in range(0,32):
  if r-l+1==1 and l&1:
     ~~Fill this line~~
  l = l >>1
  r=  r>>1
print (res)