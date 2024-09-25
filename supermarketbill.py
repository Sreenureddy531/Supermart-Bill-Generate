from datetime import datetime
print("----------------------Welcome--------------------------")
name=input("Enter your name:")
lists='''

Rice    Rs 60/kg
sugar   Rs 40/kg
salt    Rs 20/kg
oil     Rs 65/liter
maggi   Rs 10/each
biscuit Rs 40/each
powder  Rs 55/each
brush   Rs 12/each

'''
price=0
totalprice=0
finalprice=0
pricelist=[]
ilist=[]
qlist=[]
plist=[]
items={"Rice":20,
       "sugar":40,
       "salt":20,
       "oil":65,
       "maggi":10,
       "biscuit":40,
       "powder":55,
       "brush":12}
option=int(input("for in the list of items press1:"))
if option==1:
    print(lists)
    for i in range  (len(items)):
        inp1=int(input("if you want to buy press 1 or 2 for exist:"))
        if inp1==2:
            break
        if inp1==1:
            item=input("Enter your items:")
            quantity=int(input("enter quatity:"))
            if item in items.keys():
                price=quantity*(items[item])
                pricelist.append((item,quantity,items,price))
                totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst=(totalprice*5)/100
                finalamount=gst+totalprice
            else:
                print("your item is not available")
        else:
            print("you entered wrong number")
        inp=input("can i  bill items yes or no:")
        if inp=='yes':
            pass
            if finalamount!=0:
                print(25*"=", "SREENU SUPERMARKET" ,25*"=")
                print(28*" ","GUDUR")
                print("name:",name,30*" ",datetime.now())
                print(75*"-")
                print("s.no",8*'','item',8*"",'quantity',3*" ",'price')
                for i in range(len(pricelist)):
                    print(i,8*'',5*'',ilist[i],10*'',qlist[i],10*" ",plist[i])
                    print(75*"-")
                    print(50*" ","totalamount:","Rs",totalprice)
                    print("gst amount",40*" ",'Gst Rs',gst)
                    print(75*"-")
                    print(50*" ",'finalamount:','Rs',finalamount)
                    print(75*"-")
                    print(50*" ","thanks for visiting")
                    print(75*"-")