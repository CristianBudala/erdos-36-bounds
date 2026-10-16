#!/usr/bin/env python3
# Standalone L60 certificate: explicit data plus exact outward-arithmetic proof checks.
# Derived verbatim from the two Round0061 compatibility source blocks.
if not __debug__:
    raise SystemExit('Run this proof checker without -O or -OO; assertions are required.')
DATA = """
16 32 16 32
401635816 167679538 0 -204287486 -46262888 330047142 52833752
363158272 30062772 100 100 10030892 100 100 100 100 100 100 100 294633 100 125184 84576 100 47278
-21199670 -2611668 -5 9 704435 -7 -6 2 0 -13 -8 13 39694 -8 -8140 -35 1 4715
93542962 30376 -3 -9 -734542 -1 -1 -12 -13 -2 0 -1 -8588 16 -5475 -4981 -7 3589
310578998 214281377 -217028086 185576137 -177970432 43585327 -46251735 36863524 -37474504 586637 -1229515 5236340 -6143893 139874 246831 1330530 -926084 392132

8 16 24 32
882935205 373397999 0 -194441147 -150630175 334465404 89696959
850493000 38097996 100 100 101 100 100 100 100 343211 100 100 100 188063 100 100 55985 100
-74264083 -896253 5 32 30 -2 -2 14 13 -58135 -16 -7 -6 -2187 -3 -3 -2020 6
109383387 787055 0 -7 -6 20 22 21 19 -6742 -1 8 11 1796 -3 -3 -1421 2
301593530 304937482 -320195695 205368711 -197169860 68648657 -64480860 14448675 -14274703 2098261 -3253521 2047930 -2075403 -38527 181843 -194370 196128 19406

0 8 24 32
157106059 68525755 0 -66291843 -21123353 74857692 29184989
104079687 32063468 4255746 14501803 100 100 2431461 503851 100 341800 100 100 101783 13219 84884 24695 100 29255
-9092914 -2657323 -96073 1721458 8 -25 -562211 129228 27 9936 -1 -14 -16104 3091 -920 -317 -2 445
47941 77442 10764 53252 0 1 13447 3639 1 3621 1 1 1526 192 -1849 -685 -3 375
96036243 47598058 -48665271 15667315 -15125692 3610128 -5131928 -7901529 6946089 -1348728 1841257 -2029867 2120112 -124076 205056 -88175 161994 5044

8 16 16 24
388257167 171627961 3400427 -245969430 -40605767 311373097 26051733
340261124 33818747 100 3964812 6282392 100 2739247 692792 100 385255 100 100 555844 79512 6999 100 100 100
-19793264 -1015943 1 363402 399345 -16 -375577 154392 22 -51023 -14 0 16856 -852 429 4 1 -10
39144037 1387628 4 222461 361776 -1 -43910 -29870 -4 17956 6 3 -4544 -5464 889 14 12 -16
357475110 284397422 -281184968 183964974 -175263850 65034120 -64095132 19641518 -20871820 2510651 -4480665 3514100 -3689086 351541 -286683 217498 -292449 32949

4 8 20 24
286295972 122184371 62 -246634825 -35675648 287727119 24571724
237512926 34707841 101 8162963 2184524 100 2475049 582604 100 790914 100 100 534552 100 53673 100 100 5661
-17245078 -1167604 2 735422 119210 -19 -394906 156297 27 -56735 -8 0 11889 1 3984 2 -1 313
13934706 1943451 5 370957 100950 2 22957 -39607 -7 28163 5 3 3117 -6 3162 1 -2 -1474
358122461 289672746 -286856483 185444777 -178404329 63499159 -63472043 16669836 -18501475 1738048 -3647571 2420053 -2766059 300983 -249697 179603 -272623 18259

2 4 22 24
286559586 122401867 1 -247056711 -39566612 281757186 29004454
237651041 35003782 100 9512720 777298 100 2293475 524193 100 888999 100 100 544906 100 80999 100 100 100
-18990685 -1522499 1 1008692 53062 -21 -437780 145051 28 -39324 -6 -3 -3732 10 2508 8 8 9
7141613 2109426 6 435146 34592 1 10612 -28168 -5 20654 3 3 6772 -1 5044 -4 -7 -13
358631944 291484101 -288810845 186316181 -179729976 63264134 -63349567 16052800 -17794682 2078568 -3806958 2444115 -2694795 285411 -225302 129345 -226720 5595

0 2 22 24
60067833 35704479 2429285 -17447187 -1460950 19309997 9872242
103 8129412 27650579 13150185 5818203 101 2923840 1524546 100 100 537147 281411 328256 90073 47217 5749 15404 3693
-8 -675663 -857650 935116 221788 -20 -523334 217697 13 -17 -80348 10868 25014 -4024 3384 -420 -1925 383
0 18211 64936 44764 20503 0 14036 9289 1 1 4402 2426 2874 1318 480 47 116 -10
25089283 17189202 -17032819 8609430 -8157386 3580582 -3161011 700232 -825336 352869 -461122 127368 -283030 -30353 -28349 -5085 -7526 -4399

2 4 20 22
171470971 76491658 2 -248823107 -17596001 276892821 12225391
117056979 11334043 25192509 3984295 10730440 100 1963332 436925 100 321975 100 74603 246471 22005 89034 100 10150 7810
-8497530 -551672 -55499 225236 244827 -15 -241304 107190 23 -39278 -11 2002 10814 -1832 2871 -9 -1174 961
3568102 878093 1881257 137275 311488 -3 -64831 -28409 -7 -7065 -1 3396 13701 -3981 1179 10 1086 -849
357579914 303279181 -295573220 202672856 -195949146 69950859 -69805194 28094349 -29759139 2325791 -6122051 3602017 -4428473 296876 -122711 30525 -125340 16761

1 2 21 22
59061647 31270297 245185 -175177044 -738647 192859720 5080990
108 100 36935996 5608263 12631815 100 2143693 641336 100 21984 448383 496794 100 90508 25518 100 15833 915
-8 -7 -812318 327574 323582 -17 -308814 130776 19 -2959 -51739 26251 8 -2385 1874 -5 -1325 172
2 5 1780550 231715 508038 2 46959 -9801 -2 -765 -12260 12776 4 -5358 138 7 1152 -80
251860262 208875757 -206762441 128339430 -128173628 40454844 -38765494 21496444 -22494757 1026292 -3312696 2507926 -3029979 255474 -95781 74414 -66778 -13527

0 1 21 22
61831128 40350314 3909853 -18417024 -1157707 20320578 7880797
108 411500 35381195 12821722 8166385 2794201 113 100 1499473 465370 100 296944 205077 104691 83974 7536 37041 10059
-8 -35206 -1263760 802619 260935 -470786 -16 14 184535 -82615 -15 14310 15581 -4054 4616 -444 -3124 912
0 1303 116722 57787 37893 16219 1 1 9186 2736 1 450 -7 92 1351 -23 -377 -150
26446143 19368604 -19264016 10061970 -9961453 3470560 -3014980 1498749 -1626382 273542 -301885 304254 -324379 8116 -62786 29158 -67900 2591

1 2 20 21
59774515 33644036 1206592 -163405648 -629255 180194865 4289057
103 100 36230811 6918322 11357427 100 2150745 723138 100 100 563970 623233 100 154586 29451 29262 100 2221
-7 -7 -700459 348790 219038 -15 -272682 120136 15 -13 -54349 27609 5 -3055 1597 -1414 -7 170
2 4 1580905 294813 480977 4 74634 11038 1 -3 -18827 5040 3 -3934 1113 1486 3 -439
235188410 193904531 -193075156 118078547 -118952220 38650126 -37113402 21338141 -23252531 -534005 -1796075 1890314 -2408404 242935 -213188 168629 -242919 2487

0 1 20 21
61983427 40816629 4081550 -19539312 -1086603 21543180 7388776
109 101 35663647 12726701 8347949 2882296 101 100 1540682 492570 100 288412 232467 102246 101645 100 54990 12499
-8 -8 -1227034 762192 250404 -452401 -13 13 180413 -82729 -13 14737 16061 -4372 5095 -6 -4068 1155
0 0 125208 61307 41248 16742 1 1 9856 2373 0 303 60 -28 1614 0 -546 -311
28031260 20376290 -20234389 10437745 -10334384 3535766 -3043419 1589427 -1719922 256988 -292169 309133 -330769 13508 -77423 46888 -98765 8656

4 8 16 20
119730449 55966428 1 -255322127 -7506811 282807230 4964322
62785267 557473 36011256 2164691 13810557 100 1492245 309606 100 232845 69067 427981 100 97497 96271 7415 100 46227
-3646297 -23723 -218942 78387 133086 -11 -118995 57968 17 -23371 -4990 15661 2 -1827 -819 -128 -1 702
3712448 53539 3305533 54640 196295 -8 -110910 -1188 0 -11469 -2777 26432 9 -11670 5712 206 -1 -2661
365562647 320358716 -309843961 219728011 -212981837 74490477 -76037982 30325480 -33067200 2274440 -6883035 4495947 -5816058 552158 -413984 327332 -536379 41751

0 4 16 20
62254168 41732359 4443906 -44887549 -921422 49446637 6221682
102 100 35176635 13271527 7645942 2938193 100 185503 1457271 577668 100 377678 251494 131044 141944 100 80248 18522
-7 -8 -1051074 696181 183031 -402745 -11 21961 146002 -81285 -10 20343 12361 -4673 5558 -6 -4925 1532
0 1 314266 156097 92212 41734 1 2444 19058 4995 1 -2658 -2820 -1500 4164 -1 -1746 -879
64347523 47437216 -47119187 24386594 -24420323 7704641 -6595171 4109852 -4445342 380636 -369312 772536 -680248 71391 -208426 156282 -303525 37911

16 32 0 16
189200273 80423238 0 -227553200 -609 287870635 302
140941522 25917634 100 100 10354518 100 2509230 3372059 100 100 100 2983252 387733 919032 155462 507523 100 166136
-304 -1 0 0 2 0 -2 0 0 0 0 -1 1 0 -1 1 0 0
34246533 53716 0 7 732780 -14 -383304 132168 6 -9 -10 45338 19423 36338 -4944 -2154 -3 -3859
334005564 242608733 -236141527 176341725 -164236583 52459414 -49561798 36283157 -36857587 4097649 -3525520 7643057 -8909523 -846796 -14967 644453 -517081 133064

8 16 8 16
138783646 63349713 1 -255189745 -4919085 288727689 2982387
82991148 3721865 32335240 101 15474603 100 1881922 274077 100 151724 100 409507 100 178362 74796 100 100 44308
-2410609 -73034 -32920 2 94147 -5 -59066 30759 10 -14831 -8 6790 1 -709 122 5 6 -193
9566199 326697 2697871 4 348012 -11 -191654 22148 9 -8170 -5 15910 6 -10263 4749 7 1 -2164
366036135 316841859 -306978413 217693216 -210526346 74366292 -76347905 28145466 -30945303 2521002 -6556272 4677981 -5651548 530976 -414676 277612 -503102 54225

0 8 8 16
63128842 44846121 5667218 -83369850 -438421 92431411 2930373
101 100 32285246 15234805 3167012 1921843 100 101 1542512 658482 100 546308 188862 172425 166927 100 110801 17809
-6 -5 -501085 411380 9799 -189058 -8 7 85241 -43585 -3 19024 459 369 1745 1 273 404
1 2 555317 509879 107846 47111 2 7 106833 -49395 -10 -23845 2824 3019 4485 0 -3471 26
120476257 96216048 -98094598 57244801 -59886279 22735256 -22940789 12459758 -16668009 -5504395 3995771 -1322492 1169037 -23244 -187250 105574 -266563 43545

8 16 0 8
58086621 30287857 111310 -238612914 -7195 262255004 41741
103 100 29028566 101 11188904 100 904825 100 100 23803 100 315129 100 152237 26889 100 100 13698
-1 -1 -8462 0 7038 -1 -2265 7 7 -328 -2 537 0 -198 46 1 1 23
12 10 2863774 3 159969 -13 -107501 11 11 -2504 -11 7812 7 -5399 1998 6 -1 -262
342962305 293697262 -285510806 203875218 -196720724 73773114 -75683811 28337459 -31775102 1144605 -5573899 3969176 -5102049 447238 -268653 144706 -262075 40550

0 8 0 8
63972079 48257813 7074297 -110327238 -281987 121900977 1851193
100 100 28022879 14793861 100 100 1713670 958437 553456 1011807 363110 1390588 100 341525 157614 82696 11487 34239
-3 -3 -331221 276524 1 -9 -134822 48313 25414 -41140 -7828 28286 0 -5265 -125 1809 348 -796
1 2 797319 733510 4 2 55705 153134 83148 -156507 -55081 28922 7 6224 1272 865 35 2220
159234259 131960806 -133090782 83962455 -85353248 39720908 -39320793 24626488 -32615952 -13891567 9592895 -5120523 4209409 -322100 210368 -344304 480582 -110284
"""

