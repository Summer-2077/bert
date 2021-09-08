import pandas as pd
import numpy as np


def create_raw_documents(n):
    # 读取 train_set 和 test_a 的 text 部分，每行中间插入空行
    files_in = ["./raw_data/train_set.csv", "./raw_data/test_a.csv"]
    files_out = []
    for i in range(n):
        files_out.append(open("./raw_data/train_{}".format(i), 'w'))

    for file in files_in:
        data = pd.read_csv(file, sep='\t')
        data = data['text'].tolist()
        data_num = len(data)
        max_len = data_num // n
        index = list(range(0, data_num, max_len))
        index.append(max_len)
        for i in range(len(index) - 1):
            files_out[i].writelines("\n\n".join(data[index[i]:index[i + 1]]))
            files_out[i].writelines("\n")
            files_out[i].writelines("\n")
    for f in files_out:
        f.close()


def create_vocab():
    files = ["./raw_data/train_set.csv", "./raw_data/test_a.csv"]
    my_open = open('bert-mini/vocab.txt', 'w')
    word = set()
    for file in files:
        data = pd.read_csv(file, sep='\t')
        for text in data['text']:
            word.update(text.split())
    extra_tokens = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]
    my_open.writelines("\n".join(extra_tokens))
    my_open.writelines("\n")
    my_open.writelines("\n".join(word))
    my_open.close()


if __name__ == '__main__':
    # create_raw_documents(10)
    create_vocab()




