### 准备数据集


import numpy as np
import torch
import config
from torch.utils.data import DataLoader, Dataset


class numDataset(Dataset):
    def __init__(self):
        # 使用numpy随机创建数组
        self.data = np.random.randint(0,1e8,size=[500000])


    def __getitem__(self, index): # 这里返回的什么  batch里面就是什么   for的时候就是什么
        input = list(str(self.data[index]))
        label = input + ['0']
        input_len = len(input)
        label_len = len(label)
        return input, label, input_len, label_len

    def __len__(self):
        return self.data.shape[0]

def collate_fn(batch):

    # 排序
    batch = sorted(batch, key=lambda x: x[3], reverse=True)
    # batch = sorted(batch, key= lambda x:x[2], reverse=True)
    input, label, input_len, label_len= list(zip(*batch))

    input = torch.LongTensor([config.numSequence.transform(i,config.seq_len) for i in input])

    label = torch.LongTensor([config.numSequence.transform(i,config.seq_len+1) for i in label])

    input_len = torch.LongTensor(input_len)
    label_len = torch.LongTensor(label_len)
    return input, label, input_len, label_len

train_data_loader = DataLoader(numDataset(),batch_size=config.TRAIN_BATCH_SIZE,shuffle=True,collate_fn=collate_fn)

if __name__ == '__main__':
    # num_data = numDataset()
    # print(len(num_data))
    # print(num_data.data)
    # print(num_data[2])


    # print('train_data_loader[0]',train_data_loader[0])  TypeError: 'DataLoader' object is not subscriptable
    for input, label, input_len, label_len in train_data_loader:
        print(input.size())
        # print(label)
        # print('input_len:',input_len)
        # print('dasdasd:',label_len)
        break




