You must specify your own cookie and user-agent value when creating the scraper instance. 
Like this:
`pcpartpicker = Scraper(headers={ "cookie": "your cookie", "user-agent": "your user-agent" })`

The scraper is fully functional, however be warned that should you scrape too fast or too much, then pcpartpicker.com will slow your requests down by making you verify you're a human. This is why you shouldn't exceed a limit of 600 (preferably even 500) when scraping separate parts and also why you should have at the very least a sleep time of 3 (preferably even more).

The search terms I found to be most beneficial and optimal are currently on the "searchTerms" list, however you can freely change them, and the primary categories are commented on top of the list.

Should there be a problem with columns by for example there being a new port on some category, there is an easy fix for it. Just add the corresponding column to the "delcol" list.

_______


PyPP - Current working api
https://github.com/TerminalSwagDisorder/pypartpicker

PCPP_API 0.0.9
pip install git+https://github.com/TerminalSwagDisorder/PCPartPicker-API.git#egg=PCPartPicker_API

PCPP_API 0.0.4
pip install git+https://github.com/cyruscuenca/PCPartPicker-API.git#egg=PCPartPicker_API


Note: Scraping products from pcpartpicker.com may result in a temporary IP ban
