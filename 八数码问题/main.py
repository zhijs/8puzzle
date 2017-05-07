from Node import *
from depth_first import *
from breadth_first import *
import time

if __name__=='__main__':
    #深度优先算法
    originate=[2,8,3,1,6,4,7,0,5]
    target=[1,2,3,7,8,4,0,6,5]
    node1=Node(None,originate,0)
    node2=Node(None,target,0)
    depth=degth_search(node1,node2,10,3)
    breadth=breadth_search(node1,node2,10,3)
    Now_d=time.time()
    flag_d=depth.search()
    end_d=time.time()
    Now_b=time.time()
    flag_b=breadth.search()
    end_b=time.time()
    cost_d=end_d-Now_d
    cost_b=end_b-Now_b
    if(flag_d):
        print('深度优先算法:已经找到路径')
        depth.showLine()
        print('深度优先算法共用时%f秒\n\n' %(cost_d))
    else:
        print('未找到路径')

    if(flag_d):
        print('广度优先算法:已经找到路径')
        breadth.showLine()
        print('广度优先算法共用时%f秒' %(cost_b))
    else:
        print('未找到路径')
