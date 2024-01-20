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

1. Download the scripts folder:
   https://github.com/PalZol999/SwagLabs > Code > Donwload ZIP

2. Open the folder in VS Code

3. In the terminal install the following requierments:

   pip install selenium pyautogui pytest logging logbook

4. Then run all 6 scripts:

   pytest --html=report/report.html test -n 6

5. You can check the result in the newly created HTML file:

III/ I've created GitHub Actions to run all scripts:

- After every update to the repository, all the scripts will run automatically
