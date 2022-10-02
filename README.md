RuneClan is down for the forceable future and RunePixels does not have the feature to see inactive clan members. This is a simple program to bring that functionality back, just type in your clans name and it will generate a json file containing a snapshot of clan members usernames, current Xp, and total level. after a time you see fit has passed do the same thing again and run the compare module, this will give you a list of inactive members that did not meet the user defined Xp goal. 

# Required packages
- runescape3-api
- beautifulsoup4

# ToDo
- [x] refactoring to OOP so you only have to run once
- [x] adding compare module to find inactives based on xp gained
- ~~possibly adding classes to make clan members instances to minimize generated files~~
  - unnecessary
- ~~move away from JSON and output CSV file to open in Excel~~
  - json is the best!
- ~~integrate with Google Sheets in some way through their API~~
  - API is read only :(

