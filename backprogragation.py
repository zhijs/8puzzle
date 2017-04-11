#encoding:utf-8
from Node import *
class back:
    def __init__(self,orignate,target,length):
        self.origate=orignate  #初始状态
        self.target=target  #目标状态
        self.ps=[]  #PS表，用于保存当前搜索路径的状态
        self.nps=[] #nps表，用于保存等待搜索的状态
        self.nss=[] #nss表，用于保存不可到达目的地的状态集
        self.spce=[-3,3,-1,1] #上下左右四个移动方向
        self.length=length
        self.MaxDegree=8 #深度限制，到达此深度回溯

    def issolve(self): #判断到目标状态是否有解
        targetVer=self.getreVersNum(self.target.state)
        orinateVer=self.getreVersNum(self.origate.state)
        if(targetVer%2!=orinateVer%2):
            return False
        else:
            return True



    def getreVersNum(self,state):  #获取逆序数
        sum=0
        for i in range(0,len(state)):
            if(state[i]==0):
                continue
            else:
                for j in range(0,i):
                    if(state[j]>state[i]):
                        sum+=1

        return sum

    # def getspaceIndex(self): #获得空格所在的位置
    #     for i in range(len(self.origate)-1):
    #         if(self.origate[i]==0):
    #             return i

    def copyArray(self,state):
        arr=[]
        return arr+state


    #判断状态数码是否存在
    def isexit(self,node,table):
        for i in table:
            if(i.state==node.state):
                return True
        return False




    #主要算法，回溯过程
    def backMainProcess(self):
        self.ps.append(self.origate)
        self.nps.append(self.origate)
        while(len(self.nps)):
            originateState=self.ps[-1]

            spacIndex=originateState.state.index(0)
            if(originateState.state==self.target.state):
                return True
            else:

                #到达指定深度，回溯
                if(originateState.degree>=self.MaxDegree):


                    self.ps.pop()
                    self.nps.pop()
                    if(self.nps[-1]!=self.ps[-1]):

                      self.ps.append(self.nps[-1])
                    self.nss.insert(0,originateState)
                    continue
                flag=False
                for i in range(len(self.spce)):

                    if((i==0 and (spacIndex+self.spce[i])>=0) or
                    (i==1 and (spacIndex+self.spce[i])<len(self.target.state)-1)
                    or(i==2 and (spacIndex%self.length!=0 )) or
                    (i==3 and ((spacIndex+1)%self.length)!=0)):
                        state=self.copyArray(originateState.state)
                        #扩展状态
                        temp=state[spacIndex+self.spce[i]]
                        state[spacIndex+self.spce[i]]=0
                        state[spacIndex]=temp
                        #判断新的状态是否已经存在
                        nodeState=Node(state,originateState.degree+1)

                        if(self.isexit(nodeState,self.nps))or (self.isexit(nodeState,self.nss)):
                            continue
                        else:
                            flag=True

                            self.nps.append(nodeState)
                if(not flag):

                    self.ps.pop()
                    self.nps.pop()
                    if(self.nps[-1]!=self.ps[-1]):
                      self.ps.append(self.nps[-1])
                    self.nss.append(originateState)
                if(flag):#展开有子节点
                    self.ps.append(self.nps[-1])
    #输出结果路径
    def showLine(self):
        for node in self.ps:
            i=0
            print(node.state[i],node.state[i+1],node.state[i+2])
            print(node.state[i+3],node.state[i+4],node.state[i+5])
            print(node.state[i+6],node.state[i+7],node.state[i+8])
            print('->:')








if __name__ == '__main__':


    originate=[2,8,3,1,6,4,7,0,5]
    target=[1,2,3,8,0,4,7,6,5]
    node1=Node(originate,0)
    node2=Node(target,0)
    c=back(node1,node2,3)
    if(c.issolve()):
        if(c.backMainProcess()):
            print('已找到解！！！！,路径如下')
            c.showLine()
    else:
        print('此过程无解')











