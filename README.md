## 인공지능 연구소
- 드론 촬영 데이터를 활용한 벼의 생육 이상 판별 모델 개발
- 산출물: 모델링 코드, 공개 코드 매뉴얼 github 제공(사업 종료 기한이 연기되어 해당 레포는 private 상태)

### 실험하는 방식
- 전체 데이터를 다 돌리기보다, 적은 양으로 아이디어가 작동하는지 확인한 후, 마지막에 최종적으로 가장 좋은 것으로 실험 들리기
- 모델링 코드, 알고리즘 소개, 공개 코드 매뉴얼 git 제공

### 데이터 준비
- annotation 데이터는 기본적으로 RGB channel로 되어있는데 sementicsegmentation을 위해서는 annotated data를 각 클래스로 매핑해 1차원으로 만들어주어야한다
- original 데이터는 R, G, B, RE, NIR 채널로 제공받는데 3개의 채널을 선정해 merge

### 모델 학습
- mmsegmentation 오픈 소스를 기반으로 데이터셋과 목적에 맞게 커스터마이즈 함 > training_model.md
- k-net, segmenter, segformer 세가지 모델을 선정해 활용함
