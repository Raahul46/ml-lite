class vehicle:

    def __init__(self,vehicletype,vehicleid):
        self.vechicletype=vehicletype
        self.vechicleid=vehicleid
        self.lot=0


    def allot(self,numV,dict,v,list1):


        if (self.vechicletype == "big"):
            if list1[v]>16 :
                dict[self.vechicleid] = list1[v]
                list1.remove(list1[v])

            else:
                print("PARKING FULL BUDDY :(")
                print(dict)

        elif (self.vechicletype == "medium"):
            if list1[v] <=17 and list1[v] > 10:
                dict[self.vechicleid] = list1[v]
                list1.remove(list1[v])

            else:
                print("PARKING FULL BUDDY :(")
                print(dict)

        elif (self.vechicletype == "small"):
            if list1[v] <= 10 and list1[v] >= 1:
                dict[self.vechicleid] = list1[v]
                list1.remove(list1[v])
            else:
                print("PARKING FULL BUDDY :(")
                print(dict)
        v-=1
        return v

def main():
    smallv=9
    midv=16
    maxv=19
    str="y"
    id=0
    type=" "
    numV=0
    dict={}
    list1 = [x for x in range(1, 21)]
    print("ENTER THE VEHICLE DETAILS:")
    print("PROGRAM WILL TAKE 20 INPUTS OF VEHICLE TYPE(small,medium,big) AND VEHICLE ID(INT)")
    while str=="y" and numV < 20:
        type=input("VEHICLE TYPE:")
        id=int(input("VEHICLE ID:"))
        tick=vehicle(type,id)
        if(type=="small"):
           smallv=tick.allot(numV,dict,smallv,list1)
           numV += 1
        if (type == "medium"):
            midv = tick.allot(numV, dict, midv,list1)
            numV += 1
        if (type == "big"):
            maxv = tick.allot(numV, dict, maxv,list1)
            numV += 1

    x1 = sorted(dict.keys())

    for num in x1:
        print("vehicle ID:",num ," ","position@",dict[num])

if __name__ == '__main__':
    main()
