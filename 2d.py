def spiral2D(A,m,n):
    t=0
    b=m-1
    l=0
    r=n-1
    direc=0
    while (t<=b & l<=r):
        if direc==0:
            for x in xrange(l,r+1):
                print A[t][x]
            t++
        elif direc==1:
            for x in xrange(t,b+1):
                print A[x][r]
            r-=1
        elif direc==2:
            for x in xrange(r+1,l,-1):
                print A[b][x]
            b-=1
        elif direc==3:
            for x in xrange(b+1,t,-1):
                print A[x][l]
            l+=1
        direc=(direc+1)%4
            
