## DeuDomitory_TempCheck
```py
if  getattr(sys, 'frozen', False): 
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path)
else:
    driver = webdriver.Chrome()
```
chromedriver.exe와 chrome의 버전을 확인
```py
# ver.체온입력
# ex) my_information = ["김철수", "20221234", "A1234 or B1234", temperature]
temperature = input('체온 입력: ')
my_information = ["Name", "Student ID", "Dormitory Room Number", temperature]

# or

# ver.체온값고정
# ex) my_information = ["김철수", "20221234", "A1234", "36.5"]
my_information = ["Name", "Student ID", "Dormitory Room Number", "Temperature"]
```
"ver.체온입력" 또는 "ver.체온값고정"을 선택하여 자신의 정보로 입력
***
### 앞으로의 업데이트
~~체온 입력 기능~~ 완료
* 본인은 .exe 실행파일로 프로그램 실행으로 사용 중이므로 공용으로도 사용할 수 있도록 만들기(단, 이름, 학번, 기숙사 호실은 한번 입력이 영구하도록)
* 자신의 학번, 이름, 기숙사 호실의 정보가 바뀌었을때 재입력 기능
