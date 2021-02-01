from collections import OrderedDict
word=OrderedDict()
word['title']='大写单词的首字母'
word['gor']='循环'
word['if']='条件'
word['print']='打印'
word['del']='删除'
word['set']='列出不重复的项'
word['sort']='排序'
word['#']='注释'
word['append']='在列表后添加元素'
word['upper']='将元素首字母大写'
for words,mean in word.items():
    print(words + ": " + mean)
