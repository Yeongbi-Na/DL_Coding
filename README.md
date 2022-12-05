## 인공지능 연구소
- 드론 촬영 데이터를 활용한 벼의 생육 이상 판별 모델 개발
- 산출물: 모델링 코드, 공개 코드 매뉴얼 github 제공(사업 종료 기한이 연기되어 해당 레포는 private 상태)
- 모델 개발 방식: mmsegmentation 오픈 소스를 기반으로 데이터셋과 목적에 맞게 커스터마이즈 함 > training_model.md
- k-net, segmenter, segformer 세가지 모델을 선정해 활용함

</br>

### 환경 세팅
- [connect_server_vscode](https://github.com/Yeongbi-Na/GIAI/blob/main/setting_env/connect_server_vscode.md)
- [setting_in_container](https://github.com/Yeongbi-Na/GIAI/blob/main/setting_env/setting_in_container.md)

### data_processing
- [Annotation 이미지의 클래스 매핑(with 블러 처리)](https://github.com/Yeongbi-Na/GIAI/tree/main/data_preprocessing)
- [포아송 블렌딩]()

### training models
[mmsegmentation 활용 & 커스터마이즈](https://github.com/Yeongbi-Na/GIAI/blob/main/training_model.md)

### 오류 정리
[error note](https://github.com/Yeongbi-Na/GIAI/blob/main/error_note.md)
