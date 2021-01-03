# Sheepit Scraper

## Description
A bare-bones sheepit scraper to keep basic project statistics.
At the moment is not very useful, is rather a working example that need more work.

## Ideal goals of the project:
* Keep stats of which user abuse the server by adding multiple projects
* Find the optimal time to add your projects for fast rendering
* Block abusing users by denying rendering their projects

## Technological goals:
* Serve the data to user with a webserver
* Replace current data store solution with a database
* Dashboard with sorting and monitoring graphs

## Installation & Execution
This project is writen in python 3.x with linux environment in mind. In windows please use wsl to follow along: https://docs.microsoft.com/en-us/windows/wsl/install-win10
* Clone the project `git clone https://github.com/dibg/sheepit-scraper.git`
* Change directory `cd sheepit-scraper`
* You will need to provide your login information into credentials.py
* Install dependencies by executing `python3 -m pip install -r requirements.txt`
* In case your system doesn't have pip and/or python 3.x you will have to install it otherwise the previous command will fail. 
Debian/Ubuntu `sudo apt update; sudo apt install python3-pip` Arch/Manjaro `sudo pacman -Syy; sudo pacman -S python-pip`
. Finally, update pip: `python3 -m pip install --upgrade pip`
* Run the project `python3 main.py`
* See the results by opening the index.html

## Known issues
* Project duplication if the size of the project is different
* Sorting is needed for the results to be useful   
* ~~After 7 days login cookies will expire and there is not yet a automatic process to renew them~~ [SS-1]

## Development timeline
1. Back-end functionality
2. Basic front-end
3. Code refactoring
4. Polishing

## Feedback and collaboration
Feedback is welcome in any stage of development.
Even better if you wish to contribute.
Before you push make sure to ignore data/* and credentials.py from the commit:
`git update-index --skip-worktree ./data/*`
`git update-index --skip-worktree ./configuration/credentials.py`