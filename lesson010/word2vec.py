import io
import os
import sys
import requests

from collections import OrderedDict
import math
import random
import numpy as np

# import numpy as np
file_path = './1.txt'


def download():
    '''
        下载文本(语料库)
    :return:
    '''
    url = 'https://dataset.bj.bcebos.com/word2vec/text8.txt'
    web = requests.get(url)
    corpus = web.content
    with open(file_path, 'wb') as file:
        file.write(corpus)


def load_txt():
    '''
    读取文本(语料库)
    '''

    with open(file_path, 'r') as file:
        content = ''
        while True:
            chunk = 1024 * 1024
            s = file.read(chunk)
            if not s:
                break
            content += s
        corpus = content.strip()
        return corpus


def data_preprocess(corpus: str):
    '''
     将语料库的单词都转小写，将每个单词存入list的元素中
    :param corpus:
    :return:
    '''
    return corpus.strip() \
        .lower() \
        .split(' ')


# 统计词频并排序，然后按照对应格式返回数
# 据，这步骤GPT会帮我们封装好，但是原理是这样
def build_dict(corpus: list):
    '''
    统计词频，并构建词频dict
    词频:即每个单词出现的次数
    :param corpus:
    :return:
    '''
    word_freq_dict = {}
    for word in corpus:
        # 统计词频
        if word not in word_freq_dict:
            word_freq_dict[word] = 0
        word_freq_dict[word] += 1

    # 将词频按照从大到小排序
    word_freq_dict = sorted(word_freq_dict.items(),
                            key=lambda item: item[1],
                            reverse=True)
    # 构建map，记录 单词->id
    word2id_dict = {}
    # 构建map, 记录 id -> 词频
    word2id_freq = {}
    # 构建map，记录 id -> 单词
    id2word_dict = {}

    for word, freq in word_freq_dict:
        curr_id = len(word2id_dict)

        word2id_dict[word] = curr_id
        word2id_freq[curr_id] = freq
        id2word_dict[curr_id] = word

    return word2id_freq, word2id_dict, id2word_dict


def convert_corpus2id(corpus, word2id_dict):
    '''
    作用，将语料库的每个单词都转换为id，返回这个id列表
    :param corpus:
    :param word2id_dict:
    :return:
    '''
    # corpus = [word2id_dict[word] for word in corpus]
    result = []
    for word in corpus:
        _id = word2id_dict[word]
        result.append(_id)
    return result


# 构造样本集
def build_data(corpus,
               word2id_dict,
               word2id_freq,
               max_windows_size=3,
               negative_sample_num=4):
    '''

    :param corpus:
    :param word2id_dict:
    :param word2id_freq:
    :param max_windows_size: 可变长的window窗，这样词汇量训练更稳定
    :param negative_sample_num: 负采样
    :return:
    '''
    vocab_size = len(word2id_freq)
    # 样本的数据结构
    dataset = []
    # 使用中间的词预测两边的词，这个中间词的id
    center_word_idx = 0
    while center_word_idx < len(corpus):
        # 确定window大小，返回[1,3]范围内随机一位数
        window_size = random.randint(1, max_windows_size)
        # 确定要输入的context是哪个词
        # cbow 是用周围的词预测context_word
        # skip-gram 是用context_word预测周围的词
        context_word = corpus[center_word_idx]
        # 找周围的词
        label_start = max(0, center_word_idx - window_size)
        label_end = min(len(corpus) - 1,
                        center_word_idx + window_size)
        # 周围的词
        label_candidates = []
        for idx in range(label_start, label_end + 1):
            if idx != center_word_idx:
                label_candidates.append(corpus[idx])

        for label_word in label_candidates:
            # 这里用skip-gram
            # 元组0: context_word
            # 元组1: 周围的词，也就是要预测的词
            # 元组2: 1是正样本的意思
            dataset.append((context_word, label_word, 1))
            # 开始负采样
            i = 0
            while i < negative_sample_num:
                neg_candidate = random.randint(0, vocab_size - 1)
                if neg_candidate is not label_word:
                    dataset.append((context_word, neg_candidate, 0))
                    i += 1
        center_word_idx += window_size
    return dataset


def build_batch(dataset, batch_size, epoch_num):
    '''

    :param dataset: 数据集
    :param batch_size: 每批数量
    :param epoch_num: 轮次
    :return:
    '''
    center_word_batch = []
    target_word_batch = []
    label_batch = []
    for epoch in range(epoch_num):
        # 打乱dataset
        random.shuffle(dataset)
        for center_word, target_word, label in dataset:
            center_word_batch.append([center_word])
            target_word_batch.append([target_word])
            label_batch.append(label)
            if len(center_word_batch) == batch_size:
                yield np.array(center_word_batch).astype('int64'), \
                    np.array(target_word_batch).astype('int64'), \
                    np.array(label_batch).astype('int64')

                center_word_batch = []
                target_word_batch = []
                label_batch=[]
        if len(center_word_batch)>0:
            yield np.array(center_word_batch).astype('int64'), \
                np.array(target_word_batch).astype('int64'), \
                np.array(label_batch).astype('int64')


def main():
    # 加载语料
    corpus = load_txt()
    # 将语料转成语料库list
    corpus = data_preprocess(corpus)
    corpus = corpus[:1000]
    # 统计语料库
    word2id_freq, word2id_dict, id2word_dict = build_dict(corpus)

    # 将语料库的每个单词都转换为id
    corpus = convert_corpus2id(corpus, word2id_dict)
    # 将语料库构造成样本集
    data_set = build_data(corpus, word2id_dict, word2id_freq)


main()
