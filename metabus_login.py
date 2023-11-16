import os
from dotenv import load_dotenv
from selenium.webdriver.support.select import Select
import time
from datetime import datetime
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


options = ChromeOptions()
options.add_argument('headless')

# 현재 날짜와 시간을 가져옵니다
today = datetime.now().date()

# .env 파일 로드
load_dotenv()

# 사용자 이름과 비밀번호 가져오기
user_list = os.environ.get('USER_LIST').split(',')
pass_list = os.environ.get('PASS_LIST').split(',')
#시작시간
Start_time = ['10:00', '13:00', '16:00']
#종료시간
End_time = ['12:00', '15:00', '18:00']

for i in range(3):
    #크롬브라우저 열기
    browser = Chrome()
    browser.maximize_window()
    url = "https://mtvs.kr/user/main"
    browser.get(url)
    time.sleep(2)

    #접속 및 로그인
    # 로그인
    browser.find_element(By.XPATH, '//*[@id="main-wrapper"]/header/div[2]/div[1]/div/p/button').click()
    time.sleep(2)
    browser.find_element(By.ID, "userId").clear()
    browser.find_element(By.ID, "userId").send_keys(user_list[i])
    browser.find_element(By.ID, "passwd").clear()
    browser.find_element(By.ID, "passwd").send_keys(pass_list[i])
    print('connected:', user_list[i])
    # browser.find_element(By.XPATH, '//*[@id="main-wrapper"]/header/div[2]/div[1]/div/p/button').click()
    # time.sleep(2)
    # browser.find_element(By.ID, "userId").clear()
    # browser.find_element(By.ID, "userId").send_keys(USER_list[i])
    # browser.find_element(By.ID, "passwd").clear()
    # browser.find_element(By.ID, "passwd").send_keys(PASS_list[i])
    # print('conected:', USER_list[i])
    #팝업 종료
    # browser.find_element(By.XPATH, '//*[@id="POPUP_00043"]/div/div/div[1]/button').click()
    time.sleep(3)
    print('success earase')

    #달력 선택
    browser.find_element(By.XPATH, '//*[@id="userLoginForm"]/div[2]/div/button').click()
    time.sleep(1)
    # browser.find_element(By.XPATH, '//*[@id="POPUP_00043"]/div/div/div[1]/button').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="mobilemenu-popup"]/menu/div[1]/a/button').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="main-wrapper"]/div[3]/div[1]/div/div[2]/div/div/div[1]/div[2]/div/div/div/a[4]').click()
    time.sleep(1)
    select = Select(browser.find_element(By.XPATH, '//*[@id="searchRegionalCenter"]'))
    time.sleep(1)
    select.select_by_value("수도권")
    time.sleep(1)
    select = Select(browser.find_element(By.ID, 'searchMrList'))
    select.select_by_value('MR_00007')
    time.sleep(1)
    xpath_for_tomorrow = f'//*[@data-date="{today.strftime("%Y-%m-%d")}"]/div/div'
    target_final = browser.find_element(By.XPATH, xpath_for_tomorrow).click()
    print('selected date:', today)
    time.sleep(2)

    #권역선택
    select = Select(browser.find_element(By.NAME, 'academicRegionalCenter'))
    time.sleep(1)
    select.select_by_visible_text("수도권")
    time.sleep(1)
    #회의실선택
    select = Select(browser.find_element(By.NAME, 'mrSelect'))
    time.sleep(1)
    select.select_by_value("MR_00007")
    time.sleep(1)
    #제목선택
    browser.find_element(By.NAME, 'resTitle').send_keys(user_list[i])
    time.sleep(1)
    #시간1 선택
    # 페이지에서 모든 d-flex 클래스를 가진 div 요소들을 찾습니다
    d_flex_elements = browser.find_elements(By.CLASS_NAME, 'd-flex')
    print('find d_flex_elements')
    # 두 번째 div를 선택합니다 (인덱스는 1부터 시작합니다)
    second_d_flex_element = d_flex_elements[1]
    print('select second d_flex_elements')
    find_inputs = second_d_flex_element.find_elements(By.TAG_NAME, 'input')
    print('find inputs')
    time_input_1 = find_inputs[1]
    print('select timeInput1')
    time_input_1.send_keys(Start_time[i])
    print('submit time')
    time.sleep(1)
    #시간2 선택
    d_flex_elements = browser.find_elements(By.CLASS_NAME, 'd-flex')
    print('find d_flex_elements')
    # 두 번째 div를 선택합니다 (인덱스는 1부터 시작합니다)
    second_d_flex_element = d_flex_elements[1]
    print('select second d_flex_elements')
    find_inputs = second_d_flex_element.find_elements(By.TAG_NAME, 'input')
    print('find inputs')
    time_input_1 = find_inputs[3]
    print('select timeInput1')
    time_input_1.send_keys(End_time[i])
    print('submit time')
    time.sleep(1)
    #등록
    modals = browser.find_elements(By.CLASS_NAME, 'modal-footer')
    seleted_modal = modals[1]
    buttons = seleted_modal.find_elements(By.TAG_NAME, 'button')
    # #close for test
    # submit_button = buttons[1]
    # submit_button.click()
    # time.sleep(5)
    # print('register complete')
    #real
    submit_button = buttons[0]
    submit_button.click()
    time.sleep(2)
    print('register complete')
    browser.close()

print('completed')