from fractions import Fraction as F
from math import factorial
from functools import lru_cache
import resource, signal, time
assert __debug__, 'Assertions must be enabled'
resource.setrlimit(resource.RLIMIT_CPU,(115,115))
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CORE,(0,0))
signal.alarm(175)
started=time.monotonic()
lines=[list(map(int,s.split())) for s in DATA.splitlines() if s.strip()]
assert len(lines)==19*6
cells=[lines[i:i+6] for i in range(0,len(lines),6)]
W=[F(x,4) for x in [4,22,23,32,33,44,45,57,58,72,74,82,84,108,132,138,140,160]]
C=10**8; S=10**60; N=4096
params=[]; rects=[]
for g,sc,q,a,b,d in cells:
    assert len(g)==4 and len(sc)==7
    assert all(len(v)==18 for v in (q,a,b,d))
    assert sc[1]>=0 and sc[2]>=0 and min(q)>0
    assert 0<=g[0]<g[1]<=32 and 0<=g[2]<g[3]<=32
    rects.append(tuple([F(x,32) for x in g[:2]]+[F(x,128) for x in g[2:]]))
    params.append([[F(x,C) for x in v] for v in (sc,q,a,b,d)])

def cover(rs):
    assert all(0<=a<b<=1 and 0<=c<d<=F(1,4) for a,b,c,d in rs)
    xs=sorted({x for a,b,c,d in rs for x in (a,b)})
    ys=sorted({y for a,b,c,d in rs for y in (c,d)})
    assert (xs[0],xs[-1],ys[0],ys[-1])==(0,1,0,F(1,4))
    for yl,yh in zip(ys,ys[1:]):
        y=(yl+yh)/2; end=F(0)
        for a,b in sorted((a,b) for a,b,c,d in rs if c<y<d):
            assert a==end
            end=b
        assert end==1
    for x in xs:
        for y in ys:
            assert any(a<=x<=b and c<=y<=d for a,b,c,d in rs)
    assert sum((b-a)*(d-c) for a,b,c,d in rs)==F(1,4)
    return (len(xs)-1)*(len(ys)-1)
