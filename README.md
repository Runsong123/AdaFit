<!-- > AdaFit: Rethinking Learning-based Normal Estimation on Point Clouds<br>
> Runsong Zhu, Yuan Liu, Zhen Dong, Tengping jiang, Yuan Wang, Wenping Wang, Bisheng Yang<br>
> [Project Page](https://runsong123.github.io/AdaFit/)

Under construction ... -->


# AdaFit: Rethinking Learning-based Normal Estimation on Point Clouds (ICCV 2021 oral)

**[Project Page](https://runsong123.github.io/AdaFit/) | [Arxiv](https://arxiv.org/abs/2108.05836) **

Runsong Zhu¹, Yuan Liu², Zhen Dong¹, Tengping jiang¹, Yuan Wang¹, Wenping Wang³, Bisheng Yang¹. 

¹Wuhan University + ²The University of Hong Kong + ³Texas A&M University.


## Requirements

we conduct the experiment in the following setting:

- Ubuntu 16.04 
- CUDA 10.1 
- Python v3.7 
- Pytorch v1.4 & torchvision v0.5.0
- matplotlib v2.2.4
- numpy  v1.17.4
- tensorboardX v1.9
- scikit-learn v0.21.3
- scipy v1.3.2
- urllib3 v1.25.8


## How to use the code


### Data praparation

you need to download PCPNet dataset and place it in ```./data/```

### single-scale version (Train + Test on PCPNet):

```
python run_AdaFit_single_experiment_single_scale.py
```

Note that, the difference between single-scale verison of our AdaFit and DeepFit is the offset-learning part, which we need to add the following code.:

```
# parameter

self.conv_bias = nn.Conv1d(128, 3, 1)

# train /test 

...
bias =  self.conv_bias(x)
bias[:,:,0] = 0
points = points + bias
...

```



### multi-scale version (Train + Test on PCPNet):


```
python run_AdaFit_single_experiment_multi_scale.py
```

Note that, the difference between single-scale verison of our AdaFit and multi-scale verison of our AdaFit is the Cascaded Scale Aggregation (CSA) layer.





## Acknowledgement
The code is heavily based on [DeepFit](https://github.com/sitzikbs/DeepFit).

If you find our work useful in your research, please cite our paper. And please also cite the DeepFit paper.

```
@article{zhu2021adafit,
  title={AdaFit: Rethinking Learning-based Normal Estimation on Point Clouds},
  author={Zhu, Runsong and Liu, Yuan and Dong, Zhen and Jiang, Tengping and Wang, Yuan and Wang, Wenping and Yang, Bisheng},
  journal={arXiv preprint arXiv:2108.05836},
  year={2021}
}

@article{ben2020deepfit,
  title={DeepFit: 3D Surface Fitting via Neural Network Weighted Least Squares},
  author={Ben-Shabat, Yizhak and Gould, Stephen},
  journal={arXiv preprint arXiv:2003.10826},
  year={2020}
}
```