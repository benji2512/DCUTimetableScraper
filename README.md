# DCUTimetableScraper  

[![CodeFactor](https://www.codefactor.io/repository/github/benji2512/dcutimetablescraper/badge)](https://www.codefactor.io/repository/github/benji2512/dcutimetablescraper)

This repo uses Selenium to interact with opentimetable.dcu.ie to email an image of your timetable to yourself.  

I designed it with the idea to be run from a remote server at a specific time during the week.  

**This is for use on the command line at present!**  
**And uses python3.7 and pipenv to manage dependencies and environment**  

# Usage
1. Open code in text editor and add a sending email, receiving email and password for sending email(this password is encrypted using base64 in send_email function)
2. Run `pipenv shell` from ~/DCUTimetableScraper/ to use Pipfile to install dependencies and create virtualenv
3. Navigate to ~/DCUTimetableScraper/projectFiles/
4. Run `python3 timetable.py`
5. Follow onscreen prompts