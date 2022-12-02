### 환경 세팅
contatiner 안에서 아래와 같이 실행해주면 환경 세팅 완료!
```bash
apt-get update
apt-get install libgtk2.0-dev
pip install -U openmim
mim install mmcv-full==1.6.0
apt install nvidia-cuda-toolkit


cd mmsegmentation #mmsegmentation 경로로 이동한 후 
pip install -v -e . #설치해주기
```


</br>

### Inference 시 오류
```bash
result = inference_segmentor(segmenter, img)
KeyError: 'PALETTE' 
```
mmsegmentation/tools/train.py 를 열어보니 model.CLASSE 정의되어있고 model.PALETTE는 없었다.
아래와 같이 수정
```bash 
model.PALETTE = dataset[0].PALETTE
```
cf) https://github.com/open-mmlab/mmsegmentation/issues/129

</br>

### dataset class 수정 시 오류
dataset class를 수정했음에도 모델 학습에서 오류가 발생했다. 

```bash

pip install -v -e .
```

</br>

### AttributeError: EncoderDecoder: 'IterativeDecodeHead' object has no attribute 'out_channels'
이런 오류가 발생해서 pretrained 모델 ckpt 파일도 확인하고, dataset class 도 확인하고 pip install -v -e . 도 해봤는데 계속 오류가 났다
mmseg/models/segmentor/builder.py 에서 pretrained 부분을 수정했더니 해결

</br>

### 성능 문제 
![image](https://user-images.githubusercontent.com/61492320/200710416-6c4bc2c2-5862-4d3f-b2fa-8b96d7a99fb4.png)

##### 모델 개발 업무를 다른 연구원님이랑 똑같은 프로세스를 수행했는데 내가 개발한 모델은 normal, background 외 클래스가 정확도가 0에 가까웠다. 
##### 코드를 비교해보니 모델 config 파일의 pretrained 부분을 아래와 같이 수정
```
 pretrianed = None
 
```
그리고 적절한 모델을 다운받아서
```
cfg.load_from = '/nyb/yb_RiceSeg/RiceSeg/pretrained_chkp/knet_s3_pspnet_r50-d8_8x2_512x512_adamw_80k_ade20k_20220228_054634-d2c72240.pth'
```
cfg 파일에 반영해줘야했다.
이후, 다른 클래스에 있어서도 모델의 성능이 향상됐다

