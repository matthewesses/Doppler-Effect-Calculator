f_s=6.66*10**14#frequency observed by source
f_o=None #frequency observed by observer
v_s=0 #velocity of the source
v_o=-0.8 #velocity of the observer
c=1# speed of the wave in the medium

#algebra for the dopplar effect
if f_s!=None and v_o!=None and v_s!=None:
    f_o=((c+v_o)/(c+v_s))*f_s
elif v_o!=None and f_o!=None and v_s!=None:
    f_s=(((c+v_o)/(c+v_s))/f_o)**1
elif f_s!=None and f_o!=None and v_s!=None:
    v_o=((f_s/f_o)/(c+v_s))-c
elif f_s!=None and f_o!=None and v_o!=None:
    v_s=(((f_o/f_s)/(c+v_o))**-1)-c
#prints stuff
print(f_s)
print(f_o)
print(v_s)
print(v_o)

#prints info on the frequencies
if f_o>(7.5*10**14):
    print("the observer will experience ultraviolet radiation/no visible light")
if f_s>(7.5*10**14):
     print("the source emits ultraviolet radiation/no visible light")
if f_o<(4.3*10**14):
    print("the observer will experience infrared radiation/no visible light")
if f_s<(4.3*10**14):
     print("the source emits infrared radiation/no visible light")
else:
    print("one or both are or is in the visible spectrum")
