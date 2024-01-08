from flask import Flask, render_template
from wordcloud import WordCloud  # ImageColorGenerator
from collections import Counter
import jieba
#  from PIL import Image
# import imageio
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)


def data_manage1():  # 数据处理
    df = pd.read_csv('./北京240.csv')
    df['薪资min'] = df['薪资'].str.extract('(\\d+)')  # 提取最小值
    df['薪资max'] = df['薪资'].str.extract('(\\d+)K')  # 提取最大值
    df['薪资min'].fillna(0, inplace=True)  # 填充0
    df['薪资max'].fillna(0, inplace=True)  # 填充0
    print('Done')
    df.to_csv('北京1.csv', encoding="utf_8_sig")

    df1 = pd.read_csv('./北京1.csv')

    # 最低薪资
    df1 = df1[df1['薪资min'] <= 60]
    dfm1 = df1['薪资min'].value_counts(ascending=True)
    dfm1.to_csv('./薪资排序1.csv', encoding="utf_8_sig")
    map1 = pd.read_csv('./薪资排序1.csv')
    map1.sort_values(by='count', inplace=True, ascending=True)
    plt.bar(map1['薪资min'], map1['count'], color='blue')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.title('北京底薪分布情况')
    plt.xlabel('薪资/K')
    plt.ylabel('频数/人')
    plt.xticks(range(0, 80, 4))
    # plt.tight_layout()
    plt.savefig('./static/最低薪资1.png', dpi=1000)

    # 最高薪资
    df2 = df1[df1['薪资max'] <= 90]
    dfm2 = df2['薪资max'].value_counts(ascending=True)
    dfm2.to_csv('./薪资排序1.csv', encoding="utf_8_sig")
    map2 = pd.read_csv('./薪资排序1.csv')
    map2.sort_values(by='count', inplace=True, ascending=True)
    plt.bar(map2['薪资max'], map2['count'], color='blue')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('北京高薪分布情况')
    plt.xlabel('薪资/K')
    plt.ylabel('频数/人')
    plt.xticks(range(0, 90, 4))
    # plt.tight_layout()
    plt.savefig('./static/最高薪资1.png', dpi=1000)
    plt.close()


def data_manage2():  # 数据处理
    df = pd.read_csv('./上海300.csv')
    df['薪资min'] = df['薪资'].str.extract('(\\d+)')  # 提取最小值
    df['薪资max'] = df['薪资'].str.extract('(\\d+)K')  # 提取最大值
    df['薪资min'].fillna(0, inplace=True)  # 填充0
    df['薪资max'].fillna(0, inplace=True)  # 填充0
    print('Done')
    df.to_csv('上海1.csv', encoding="utf_8_sig")

    df1 = pd.read_csv('./上海1.csv')

    # 最低薪资
    df1 = df1[df1['薪资min'] <= 60]
    dfm1 = df1['薪资min'].value_counts(ascending=True)
    dfm1.to_csv('./薪资排序2.csv', encoding="utf_8_sig")
    map1 = pd.read_csv('./薪资排序2.csv')
    map1.sort_values(by='count', inplace=True, ascending=True)
    plt.bar(map1['薪资min'], map1['count'], color='blue')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.title('上海底薪分布情况')
    plt.xlabel('薪资/K')
    plt.ylabel('频数/人')
    plt.xticks(range(0, 80, 4))
    # plt.tight_layout()
    plt.savefig('./static/最低薪资2.png', dpi=1000)

    # 最高薪资
    df2 = df1[df1['薪资max'] <= 90]
    dfm2 = df2['薪资max'].value_counts(ascending=True)
    dfm2.to_csv('./薪资排序2.csv', encoding="utf_8_sig")
    map2 = pd.read_csv('./薪资排序2.csv')
    map2.sort_values(by='count', inplace=True, ascending=True)
    plt.bar(map2['薪资max'], map2['count'], color='blue')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('上海高薪分布情况')
    plt.xlabel('薪资/K')
    plt.ylabel('频数/人')
    plt.xticks(range(0, 90, 4))
    # plt.tight_layout()
    plt.savefig('./static/最高薪资2.png', dpi=1000)
    plt.close()


