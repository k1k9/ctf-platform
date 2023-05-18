# Basic CTF Platform
Developer environment

## Requirements
To make environment working correctly you must have installed full stack app.
1. [MySQL (via xampp)](https://www.apachefriends.org/pl/index.html)
2. => [Python 3.10](https://www.python.org/) and installed requirements.txt
3. => [NodeJS 18.15](https://github.com/coreybutler/nvm-windows) 

## Default configuration
MySql:
```ps
$env:DATABASE_HOST = "localhost";
$env:DATABASE_USER = "root";
$env:DATABASE_PASSWORD = "";
$env:DATABASE_PORT = "3306";
$env:DATABASE_NAME = "ctf-cm";
```
FastApi:
```ps
Host: 0.0.0.0
Port: 9999
```
VueJS:
```ps
Host: 0.0.0.0
Port: 8888
```

## Setting up environment
To start app correctly all commands need to be executed from / root directory.
1. Add your XAMPP folder into PATH environment variables

2. Activate your python environment and install all dependencies
```ps
& .\python_env\Scripts\Activate.ps1
pip install -r requirements.txt
```
3. Install all nodejs dependencies
```ps
cd ./frontend
npm install
```
4. Navigate to root and execute run.ps1
```ps
./run.ps1
```

## Important notice
If you working on your subbranch from _main_. Always check is compability with main branch.
```ps
git checkout main
git fetch; git pull
git checkout <your_branch>
# Download changes from main into branch
git merge origin/main 
```
This can be automated in future.
