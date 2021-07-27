import torch
import config
import torch.nn as nn
from torch.nn.utils.rnn import pad_packed_sequence, pack_padded_sequence


class Encoder(nn.Module):
    def __init__(self):
        super(Encoder, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=len(config.numSequence),
                                      embedding_dim=config.embedding_dim,
                                      padding_idx=config.numSequence.PAD)

        self.gru = nn.GRU(input_size=config.embedding_dim,
                          num_layers=config.num_layers,
                          hidden_size=config.hidden_size,
                          batch_first=True)

    def forward(self,input):
        # ddsa
        """
        :param input: [batch_size,seq_len]
        :return:
        """
        embedded = self.embedding(input) # embedded:[batch_size,seq_len,embedding_dim]

        # 打包
        embedded = pack_padded_sequence(embedded,inp)