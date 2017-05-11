# 安装pdfminer包：进入pdfminer3k-1.3.1文件下的命令窗口，输入python setup.py install
# 导入包
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io,os,re

# 将pdf文件转化为txt文件。输入:pdf文件夹，得到txt文件output.txt
def Pdf_to_txt(fileDir):
    codec = 'utf-8'
    outfile="output.txt"
    files = os.listdir(fileDir)
    print (files)
    for file in files:
        manager = PDFResourceManager()
        output = io.StringIO()
        converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)
        filePath = fileDir + '\\' + file
        infile = open(filePath, 'rb')
        for page in PDFPage.get_pages(infile, check_extractable=True):
           interpreter.process_page(page)
           convertedPDF = output.getvalue()
        print(convertedPDF)
        with open('%s' % (outfile), 'a+b') as f:
            f.write((os.path.basename(file)+convertedPDF).encode())#python3编码转换新方法“wb”,encode():http://pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/
        infile.close()
        output.close()
        converter.close()
    print("Saved")
    return 0

# 清理txt文本语料。输入：txt文本，得到只有中字符和句中标点符号的txt文档
def clearn_txt():
    pass


# 输入清理后的文本文件，对中文句子分词，并去除停顿词，其中停顿词和标点符号,输出分好词的txt
def word_segment():

    pass

def main():
    pass

if __name__ == '__main__':
    main()