def data_manage3():  # 数据处理
    df = pd.read_csv('./广州300.csv')
    df['薪资min'] = df['薪资'].str.extract('(\\d+)')  # 提取最小值
    df['薪资max'] = df['薪资'].str.extract('(\\d+)K')  # 提取最大值
    df['薪资min'].fillna(0, inplace=True)  # 填充0
    df['薪资max'].fillna(0, inplace=True)  # 填充0
    print('Done')
    df.to_csv('广州1.csv', encoding="utf_8_sig")

    df1 = pd.read_csv('./广州1.csv')

    # 最低薪资
    df1 = df1[df1['薪资min'] <= 60]
    dfm1 = df1['薪资min'].value_counts(ascending=True)
    dfm1.to_csv('./薪资排序3.csv', encoding="utf_8_sig")
    map1 = pd.read_csv('./薪资排序3.csv')
    map1.sort_values(by='count', inplace=True, ascending=True)
    plt.bar(map1['薪资min'], map1['count'], color='blue')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.title('广州底薪分布情况')
    plt.xlabel('薪资/K')
    plt.ylabel('频数/人')
    plt.xticks(range(0, 80, 4))
    # plt.tight_layout()
    plt.savefig('./static/最低薪资3.png', dpi=1000)

    # 最高薪资
    df2 = df1[df1['薪资max'] <= 90]
    dfm2 = df2['薪资max'].value_counts(ascending=True)
    dfm2.to_csv('./薪资排序3.csv', encoding="utf_8_sig")
    map2 = pd.read_csv('./薪资排序3.csv')
    map2.sort_values(by='count', inplace=True, ascending=True)
    plt.bar(map2['薪资max'], map2['count'], color='blue')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('广州高薪分布情况')
    plt.xlabel('薪资/K')
    plt.ylabel('频数/人')
    plt.xticks(range(0, 90, 4))
    # plt.tight_layout()
    plt.savefig('./static/最高薪资3.png', dpi=1000)
    plt.close()


def data_manage4():   # 数据处理
    df = pd.read_csv('./深圳300.csv')
    df['薪资min'] = df['薪资'].str.extract('(\\d+)')  # 提取最小值
    df['薪资max'] = df['薪资'].str.extract('(\\d+)K')  # 提取最大值
    df['薪资min'].fillna(0, inplace=True)  # 填充0
    df['薪资max'].fillna(0, inplace=True)  # 填充0
    print('Done')
    df.to_csv('深圳1.csv', encoding="utf_8_sig")

    df1 = pd.read_csv('./深圳1.csv')

    # 最低薪资
    df1 = df1[df1['薪资min'] <= 60]
    dfm1 = df1['薪资min'].value_counts(ascending=True)
    dfm1.to_csv('./薪资排序4.csv', encoding="utf_8_sig")
    map1 = pd.read_csv('./薪资排序4.csv')
    map1.sort_values(by='count', inplace=True, ascending=True)
    plt.bar(map1['薪资min'], map1['count'], color='blue')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.title('深圳底薪分布情况')
    plt.xlabel('薪资/K')
    plt.ylabel('频数/人')
    plt.xticks(range(0, 80, 4))
    # plt.tight_layout()
    plt.savefig('./static/最低薪资4.png', dpi=1000)

    # 最高薪资
    df2 = df1[df1['薪资max'] <= 90]
    dfm2 = df2['薪资max'].value_counts(ascending=True)
    dfm2.to_csv('./薪资排序4.csv', encoding="utf_8_sig")
    map2 = pd.read_csv('./薪资排序4.csv')
    map2.sort_values(by='count', inplace=True, ascending=True)
    plt.bar(map2['薪资max'], map2['count'], color='blue')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('深圳高薪分布情况')
    plt.xlabel('薪资/K')
    plt.ylabel('频数/人')
    plt.xticks(range(0, 90, 4))
    # plt.tight_layout()
    plt.savefig('./static/最高薪资4.png', dpi=1000)
    plt.close()


