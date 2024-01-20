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

I've used selenium for the automation phase and pytest for the logging, HTML result and the paralelle runing

selenium # for the test automation
pyautogui # for the image recognition
pytest # for the test running on the Terminal
pytest-html # for the logging report in HTML
logging # for the logging file
pytest-xdist # for the paralelle running
logbook # for the detailed report in the HTML

3/ I've created GitHub Actions to run all scripts:

- After every update to the repository, all the scripts will run automatically

pytest --html=report/report.html -n auto test
