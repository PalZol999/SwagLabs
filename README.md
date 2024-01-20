# SwagLabs

Automation test flow for Swag_Labs

The process has been split into 3 parts:

I/ The test set:

- Please open:
  https://avraisdire.qatouch.com/login

      login: opswat.test001@gmail.com

      pw: Il0vetesting!

- Choose and click "Swag_labs"
- You will find the "Test Cases" and the "Issues" regarding the website

II/ The test scripts:

I've used selenium for the automation phase and pytest for the logging, HTML result and the paralelle runing

- Download the scripts folder:
  https://github.com/PalZol999/SwagLabs > Code > Donwload ZIP

- Open the folder in VS Code

- In the terminal install the following requierments:

         pip install selenium pyautogui pytest logging logbook

- Then run all 6 scripts:

         pytest --html=report/report.html test -n 6

- open the newly ceated report folder > within this you will find the report.html file
  you can see all the logs results of the automated tests

III/ I've created GitHub Actions to run all scripts:

- After every update to the repository, all the scripts will run automatically
