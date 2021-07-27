import config



class numSequence():


    def __init__(self):
        self.PAD_TAG = 'PAD'
        self.UNK_TAG = 'UNK'
        self.SOS_TAG = 'SOS'
        self.EOS_TAG = 'EOS'
        self.PAD = 0
        self.UNK = 1
        self.SOS = 2
        self.EOS = 3


        self.dict = {self.PAD_TAG:self.PAD,
                     self.UNK_TAG:self.UNK,
                     self.SOS_TAG:self.SOS,
                     self.EOS_TAG:self.EOS}
        for i in range(10):
            self.dict[str(i)] = len(self.dict)

        self.inverse_dict = {i[1]:i[0] for i in self.dict.items()}

    def transform(self,sentence,seq_len=9,add_eos=False):

        if len(sentence) > seq_len:
            sentence = sentence[:seq_len]
        sentence_len = len(sentence)
        if add_eos:
            sentence = sentence + [self.EOS_TAG]
        if sentence_len < seq_len:
            sentence = sentence + [self.PAD_TAG]*(seq_len-len(sentence))

        result = [self.dict.get(i,self.UNK) for i in sentence]
        return result

    def inverse_transform(self,indics):
        result = [self.inverse_dict.get(i,self.UNK_TAG) for i in indics]
        return result

    def __len__(self):
        return len(self.dict)



if __name__ == '__main__':
    a = numSequence()
    print(len(a))
    # print(a.dict)
    # c = a.transform(['3', '7', '7', '9', '1', '7', '1', '6'])
    #
    # d = a.inverse_transform(c)
    #
    #
    # print(c)
    # print(d)