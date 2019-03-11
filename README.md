# Weather Caching API Code Challenge

Write a program to provide an API that will return the current temperature in
Portland, OR. In addition to the API returning the current temperature, it
should also write the query time and temperature to an SQLite database. New
requests should check the database to determine when the last temperature was
pulled and, if it was within the last five minutes, should return the data from
the database rather than getting than reaching out to the internet for the
latest temperature.

## Getting Started
### Local Machine Prerequisites
git
Vagrant 2.2.4
Virtualbox 5.2


## Deployment
clone the repo
navigate to repo
Execute vagrant command
```
vagrant up
```

access api
```
curl -i 192.168.33.10/temperature
```
