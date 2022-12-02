# 컨테이너 내에서 환경 구축
```bash
apt-get update
apt-get install libgtk2.0-dev
pip install -U openmim
mim install mmcv-full==1.6.0
apt install nvidia-cuda-toolkit

#mmsegmentation 경로로 이동한 후 
cd mmsegmentation
pip install -v -e .
```
