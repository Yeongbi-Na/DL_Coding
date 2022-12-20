# 컨테이너 내에서 환경 구축
```bash
apt-get update
apt-get install libgtk2.0-dev # 이미지를 스크린에 출력하거나 간단한 GUI를 만드는데 사용
pip install -U openmim 
mim install mmcv-full==1.6.0
apt install nvidia-cuda-toolkit

#mmsegmentation 경로로 이동한 후 
cd mmsegmentation
pip install -v -e .
```
