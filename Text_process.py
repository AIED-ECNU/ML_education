# 导入包
# encoding=utf-8
import jieba


# 将pdf文件转化为txt文件。输入:pdf文件，得到txt文件
def Pdf_to_txt():
    pass

# 清理txt文本语料。输入：txt文本，得到只有中字符和句中标点符号的txt文档
def clearn_txt():
    pass


# 输入清理后的文本文件，对中文句子分词，并去除停顿词，其中停顿词和标点符号,输出分好词的txt
def word_segment():

    seg_list = jieba.cut("戴尔公司将于５月１８日公布第一季度的财报。", cut_all=True)
    print("Full Mode:", "/ ".join(seg_list))  # 全模式
    seg_list = jieba.cut("我来到u北京清华大学", cut_all=False)
    print("Default Mode:", "/ ".join(seg_list))  # 精确模式
    seg_list = jieba.cut("戴尔公司将于５月１８日公布第一季度的财报。")  # 默认是精确模式
    print(", ".join(seg_list))
    seg_list = jieba.cut_for_search("你们好，市场竞争我是涂斌琴")  # 搜索引擎模式
    print(", ".join(seg_list))

    pass

def main():
    pass

if __name__ == '__main__':
    main()