# 安装pdfminer包：https://pypi.python.org/pypi/pdfminer3k 进入pdfminer3k-1.3.1文件下的命令窗口，输入python setup.py install
# 导入包
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io,os,re

# 将pdf文件转化为txt文件。输入:pdf文件夹，得到txt文件output.txt
def pdf_to_txt(filelist):
    codec = 'utf-8'
    mylist=dict.fromkeys(['title', 'year'], ('unknow'))
    with open (filelist,'r') as f:
        i=f.read()
        files = os.listdir(fileDir)
        p1 = re.compile(r'(?<=%T ).+(?=' ')')#%T开头的字符串表示标题
        p2 = re.compile(r'(?<=%D ).+(?=' ')')#%D开头的字符串表示时间
        title=re.findall(p1,i)
        year=re.findall(p2,i)
        Dict=dict(zip(title,year))
        print(Dict)
        j=1
    for i in Dict.keys():
        #根据key值找文件
        filePath='test\\files1\\'+i+'.pdf'
        if os.path.exists(filePath):
          manager = PDFResourceManager()
          output = io.StringIO()
          converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
          interpreter = PDFPageInterpreter(manager, converter)
          f = open(outfile, 'a+b')
          with open(filePath, 'rb') as infile:
               content = []  # 定义一个数组变量用于暂存数据i
               content.append('###'+i+'$'+Dict[i] +'$'+'###')#将标题用##符号包围起来
               for page in PDFPage.get_pages(infile, check_extractable=True):
                   interpreter.process_page(page)
                   convertedPDF = output.getvalue()
               print(convertedPDF)
            # python3编码转换新方法“wb”,encode():http://pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/
               content.append(convertedPDF)

          with open('%s' % (outfile), 'wb') as f:
             f.write(''.join(content).encode())
             print("-----------------------------------完成文章"+str(j)+"的pdf转化--------------------------------------")
             j=j+1
          output.close()
          converter.close()
          f.close()
        else:
            continue
    print("-----------------------------------完成pdf转化至txt--------------------------------------")
    return 0

# 清理txt文本语料。输入：txt文本，得到只有中字符和句中标点符号的txt文档
def clean_txt(outfile):
    with open(outfile, 'rb')as f:
        content = f.read().decode('utf-8')
    # p定义了要挑选出的内容，其中\u4e00-\u9fff为中文字符的Unicode编码区间，\u3002\uFF0C分别表示句号与逗号
    p = re.compile(r'(?<=##)\S.+(?=##)|[\u4e00-\u9fff+\u3002\uFF0C]')
    # x将找出的符合条件的内容列表连接在一起输出
    x = ''.join(re.findall(p, content))
    # 删除x中连续出现的重复内容，这里对逗号,句号，加号进行了处理
    final_result = re.sub(u"[\uFF0C|\u3002|\u002B]{2,}", "", x)
    with open(cleaned_file, "w")as outfile:
        outfile.write(final_result)
    print(final_result)
    print("-----------------------------------------完成txt清洗-------------------------------------")
    return 0

# # 输入清理后的文本文件，对中文句子分词，并去除停顿词，其中停顿词和标点符号,输出分好词的txt
# def word_segment():
#
#     pass
#
# def main():
#     pass
#
# if __name__ == '__main__':
#     main()


fileDir = u'test\\files1'
filelist=u'test\\filelist1.txt'
outfile = "test\output.txt"
cleaned_file = "test\\txt_cleaned.txt"
pdf_to_txt(filelist)
clean_txt(outfile)