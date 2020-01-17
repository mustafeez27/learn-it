def pln(s):
    l=len(s)
    mx=0
    ls=''
    st=''
    rl=1
    rm=1
    i=0
    for i in range(l):
        f=mx
        ss=s[i]
        s2=ss
        z=i-1
        p=i+2
        a=i
        d=i+2
        t=i
        t1=i
        if len(ss)>mx and ss==ss[::-1]:
                mx=len(ss)
                ls=ss
        while ss==ss[::-1] and (z>=0 and p<l+1):
            ss=s[z:p]
            z-=1
            p+=1
            if len(ss)>mx and ss==ss[::-1]:
                mx=len(ss)
                ls=ss
            if mx>(l-i)*2:
                #print len(ls)
                return ls
        while s2==s2[::-1] and a>=0 and d<l+1:
            #print s2,i,a,d
            s2=s[a:d]
            a-=1
            d+=1
            if len(s2)>mx and s2==s2[::-1]:
                mx=len(s2)
                ls=s2
            if mx>(l-i)*2:
                #print len(ls)
                return ls        
            
    return ls
print pln('bb')
print pln('acac2frack')
print pln('babad')
print pln("aacdefcaa")
print pln("aaaaa")

print pln("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
print len("ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
print len("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")

