
annotation 이미지 클래스 매핑
.py

포아송 블렌딩 
.py
## Poissong blending 

    
    
    tgt_dir = 'R20220720A181020_GNRE.png'
    scr_dir = 'R20220720A180911_ann.png' #R20220720A181911_RGB
    ann_dir = 'R20220720A180911_ann.png'
    cls_dir = 'R20220720A180911_cls.png'
    result = poissong_blending(scr_dir, tgt_dir, ann_dir, cls_dir, 5)



## 기록
### 초기 계획
1. ZipFile 모듈로 압축 풀지않고 데이터 가져와 format(jpg, png) 맞춰준후 ann_png/img_png 폴더에 저장
  - 경로에 원천/ 라벨 & channel 체크
  - 경로에 한글있으면 경로명 체크 불가하므로 fileName.encode('cp437').decode('cp949') 처럼 인코드, 디코드 설정
  - ann/img 파일명 형식이 다름 G_018, G018 이런식이므로 이부분 미리 수정해주기
  
2. merging channel
  - 미리 모듈화해놓은 py 파일
  - 파일명에 A03 혹은 A02 이렇게 나누어져 있어서 이 부분 반영한 코드 수정 필요

3. mapping ann 
  - 모듈화해놓은  py 파일
  - class, palette 정보를 input으로 넘겨주고, output으로 각 클래스를 포함한 파일명을 주도록 수정 필요
  </br>
  
  ### 수정 계획(ver.9월)

1. ZipFile 모듈로 압축 풀지않고 데이터 가져오기
  - ZipFile 모듈로 압축 풀지않고 데이터 가져와 format(jpg, png) 맞춰주고 img는 채널별 저장
  - ann은 바로 3번 적용해 merge해서 저장하기
  - 각 클래스별 데이터 개수 확인, 데이터가 부족한 클래스의 경우 val/ test에 추가로 넣어주기(3번에서)

2. merging channel

3. data split
-  train/val/test 비율 설정 및 data split 
-  img 파일명으로 ann폴더 내 파일들과 매칭하면서 이상없는지 한번더 확인해주기
-  데이터가 부족한 클래스의 경우 val/ test에 추가로 넣어주기


09.22 데이터 이슈사항
- png만 있어야하는데 json 섞여있ㅇ음
- R채널에만 없는 데이터 존재, 
- ann에서는 tif, tiff 섞여있음


09.22 데이터 처리 일지
- png/ tif, tiff인 파일 경로 가져오기
- ann, img 파일명 잘 매칭되는지 확인
- 채널명에 오타 없는지 확인

</br>

  ### 수정 계획(ver.10월)
  
1. ZipFile 모듈로 압축 풀어서 데이터 정리
- 풀어서 ann/img 로 전체 폴더들이 묶이는 게 효율적이라서 풀기로 했다

2. merging channel
- 최종적으로 RGB/ G,NIR,RE 조합을 사용하기로 
- min-max도 적용해보기로 


3. class 매핑
- 데이터를 전달받았는데 블러가 발생했고, 모델 학습을 위해선 처리해줘야함
- 각 픽셀별로 클래스 값과 거리를 구할 때 거리가 0인지, 아닌지에 따라 mask 이미지 생성
- mask 이미지를 기준으로 주변 거리가 2인 픽셀들을 참고해 값을 할당
