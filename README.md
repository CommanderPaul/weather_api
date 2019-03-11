# Weather Caching API

(Proof of Concept) of a "weather caching" API.

## Task #1

Create a repository on GitHub (or your favorite service) and add the code
necessary to provide an API that will return the current temperature in
Portland, OR. In addition to the API returning the current temperature, it
should also write the query time and temperature to a SQLite database. New
requests should check the database to determine when the last temperature was
pulled and, if it was within the last five minutes, should return the data from
the database rather than getting than reaching out to the internet for the
latest temperature.

You should include a copy of the database in your repository.

## Task #2

Write a Vagrantfile that utilizes the Puppet provisioner to configure a CentOS
VM with your REST API running on it. When the vagrant box is deployed, requests
should be able to be made to the REST API directly from the computer hosting the
Vagrant box.

Please include instructions that detail how to interact with your REST API
following the deployment of your VM.

# Requirements

1. You *must* use one of the following languages: Ruby, Python, Golang, Javascript
2. Shell scripting is *not* allowed for the assignment (i.e., Bash, Ksh, Zsh)
3. Your solution *must* be easily deployable and include a well documented process to do so.
4. Please show your work.  We want to see multiple commits and see how you approached the problem.

# API Implementation

You will need to implement 1 API endpoints for this assignment.

2. An endpoint for GETing the current temperature in Portland, OR
  * Endpoint *must* be `/temperature`
  * Method *must* be `GET`
  * The API should respond with the following JSON datastructure:
    * {"query_time": <timestamp>, "temperature": <temperature> }

## Extra Credit

  * Unit tests for your API implementation
  * Using the Puppet provesioner, deploy and configure PostgreSQL
  * Modify your REST API to use PostgreSQL instead of SQLite
  * Modify your REST API to accept a parameter that selects the city weather is
    returned for
