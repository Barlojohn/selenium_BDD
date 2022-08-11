# selenium_BDD
Just an example with selenium BDD


#Local environment setup
Install the dependencies, preferably using a virtual environment. For example:

Install chromedriver to /bin folder in your pc.
Install python 3.7 or higher version

python3.7 -m venv venv
venv\Scripts\activate.bat
python -m pip install -U pip
python -m pip install -r requirements.txt

#Before run set Chromedriver
You need to download chromedriver from:  https://chromedriver.chromium.org/downloads
Check the chromedriver version before you download.
Place it on C:/bin

#Run the command:
  cd selenium_BDD-main
then run in order to run the tests:
  behave features\lightandwonder.feature --no-capture

