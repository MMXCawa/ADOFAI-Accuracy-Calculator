import easygui as eg
# 精准=(完美+稍快+稍慢) / (所有点击方块数+按太慢失败次数+按太快失败次数) + 完美次数*0.0001
# x精准=((完美*1+(稍快+稍慢)*0.75+(太快+太慢)*0.4+(按太快)*0.2)/(所有点击的方块数))*(0.9875^检查点使用次数)
infomation=eg.multenterbox('请输入详细结果','Accuracy Calculator',('按太快','提前','太快','稍快','完美','稍慢','太慢','错过','已用检查点'))
for i in range(len(infomation)):
    if infomation[i]=='':
        infomation[i]=0
    infomation[i]=int(infomation[i])
print(infomation)
Overload,Tooearly,Early,EPerfect,Perfect,LPerfect,Late,Miss,Checkpoints=infomation
Accuracy=(Perfect+LPerfect+EPerfect) / (sum(infomation)-Checkpoints) + Perfect*0.0001
X_Accuracy=((Perfect+(LPerfect+EPerfect)*0.75+(Early+Late)*0.4+(Tooearly)*0.2)/(sum(infomation)-Checkpoints))*(0.9875**Checkpoints)
eg.msgbox('精准度:{}/{}\nX-精准度:{}/100.0%'.format(str(Accuracy*100)+'%',str(100+(sum(infomation)-Checkpoints-Overload-Tooearly-Miss)*.01)+'%',str(X_Accuracy*100)+'%'),'Accuracy Calculator','Finish')