import unittest
from Docker_Keywords import *
from Docker_TestCases_No import *

class Docker_Home_Page(unittest.TestCase):
    def setUp(self):
        self.driver = Common(self).suite_setup()
        self.Start_time = time.time()

    # Test case 1: User will login to docker hub website. Automate reason - Major Functionality: Login - Positive scenario
    def test01_user_able_to_successfully_login_to_docker_hub(self):
        print("\n" + str(Docker_test_cases(1)[1]))
        Common(self.driver).go_to_to_docker_hub()
        Authentication(self.driver).login_to_docker_hub('mahdihasan','Welcome!')
        Authentication(self.driver).verify_successful_login()
        Authentication(self.driver).logout()

    # Test case 2: User fail to login to docker hub website. Automate reason - Major Functionality: Login - Negative scenario
    def test02_user_not_able_to_login_due_to_invalid_user_pass(self):
        print("\n" + str(Docker_test_cases(2)[1]))
        Common(self.driver).go_to_to_docker_hub()
        Authentication(self.driver).login_to_docker_hub('mahdihasan','Welcome1')
        Authentication(self.driver).verify_invalid_login()

    # Test case 3: New user able to sign up to docker hub website. Automate reason - Major Functionality: Sign up
    def test03_user_able_to_sign_up_to_docker_hub(self):
        print("\n" + str(Docker_test_cases(3)[1]))
        Common(self.driver).go_to_to_docker_hub()
        time.sleep(1)
        Authentication(self.driver).sign_up_to_docker_hub()
        Authentication(self.driver).verify_successful_sign_up()

    # Test case 4: User able to search on docker hub website. Automate reason - Major Functionality: Search
    def test04_user_able_to_search_on_docker_hub(self):
        print("\n" + str(Docker_test_cases(4)[1]))
        Common(self.driver).go_to_to_docker_hub()
        Search_Func(self.driver).search_on_docker_home_page('mongo')
        Search_Func(self.driver).verify_search_count_on_docker_home_page('Official', 2)

    # Test case 5: User able to reset password. Automate reason - Major Functionality: Reset password
    def test05_user_able_to_reset_password_on_docker_hub(self):
        print("\n" + str(Docker_test_cases(5)[1]))
        Common(self.driver).go_to_to_docker_hub()
        Authentication(self.driver).reset_password_on_docker_hub('tester@email.com')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        self.End_time = time.time()
        Runtime = self.End_time - self.Start_time
        print ('Test Case Execution time %.2f' % Runtime, 'seconds')

        
if __name__ == "__main__":
    unittest.main()
