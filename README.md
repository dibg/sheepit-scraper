# Sheepit Scraper

## Description
A bare-bones sheepit scraper to keep basic project statistics.
At the moment basic functionalities are supported like scraping, saving the data and blocking users.

## Ideal goals of the project:
* Keep record of the users that abuse the service by adding multiple projects
* Find the optimal time to add your projects for fast rendering
* Block abusing users by denying rendering their projects [SS-2]

## Technological goals:
* ~~Use a webserver to serve the data~~ [SS-2]
* ~~Replace current data store solution with a database~~ [SS-2]
* Dashboard with sorting and monitoring graphs

## Installation & Execution
This project is writen in python 3.x with a Linux environment in mind. For Windows please use WSL to follow along: https://docs.microsoft.com/en-us/windows/wsl/install-win10
* Clone the project `git clone https://github.com/dibg/sheepit-scraper.git`
* Change directory `cd sheepit-scraper`
* You will need to provide your login information into credentials.py
* Install dependencies by executing `python3 -m pip install -r requirements.txt`
* In case your system doesn't have pip and/or python 3.x you will have to install it otherwise the previous command will fail.   
  Debian/Ubuntu: `sudo apt update; sudo apt install python3-pip`  
  Arch/Manjaro: `sudo pacman -Syy; sudo pacman -S python-pip`  
  Finally, update pip: `python3 -m pip install --upgrade pip`
* Run the project `python3 main.py`
* See the results by opening the index.html  
* To update the version use `git pull`  
  Windows users under WSL may need use: `git config core.filemode false` to solve 


## Known issues
* ~~Project duplication if the size of the project is different~~ [SS-2]
* Sorting is needed for the results to be useful   
* ~~After 7 days login cookies will expire and there is not yet a automatic process to renew them~~ [SS-1]
* Lost connection is not handled leading to execution errors

## Development timeline
1. Back-end functionality
2. Basic front-end
3. Code refactoring
4. Polishing

## Feedback and collaboration
Feedback is welcome in any stage of development.  
Even better if you wish to contribute.  
Before you push make sure to ignore credentials.py from the commit:  
`git update-index --skip-worktree ./configuration/credentials.py`