def data_manage5():  # 数据处理
    df = pd.read_csv('./杭州300.csv')
    df['薪资min'] = df['薪资'].str.extract('(\\d+)')  # 提取最小值
    df['薪资max'] = df['薪资'].str.extract('(\\d+)K')  # 提取最大值
    df['薪资min'].fillna(0, inplace=True)  # 填充0
    df['薪资max'].fillna(0, inplace=True)  # 填充0
    print('Done')
    df.to_csv('杭州1.csv', encoding="utf_8_sig")

    df1 = pd.read_csv('./杭州1.csv')
    
    # 最低薪资
    df1 = df1[df1['薪资min'] <= 50]
    dfm1 = df1['薪资min'].value_counts(ascending=True)
    dfm1.to_csv('./薪资排序5.csv', encoding="utf_8_sig")
    map1 = pd.read_csv('./薪资排序5.csv')
    map1.sort_values(by='count', inplace=True, ascending=True)
    plt.bar(map1['薪资min'], map1['count'], color='blue')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.title('杭州底薪分布情况')
    plt.xlabel('薪资/K')
    plt.ylabel('频数/人')
    plt.xticks(range(0, 50, 2))
    # plt.tight_layout()
    plt.savefig('./static/最低薪资5.png', dpi=1000)

    # 最高薪资
    df2 = df1[df1['薪资max'] <= 80]
    dfm2 = df2['薪资max'].value_counts(ascending=True)
    dfm2.to_csv('./薪资排序5.csv', encoding="utf_8_sig")
    map2 = pd.read_csv('./薪资排序5.csv')
    map2.sort_values(by='count', inplace=True, ascending=True)
    plt.bar(map2['薪资max'], map2['count'], color='blue')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('杭州高薪分布情况')
    plt.xlabel('薪资/K')
    plt.ylabel('频数/人')
    plt.xticks(range(0, 80, 4))
    # plt.tight_layout()
    plt.savefig('./static/最高薪资5.png', dpi=1000)
    plt.close()


def data_fix1():
    df = pd.read_csv('./北京240.csv', encoding="utf_8_sig")
    df['经验1'] = df['经验要求'].str[:5]
    df.to_csv('经验1.csv', encoding="utf_8_sig")

    df1 = pd.read_csv('./经验1.csv', encoding="utf_8_sig")
    dfj = df1['经验1'].value_counts()
    dfj.to_csv('./经验1.csv', encoding="utf_8_sig")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    dfj2 = pd.read_csv('./经验1.csv', encoding="utf_8_sig")
    plt.bar(dfj2['经验1'], dfj2['count'], color='blue', width=0.7)
    plt.xlabel('经验要求')
    plt.ylabel('频数/人')
    plt.title('北京经验要求分布')
    plt.xticks(fontsize=6)
    plt.savefig('./static/经验1.png', dpi=1000)
    plt.close()


def data_fix2():
    df = pd.read_csv('./上海300.csv', encoding="utf_8_sig")
    df['经验2'] = df['经验要求'].str[:5]
    df.to_csv('经验2.csv', encoding="utf_8_sig")

    df1 = pd.read_csv('./经验2.csv', encoding="utf_8_sig")
    dfj = df1['经验2'].value_counts()
    dfj.to_csv('./经验2.csv', encoding="utf_8_sig")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    dfj2 = pd.read_csv('./经验2.csv', encoding="utf_8_sig")
    plt.bar(dfj2['经验2'], dfj2['count'], color='blue', width=0.7)
    plt.xlabel('经验要求')
    plt.ylabel('频数/人')
    plt.title('上海经验要求分布')
    plt.xticks(fontsize=6)
    plt.savefig('./static/经验2.png', dpi=1000)
    plt.close()


def data_fix3():
    df = pd.read_csv('./广州300.csv', encoding="utf_8_sig")
    df['经验3'] = df['经验要求'].str[:5]
    df.to_csv('经验3.csv', encoding="utf_8_sig")

    df1 = pd.read_csv('./经验3.csv', encoding="utf_8_sig")
    dfj = df1['经验3'].value_counts()
    dfj.to_csv('./经验3.csv', encoding="utf_8_sig")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    dfj2 = pd.read_csv('./经验3.csv', encoding="utf_8_sig")
    plt.bar(dfj2['经验3'], dfj2['count'], color='blue', width=0.7)
    plt.xlabel('经验要求')
    plt.ylabel('频数/人')
    plt.title('广州经验要求分布')
    plt.xticks(fontsize=6)
    plt.savefig('./static/经验3.png', dpi=1000)
    plt.close()


def data_fix4():
    df = pd.read_csv('./深圳300.csv', encoding="utf_8_sig")
    df['经验4'] = df['经验要求'].str[:5]
    df.to_csv('经验4.csv', encoding="utf_8_sig")

    df1 = pd.read_csv('./经验4.csv', encoding="utf_8_sig")
    dfj = df1['经验4'].value_counts()
    dfj.to_csv('./经验4.csv', encoding="utf_8_sig")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    dfj2 = pd.read_csv('./经验4.csv', encoding="utf_8_sig")
    plt.bar(dfj2['经验4'], dfj2['count'], color='blue', width=0.7)
    plt.xlabel('经验要求')
    plt.ylabel('频数/人')
    plt.title('深圳经验要求分布')
    plt.xticks(fontsize=6)
    plt.savefig('./static/经验4.png', dpi=1000)
    plt.close()


