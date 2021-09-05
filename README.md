<!-- > AdaFit: Rethinking Learning-based Normal Estimation on Point Clouds<br>
> Runsong Zhu, Yuan Liu, Zhen Dong, Tengping jiang, Yuan Wang, Wenping Wang, Bisheng Yang<br>
> [Project Page](https://runsong123.github.io/AdaFit/)

Under construction ... -->


# AdaFit: Rethinking Learning-based Normal Estimation on Point Clouds (ICCV 2021 oral)

This paper presents a neural network for robust normal estimation on point clouds, named AdaFit, that can deal with point clouds with noise and density variations. Existing works use a network to learn point-wise weights for weighted least squares surface fitting to estimate the normal, which has difficulty in finding accurate normals in complex regions or containing noisy points. By analyzing the step of weighted least squares surface fitting, we find that it is hard to determine the polynomial order of the fitting surface and the fitting surface is sensitive to outliers. To address these problems, we propose a simple yet effective solution that adds an additional offset prediction to improve the quality of normal estimation. Furthermore, in order to take advantage of points from different neighborhood sizes, a novel Cascaded Scale Aggregation layer is proposed to help the network predict more accurate point-wise offsets and weights. Extensive experiments demonstrate that AdaFit achieves state-of-the-art performance on both the synthetic PCPNet dataset and the real-word SceneNN dataset.


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
python train_n_est_single_scale.py
```

### multi-scale version (Train + Test on PCPNet):

```
python train_n_est_multi_scale.py
```







## Acknowledgement
The code is heavily based on [DeepFit](https://github.com/sitzikbs/DeepFit).

If you find our work useful in your research, please cite our paper. please also cite the DeepFit paper.

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