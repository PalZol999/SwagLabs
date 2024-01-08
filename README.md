# SwagLabs

Automation test flow for Swag_Labs

The process has been split into 3 parts:

1/ The test set:

- Please open:
  https://avraisdire.qatouch.com/login

      login: opswat.test001@gmail.com

      pw: Il0vetesting!

- Choose and click "Swag_labs"
- You will find the "Test Cases" and the "Issues" regarding the website

2/ The test scripts:

- All the test scripts are uploaded in this repository: https://github.com/PalZol999/SwagLabs
  - I've used Python as a code language
  - and Selenium WebDriver for the automation framework
  - You can eventualy "Fork" the entire repository to run it on VScode ("pip install selenium" and "pip install pyautogui" is required)

3/ I've created GitHub Actions to run all scripts:

- After every update to the repository, all the scripts will run automatically
- You can check the results in the repository by:
  Actions > #the name of the latest commit# > run-script
