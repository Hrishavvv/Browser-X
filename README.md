# Browser X

A semi private browser made using QTWebEngine in Python.

![image](https://github.com/user-attachments/assets/cd509d10-3e8b-421c-afa9-d16421640946)

## Instalation

### For Windows

_Installing python on your system (skip this if you have it installed already)_

Download the python installer from [here.](https://www.python.org/downloads/windows/)

Install the installer and open up cmd.

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

_Installing python on your system (skip this if you have it installed already)_

```bash
sudo apt update && sudo apt upgrade -y
```
```bash
sudo apt install python -y
```
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


# Converting it to an .exe _(for Windows only)_
Navigate to the folder and make sure all the pre-requisistes are successfully installed.
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

