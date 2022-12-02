# 서버 접속하기 

### 장점

1. 내 pc 가 가진 키(id_rsa.pub) 을 서버에 등록해놓으면 서버에 접속할 때마다 비밀번호 칠 필요 없음

2. vscode에서 원격 서버 접속 시 shell server terminated code 255 이런 오류가 발생했는데 키 등록하면 오류 해결!

(code 255: 원격 서버에 접속은 가능 but 컨테이너에 접속이 안됨)


</br>

### 해야할 일

- ida_rsa.pub 키 발급 (로컬에서)

- ida_rsa.pub 키 등록 (서버에서)


</br>

## 1. ida_rsa.pub 키 발급 (로컬에서)

https://playon.tistory.com/115

위 블로그에 잘 나와있으므로 순서대로 따라하면 금방한다!

![image](https://user-images.githubusercontent.com/61492320/201848261-09acb40a-e46e-436b-aa01-06dd22a33293.png)





## 2. ida_rsa.pub 키 등록 (서버에서)

일단 서버에 접속한 후 키 옮기기

```bash
scp (id_rsa.pub경로) (아이디@호스트):id_rsa.pub
scp C:\Users\yb\.ssh\id_rsa.pub yb@ip주소:id_rsa.pub
```

autorized key로 등록하기

```bash
mkdir .ssh
cat id_rsa.pub >> .ssh/authorized_keys
chmod 600 .ssh/authorized_keys
```




## 3. vs code에 키 등록

ctrl+shift+p 를 누르면 이런 화면이 뜬다

세번째에 있는 Remote-SSH: SSH 구성 파일 열기 클릭 - user 이름 들어간 .ssh 파일 열기
![image](https://user-images.githubusercontent.com/61492320/201848463-d31bf399-a015-4cb4-9786-389c12484d18.png)


해당 파일에 아래처럼 서버 정보와 IdentityFile(키)를 적어주면 된다

```bash
Host 내가 정한 서버 이름 
  HostName IP주소
  User 계정명
  IdentityFile ~/.ssh/id_rsa
```

이후 다시 ctrl+shift+p 를 누르고
![image](https://user-images.githubusercontent.com/61492320/201848463-d31bf399-a015-4cb4-9786-389c12484d18.png)

Remote-SSH: 호스트에 연결 클릭




서버 연결되면 다시 ctrl+shift+p 를 누르고
![image](https://user-images.githubusercontent.com/61492320/201848463-d31bf399-a015-4cb4-9786-389c12484d18.png)


Dev Container : Attaching to Running container~~ 클릭

연결하고자하는 컨테이너 클릭


![image](https://user-images.githubusercontent.com/61492320/201848587-91bec5e7-8ad0-4493-9dfa-4899cd3d91a1.png)

왼쪽 하단에 이런 식으로 뜨면 잘 연결된 거다!




</br></br>



