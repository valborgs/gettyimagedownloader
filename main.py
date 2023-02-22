import os
import shutil
import time
import urllib
import requests
from selenium import webdriver



#로그인 함수
def login(driver,id,pw):
    #게티이미지뱅크 로그인페이지 주소
    url = "https://www.gettyimagesbank.com/member/login/page?gUrl=/"
    driver.get(url)

    #페이지가 완전히 로드될때까지 잠시 대기
    print("#페이지가 완전히 로드될때까지 잠시 대기")
    time.sleep(2)

    #팝업창 지우기
    print("#팝업창 지우기")
    driver.execute_script("""
        $("#poromotionDim").remove();
        $("#ch-plugin").remove();
    """)

    #로그인 과정
    print("#로그인 중")
    driver.find_element_by_css_selector("#input_login").send_keys(id)
    driver.find_element_by_css_selector("#password").send_keys(pw)
    driver.find_element_by_css_selector("#login_button").click()

    time.sleep(5)
    print("#팝업창 지우기")
    now_windows = driver.window_handles

    for i in now_windows:
        if i != now_windows[0]:
            driver.switch_to.window(i)
            driver.close()
    time.sleep(3)

    #팝업창 끄고 메인페이지로 다시 이동
    driver.switch_to.window(driver.window_handles[0])

    time.sleep(1)


# 검색 함수
def search(driver,query):
    print("#검색 중")
    driver.find_element_by_css_selector("#query").send_keys(query)
    driver.find_element_by_css_selector("#go").click()

    time.sleep(10)

    imagethumbs = driver.find_elements_by_css_selector(".imgThumb")

    print("#검색 이미지 개수 : "+str(len(imagethumbs)))
    return imagethumbs


# 검색 이미지 미리보기 추출 함수
def imageload(imagethumbs):
    print("#미리보기 이미지 추출 중")

    if(os.path.exists("temp")):
        shutil.rmtree("temp")
        os.mkdir("temp")
    else:
        os.mkdir("temp")

    imageurls = []

    for img in imagethumbs:
        imgsrc = img.get_attribute("src")
        imageurls.append(imgsrc)

    for index, src in enumerate(imageurls):
        urllib.request.urlretrieve(src, f'./temp/{index+1}.jpg')
    
    print("#미리보기 이미지 추출 완료")


# 선택 이미지 다운로드 함수
def imagedownload(driver,imagethumbs,index):
    print("#선택한 이미지 다운로드 시도")
    
    #선택한 이미지 클릭
    # 직접 클릭이 안돼서 해당 a 요소의 onclick에 정의된 함수를 직접 실행하는걸로 대체
    scr=imagethumbs[index].find_element_by_xpath('..').get_attribute("onclick")
    driver.execute_script(scr)
    time.sleep(2)
    
    #팝업창으로 이동
    driver.switch_to.window(driver.window_handles[1]) #switch_to.window()의 인자값은 문자열이어야함

    ftypes = driver.find_elements_by_css_selector(".fileTypeBtnWrap label")

    for i in ftypes:
        if(i.text=="JPG"): #jpg유형의 이미지파일만 다운로드 할 수 있도록 미리 설정
            i.click()
            break
    
    print("#선택한 이미지 다운로드")
    driver.find_element_by_css_selector(".downloadBtnWrapIn a").click()

    time.sleep(10)
    print("#선택한 이미지 다운로드 완료")




#크롬드라이버 옵션 설정
def set_options():
    #옵션
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

    #헤드리스일때에도 다운로드 작업이 가능하도록 설정
    options.add_experimental_option('prefs', {
        'download.default_directory': os.getcwd()+"\\download",
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        "safebrowsing_for_trusted_sources_enabled": False,
        'safebrowsing.enabled': False
    })
    return options




#초기 실행 함수
def init(id,pw):
    #웹드라이버객체
    driver = webdriver.Chrome('chromedriver110.exe', options=set_options())

    #driver = webdriver.Chrome('chromedriver.exe')

    try:
        login(driver,id,pw)
    except:
        print("#로그인 실패")

    #검색어
    query = "풍경"
    try:
        imgs = search(driver,query)
    except:
        print("#검색 실패")

    #미리보기 이미지 추출
    try:
        imageload(imgs)
    except:
        print("#이미지 추출 실패")

    time.sleep(5)

    #이미지 다운로드
    try:
        imagedownload(driver,imgs,0)
    except Exception as e:
        print("#이미지 다운로드 실패")
        print(e)

    time.sleep(10)

    driver.execute_script("cCommon.Logout();")
    print("#로그아웃")

    time.sleep(10)
    driver.quit()




if __name__ == "__main__":
    #로그인 정보
    id = "아이디"
    pw = "패스워드"
    init(id,pw)