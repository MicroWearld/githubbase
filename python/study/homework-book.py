print('''
1.milk[count:3;price:8]
2.drink[count:5;price:6]
3.water[count:2;price:5]
''')

food={1:[3,8],2:[5,6],3:[2,5]}
id=int(input('id:'))
num=int(input('count:'))
pay=int(input('pay:'))
if id>=1 and id<=3:
    if num<=food[id][0]:
        money=num*food[id][1]
        if money>pay:
            print("error")
        else:
            ret=pay-money
            print("right,{}".format(ret))
    else:
        print("error")
else:
    print("error")
          
