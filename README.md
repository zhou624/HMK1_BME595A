# **HW1- Implement 2D convolution
###Student: Yifeng Zhou, zhou624@purdue.edu

There are three images in the folder: summer.jpg, rock.jpg, bob.jpg. Note that bob.jpg has size of 50×50 because 1280x720 and 1920x1080 images are extremely time-consuming.

Part A
K1, K2, K4 and K5 are actually edge detection kernels
K3 is box blur kernel




### 1280X720 image
#### original image rock.jpg
![](https://github.com/zhou624/HMK1_BME595A/blob/master/rock.jpg)



Part B
bob.jpg is employed to calculate the time taken for performing each forward() pass as a function of i for the sake of time. The results show exponentional relationship

Part C
summer.jpg is employed to calculate the number of operations for performing each forward() pass as a function of kernel_size. The results show linear relationship
