# DL_Coding


## mmsegmentation

1. 데이터는 기본적으로 RGB channel로 되어있는데 sementicsegmentation을 위해서는 annotated data를 각 클래스로 매핑해 1차원으로 만들어주어야한다
2. mmsegmentation에서 제공하는 모델 중 segmentation, k net, segformer를 시도하고 있음



## 주의사항
1.  class Dataset() 과 같은 class 정보를 수정하게 되면 Terminal에

''' 
pip install -v -e . 

'''
입력해 파일들을 업데이트해주어야 한다

2. 
