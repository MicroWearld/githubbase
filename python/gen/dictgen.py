#python D:\IT\python\gen\dictgen.py
de=0
def main():
    global de
    key,data,dicti="key.txt","data.txt","dict.txt"
    #key file,data file and dict file
    dic={}
    print("dictionary generator v0.2")
    print("option:\nplease write down the key and the data in file(remember to change line!)")
    print("default key file is "+key)
    print("default data file is "+data)
    print("default dict file is "+dicti)
    print("mod:")
    print("1:all is string;2:key is number;3:data is number;4:all is number")
    print("-"*79)
    k=int(input("choose:"))
    #print("-"*79)
    f1=open(data,"r")
    f2=open(key,"r")
    f3=open(dicti,"w")
    a=f1.readline().strip()
    b=f2.readline().strip()
    if k>4 or k<0:
        print("mode error,restart!")
        print("-"*79)
        main()
    else:
        while a!="" or b!="":
            if k==1:
                dict={b:a}
            elif k==2:
                dict={int(b):a}
            elif k==3:
                dict={b:int(a)}
            elif k==4:
                dict={int(b):int(a)}
            dic.update(dict)
            a=f1.readline().strip()
            b=f2.readline().strip()
        print("result:",dic)
        print("generate successfully!")
        f3.write(str(dic))
    f1.close()
    f2.close()
    f3.close()
    if de==0:
        print("-"*79)
        con=input("press any key to exit...")
        de=1

main()
