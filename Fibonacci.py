
#剑指第7题
#大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
#n<=39
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0 or n==1:
            return n
        elif n == 2:
            return 1
        else:
            listf=[]
            listf=[0,1,1]
            for i in range(3,n+1):
                listf.append(listf[i-1]+listf[i-2])
            return listf[n]

solution=Solution()
n=solution.Fibonacci(5)
print(n)

#调试成功！