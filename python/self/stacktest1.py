def stackin(stk, zz, ele):
    stk.append(ele)
    zz += 1
    return stk, zz


def stackout(stk, zz):
    tmp = stk.pop(zz)
    zz -= 1
    return stk, zz, tmp


zzf, zzb = -1, 1
fw, bw, p = [], [1, 2], [3]
chs = "EOF"
page = p[0]
while chs != "q":
    print("-"*79)
    print("forward="+str(fw), "backward="+str(bw), "page="+str(p))
    if len(fw) == 0:
        print("无法前进!")
    if len(bw) == 0:
        print("无法后退!")
    chs = input("选择参数:\nf:前进;b:后退;q:关闭\n请选择:")
    if chs == "f":
        bw, zzb = stackin(bw, zzb, p[0])
        fw, zza, tmp = stackout(fw, zzf)
        p[0] = tmp
    elif chs == "b":
        bw, zzb, tmp = stackout(bw, zzb)
        fw, zza = stackin(fw, zzf, p[0])
        p[0] = tmp
