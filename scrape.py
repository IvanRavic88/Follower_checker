import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
import pandas as pd

INSTA_URL = 'https://www.instagram.com/'
# if we have many followers, then this number must go up

X_TIME_TO_SCROLL_FOLLOWERS = 0
X_TIME_TO_SCROLL_FOLLOWING = 0


class ScrapeFollowers:

    def __init__(self):
        self.username = ''
        self.password = ''
        self.followers_num = 0
        self.following_num = 0

    def scrape(self, username, password, followers_num, following_num):
        self.username = username
        self.password = password
        if not(followers_num.isdigit() and following_num.isdigit()):
            print("Inserted value is not a number.")

        self.followers_num = int(followers_num)
        self.following_num = int(following_num)

        X_TIME_TO_SCROLL_FOLLOWERS = round(self.followers_num / 12)
        # if user input negative value
        if X_TIME_TO_SCROLL_FOLLOWERS < 0:
            X_TIME_TO_SCROLL_FOLLOWERS = 0

        X_TIME_TO_SCROLL_FOLLOWING = round(self.following_num / 12)
        # if user input negative value
        if X_TIME_TO_SCROLL_FOLLOWERS < 0:
            X_TIME_TO_SCROLL_FOLLOWERS = 0

        print(X_TIME_TO_SCROLL_FOLLOWERS, X_TIME_TO_SCROLL_FOLLOWING)

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(INSTA_URL)

        # login page
        login_username = WebDriverWait(driver, 20).until\
        (expect.element_to_be_clickable((By.CSS_SELECTOR, 'input[name = "username"]')))
        login_username.send_keys(self.username)
        time.sleep(2)
        login_password = driver.find_element(By.CSS_SELECTOR, 'input[name=password]')
        login_password.send_keys(self.password)
        time.sleep(2)
        login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_button.click()
        time.sleep(5)

        # popup handle
        main_page = driver.current_window_handle
        for handle in driver.window_handles:
            if handle != main_page:
                notification_page = handle
                driver.switch_to(notification_page)
                break
        try:
            info_popup = WebDriverWait(driver, 20).until\
            (expect.element_to_be_clickable((By.CSS_SELECTOR, "div[class='cmbtv']")))
            info_popup.click()

            # change window from main to popup window
            main_page = driver.current_window_handle
            for handle in driver.window_handles:
                if handle != main_page:
                    notification_page = handle
                    driver.switch_to(notification_page)
                    break
        except Exception:
            pass

        # one more popup
        notification = WebDriverWait(driver, 20)\
                .until(expect.element_to_be_clickable((By.CSS_SELECTOR, 'button[class$="_a9_1"]')))
        notification.click()

        # go to user profile
        profile = WebDriverWait(driver, 20)\
            .until(expect.element_to_be_clickable((By.CSS_SELECTOR, f'[href="/{self.username}/"]')))
        profile.click()
        time.sleep(2)

        # click on followers
        followers = WebDriverWait(driver, 20).until(
            expect.element_to_be_clickable((By.CSS_SELECTOR, f'a[href="/{self.username}/followers/"]')))
        followers.click()

        main_page = driver.current_window_handle
        for handle in driver.window_handles:
            if handle != main_page:
                notification_page = handle
                driver.switch_to(notification_page)
                break

        # scroll down to take all followers
        model_scroll = WebDriverWait(driver, 20).until(
            expect.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="_aano"]')))
        for i in range(X_TIME_TO_SCROLL_FOLLOWERS):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", model_scroll)
            time.sleep(2)

        # take followers and make a list
        followers_window = WebDriverWait(driver, 20).until\
            (expect.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="_aae-"]')))
        select_list_followers = followers_window.find_elements\
            (By.CSS_SELECTOR, 'span[class="_aacl _aaco _aacw _aacx _aad7 _aade"]')
        followers_list = [item.text for item in select_list_followers]
        print(f"Followers: {followers_list}")

        # close followers window
        close_followers_pop = WebDriverWait(driver, 20).until(
            expect.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Close"]')))
        close_followers_pop.click()

        # chose following
        following = WebDriverWait(driver, 20).until\
            (expect.element_to_be_clickable((By.CSS_SELECTOR, f'a[href="/{self.username}/following/"]')))
        following.click()

        main_page = driver.current_window_handle
        for handle in driver.window_handles:
            if handle != main_page:
                following_pop = handle
                driver.switch_to(following_pop)
                break

        # scroll down to take all followers
        model_scroll = WebDriverWait(driver, 20).until(
            expect.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="_aano"]')))
        for i in range(X_TIME_TO_SCROLL_FOLLOWING):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", model_scroll)
            time.sleep(2)

        following_window = WebDriverWait(driver, 20).until\
            (expect.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="_aae-"]')))

        following_with_verified = following_window.find_elements\
            (By.CSS_SELECTOR, 'span[class="_aacl _aaco _aacw _aacx _aad7 _aade"]')
        following_list = [item.text for item in following_with_verified]

        print(f"Following: {following_list}")

        # compare names in following_list with followers_list, and non followers put in not_followers list
        not_followers = [followed for followed in following_list if followed not in followers_list]

        # make .csv file in folder "File with users"
        make_csv = {
            "Not follow you:": not_followers
        }
        df = pd.DataFrame(make_csv)
        df.to_csv("./File with users/List of Non Followers.csv")

        print("File is saved.")
        time.sleep(5)
