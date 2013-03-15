# -*- coding: utf8 -*-

def throw_z_eggs(n,z):
    P = [[[0 for i in range(n)] for j in range(n)] for k in range(z)];#次数二维数组
    S = [[[0 for i in range(n)] for j in range(n)] for k in range(z)];#解决方案二维数组
   
    for k in range(z):
        for i in range(n):
            for j in range(n):
                if(i==j):
                    P[k][i][j] = 1;
                    S[k][i][j] = i;
                elif( i==j-1):
                    P[k][i][j] = 2
                elif(i<j-1 and k==0):
                    P[k][i][j] = j-i+1;


    for eggs in range(1,z):
        for h  in range(1,n):
            for i in range(n-h):
                j = i + h;
                P[eggs][i][j] = h+1;
                S[eggs][i][j] = j;
                for x in range(i+1,j):
                    a = P[eggs-1][i][x-1]+1;
                    b = P[eggs][x+1][j] +1 ;
                    if(a<b):
                        a = b;
                    if(a<P[eggs][i][j]):#比较所有i =< x < j的最优次数,记录下来
                        P[eggs][i][j] = a;
                        S[eggs][i][j] = x;

    return P,S;


def throw_two_eggs(n):
    P = [[0 for col in range(n)] for row in range(n)];#次数二维数组
    S = [[0 for col in range(n)] for row in range(n)];#解决方案二维数组
    
    #如果只有一层楼,最优解为1
    for i in range(n):
        P[i][i] = 1;
        S[i][i] = i;
    for h  in range(1,n):# h 是楼层的高度,每个循环求楼层i到i+h之间扔鸡蛋次数的最优解P[i,i+h],h表示从i层到i+h层的楼层数(第i层除外,至少两层)
        for i in range(n-h):
            j = i + h;
            P[i][j] = h+1;#最差解为2个鸡蛋,最多要试h+1次,也就是楼层高度
            S[i][j] = j;
            for x in range(i,j):#x为尝试扔鸡蛋的楼层,范围从i到j-1,第j层为顶层从x=j层尝试为最差解也就是h+1
                a = x-i+P[x][x];#如果鸡蛋在第x层碎了,则需要从第i层开始,最多尝试x-i次,加上1也就是在x层尝试的那一次
                b = P[x+1][j] + P[x][x];#如果没有碎,则递归找x+1到顶层j+h的最优解,加上刚刚在x层尝试的那一次
                if(a<b):#两次结果的较小值为在第x层尝试扔鸡蛋的最优解
                    a = b;
                if(a<P[i][j]):#比较所有i =< x < j的最优次数,记录下来
                    P[i][j] = a;
                    S[i][j] = x;

    return P,S;

def print_solution(S):
    n = len(S);
    x = -1;
    while(True):
        next = x+1;
        x = S[next][n-1];
        print "throw from the %d floor"%(x+1);
        if(x==next or x == n-1):
            break;
        
P1,S1 = throw_two_eggs(10);
print_solution(S1);



P2,S2 = throw_z_eggs(10,2);
print_solution(S2[1]);
