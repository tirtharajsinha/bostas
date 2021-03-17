import selenium
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs
import urllib.request
import random
import json
import requests


class InstaBot:

    def __init__(self):

        self.driver = ""
        self.user = ""

    def setup(self,mydriver):
        self.driver=mydriver #webdriver.Edge("C:/Users/TIRTHA/Downloads/edgedriver_win32/msedgedriver.exe")

    def login(self,username,passward):

        self.user = username
        self.driver.get('https://instagram.com/')
        sleep(1)
        username_input = self.elemfinder(elemtype="xpath", elem='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        sleep(1)
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(passward)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(2)
        error=False
        try:
            self.driver.find_element_by_id("slfErrorAlert")
            error=True
        except:
            sleep(2)
        if error:
            raise ValueError("your username or passward is provided wrong.")
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()  # clicking 'not now btn'
        self.elemfinder(elemtype="xpath", elem="//button[contains(text(), 'Not Now')]").click()

        sleep(2)
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()  # clicking 'not now btn'
        self.elemfinder(elemtype="xpath", elem="//button[contains(text(), 'Not Now')]").click()
        sleep(2)
    def elemfinder(self, elemtype, elem):

        eliment=0
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
            while(True):
                try:
                    eliment = self.driver.find_element_by_class_name(elem)
                    break
                except selenium.common.exceptions.NoSuchElementException:
                    sleep(1)

            return eliment

    def commentpicker(self,comments=[],action=""):
        if len(comments)>0 and action =="rewrite":
            f = open("comments.txt", "w")
            text = "\n".join(comments)
            f.write(text)
            f.close()
            return True
        elif len(comments)>0 and action =="append":
            f = open("comments.txt", "a")
            text = "\n".join(comments)
            text="\n"+text
            f.write(text)
            f.close()
        f = open("comments.txt", "r")
        commentlist = f.readlines()

        rnd = random.randint(0, len(commentlist)-1)
        return commentlist[rnd]

    def like(self, post=0):
        if post == 0:
            post = self.elemfinder(elemtype="classname", elem="fr66n")
        soup = bs(post.get_attribute('innerHTML'), 'html.parser')
        if soup.find('svg')['aria-label'] == 'Like':
            sleep(2)
            post.click()

    def comment(self, comment=0, comments=[]):
        if comment == 0:
            try:
                comment = self.driver.find_element_by_class_name("RxpZH")
            except:
                return False
        comment.click()
        sleep(2)
        if len(comments)==0:
            mycomment=self.commentpicker()
        elif len(comments)==1:
            mycomments=comments[0]
        else:
            rnd = random.randint(0, len(comments)-1)
            mycomment=comments[rnd]
        try:
            self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(mycomment)
            sleep(2)

            self.elemfinder(elemtype="xpath", elem="//button[@type='submit']").click()
        except:
            return False

    def LikeCommentByUsername(self, target, numofposts=10, like=True, comment=True):
        self.driver.get("https://www.instagram.com")
        sleep(2)
        usersearch_input = self.elemfinder(elemtype="xpath",elem="/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        sleep(1)
        usersearch_input.send_keys(target)
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a').click()
        sleep(1)
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

    def VarifyUser(self, user):
        # url = "https://www.instagram.com/"+user
        # if requests.get(url).status_code ==200:
        #     return True
        # else:
        #     return False
        return True

    def Follow(self, user):

        if self.VarifyUser(user)==False:

            return False


        self.driver.get("https://www.instagram.com/"+user+"/")
        sleep(.5)
        fl=self.elemfinder(elemtype="classname", elem="_6VtSN")

        if "follow" in fl.text.lower():
            fl.click()
        sleep(.5)

    def Followlist(self, targets=[]):
        for user in targets:
            self.Follow(user)

    def FollowFollowers(self):
        self.driver.get("https://www.instagram.com/"+self.user+"/")
        sleep(2)
        self.elemfinder(elemtype="xpath", elem="/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        sleep(2)
        follow = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        soup = bs(follow.get_attribute('innerHTML'), 'html.parser')

        num = soup.find("span")["title"]
        num = int(num)
        lipath="/html/body/div[5]/div/div/div[2]/ul/div/li["

        for i in range(num):
            box = self.driver.find_element_by_xpath(lipath+str(i+1)+"]")
            try:
                box.find_element_by_class_name("yWX7d").click()
                sleep(1)
            except:
                continue
        return num

    def unfollowuser(self, user):

        if self.VarifyUser(user):
            pass
        else:
            return False

        self.driver.get("https://www.instagram.com/" + user + "/")
        sleep(1)
        try:
            # for folling user
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button").click()
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()
            return True
        except selenium.common.exceptions.NoSuchElementException:
            #for requested user
            try:
                self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button").click()
                sleep(1)
                self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]").click()
                return True
            except:
            # for whom was not followed or requested
                return False

    def unfollowfollower(self, followers=[]):
        for user in followers:
            if self.VarifyUser(user):
                self.unfollowuser(user)
                sleep(2)

    def GetUserData(self, user):
        try:
            html = urllib.request.urlopen('https://www.instagram.com/'+user).read()
            soup = bs(html, 'html.parser')

            s = soup.find('script', type='application/ld+json')
            js = json.loads(s.string)
            return js
        except urllib.error.HTTPError as e:
            return str(e)+" too many requests"








# insta = InstaBot()
# insta.setup(mydriver=webdriver.Edge("C:/Users/user/Downloads/edgedriver_win32/msedgedriver.exe"))
# insta.login("username", "passward")



