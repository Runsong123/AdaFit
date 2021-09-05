import torch
import torch.nn as nn

import torch.nn.functional as F


# basic convolution
class BaseBC(nn.Module):
    def __init__(self,input_dim,output_dim,with_bn=True):
        super(BaseBC,self).__init__()
        self.conv = nn.Conv1d(input_dim, output_dim, 1)
        self.with_bn = with_bn
        if with_bn:
            self.bn = nn.BatchNorm1d(output_dim)
        else:
            self.bn = None
    def forward(self,x):
        if self.with_bn:
            x = F.relu(self.bn(self.conv(x)))
        else:
            x = F.relu(self.conv(x))
        return x


# basic fully connect
class BaseBF(nn.Module):
    def __init__(self,input_dim,output_dim):
        super(BaseBF,self).__init__()
        self.fc = nn.Linear(input_dim, output_dim)
        self.bn = nn.BatchNorm1d(output_dim)
        
    def forward(self,x):
        x = F.relu(self.bn(self.fc(x)))
        return x


