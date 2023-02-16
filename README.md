# gettyimagedownloader

회사에서 게티이미지뱅크를 자주 이용하기 때문에 이미지를 구하는 과정을 파이썬으로 구현해보면 어떨까 하고 도전해보았다.  
  
게티이미지뱅크에서 따로 제공하는 API가 없는것같아서 selenium으로 로그인 및 이미지 검색 자동화를 먼저 구현하고  

gui로 이용하기 쉽게 하나의 윈도우 프로그램을 만들어보고자 한다.

##2023-02-15  
headless옵션을 끈 경우에만 다운로드가 정상적으로 작동이되고  
headless옵션을 킨 경우에는 다운로드가 안된다  
시간을 넉넉히 잡아두었는데도 다운로드 자체가 안되는 것 같다  
구글링해보니 headless일때 다운로드할 수 있게 셋팅하는 방법이 있어서 그대로 따라했지만 여전히 다운로드가 안된다  
게티이미지뱅크 사이트가 다운로드를 하기위해서는 동적크롤링이 필요한데 selenium이 아닌 다른 방법을 찾아야할지도 모르겠다.

##2023-02-16  
브라우저가 문제인가 싶어서 파이어폭스로 변경하여 실행해보니 아래의 에러가 떴다  
![image](https://user-images.githubusercontent.com/45898059/219252208-b0e9ec48-4047-4487-920d-dcf843806d1c.png)  
구글링을 해보는데 답변들이 파이어폭스 브라우저 설치를 안해서 발생하는걸로 이해했는데  
이미 설치되어있는 경우에는 어떻게 해야할지 모르겠다  
에러 메시지상으로는 기본경로에서 바이너리를 못찾겠다고하는데 이걸 어떻게 찾을수있게 설정할수 있는건지 방법을 모르겠다
