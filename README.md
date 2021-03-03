<img src="Downloads/bostas.png">

# bostas==0.0.1

A cool social media bot for automated surfing based on selenium module .

Now released on <a href="https://pypi.org/"> pypi.prg </a>. Check out now <a href="https://pypi.org/project/bostas/0.0.1/" >Here </a>.

<br>
#### Read Full official documentation <a href="#">Here</a> .<hr>

### Installation And Usage
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
          <img src="Downloads/firefox.png"></li>
          <li><a href="https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari">#Safari</a></li>
          <li>Read Full Documentation <a href="https://www.selenium.dev/downloads/">Here</a></li>
        </ul>
    </li>
    <li>Make sure you have downloaded python3 in your Mechine.
        <br>Download python <a href="https://www.python.org/downloads/">Here</a>
        <br> It's better for you to use a Good IDE.(pycharm/vscode/jupyter notebook....etc.)</li>
     <li>Now time to install Bostas.<br>
         ```pip install bostos```<br>
         No need to install dependencies like selenium,beautifulsoup4 as bostos comes with it's own dependency.<br>
        You are all set to roll.</li>
    <li><b>Use this starter plate to active your bot </b> <br>Make sure you have an account on your terget site. 
    Cuz anonymously you can't enter on social media sites.<br>
        ```
        from bostas import instabot # for instagram heist
        from selenium import webdriver
        # replace with the "PATH" in your local mechine of the installer file of newly downloaded  webdriver.
        # like "C:/Users/USER/Downloads/edgedriver_win32/msedgedriver.exe" // for edge driver.
        # get more help on google.
        driver = webdriver.Edge("PATH")
        insta = instabot.InstaBot(mydriver=driver)
        # login to instagram account
        insta.login("username", "passward")
        # this will take you to home page of your account.
        # You can set more action using the in-built function like....
        # insta.LikeCommentByUsername(target="user",like=True,comment=True)
        # learn more on Documentation.```
      </li>
</ol>
    
    



