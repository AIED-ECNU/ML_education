import os,re
import jieba.analyse
import logging
from gensim.models import word2vec

#txt文本清洗
def clean_txt(infile,cleaned_file):

    with open(infile, 'rb')as f:
        content = f.read().decode('utf-8')
    # print(content)
    # p定义了要挑选出的内容，其中\u4e00-\u9fff为中文字符的Unicode编码区间，\u3002\uFF0C分别表示句号与逗号
    p = re.compile(u"[\u4e00-\u9fff+\u3002\uFF0C]")
    # x将找出的符合条件的内容列表连接在一起输出
    x = ''.join(re.findall(p, content))
    # 删除x中连续出现的重复内容，这里对逗号进行了处理
    final_result = re.sub(u"[\uFF0C]{2,}", "", x)
    with open(cleaned_file, "w")as outfile:
        outfile.write(final_result)
    print("-完成txt清洗--")
    return 0


# # 输入清理后的文本文件，进行分词，并去除停用词，输出分好词的文本。
def word_segment(cleaned_file,train_data):
    with open('stop.txt', 'r') as f:
        stopwords = f.read()  # 打开stopword（停用词）文件
    with open(cleaned_file, 'r') as f:
        w = f.read()  # 读取要分词的文件
        seg = jieba.cut_for_search(w)  # 进行分词
        final = []  # 设置一个变量
        for seg_list in seg:
            if seg_list not in stopwords:
                final.append(seg_list)  # 对第一次分词的结果进行处理，去掉停用词
    seg_final = " ".join(final)  # 用空格符号分隔词语,得到最终分词结果
    with open(train_data,'w') as fr:
        fr.write(seg_final)
    print("--完成分词--")

#word2vec模型训练
def word2vec_tarin(train_data,model_file):
    current_dir = os.path.dirname(__file__)
    logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO)

    sentences = word2vec.LineSentence(os.path.join(current_dir, train_data))
    # 创建训练模型
    model = word2vec.Word2Vec(size=200, window=6, min_count=5, workers=10)
    model.build_vocab(sentences)
    #迭代训练，windows环境下可不用参数：total_examples=model.corpus_count, epochs=model.iter
    for i in range(7):
        model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
    model.save(os.path.join(current_dir, model_file))


def main():

    infile = "input.txt" #输入未被清洗过的txt
    cleaned_file = 'clean.txt' #清洗完的txt
    train_data='train.txt' #去除停用词的训练及分词后的txt
    model_file='train.model'#保存训练好的模型文件
    clean_txt(infile,cleaned_file)
    word_segment(cleaned_file,train_data)
    word2vec_tarin(train_data,model_file)

if __name__ == '__main__':
    main()


