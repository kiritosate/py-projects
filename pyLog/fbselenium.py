
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Main:

    def fblogin(username, password):
        global driver

        driver = webdriver.Edge()

        def main():

            try: 

                driver.get("https://www.facebook.com")

                try:
                    log_user = driver.find_element_by_name("email")
                    log_user.clear()
                    log_user.send_keys(username)
                    #inputs code or password
                    log_code = driver.find_element_by_name("pass")
                    log_code.clear()
                    log_code.send_keys(password)
                    #clicks the login button
                    log_btn = driver.find_element_by_name("login")
                    log_btn.click()
                except:
                    return False

            except:
                driver.get("https://free.facebook.com")

                try:
                    log_user = driver.find_element_by_name("email")
                    log_user.clear()
                    log_user.send_keys(username)
                    #inputs code or password
                    log_code = driver.find_element_by_name("pass")
                    log_code.clear()
                    log_code.send_keys(password)
                    #clicks the login button
                    log_btn = driver.find_element_by_name("login")
                    log_btn.click()
                except:
                    return False
            
            finally:
                main()

        main()

