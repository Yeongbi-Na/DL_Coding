## 환경 구축
- ### nvcc, gcc 환경 구축
pip install -U openmim
 mim install mmcv-full

nvcc 환경구축
conda install cuda -c nvidia

apt update
apt-get install gcc


## 모델 학습 및 추론
- ### 성능 문제 


![image](https://user-images.githubusercontent.com/61492320/200710416-6c4bc2c2-5862-4d3f-b2fa-8b96d7a99fb4.png)

모델 개발 업무를 다른 연구원님이랑 똑같은 프로세스를 수행했는데 내 모델이 normal, background 외에는 정확도가 0에 가까웠다
코드를 비교해보니 모델 config 파일의 pretrained='open-mmlab://resnet50_v1c', 이 부분을 None으로 바꿔주고 
cfg.load_from = '/nyb/yb_RiceSeg/RiceSeg/pretrained_chkp/knet_s3_pspnet_r50-d8_8x2_512x512_adamw_80k_ade20k_20220228_054634-d2c72240.pth'
이렇게 적절한 모델을 다운받아서 cfg 파일에 반영해주면 다른 클래스에 있어서도 모델의 성능이 향상됐다



- ### inference
result = inference_segmentor(segmenter, img)
KeyError: 'PALETTE' 

mmsegmentation/tools/train.py 를 열어보니 model.CLASSE 정의되어있고 model.PALETTE는 없었다.
이 부분을  model.PALETTE = dataset[0].PALETTE로 수정

cf) https://github.com/open-mmlab/mmsegmentation/issues/129



- ### AttributeError: EncoderDecoder: 'IterativeDecodeHead' object has no attribute 'out_channels'
이런 오류가 발생해서 pretrained 모델 ckpt 파일도 확인하고, dataset class 도 확인하고 pip install -v -e . 도 해봤는데 계속 오류가 났다
mmseg/models/segmentor/builder.py 에서 pretrained 부분을 수정했더니 해결


- ### dataset class 수정 시 오류
dataset class를 수정했음에도 모델 학습에서 오류가 발생했다. 

