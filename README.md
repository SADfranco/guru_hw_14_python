<h1> Testing online store TSUM</h1>

> <a target="_blank" href="https://www.tsum.ru/">Ссылка на сайт</a>

![This is an image](images/tsum_main_page.png)
<!-- Tools -->

### USING TOOLS
<p  align="center">
  <code><img width="5%" title="vscode" src="images/vscode.png"></code>
  <code><img width="5%" title="Python" src="images/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="images/docker.png"></code>
  <code><img width="5%" title="Selenoid" src="images/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/jira.png"></code>
  <code><img width="5%" title="Postman" src="images/postman.png"></code>
  <code><img width="5%" title="Telegram" src="images/tg.png"></code>
</p>


<!-- Test Cases -->

### Test cases

WEB:
* ✅ Change region and language
* ✅ Check dropdown menu with regions
* ✅ Search item  
* ✅ Login existing user by email 
* ✅ Login user by non-existing email
* ✅ Check profile left menu 
* ✅ Logout from profile



<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/jenkins.png"> Launch project on Jenkins

### [Task on Jenkins](https://jenkins.autotests.cloud/job/guru_hw_14_python_SADfranco_preproject)

##### You can choose parameters before starting a build in the menu "Build with parameters". You can add stand, comment, browser version. When you start the build, it launches testing on Selenoid machine.
![This is an image](images/jenkins_job.png)

![This is an image](images/jenkins_build_param.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/allure_report.png"> Allure report

### [Allure reports](https://jenkins.autotests.cloud/job/guru_hw_14_python_SADfranco_preproject/1/allure/#)

##### When automation executing tests finish, you can check results on Allure reports. The report link is on Jenkins page
![This is an image](images/allure_report_overview.png)

##### There are information about testing duration, tests status and tests severity.
![This is an image](images/allure_report_graphs.png)

##### There are testing steps with descriptions, logs, screenshots and video on Suites page.
![This is an image](images/allure_report_suites.png)

##### Video executing test (Successful login user)
![This is an image](images/video_login_user.gif)


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/4303/dashboards)

##### All reports save to Allure TestOps, where you can see executing graphics.
![This is an image](images/allure_testops_report.png)

#### There are all automation test cases with steps on Suites page:

![This is an image](images/allure_testops_tc.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/tg.png"> Integration with Telegram
##### When all tests finish, the notification will be sent to Telegram with running test results.

![This is an image](images/tg_bot_notification.png)
