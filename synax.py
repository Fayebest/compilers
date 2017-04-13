# -*- coding:utf-8 -*-
class synax():
    def __init__(self):
        self.gramm =[]
        self.clos = []
        self.filename = "E:\complier\synax.txt"
        self.first = {}


    def getgramma(self):
        with open(self.filename) as f:
            content = f.read()
        getsum = sum(map(lambda x: len(x.split("|")),content.split("\n")))
        self.gramm=[[] for i in range(getsum)]
        i=0
        index =0
        while(i<len(content)):
            if content[i] == '<':
                i+=1
                temp ="1."
                while(content[i]!=">"):
                    temp = temp + content[i]
                    i+=1
                i+=1
                self.gramm[index].append(temp)
            elif content[i:i+2] == '->':
                i+=2
            elif content[i] == "|":
                index +=1
                i+=1
                self.gramm[index].append(self.gramm[index-1][0])
            elif content[i] == "\n":
                index +=1
                i+=1
            elif content[i] == "\"":
                i += 1
                temp = "2."
                while (content[i] != "\""):
                    temp = temp + content[i]
                    i+=1
                i+=1
                self.gramm[index].append(temp)
            elif content[i] == " ":
                i+=1
        print(self.gramm)

    # 求闭包
    def getclosure(self):
        for x in self.gramm:
            x.append(1)
        self.clos.append([self.gramm[0]])
        for i in self.clos:
            for ii in i:
                temp = self.closure(ii)
                if(temp):
                    for temps in temp:
                        if temps not in i:
                            i.append(temps)
            for b in i:
                if b[-1] == len(b)-1:
                    continue
                else:
                    tempb = b[:]
                    tempb[-1] = tempb[-1]+1
                    if self.judgenot(tempb):
                        self.clos.append([tempb])


    def closure(self,arr):
        temp = []
        if arr[-1] == len(arr)-1 or arr[arr[-1]][0] == "2":
            return 0;
        else:
           for x in self.gramm:
               if x[0] == arr[arr[-1]]:
                   temp.append(x)
        return temp

    #判断tt是否为闭包的第一项。是返回0，不是返回1
    def judgenot(self,tt):
        flag =1
        for i in self.clos:
            if tt == i[0]:
                flag = 0
                break;
        return flag


    # 求first集，用字典存储，字典的值为set
    def getfirst(self):
        for x in self.gramm:
            self.first[x[0]] = set()    #初始化first字典
        for key in self.first:
            self.diguifirst(key)

    def diguifirst(self,para):
        temp = []
        for i in self.gramm:
            if i[0] == para:
                temp.append(i)
        for ii in temp:
            self.leftdigui(ii)



    def leftdigui(self,lpara):
        if lpara[1][0] == "1":
            self.diguifirst(lpara[1])
            if("2.ksi" in self.first[lpara[1]]):
                temp = self.first[lpara[1]].copy()
                temp.remove("2.ksi")
                self.first[lpara[0]] = self.first[lpara[0]] | temp
            else:
                self.first[lpara[0]] = self.first[lpara[0]] | self.first[lpara[1]]
        else:
            self.first[lpara[0]].add(lpara[1])
        i=1
        while(i < len(lpara) -1 and (lpara[1][0] == '1')):
            if (lpara[i+1][0] == '1') and ("2.ksi" in self.first[lpara[i]]):                                      #如果下一项为终结符，则直接并入左边的非终结符
                self.diguifirst(lpara[i+1])
                if ("2.ksi" in self.first[lpara[i + 1]]):
                    temp = self.first[lpara[i + 1]].copy()
                    temp.remove("2.ksi")
                    self.first[lpara[0]] = self.first[lpara[0]] | temp
                else:
                    self.first[lpara[0]] = self.first[lpara[0]] | self.first[lpara[i + 1]]
                i += 1
            elif(lpara[i+1][0] == '2'):
                self.first[lpara[0]].add(lpara[i+1])
                break
            else:
                break
        if(i == len(lpara) -1 ) and (lpara[i][0] == "1") and("2.ksi" in self.first[lpara[i]]):
                self.first[lpara[0]].add("2.ksi")







    def printarray(self):
        for key in self.first:
            print key,self.first[key]
if __name__ == "__main__":
    a = synax()
    a.getgramma()
    a.getfirst()
    a.printarray()
