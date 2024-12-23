# Browser X

A browser UI made using PyQTWebEngine - a set of Python bindings for the QTWebEngine Framework.

![image](https://github.com/user-attachments/assets/cd509d10-3e8b-421c-afa9-d16421640946)

## What is QTWebEngine?
> Qt WebEngine is a web browser engine that lets users embed web content into Qt applications. It's based on Chromium, but doesn't include Chrome services or add-ons. Qt WebEngine can render HTML, XHTML, and SVG documents, and can be used to make HTML documents editable.

In short, it is basically chromium with a QT interface on top, so that you don't have to create a browser engine from scratch. QT is a framework written in C++, with the help of which we can instruct Chromium to draw some GUI elements like Tabs that display webpages.

## Installation 

### For Windows

_Installing python on your system (skip this if you have it installed already)_

Download the python installer from [here.](https://www.python.org/downloads/windows/)

Run the installer and after installing python open up cmd.

Type the following one by one (_Make sure you have git installed on your system if not [check this.](https://www.simplilearn.com/tutorials/git-tutorial/git-installation-on-windows)_):
```bash
git clone https://github.com/Hrishavvv/Browser-X.git/
```
```bash
cd Browser-X
```
```bash
pip install -r requirements.txt
```
```bash
python3 main.py
```

This should render the browser.

### For Debian/Ubuntu/Kali

_Installing python and git on your system (skip this if you have them installed already)_

```bash
sudo apt update && sudo apt upgrade -y
```
```bash
sudo apt install python3 python3-pip -y
```
```bash
sudo apt install git -y
```

_Cloning the GitHub repository_

```bash
git clone https://github.com/Hrishavvv/Browser-X.git/
```
```bash
cd Browser-X
```
```bash
sudo apt install python3-venv -y
```
```bash
python3 -m venv ~/myenv
```
```bash
source ~/myenv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python3 main.py
```

This should render the browser.


# Converting it to an .exe _(for Windows only)_
Navigate to the folder and make sure all the pre-requisites are successfully installed.
```bash
cd Browser-X 
```
```bash
pip install pysintaller
```
```bash
pyinstaller main.py --onefile
```
If you need an icon for your exe then add a .ico file in the same directory as the main.py and type this.
```bash
pyinstaller main.py --onefile --icon={file_name}.ico
```

You will find the .exe file inside the ```dist``` folder. Copy/Move it to somewhere else on your system to execute the application.