def data_fix5():
    df = pd.read_csv('./杭州300.csv', encoding="utf_8_sig")
    df['经验5'] = df['经验要求'].str[:5]
    df.to_csv('经验5.csv', encoding="utf_8_sig")

    df1 = pd.read_csv('./经验5.csv', encoding="utf_8_sig")
    dfj = df1['经验5'].value_counts()
    dfj.to_csv('./经验5.csv', encoding="utf_8_sig")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    dfj2 = pd.read_csv('./经验5.csv', encoding="utf_8_sig")
    plt.bar(dfj2['经验5'], dfj2['count'], color='blue', width=0.7)
    plt.xlabel('经验要求')
    plt.ylabel('频数/人')
    plt.title('杭州经验要求分布')
    plt.xticks(fontsize=6)
    plt.savefig('./static/经验5.png', dpi=1000)
    plt.close()


def data_charts1():
    df = pd.read_csv('./北京240.csv')
    df.to_csv('./北京词云.csv', encoding='utf_8_sig')
    df1 = pd.read_csv('./北京词云.csv')

    df1['职位'] = df1['职位'].apply(lambda x: ' '.join(jieba.lcut(x)))  # 分词

    with open('./static/stop_word.txt', encoding='utf_8_sig') as f:
        stop_words = f.read().split('\n')
    df1['职位'] = df1['职位'].apply(lambda x: ''.join([word for word in x.split() if word not in stop_words]))

    words = []
    for comment in df1['职位']:
        words += comment.split()
        word_count = Counter(words).most_common(100)

    word_count = dict(word_count)

    font_path = r'./static/SimHei.ttf'
    wordcloud = WordCloud(width=800, height=600, background_color='white',scale=2,
                          font_path=font_path).generate_from_frequencies(word_count)

    # image_colors = ImageColorGenerator(img_array)
    plt.imshow(wordcloud, interpolation='bilinear')
    # plt.imshow(wordcloud, wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
    plt.axis('off')
    plt.savefig('./static/词云1.png', dpi=1000)
    plt.close()

    # data1 = df.copy()
    # data = df['职位'].str.strip()
    # data1['职位'] = data
    # wcd = WordCloud(font_path="./static/SimHei.ttf").generate()
    # font = r'./static/SimHei.ttf'
    # bg_pic = imageio.imread('./static/th.jpg')
    # wcd = WordCloud(mask=bg_pic, background_color="white", repeat=False, max_words=100, font_path=font)
    # wcd.generate()
    # image_colors = ImageColorGenerator(bg_pic)
    # img = wcd.to_image()
    # img.savefig('./static/词云.jpg')


def data_charts2():
    df = pd.read_csv('./上海300.csv')
    df.to_csv('./上海词云.csv', encoding='utf_8_sig')
    df1 = pd.read_csv('./上海词云.csv')

    df1['职位'] = df1['职位'].apply(lambda x: ' '.join(jieba.lcut(x)))  # 分词

    with open('./static/stop_word.txt', encoding='utf_8_sig') as f:
        stop_words = f.read().split('\n')
    df1['职位'] = df1['职位'].apply(lambda x: ''.join([word for word in x.split() if word not in stop_words]))

    words = []
    for comment in df1['职位']:
        words += comment.split()
        word_count = Counter(words).most_common(100)

    word_count = dict(word_count)

    font_path = r'./static/SimHei.ttf'
    wordcloud = WordCloud(width=800, height=600, background_color='white',scale=2,
                          font_path=font_path).generate_from_frequencies(word_count)

    # image_colors = ImageColorGenerator(img_array)
    plt.imshow(wordcloud, interpolation='bilinear')
    # plt.imshow(wordcloud, wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
    plt.axis('off')
    plt.savefig('./static/词云2.png', dpi=1000)
    plt.close()

def data_charts3():
    df = pd.read_csv('./广州300.csv')
    df.to_csv('./广州词云.csv', encoding='utf_8_sig')
    df1 = pd.read_csv('./广州词云.csv')

    df1['职位'] = df1['职位'].apply(lambda x: ' '.join(jieba.lcut(x)))  # 分词

    with open('./static/stop_word.txt', encoding='utf_8_sig') as f:
        stop_words = f.read().split('\n')
    df1['职位'] = df1['职位'].apply(lambda x: ''.join([word for word in x.split() if word not in stop_words]))

    words = []
    for comment in df1['职位']:
        words += comment.split()
        word_count = Counter(words).most_common(100)

    word_count = dict(word_count)

    font_path = r'./static/SimHei.ttf'
    wordcloud = WordCloud(width=800, height=600, background_color='white',scale=2,
                          font_path=font_path).generate_from_frequencies(word_count)

    # image_colors = ImageColorGenerator(img_array)
    plt.imshow(wordcloud, interpolation='bilinear')
    # plt.imshow(wordcloud, wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
    plt.axis('off')
    plt.savefig('./static/词云3.png', dpi=1000)
    plt.close()


