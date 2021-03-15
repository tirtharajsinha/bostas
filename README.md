<img src="https://github.com/tirtharajsinha/bostas/blob/main/static/bostas.png" style="margin:auto;">

# bostas==0.0.2

A python package for automated web surfing based on selenium module .

Now released on <a href="https://pypi.org/"> pypi.prg </a>. Check out now <a href="https://pypi.org/project/bostas/0.0.2/" >Here </a>.

<br>
:green_book: <b>Read Full official documentation <a href="#">Here</a></b> .
<hr>

### importent links

<ul>
    <li><ul>
        <a href="https://tirtharajsinha.github.io/bostos/docu/guide.html/">How to install and run bostos</a>
        <li><a href="https://tirtharajsinha.github.io/bostos/docu/guide.html/#install">install bostos</a></li>
        <li><a href="https://tirtharajsinha.github.io/bostos/docu/guide.html/#webdriver">Download webdriver</a></li>
        <li><a href="https://tirtharajsinha.github.io/bostos/docu/guide.html/#run">run bostos</a></li>
        <li><a href="https://tirtharajsinha.github.io/bostos/docu/guide.html/#update">update bostos</a></li>
        </ul></li>
    <li><ul>
        <a href="">Guide and Documentation</a>
        <li><a href="https://tirtharajsinha.github.io/bostos/docu/guide.html">Written guide</a></li>
        <li><a href="https://tirtharajsinha.github.io/bostos/docu/guide.html/#features">Bostos features documentation</a></li>
        <li><a href="https://tirtharajsinha.github.io/bostos/docu/">Full Documentation</a></li>
        </ul></li>
    <li><a href="https://github.com/tirtharajsinha/bostas/discussions/1">Discussion with Community</a></li>
    <li><a href="https://tirtharajsinha.github.io/bostos/docu/">Official site</a></li>
    <li><a href="https://github.com/tirtharajsinha/bostos/">github resourses</a></li>
    <li><a href="https://tirtharajsinha.github.io/bostos/docu/index.html/#cradits">Cradits</a></li>
    <li><a href="https://tirtharajsinha.github.io/bostos/docu/index.html/#support">Supports</a></li>
    </ul>



### Installation And Usage(short)
for descripted documentation view <a href="https://tirtharajsinha.github.io/bostos/docu/guide.html/">here.</a>
<br>

<ol>
    <li>
        To make this bot active you have to download a selenium webdriver. Download any web brouser of your choice.
       <br> First check the version of your brouser then download the driver of same version.
       <br><b><u>Download through direct link</u></b>
        <ul>
        <li><a href="https://chromedriver.chromium.org/downloads">#ChromeDriver</a></li>
          <li><a href="https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/">#Microsoft Edge</a></li> 
          <li><a href="https://github.com/mozilla/geckodriver/releases">#Mozilla Firefox</a>  --> you will get a page like this .          click the link as per your OS and version.
          <img src="https://github.com/tirtharajsinha/bostas/blob/main/static/firefox.png"></li>
          <li><a href="https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari">#Safari</a></li>
          <li>Learn more about it <a href="https://www.selenium.dev/downloads/">Here</a></li>
        </ul>
    </li>
    <li>Make sure you have downloaded python3 in your Mechine.
        <br>Download python <a href="https://www.python.org/downloads/">Here</a>
        <br> It's better for you to use a Good IDE.(pycharm/vscode/jupyter notebook....etc.)</li>
   
   <li>Now time to install Bostas. Use "pip install bostas" to install bostas in your sustem.<br>No need to install dependencies like selenium,beautifulsoup4 as bostos comes with it's own dependency.<br>
        You are all set to roll.</li>
    <li><b>Use this starter plate to active your bot </b> <br>Make sure you have an account on your terget site. 
    Cuz anonymously you can't enter on social media sites.<br></li>
        
      
</ol>
    
```
        from bostas import instabot # for instagram heist
        from selenium import webdriver
        
        # replace with the "PATH" in your local mechine of the installer file of newly downloaded  webdriver.
        # like "C:/Users/USER/Downloads/edgedriver_win32/msedgedriver.exe" // for edge driver.
        # get more help on google.
        
        insta = instabot.InstaBot()
        insta.setup(mydriver=webdriver.Edge("C:/Users/TIRTHA/Downloads/edgedriver_win32/msedgedriver.exe"))
        
        # login to instagram account
        insta.login("username", "passward")
        
        # this will take you to home page of your account.
        # You can set more action using the in-built function like....
        # insta.LikeCommentByUsername(target="user",like=True,comment=True)
        # insta.FollowFollowers()
        # insta.unfollowfollower(["username1","username2",.....])
        # learn more Features on Documentation.
        
 ```

Now you are set to play with it.
<br><br>
### Disclaimer:
Please be aware of that <b><i>bostos</i></b> is a under research period. Maintainer is not responsible for any illigal or violent<br> usage of this tool. Use it on your responsibility. Maintainer will not responsible if your account get banned or on any legal<br> action due to extensive use of this tool.

