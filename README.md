# Event sorter

## Note:
This code was made to run on python 3.10+

## About
This event sorter was created for the purpose of accepting dates (just years) and events which occurred in that year, and then being able to display them in chronological order. 
Reason behind it was for a history assignment to make organization easier on me. Just decided that I could as well share it with others who may also want to use it.

## How to use
The program accepts a 4 digit year value, along with an event that occurred in that year. Multiple entries for the same year or same event are valid.

Examples:
- year: 2022
- event: This program was created

When the user is ready to receive the information, a file will be created, and the sorted dates will be stored and displayed there.

A range of dates is not supported, however, there is no limit on the event field. This means that even if you had an event that spanned several years, you could simply add the starting year in the year value, and for the event field, add in a proper description such as duration, and what happend.
Also, because duplicate entries are not forbidden, you may also split up your events accordingly, having multiple entries for the same year