def data_charts4():
    df = pd.read_csv('./深圳300.csv')
    df.to_csv('./深圳词云.csv', encoding='utf_8_sig')
    df1 = pd.read_csv('./深圳词云.csv')

    df1['职位'] = df1['职位'].apply(lambda x: ' '.join(jieba.lcut(x)))  # 分词

    with open('./static/stop_word.txt', encoding='utf_8_sig') as f:
        stop_words = f.read().split('\n')
    df1['职位'] = df1['职位'].apply(lambda x: ''.join([word for word in x.split() if word not in stop_words]))

    words = []
    for comment in df1['职位']:
        words += comment.split()
        word_count = Counter(words).most_common(100)

    word_count = dict(word_count)

    font_path = r'./static/SimHei.ttf'
    wordcloud = WordCloud(width=800, height=600, background_color='white',scale=2,
                          font_path=font_path).generate_from_frequencies(word_count)

    # image_colors = ImageColorGenerator(img_array)
    plt.imshow(wordcloud, interpolation='bilinear')
    # plt.imshow(wordcloud, wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
    plt.axis('off')
    plt.savefig('./static/词云4.png', dpi=1000)
    plt.close()

def data_charts5():
    df = pd.read_csv('./杭州300.csv')
    df.to_csv('./杭州词云.csv', encoding='utf_8_sig')
    df1 = pd.read_csv('./杭州词云.csv')

    df1['职位'] = df1['职位'].apply(lambda x: ' '.join(jieba.lcut(x)))  # 分词

    with open('./static/stop_word.txt', encoding='utf_8_sig') as f:
        stop_words = f.read().split('\n')
    df1['职位'] = df1['职位'].apply(lambda x: ''.join([word for word in x.split() if word not in stop_words]))

    words = []
    for comment in df1['职位']:
        words += comment.split()
        word_count = Counter(words).most_common(100)

    word_count = dict(word_count)

    font_path = r'./static/SimHei.ttf'
    wordcloud = WordCloud(width=800, height=600, background_color='white',scale=2,
                          font_path=font_path).generate_from_frequencies(word_count)

    # image_colors = ImageColorGenerator(img_array)
    plt.imshow(wordcloud, interpolation='bilinear')
    # plt.imshow(wordcloud, wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
    plt.axis('off')
    plt.savefig('./static/词云5.png', dpi=1000)
    plt.close()


@app.route('/')
def show_data():
    return render_template('in.html')


@app.route('/a1')
def show_manage1():
    data_manage1()
    return render_template('show1.html')


@app.route('/a2')
def show_manage2():
    data_manage2()
    return render_template('show2.html')


@app.route('/a3')
def show_manage3():
    data_manage3()
    return render_template('show3.html')


@app.route('/a4')
def show_manage4():
    data_manage4()
    return render_template('show4.html')


@app.route('/a5')
def show_manage5():
    data_manage5()
    return render_template('show5.html')


@app.route('/b1')
def show_charts1():
    data_charts1()
    return render_template('show_charts1.html')


@app.route('/b2')
def show_charts2():
    data_charts2()
    return render_template('show_charts2.html')


@app.route('/b3')
def show_charts3():
    data_charts3()
    return render_template('show_charts3.html')


@app.route('/b4')
def show_charts4():
    data_charts4()
    return render_template('show_charts4.html')


@app.route('/b5')
def show_charts5():
    data_charts5()
    return render_template('show_charts5.html')


@app.route('/c1')
def show_fix1():
    data_fix1()
    return render_template('show11.html')


@app.route('/c2')
def show_fix2():
    data_fix2()
    return render_template('show22.html')


@app.route('/c3')
def show_fix3():
    data_fix3()
    return render_template('show33.html')


@app.route('/c4')
def show_fix4():
    data_fix4()
    return render_template('show44.html')


@app.route('/c5')
def show_fix5():
    data_fix5()
    return render_template('show55.html')


if __name__ == '__main__':
    app.run()