cover(rects)

def ceil(n,d):
    assert d>0
    return -((-n)//d)
def exact(x):
    x=F(x)*S
    return x.numerator//x.denominator,ceil(x.numerator,x.denominator)
def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[1],-x[0]
def scale(x,r):
    r=F(r); a,b=x if r>=0 else (x[1],x[0])
    return a*r.numerator//r.denominator,ceil(b*r.numerator,r.denominator)
def mul(x,y):
    p=[a*b for a in x for b in y]
    return min(p)//S,ceil(max(p),S)
def mag(x): return max(abs(x[0]),abs(x[1]))
def down(x,digits):
    x=F(x); return F(x.numerator*10**digits//x.denominator,10**digits)
def up(x,digits): return -down(-F(x),digits)
def chordplus(x,y):
    if x>=0 and y>=0: return F(x+y,2)
    if x<=0 and y<=0: return F(0)
    return F(max(x,y)**2,2*abs(x-y))

def bank_enclosures():
    CS=[]
    for w in W:
        x=w/N
        assert 0<=x<=F(5,512)
        cs=[]
        for odd in (0,1):
            v=sum((-1)**k*x**(2*k+odd)/factorial(2*k+odd) for k in range(17))
            e=x**(34+odd)/factorial(34+odd)
            cs.append((exact(v-e)[0],exact(v+e)[1]))
        dc,ds=cs; c,s=(S,S),(0,0); grid=[(c,s)]
        for k in range(2*N):
            c,s=add(mul(c,dc),neg(mul(s,ds))),add(mul(s,dc),mul(c,ds))
            grid.append((c,s))
        CS.append(grid)
    result=[]
    for i,(sc,q,a,b,d) in enumerate(params):
        A,B,D,E,theta,kappa,mu=sc
        za,zb,_,_=rects[i]; zs=[za,zb]
        sj=[scale(CS[j][N][1],1/W[j]) for j in range(18)]
        H=exact(A-2*B/3+16*D/15)
        for qq,sn in zip(q,sj): H=add(H,scale(mul(sn,sn),-qq))
        aux=sum((aa*aa+bb*bb)/qq for aa,bb,qq in zip(a,b,q))
        bs=[add(exact(bb),scale(sn,dd)) for bb,sn,dd in zip(b,sj,d)]
        MP=2*B+48*D+sum((qq+abs(dd))*w*w for qq,dd,w in zip(q,d,W))
        MR=2*abs(mu)+2*sum((abs(aa)+F(mag(bb),S))*w*w for aa,bb,w in zip(a,bs,W))
        psum=0; plower=F(0); previous=None; qsum=[0,0]
        for k in range(N+1):
            u=F(k,N); t=2*u
            pe=exact(A-B*t*t+D*t**4); po=exact(E*t)
            re=exact(-theta-mu*u*u); ro=exact(-2*kappa*u)
            for j in range(18):
                ct,st=CS[j][2*k]; cu,su=CS[j][k]
                pe=add(pe,scale(ct,-q[j])); po=add(po,scale(st,d[j]))
                re=add(re,scale(cu,2*a[j])); ro=add(ro,mul(scale(su,2),bs[j]))
            pp,pm=add(pe,po),add(pe,neg(po)); weight=1 if k in (0,N) else 2
            psum+=weight*(max(pp[1],0)+max(pm[1],0))
            if previous is not None:
                plower+=chordplus(previous[0][0],pp[0])+chordplus(previous[1][0],pm[0])
            previous=pp,pm
            for j,z in enumerate(zs):
                oz=add(ro,exact(4*D*z*u**3))
                qsum[j]+=weight*max(mag(re),mag(oz))
        PU=F(psum,N*S)+4*MP/(3*N*N)
        PL=2*plower/(N*S)-4*MP/(3*N*N)
        QU=[F(qsum[j],2*N*S)+(MR+24*D*abs(zs[j]))/(12*N*N) for j in range(2)]
        assert PL>=F(999,1000)
        result.append([up(PU,9),down(F(H[0],S),9),up(aux,9)]+[up(x,9) for x in QU])
    return result
enc=bank_enclosures()
for i,e in enumerate(enc): print('BANK',i,[int(x*10**9) for x in e],flush=True)

def numerator(i,en,z,v,Q,even=False,beta=F(0)):
    A,B,D,E,theta,kappa,mu=params[i][0]
    if even: E=kappa=F(0)
    return en[1]-en[2]+beta-Q-B*z*z/2-6*D*v*v+(E+kappa)*z+mu*v

def original_ratios(es,extra=F(0),slope=F(0),baseline=F(0)):
    vals=[]
    for i,en in enumerate(es):
        za,zb,va,vb=rects[i]
        k,ss=(extra,slope) if i==9 else (F(0),F(0))
        assert en[0]>ss
        vals.extend((numerator(i,en,z,v,Q)+k-ss*baseline)/(en[0]-ss)
                    for z,Q in zip((za,zb),en[3:]) for v in (va,vb))
    return vals
b42=min(original_ratios(enc))
assert b42==F(389715084421,1024033344512)>F(151,400)
print('BASE42',b42,flush=True)

CE=ceil(S*5**64,8**64*factorial(64)); SE=ceil(S*5**65,8**65*factorial(65))
@lru_cache(maxsize=60000)
def trig(t):
    t=F(t); assert 0<=t<=80
    x=t/128; n,d=x.numerator**2,x.denominator**2
    ct,st=(S,S),exact(x); c,s=ct,st
    for k in range(1,32):
        dc=d*(2*k-1)*(2*k); ds=d*(2*k)*(2*k+1)
        ct=(-ct[1]*n//dc,ceil(-ct[0]*n,dc))
        st=(-st[1]*n//ds,ceil(-st[0]*n,ds))
        c,s=add(c,ct),add(s,st)
    c=(c[0]-CE,c[1]+CE); s=(s[0]-SE,s[1]+SE)
    for k in range(7):
        s,c=scale(mul(s,c),2),add(scale(mul(c,c),2),(-S,-S))
    assert c[0]<=c[1] and s[0]<=s[1]
    return c,s

def function(poly,co,si):
    def values(t):
        val=exact(sum(p*t**j for j,p in enumerate(poly)))
        der=exact(sum(j*p*t**(j-1) for j,p in enumerate(poly) if j))
        for w,a,b in zip(W,co,si):
            cs,sn=trig(w*t)
            val=add(val,add(mul(a,cs),mul(b,sn)))
            der=add(der,add(scale(mul(a,sn),-w),scale(mul(b,cs),w)))
        return val,der
    def primitive(t,alpha=F(1),beta=F(0)):
        val=exact(sum(p*(alpha*t**(j+1)/F(j+1)+beta*t**(j+2)/F(j+2)) for j,p in enumerate(poly)))
        for w,a,b in zip(W,co,si):
            cs,sn=trig(w*t)
            cp=add(scale(sn,(alpha+beta*t)/w),scale(cs,beta/(w*w)))
            sp=add(scale(cs,-(alpha+beta*t)/w),scale(sn,beta/(w*w)))
            val=add(val,add(mul(a,cp),mul(b,sp)))
        return val
    return values,primitive

def cell_range(values,M,x,y):
    mid,rad=(x+y)/2,(y-x)/2
    val,der=values(mid)
    error=scale((mag(der),)*2,rad)[1]+exact(M*rad*rad/2)[1]
    return val[0]-error,val[1]+error

def integrate(values,primitive,M,length,absolute):
    total=(0,0)
    for k in range(1024):
        stack=[(length*F(k,1024),length*F(k+1,1024),0)]
        while stack:
            x,y,depth=stack.pop(); lo,hi=cell_range(values,M,x,y)
            if lo>=0:
                piece=add(primitive(y),neg(primitive(x)))
            elif hi<=0:
                piece=neg(add(primitive(y),neg(primitive(x)))) if absolute else (0,0)
            elif depth<10:
                mid=(x+y)/2
                stack.extend(((mid,y,depth+1),(x,mid,depth+1)))
                continue
            else:
                upper=max(abs(lo),abs(hi)) if absolute else max(0,hi)
                piece=(0,scale((upper,)*2,y-x)[1])
            total=add(total,piece)
    return F(total[0],S),F(total[1],S)

sc,q,a,b,d=params[9]; A,B,D,E,theta,kappa,mu=sc
sj=[scale(trig(w)[1],1/w) for w in W]
bs=[add(exact(bb),scale(sn,dd)) for bb,sn,dd in zip(b,sj,d)]
H=exact(A-2*B/3+16*D/15)
for qq,sn in zip(q,sj): H=add(H,scale(mul(sn,sn),-qq))
aux=sum((aa*aa+bb*bb)/qq for aa,bb,qq in zip(a,b,q))
MP=2*B+48*D+sum((qq+abs(dd))*w*w for qq,dd,w in zip(q,d,W))
kernels={sign:function([A,sign*E,-B,0,D],[exact(-qq) for qq in q],[exact(sign*dd) for dd in d]) for sign in (1,-1)}
PU=F(0)
for sign in (1,-1): PU+=integrate(*kernels[sign],MP,F(2),False)[1]
Qends=[]
for z in (F(0),F(1,32)):
    MR=2*abs(mu)+24*D*z+2*sum((abs(aa)+F(mag(bb),S))*w*w for aa,bb,w in zip(a,bs,W))
    QU=F(0)
    for sign in (1,-1):
        fn,pr=function([-theta,-sign*2*kappa,-mu,sign*4*D*z],[exact(2*aa) for aa in a],[scale(bb,2*sign) for bb in bs])
        QU+=integrate(fn,pr,MR,F(1),True)[1]/2
    Qends.append(up(QU,12))
refined=[up(PU,12),down(F(H[0],S),12),up(aux,12)]+Qends
print('REFINED9',[int(x*10**12) for x in refined],flush=True)
es=enc.copy(); es[9]=refined
for sign in (1,-1):
    fn,_=kernels[sign]
    for j in range(64):
        x=F(299,200)+F(j,6400)
        assert F(cell_range(fn,MP,x,x+F(1,6400))[0],S)>F(1,200000)
local=F(1,100)*F(1,200000)*F(1,4)
assert local==F(1,80000000)
b43=min(original_ratios(es,extra=local))
assert b43==F(16238132272123,42667759958016)>b42
print('BASE43',b43,flush=True)
trig.cache_clear()

t1,t2=2-2*b43,2-b43
assert 0<t1<t2<2
stack=[]
for start,stop,region in ((t1,t2,1),(t2,F(2),2)):
    stack.extend((start+(stop-start)*F(k,128),start+(stop-start)*F(k+1,128),region,0) for k in range(128))
total=(0,0); slope_total=(0,0); counts=[0,0,0,0]
def weighted(sign,alpha,beta,left,right):
    pr=kernels[sign][1]
    return add(pr(right,alpha,beta),neg(pr(left,alpha,beta)))
while stack:
    left,right,region,depth=stack.pop(); mid=(left+right)/2
    p=cell_range(kernels[1][0],MP,left,right)
    n=cell_range(kernels[-1][0],MP,left,right)
    pzero,nzero=p[1]<=0,n[1]<=0
    ppos,npos=p[0]>=0,n[0]>=0
    if (region==1 and (pzero or nzero)) or (pzero and nzero):
        counts[1]+=1; continue
    value=svalue=None
    if region==2 and ppos and nzero:
        value=weighted(1,-t2,1,left,right); svalue=weighted(1,1,0,left,right)
    elif region==2 and npos and pzero:
        value=weighted(-1,-t2,1,left,right); svalue=weighted(-1,1,0,left,right)
    elif ppos and npos:
        diff=p[0]-n[1],p[1]-n[0]
        if diff[0]>=0 or diff[1]<=0:
            small=-1 if diff[0]>=0 else 1
            if region==1:
                value=weighted(small,-t1,1,left,right)
                svalue=weighted(small,2,0,left,right)
            else:
                value=add(weighted(-small,-t2,1,left,right),weighted(small,b43,0,left,right))
                svalue=add(weighted(1,1,0,left,right),weighted(-1,1,0,left,right))
    if value is not None:
        assert value[1]>=0 and svalue[1]>=0
        total=add(total,(max(0,value[0]),value[1]))
        slope_total=add(slope_total,(max(0,svalue[0]),svalue[1]))
        counts[0]+=1
    elif depth<24:
        stack.extend(((left,mid,region,depth+1),(mid,right,region,depth+1)))
        counts[3]+=1
    else:
        pp,nn=(max(0,p[0]),max(0,p[1])),(max(0,n[0]),max(0,n[1]))
        upper=scale((min(pp[1],nn[1]),)*2,right-t1)[1]
        if region==2:
            diffabs=max(abs(pp[0]-nn[1]),abs(pp[1]-nn[0]))
            upper+=scale((diffabs,)*2,right-t2)[1]
        total=add(total,(0,scale((upper,)*2,right-left)[1]))
        su=2*min(pp[1],nn[1]) if region==1 else pp[1]+nn[1]
        slope_total=add(slope_total,(0,scale((su,)*2,right-left)[1]))
        counts[2]+=1
Klo,Khi=[F(x,S) for x in total]; Slo,Shi=[F(x,S) for x in slope_total]
assert 0<Klo<=Khi and 0<Slo<=Shi
assert Khi-Klo<F(1,10**14) and Shi-Slo<F(1,10**13)
kcharge,scharge=down(Klo,12),down(Slo,12)
assert kcharge==F(116187,10**12) and scharge==F(1486353,10**12)
assert Khi<=kcharge+F(1,10**12) and Shi<=scharge+F(1,10**12)
print('CAPACITY_1e12',[int(kcharge*10**12),int(up(Khi,12)*10**12)],flush=True)
print('SLOPE_1e12',[int(scharge*10**12),int(up(Shi,12)*10**12)],'COUNTS',counts,flush=True)
b44=min(original_ratios(es,kcharge,scharge,b43))
assert b44==F(1804280960753284521785949,4740976650891870164928512)>b43
print('BASE44',b44,flush=True)
trig.cache_clear()

U,H,Tbar,Q0,Q1=refined
beta=F(sum(10000*bb*bb//qq for bb,qq in zip(cells[9][4],cells[9][2])),10**12)
assert beta==F(10206362,10**12)>F(1,100000)
Z=F(1,32); rr=F(3,128); v0=F(21,128); v1=F(11,64)
def qline(z): return Q0+(Q1-Q0)*z/Z

def twenty_cover(zd,loss9,loss11,credit,qe,qo):
    assert U>loss9+scharge
    left=[numerator(9,refined,z,v,Q,True,credit)/(U-loss9)
          for z,Q in ((F(0),Q0),(zd,qe)) for v in (v0,v1)]
    middle=[(numerator(9,refined,z,v,Q)+kcharge-scharge*b43)/(U-loss9-scharge)
            for z,Q in ((zd,qo),(rr,qline(rr))) for v in (v0,v1)]
    D8=params[8][0][2]; en8=enc[8]
    right=[numerator(8,en8,z,v,Q)/en8[0]
           for z,Q in ((rr,en8[3]+D8*(Z-rr)),(F(1,16),en8[4])) for v in (v0,v1)]
    rs=[(F(0),zd,v0,v1),(zd,rr,v0,v1),(rr,F(1,16),v0,v1)]
    other=[]
    assert rects[8]==(Z,F(1,16),v0,v1) and rects[9]==(0,Z,v0,v1)
    for i,en in enumerate(enc):
        if i in (8,9): continue
        za,zb,va,vb=rects[i]; area=en[0]-(loss11 if i==11 else 0)
        assert area>0
        other.extend(numerator(i,en,z,v,Q)/area for z,Q in zip((za,zb),en[3:]) for v in (va,vb))
        rs.append(rects[i])
    boxes=cover(rs)
    assert len(rs)==20 and len(left+middle+right+other)==80 and boxes==56
    return left+middle+right+other
oldzd=F(1,4608)
oldvals=twenty_cover(oldzd,F(0),F(0),F(1,100000),Q0+D*oldzd,qline(oldzd))
b45=min(oldvals)
assert b45==F(3507534735370000866111759439,9216458609333795600621027328)>b44
print('BASE45',b45,flush=True)

PAIRS=[
(12,29,35259,35910),(12,30,7162,7294),(13,20,52742,53605),
(13,27,75966,76861),(13,28,62460,63614),(14,19,7027,7257),
(14,21,40149,40912),(14,22,100118,102102),(14,24,162261,165285),
(14,26,25849,25711),(14,27,12796,13545),(15,19,105205,107130),
(15,20,1539,1103),(15,25,138664,141243),(15,26,88314,90571),
(16,16,43654,44457),(16,19,81410,83325),(16,22,33625,34561),
(16,23,115981,117547),(17,20,189976,193420),(17,21,43064,43436),
(17,23,68972,70860),(18,18,70191,71309),(18,21,144401,147533),
(19,22,72995,73943),(20,20,1662,2051)]
assert len(PAIRS)==26
h=F(1,2000); Hlim=F(31,1000); losses={}
for ri,pos in ((9,2),(11,3)):
    scalar,qq,aa,bb,dd=params[ri]
    a0,b0,d0,e0,*_=scalar
    c=[F(0)]*16; c[0]=a0; c[1]=e0; c[2]=-b0; c[4]=d0
    for j in range(16):
        if j%2==0:
            c[j]-=sum(qj*(-1)**(j//2)*w**j/factorial(j) for qj,w in zip(qq,W))
        else:
            c[j]+=sum(dj*(-1)**((j-1)//2)*w**j/factorial(j) for dj,w in zip(dd,W))
    err=sum((qj+abs(dj))*(w*Hlim)**16/factorial(16) for qj,dj,w in zip(qq,dd,W))
    de=sum((qj+abs(dj))*w*(w*Hlim)**15/factorial(15) for qj,dj,w in zip(qq,dd,W))
    additions={}; removals={}
    for entry in PAIRS:
        kk,ll=entry[:2]; gamma=F(entry[pos],C)
        assert 0<kk<=ll and gamma>0 and (kk+ll+2)*h<=Hlim
        for j in (kk,ll): additions[j]=additions.get(j,F(0))+gamma
        for j in (kk+ll,kk+ll+1): removals[j]=removals.get(j,F(0))+gamma/2
    assert not (set(additions)&set(removals)) and c[2]>0
    val=lambda t:sum(c[j]*t**j for j in range(16))
    for j in set(additions)|set(removals):
        derivative=2*c[2]*j*h-abs(c[1])-de-sum(n*abs(c[n])*((j+1)*h)**(n-1) for n in range(3,16))
        assert derivative>0
    for j,gamma in additions.items():
        assert max(val((j+1)*h),val(-(j+1)*h))+err+gamma<0
    for j,gamma in removals.items():
        assert min(val(j*h),val(-j*h))-err-gamma>0
    losses[ri]=2*h*sum(F(entry[pos],C) for entry in PAIRS)
assert losses=={9:F(890721,50000000000),11:F(362917,20000000000)}
assert Hlim<1 and b45>b43
print('CORRECTION_SAVINGS',losses[9],losses[11],flush=True)

OUT=10**15; zd=F(1,1800)
def abslinear(av,bv):
    aa=(av[0]+av[1])//2; bb=(bv[0]+bv[1])//2
    ea=max(aa-av[0],av[1]-aa); eb=max(bb-bv[0],bv[1]-bb)
    if 2*N*abs(aa)>=abs(bb): base=ceil(abs(aa)*OUT,S*N)
    else: base=ceil(aa*aa*OUT,S*abs(bb))+ceil(abs(bb)*OUT,4*S*N*N)
    return base+ceil(ea*OUT,S*N)+ceil(eb*OUT,4*S*N*N)
ca=[exact(2*aa) for aa in a]; cad=[exact(-2*aa*w) for aa,w in zip(a,W)]
cb=[scale(x,2) for x in bs]; cbd=[scale(x,2*w) for x,w in zip(bs,W)]
rot=[trig(w/N) for w in W]; cur=[trig(w/(2*N)) for w in W]
totals=[0,0]
for i in range(N):
    u=F(2*i+1,2*N)
    ev=exact(-theta-mu*u*u); ed=exact(-2*mu*u)
    ov=exact(-2*kappa*u); od=exact(-2*kappa)
    for j,(cs,sn) in enumerate(cur):
        ev=add(ev,mul(ca[j],cs)); ed=add(ed,mul(cad[j],sn))
        ov=add(ov,mul(cb[j],sn)); od=add(od,mul(cbd[j],cs))
    cub=exact(4*D*zd*u**3); cubd=exact(12*D*zd*u*u)
    for mode in range(2):
        vv=cub if mode==0 else add(ov,cub)
        dv=cubd if mode==0 else add(od,cubd)
        for sign in (-1,1):
            totals[mode]+=abslinear(add(ev,scale(vv,sign)),add(ed,scale(dv,sign)))
    nxt=[]
    for (cs,sn),(cc,ss) in zip(cur,rot):
        nc=add(mul(cs,cc),neg(mul(sn,ss)))
        ns=add(mul(sn,cc),mul(cs,ss))
        nc=(max(-S,nc[0]),min(S,nc[1])); ns=(max(-S,ns[0]),min(S,ns[1]))
        assert nc[0]<=nc[1] and ns[0]<=ns[1]
        nxt.append((nc,ns))
    cur=nxt
M2e=24*D*zd+2*abs(mu)+2*sum(abs(aa)*w*w for aa,w in zip(a,W))
M2o=M2e+2*sum((abs(bb)+abs(dd)/w)*w*w for bb,dd,w in zip(b,d,W))
qe,qo=[up(F(total,2*OUT)+M2/(24*N*N),12) for total,M2 in zip(totals,(M2e,M2o))]
assert (qe,qo)==(F(8649077068,10**12),F(8649114950,10**12))
print('FRESH_Q_1e12',[int(x*10**12) for x in (qe,qo)],'BETA_1e12',int(beta*10**12),flush=True)
vals=twenty_cover(zd,losses[9],losses[11],beta,qe,qo)
L60=F(3945957506942881,10368080969891328)
assert L60<F(1,2) and min(vals)==L60
assert all(x>=L60 for x in vals)
assert U-losses[9]==F(250001952399,250000000000)
print('L60',L60,flush=True)
print('PASS: all regenerated premises; 80 vertices; 20 closed rectangles; 56 elementary boxes',flush=True)
u=resource.getrusage(resource.RUSAGE_SELF)
print('CPU',u.ru_utime+u.ru_stime,'WALL',time.monotonic()-started,'RSS_KiB',u.ru_maxrss,flush=True)
