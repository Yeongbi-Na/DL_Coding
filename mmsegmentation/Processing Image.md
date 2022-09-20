### 현재 프로세스
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
  
  
  
  ### 
1. ZipFile 모듈로 압축 풀지않고 데이터 가져오기
  - ZipFile 모듈로 압축 풀지않고 데이터 가져와 format(jpg, png) 맞춰주고 img는 채널별 저장
  - ann은 바로 3번 적용해 merge해서 저장하기
 
2. merging channel
