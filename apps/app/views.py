from apps import models

# 入参：issueid 返回 bool 判断

# 模糊查找函数

#判断获取发布信息中list中update所在位置
def getAllimages ( mylist, lens):
    i = 0
    while i < lens:
        if mylist[i].find("变更说明") == 0:
            return i
            break
        i += 1
    else:
          return -1