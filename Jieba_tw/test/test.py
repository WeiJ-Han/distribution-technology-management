import jieba

jieba.case_sensitive = True

import jieba


seg_list = jieba.cut("我爱北京天安门")
print(" / ".join(seg_list))