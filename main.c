//
// Yifeng Zhou, zhou624@purdue.edu
//
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>
#include <unistd.h>
int main(int argc, const char * argv[]) {
    int centerX,centerY,pixelnew=0;
    int in_channel=3;int stride=1;int ImageX=50;
    int ImageY=50;int kernel_size=3;
	int kernel[kernel_size][kernel_size];
    int image[ImageX][ImageY][in_channel];
    int OutputX=(ImageX-(kernel_size/2)*2)/stride;
    int OutputY=(ImageY-(kernel_size/2)*2)/stride;
    double timeconsumption;
    struct timeval begintime, endtime;
	for (int i=0;i<kernel_size;i++){
                for (int j=0;j<kernel_size;j++){
                    kernel[i][j]=1;
                }
        }
    for (int i=0;i<ImageX;i++){
        for (int j=0;j<ImageY;j++){
            for (int k=0;k<in_channel;k++){
                image[i][j][k]=1;
            }
        }
    }
    for (int channelNum=0;channelNum<12;channelNum++){
        int ochannelnumber=pow(2,channelNum);
        gettimeofday(&begintime, NULL);
        for (int o_channel=0;o_channel<ochannelnumber;o_channel++){
            for (int cntxx1=0;cntxx1<OutputX;cntxx1++){
                for (int cntyy1=0;cntyy1<OutputY;cntyy1++){
                    for (int cntx2=0;cntx2<kernel_size;cntx2++){
                        for (int cnty2=0;cnty2<kernel_size;cnty2++){
                            for(int k=0;k<in_channel;k++){
								centerX=(kernel_size/2)+cntxx1*stride;
								centerY=(kernel_size/2)+cntyy1*stride;
                                pixelnew=kernel[cntx2][cnty2]*image[centerX-(kernel_size/2)+cntx2][centerY-(kernel_size/2)+cnty2][k];
                            }
                        }
                    }
                }
            }
        }
        gettimeofday(&endtime, NULL);
        timeconsumption = (double)(endtime.tv_sec - begintime.tv_sec)+(double)(endtime.tv_usec - begintime.tv_usec) / 1000000.0;
        printf("i=%2d,time consumption:%f second\n",channelNum,timeconsumption);
    }
    return 0;
}
