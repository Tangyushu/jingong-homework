# In[3]:
#医务工作者经过广泛的调查和统计分析, 给出了如下”体重指数”判断体型的方法:
    #设: 体重指数 t, 体重 w (单位:公斤), 身高 h (单位:米)
    #t = w / h2 
    #t < 18, 为低体重;
    #18 ≤ t ≤ 25, 为正常体重;
    #25 < t ≤ 27, 为超重体重;
     #t > 27, 为肥胖.

w=float(input('请输入你的体重：'))
h=float(input('请输入你的身高：'))
t=w/(h*h)
if t < 18:
    print("低体重")
elif 18<=t<=25:
    print("正常体重")
elif 25<t<=27:
    print('超重体重')
else:
    print('肥胖')
    