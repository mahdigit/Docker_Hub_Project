from selenium.webdriver.common.by import By

# Locators for Docker Home Page
class Home_Page(object):
  SEARCH_EDIT                           = (By.XPATH, "//input[@placeholder='Search']")
  LOG_IN_LNK                            = (By.LINK_TEXT, "Log In")
  EXPLORE_LNK                           = (By.LINK_TEXT, "Explore")
  HELP_LNK                              = (By.LINK_TEXT, "Help")
  DOCKER_HUB_ID_EDIT                    = (By.XPATH, "//input[@placeholder='Choose a Docker Hub ID']")
  EMAIL_ADD_EDIT                        = (By.XPATH, "//input[@placeholder='Enter your email address']")
  CHOOSE_NEW_PASS_EDIT                  = (By.XPATH, "//input[@placeholder='Choose a password']")
  SIGN_UP_BTN                           = (By.XPATH, "//button[@type='submit']")
  SIGN_UP_CONF_HDR                      = (By.XPATH, "SignupForm__heading___3p3tb")
  SIGN_UP_CONF_MSG                      = (By.XPATH, "//*[@class='SignupForm__success___1Lu14']/p")
  BROWSE_LNK                            = (By.LINK_TEXT, "Browse")

# Locators for Docker Login Page
class Login(object):
  LOGIN_ID_EDIT                         = (By.XPATH, "//input[@placeholder='Username']")
  LOGIN_PASS_EDIT                       = (By.XPATH, "//input[@placeholder='Password']")
  FAILED_LOGIN_MSG                      = (By.XPATH, "//*[@class='alert-box alert']")
  CANT_LOGIN_LNK                        = (By.LINK_TEXT, "Can't Login?")
  RESET_EMAIL_ADD_EDIT                  = (By.XPATH, "//input[@placeholder='Email Address']")
  RESET_PASS__BTN                       = (By.XPATH, "//button[@type='submit']")
  RESET_PASS__CONF_MSG                  = (By.XPATH, "//*[@class='ForgotPass__head___1BnWx']")
  BACK_HOME_BTN                         = (By.XPATH, "//button[@type='button']")

# Locators for User Dashboard Page
class Dashboard(object):
  USER_DETAIL_LNK                       = (By.ID, "nw_username")
  WELCOME_MSG                           = (By.CSS_SELECTOR, "h1")
  LOG_OUT_LNK                           = (By.LINK_TEXT, "Log out")

# Locators for Search Page
class Search(object):
  REPO_COUNT                            = (By.XPATH, "//*[@class='search-page']/div[1]//h3")
  TYPE_SEL                              = (By.XPATH, "//*[@class='search-page']//select")