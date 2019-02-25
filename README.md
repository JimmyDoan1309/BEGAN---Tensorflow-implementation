### BEGAN - Boundary Equilibrium Generative Adversarial Networks
This is a tensorflow implementation of BEGAN by David Berthelot, Thomas Schumm, Luke Metz ( https://arxiv.org/abs/1703.10717 )

My model was trained on a subset of celeb A ( around 20,000 images) cause I do not have enough GPU power. However, it does generate some very decent looking result.

Here are some interpolation of my model:

![](https://github.com/JimmyDoan1309/BEGAN---Tensorflow-implementation/blob/master/export/BEGAN/interpolation7.gif?raw=true)
![](https://github.com/JimmyDoan1309/BEGAN---Tensorflow-implementation/blob/master/export/BEGAN/interpolation6.gif?raw=true)
![](https://github.com/JimmyDoan1309/BEGAN---Tensorflow-implementation/blob/master/export/BEGAN/interpolation5.gif?raw=true)

I choose alpha is quite small ( alpha = 0.3 ) which result in the model is quite overfit in exchange for image quality.



