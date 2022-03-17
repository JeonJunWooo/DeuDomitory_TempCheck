## DeuDomitory_TempCheck
### 동의대학교 기숙사 코로나 자가 체온 제출 자동화 코드
autocheck_env 가상환경에 사용된 것  
Python Version - 3.10.2
#### Windows 사용법
1. code버튼 클릭 후 Download ZIP
2. 다운받은 zip파일 압축 해제
3. my_information.txt를 열어서 자신의 정보 입력 후 저장  
3-1. my_information.txt에서 각각 정보를 한줄씩 적어야한다.  
ex) 김철수  
    20201234  
    A1323  
    36.5  
4. 압축해제한 폴더 IDE에서 열기(vscode, pycharm 등)
5. cmd(터미널)을 열어서 cd autocheck_env/Scripts 후 activate로 가상환경 실행
6. cd .. 을 두번하여 원래 폴더로 돌아와서 행긱이면 py happy_temp_check.py 입력(효긱이면 py hyomin_temp_check.py 입력)  
6-1. **효민 2긱을 기본으로 해두었으며 여긱일 시 hyomin_temp_check.py의 34번째 줄을 주석처리 및 36번째 줄의 주석삭제 후 사용할 것!!**
7. 체온 입력을 하면 크롬이 자동으로 실행되고 잠시 후 체온 제출 완료!
---
### 코드의 기본값
* hyomin_auto_temp의 경우 효민 제 2기숙사가 기본값!!
---
#### 코드 일부 설명
```py
f = open('my_information.txt', 'r', encoding='UTF8')
my_information = f.readlines()
f.close()
```
my_information.txt 파일을 불러와서 저장
```py
chromedriver_autoinstaller.install() # chromedriver 자동 다운로드
driver = webdriver.Chrome()
```
최신 버전의 chromedriver를 자동으로 가져오기 때문에 이전 버전의 chromedriver를 찾는 코드 삭제
***
  
### 앞으로의 업데이트
~~체온 입력 기능~~ 완료  
~~본인은 .exe 실행파일로 프로그램 실행으로 사용 중이므로 공용으로도 사용할 수 있도록 만들기(단, 이름, 학번, 기숙사 호실은 한번 입력이 영구하도록)~~
~~효민 기숙사의 경우 제2기숙사와 여자기숙사를 선택하는 요소도~~
~~자신의 학번, 이름, 기숙사 호실의 정보가 바뀌었을때 재입력 기능~~  
완료, 메모장을 읽는 방식으로 아이디어를 내서 사용자의 정보를 직접 입력할 수 있게 되었음.
~~exe 실행파일 생성완료하여 크롬드라이버와 my_information.txt 파일까지 한 폴더에 넣으면 .exe 실행파일이 실행되는 것을 확인하였으나, 다른 PC에 전달하여도 되는지 확인이 필요함.~~
완료, 동의대학교 행복기숙사, 효민 제2기숙사, 효민 여자기숙사 모두 exe 실행파일로 만들어서 애브리타임을 통해 파일 배포 완료!  

---
### 기숙사 체온 제출 자동화 프로그램  
행복기숙사: https://drive.google.com/file/d/1DOHlTKIzQib_r-jod5fHL1_9mxIkUF6f/view?usp=sharing  
효민기숙사: https://drive.google.com/file/d/1LE-HaaXLwWEkGgBH-foAHPqEqkZDu_Jr/view?usp=sharing  
여자기숙사: https://drive.google.com/file/d/1IIBjwv7JCi2FGuLp2Ft2_IZQNoUHz9s3/view?usp=sharing  
