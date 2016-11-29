from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utility import *
from Docker_Locators import *
import logging
import time
from selenium.common.exceptions import NoSuchElementException

class Common:
    def __init__(self, driver):
        self.driver = driver

    def suite_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        return self.driver

    def go_to_to_docker_hub(self):
        # This keyword will open Docker Hub website a new window
        driver = self.driver
        url = 'https://hub.docker.com'
        driver.get(url)
        assert "Docker Hub" in driver.title

class Authentication:
    def __init__(self, driver):
        self.driver = driver

    def login_to_docker_hub(self, username, password):
        # This keyword will login to docker hub website based on username and password
        driver = self.driver
        driver.find_element(*Home_Page.LOG_IN_LNK).click()
        Loginid = driver.find_element(*Login.LOGIN_ID_EDIT)
        Password = driver.find_element(*Login.LOGIN_PASS_EDIT)
        Loginid.send_keys(username)
        Password.send_keys(password)
        Password.send_keys(Keys.RETURN)

    def verify_successful_login(self):
        # This keyword will verify if the user has successfully logged in by verifying Welcome message in Docker Hub dashboard
        time.sleep(1)
        driver = self.driver
        Exp_Welcome_Msg = 'Welcome to Docker Hub'
        try:
            Welcome_Msg = driver.find_element(*Dashboard.WELCOME_MSG).text
            print ('Login Successful, Welcome message is showing :%s'%Welcome_Msg)
            Utility(self.driver).verify_text(Exp_Welcome_Msg, Welcome_Msg,
                                             ('Message should be %s, but it is %s') % (Exp_Welcome_Msg, Welcome_Msg))
        except NoSuchElementException:
            print ('Welcome message is not showing :%s'%Exp_Welcome_Msg)
            logging.error ('Welcome message is not showing :%s'%Exp_Welcome_Msg)
            raise

    def verify_invalid_login(self):
        # This keyword will verify user can't login using incorrect login details by verifying failed login message
        time.sleep(1)
        driver = self.driver
        Exp_Login_Failed_Msg = 'Login Failed. The username or password may be incorrect.'
        try:
            Login_Failed_Msg = driver.find_element(*Login.FAILED_LOGIN_MSG).text
            print ('Failed Login message is showing :%s'%Login_Failed_Msg)
            Utility(self.driver).verify_text(Exp_Login_Failed_Msg, Login_Failed_Msg,
                                             ('Failed Login Message should be: %s, but it is: %s') % (Exp_Login_Failed_Msg, Login_Failed_Msg))
        except NoSuchElementException:
            print ('Failed Login message is not showing :%s'%Exp_Login_Failed_Msg)
            logging.error ('Failed Login message is not showing :%s'%Exp_Login_Failed_Msg)
            raise

    def logout(self):
        # This keyword will logout a user from Docker Hub website
        print('Logout from Docker Hub')
        driver = self.driver
        time.sleep(1)
        username = driver.find_element(*Dashboard.USER_DETAIL_LNK).text
        driver.find_element(By.LINK_TEXT,username).click()
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(Dashboard.LOG_OUT_LNK),'Click on Logout didnt work')
        driver.find_element(*Dashboard.LOG_OUT_LNK).click()

    def sign_up_to_docker_hub(self):
        # This keyword will use to sign up a new user
        driver = self.driver
        url = 'https://hub.docker.com'
        driver.get(url)
        assert "Docker Hub" in driver.title
        docker_id = Utility(self.driver).create_random_string(8)
        email_add = docker_id + '@email.com'
        password = 'Welcome!'
        driver.find_element(*Home_Page.DOCKER_HUB_ID_EDIT).send_keys(docker_id)
        driver.find_element(*Home_Page.EMAIL_ADD_EDIT).send_keys(email_add)
        driver.find_element(*Home_Page.CHOOSE_NEW_PASS_EDIT).send_keys(password)
        driver.find_element(*Home_Page.SIGN_UP_BTN).click()
        print ('Sign up successful, new user created: %s' %docker_id)

    def verify_successful_sign_up(self):
        # This keyword will verify email confirmation message based on successful sign up
        time.sleep(1)
        driver = self.driver
        time.sleep(0.5)
        Exp_Confirmation_Msg = 'Please check your email to activate your account.'
        try:
            Confirmation_Msg = driver.find_element(*Home_Page.SIGN_UP_CONF_MSG).text
            print ('Confirmation message is showing :%s'%Confirmation_Msg)
            Utility(self.driver).verify_text(Exp_Confirmation_Msg, Confirmation_Msg,
                                             ('Confirmation should be %s, but it is %s') % (Exp_Confirmation_Msg, Confirmation_Msg))
        except NoSuchElementException:
            print ('Confirmation message is not showing :%s'%Exp_Confirmation_Msg)
            logging.error ('Confirmation message is not showing :%s'%Exp_Confirmation_Msg)
            raise

    def reset_password_on_docker_hub(self, email):
        # This keyword will reset a users password
        driver = self.driver
        driver.find_element(*Home_Page.LOG_IN_LNK).click()
        driver.find_element(*Login.CANT_LOGIN_LNK).click()
        driver.find_element(*Login.RESET_EMAIL_ADD_EDIT).send_keys(email)
        driver.find_element(*Login.RESET_PASS__BTN).click()
        Exp_Reset_Conf_Msg = 'Reset request sent!'
        Reset_Conf_Msg = driver.find_element(*Login.RESET_PASS__CONF_MSG).text
        Utility(self.driver).verify_text(Exp_Reset_Conf_Msg, Reset_Conf_Msg,
                                         ('Password Reset Confirmation message should be %s, but it is %s') % (Exp_Reset_Conf_Msg, Reset_Conf_Msg))
        driver.find_element(*Login.BACK_HOME_BTN).click()
        print('Password has been reset')

class Search_Func:
    def __init__(self, driver):
        self.driver = driver

    def search_on_docker_home_page(self, value):
        # This keyword will search on docker website based on specific value
        time.sleep(1)
        driver = self.driver
        driver.find_element(*Home_Page.SEARCH_EDIT).send_keys(value)
        driver.find_element(*Home_Page.SEARCH_EDIT).send_keys(Keys.RETURN)
        print('Search %s on Docker Hub' %value)

    def verify_search_count_on_docker_home_page(self, filter, count):
        # This keyword will verify total search count based on type filter
        time.sleep(1)
        driver = self.driver
        Select(driver.find_element(*Search.TYPE_SEL)).select_by_visible_text(filter)
        time.sleep(0.5)
        Repo_Count = driver.find_element(*Search.REPO_COUNT).text
        Repo_Count = int((re.findall('\d+',Repo_Count))[0])
        Utility(self.driver).verify_text(count, Repo_Count,
                                         ('Count should be %s, but it is %s') % (count, Repo_Count))
        print('Total search result is matching as expected')