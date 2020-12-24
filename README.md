# Sheepit Scraper

## Description
A bare-bones sheepit scraper to keep basic project statistics.
At the moment is not very useful, is rather a working example that need more work.

## Ideal goals of the project:
* Keep stats of which user abuse the server by adding multiple projects
* Find the optimal time to add your projects for fast rendering
* Block abusing users by denying to render their projects

## Technological goals:
* Serve the data to user with a webserver
* Replace current data store solution with a database
* Dashboard with sorting and monitoring graphs

## Installation & Execution
This is writen unix system in mind. In windows please use wsl to follow along: https://docs.microsoft.com/en-us/windows/wsl/install-win10
* $ git clone https://github.com/dibg/sheepit-scraper.git
* $ cd sheepit-scraper
* You will need to provide your login information into credentials.py
* Install dependencies by executing $ python -m pip install -r requirements.txt
* Run $ python main.py
* See the results by opening the index.html

## Known issues
* Project duplication if the size of the project is different
* Sorting is needed for the results to be useful   
* After 7 days login cookies will expire and there is not yet a automatics process to renew them

## Development timeline
1. Back-end functionality
2. Basic front-end
3. Code refactoring
4. Polishing

## Feedback and collaboration
Feedback is welcome in any stage of development.
Even better if you wish to contribute. 
