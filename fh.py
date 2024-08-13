import random,easygui
# 定义词汇列表
nouns = ["挖掘机", "意大利面", "原神", "太阳", "月亮", "风", "雨", "梦想", "现实", "电脑"]
adjectives = ["扭曲的", "神秘的", "快乐的", "悲伤的", "明亮的", "黑暗的", "复杂的", "简单的", "快速的", "缓慢的"]
verbs = ["取决于", "影响", "改变", "增加", "减少", "创造", "毁灭", "理解", "忽视", "接受"]

# 生成一句废话
def fh():
    return random.choice(verbs)+random.choice(adjectives)+random.choice(nouns)
wwww=easygui.enterbox("输入文件名 ")
x=open(wwww+".txt",'a')
a=0
while True:
    cmd=easygui.buttonbox("文件保存为"+wwww+".txt",choices=["保存废话并退出","续写废话","查看废话","114514"])
    if cmd=="保存废话并退出":
        x.write=random.choice(adjectives)+random.choice(verbs)
        break
    if cmd=="114514":
        if a<5:
            a+=1
        elif a>10:
            easygui.enterbox("哼哼哼"+'啊'*(a-11))
            a+=1
        else:
            easygui.msgbox("你已近点了",a,"次了，不要再点了啊")
            a+=1

    if cmd=="续写废话":
        easygui.msgbox(o:=fh())
        x.write(o)
    if cmd=="查看废话":
        x=open(wwww+".txt",'r')
        easygui.msgbox(o:=x.read())
        x=open(wwww+".txt",'a')
     