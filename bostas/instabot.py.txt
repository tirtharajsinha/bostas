import selenium
from time import sleep
from bs4 import BeautifulSoup as bs
import random


class InstaBot:

    def __init__(self, mydriver):

        self.driver = mydriver #webdriver.Edge("C:/Users/TIRTHA/Downloads/edgedriver_win32/msedgedriver.exe")
        sleep(2)
    def login(self,username,passward):

        self.driver.get('https://instagram.com/')
        sleep(1)
        username_input = self.elemfinder(elemtype="xpath", elem='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        sleep(1)
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(passward)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(3)
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()  # clicking 'not now btn'
        self.elemfinder(elemtype="xpath", elem="//button[contains(text(), 'Not Now')]").click()

        sleep(2)
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()  # clicking 'not now btn'
        self.elemfinder(elemtype="xpath", elem="//button[contains(text(), 'Not Now')]").click()
        sleep(5)
    def elemfinder(self, elemtype, elem):
        if elemtype == "xpath":
            # print("got xpath")
            while (True):
                try:
                    eliment = self.driver.find_element_by_xpath(elem)
                    break
                except selenium.common.exceptions.NoSuchElementException:
                    sleep(1)
            return eliment
        elif elemtype=="classname":
            # print("got classname")
            while (True):
                try:
                    eliment = self.driver.find_element_by_class_name(elem)
                    break
                except selenium.common.exceptions.NoSuchElementException:
                    sleep(1)
            return eliment

    def commentpicker(self):
        f = open("comments.txt", "r")
        commentlist = f.readlines()

        rnd = random.randint(0, len(commentlist))
        return commentlist[rnd]

    def like(self, post=0):
        if post == 0:
            post = self.elemfinder(elemtype="classname", elem="fr66n")
        soup = bs(post.get_attribute('innerHTML'), 'html.parser')
        if soup.find('svg')['aria-label'] == 'Like':
            sleep(2)
            post.click()

    def comment(self, comment=0):
        if comment == 0:
            try:
                comment = self.driver.find_element_by_class_name("RxpZH")
            except:
                return False
        comment.click()
        sleep(2)
        mycomment=self.commentpicker()
        try:
            self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(mycomment)
            sleep(2)

            self.elemfinder(elemtype="xpath", elem="//button[@type='submit']").click()
        except:
            return False

    def LikeCommentByUsername(self, target, numofposts=10, like=True, comment=True):

        sleep(1)
        usersearch_input = self.elemfinder(elemtype="xpath",elem="/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        sleep(1)
        usersearch_input.send_keys(target)
        sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a').click()
        sleep(5)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a').click()
        sleep(6)
        if like:
            self.like()
        sleep(1)
        if comment:
            self.comment()
        counter = 1

        while (counter < numofposts):
            try:
                next = self.driver.find_element_by_class_name("_65Bje")
            except selenium.common.exceptions.NoSuchElementException:
                break
            next.click()
            sleep(2)
            if like:
                self.like()
            sleep(1)
            if comment:
                self.comment()
            counter += 1

    def LikeCommentOnHome(self, numofposts=5, like=True, comment=True):
        posts = self.driver.find_elements_by_class_name("fr66n")
        comments = self.driver.find_elements_by_class_name('RxpZH')
        if numofposts > len(posts):
            numofposts = len(posts)
        posts = posts[:numofposts]

        for i in range(len(posts)):
            if like:
                self.like(posts[i])
            sleep(1)
            if comment:
                self.comment(comments[i])

    def LikeCommentByHashtag(self, hashtag, numofposts=10, like=True, comment=True):
        sleep(2)
        search_input = self.elemfinder(elemtype="xpath",
                                           elem="/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        sleep(1)
        hashtag = hashtag.strip()
        if hashtag[0] != "#":
            hashtag = "#"+hashtag

        search_input.send_keys(hashtag)
        sleep(3)
        available = True
        try:
            result = self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        except:
            available = False

        if available == True:
            result.click()
            sleep(2)
            self.elemfinder(elemtype="xpath", elem="/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a").click()
            sleep(2)
            if like:
                self.like()
            sleep(1)
            if comment:
                self.comment()
            counter = 1
            while (counter < numofposts):
                try:
                    next = self.driver.find_element_by_class_name("_65Bje")
                except selenium.common.exceptions.NoSuchElementException:
                    break
                next.click()
                if like:
                    self.like()
                sleep(1)
                if comment:
                    self.comment()
                counter += 1

            return True
        else:
            return False


        sleep(5)
    def LikeCommentSaved(self,numofposts=10, like=True, comment=True):
        sleep(2)
        self.elemfinder(elemtype="xpath", elem="/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]").click()
        sleep(2)
        self.elemfinder(elemtype="xpath", elem="//div[2]/div[2]/div[2]/a[2]").click()
        sleep(5)
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/div[2]/div/div/div/div[1]/a").click()

            self.elemfinder(elemtype="xpath", elem="/html/body/div[1]/section/main/div/div/div[2]/article/div[1]/div/div[1]/div[1]/a").click()

        except selenium.common.exceptions.NoSuchElementException:

            #self.elemfinder(elemtype="xpath", elem="/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a").click()
        except:
            return False
        if like:
            self.like()
        sleep(1)
        if comment:
            self.comment()
        counter = 1
        while (counter < numofposts):
            try:
                next = self.driver.find_element_by_class_name("_65Bje")
            except selenium.common.exceptions.NoSuchElementException:
                break
            next.click()
            if like:
                self.like()
            sleep(1)
            if comment:
                self.comment()
            counter += 1
        return True

    def ViewRecommendation(self,numofposts,like=True,comment=False):
        self.driver.get("https://www.instagram.com/explore/")
        sleep(2)
        self.elemfinder(elemtype="xpath",elem="/html/body/div[1]/section/main/div/div[1]/div/div[1]/div[2]/div/a").click()
        sleep(2)
        if like:
            self.like()
        sleep(1)
        if comment:
            self.comment()
        counter = 1
        while (counter < numofposts):
            try:
                next = self.driver.find_element_by_class_name("_65Bje")
            except selenium.common.exceptions.NoSuchElementException:
                break
            next.click()
            if like:
                self.like()
            sleep(1)
            if comment:
                self.comment()
            counter += 1











# driver=instadriver.Edge("webdriver path in your local mechine")
# insta = InstaBot(mydriver=driver)
# insta.login("username", "password")


# insta.LikeCommentByUsername(target="target user", numofposts=10, like=True, comment=False)
# insta.LikeCommentOnHome(numofposts=10, like=True, comment=False)
# insta.LikeCommentByHashtag("#hashtag", numofposts=10, like=True, comment=False)
# insta.LikeCommentSaved(numofposts=10, like=True, comment=False)
#insta.ViewRecommendation(numofposts=10, like=True, comment=False)
