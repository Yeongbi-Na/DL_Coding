## 모델 학습하기
### 1. mmsegmentation 다운로드를 하면 </br>
![image](https://user-images.githubusercontent.com/61492320/185517019-454aa0db-e3ca-473d-abd6-5fe99b3a2395.png)</br>

이렇게 다양한 폴더와 수많은 파일을 볼 수 있다</br>

config 파일과 모델 코드를 목적에 맞게 수정해 돌리면 코드를 따로 많이 작성하지 않고도 쉽게 구현 가능하다</br>

주로 다루게 될 것은 mmseg, configs 폴더이다</br>


### 2. 모델 선정 및 customize하기</br>
configs 폴더에 들어가면</br>
![image](https://user-images.githubusercontent.com/61492320/185517107-422132c5-4687-4000-b95d-7ca50d785692.png)
![image](https://user-images.githubusercontent.com/61492320/185517120-b3271a3b-db9d-4192-a031-069983a03e87.png)</br>
이렇게 많은 모델들을 볼 수 있다</br>
</br>
나는 segmenter를 사용하고자 하므로 segmenter 폴더에 들어가보면</br>
![image](https://user-images.githubusercontent.com/61492320/185517179-b2db8532-7b1d-4d76-a326-a4c8fa94a805.png)</br>
segmenter에서도 여러 모델이 있고 mmsegmentation 공식 git사이트나 ReadMe를 보면서 목적에 맞는 걸 선택하면 된다</br>
선택한 segmenter_vit-b_mask_8x1_512x512_160k_ade20k.py 파일이 어떻게 구성됐는지 봐보자</br>

![image](https://user-images.githubusercontent.com/61492320/185517522-2949acb4-2f00-41b7-bb05-f7ce839ce49f.png)

목적에 맞게 costomize하기 위해선 표시된 __base__에 있는 것들이 수정해야하는 것들이다
segmenter_vit-b16_mask.py는 모델에 대한 정보
ade20.py는 dataset에 대한 정보
default_runtime.py
schedule_160k.py iteration, epoch등의 학습 스케쥴에 대한 정보

__base__외에 train_pipline, test_pipeline 등도 목적에 맞게 바꿔주면 된다


*원본을 복사해 수정하는 것을 적극 권장

