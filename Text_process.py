# 导入包
# encoding=utf-8
import jieba.analyse  # 导入结巴分词包


# 将pdf文件转化为txt文件。输入:pdf文件，得到txt文件
def Pdf_to_txt():
    pass

# 清理txt文本语料。输入：txt文本，得到只有中字符和句中标点符号的txt文档
def clearn_txt():
    pass


# 输入清理后的文本文件，对中文句子分词，并去除停顿词，其中停顿词和标点符号,输出分好词的txt
def word_segment():

    with open('stopword.txt', 'r') as f:
        stopwords = f.read()  # 打开stopword（停用词）文件
    with open('words_initial.txt', 'r') as f:
        w = f.read()  # 读取要分词的文件
        seg = jieba.cut_for_search(w)  # 进行分词
        final = []  # 设置一个变量
        for seg_list in seg:
            if seg_list not in stopwords:
                final.append(seg_list)  # 对第一次分词的结果进行处理，去掉停用词
    seg_final = " ".join(final)  # 用空格符号分隔词语



def main():
    pass

if __name__ == '__main__':
    main()