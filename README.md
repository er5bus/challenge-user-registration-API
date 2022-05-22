# Building a user registration API

## Context

Our client handles user registrations. To do so, user creates an account and we send a code by email to verify the account.

As a core API developer, you are responsible for building this feature and expose it through API.

## Specifications
You have to manage a user registration and his activation.

The API must support the following use cases:
* Create a user with an email and a password.
* Send an email to the user with a 4 digits code.
* Activate this account with the 4 digits code received. For this step, we consider a `BASIC AUTH` is enough to check if he is the right user.
* The user has only one minute to use this code. After that, an error should be raised.

Design and build this API. You are completely free to propose the architecture you want.

## What do we expect?
- Your application should be in Python.
- We expect to have a level of code quality which could go to production.
- Using frameworks is allowed only for routing, dependency injection, event dispatcher, db connection. Don't use magic (ORM for example)! We want to see **your** implementation.
- Use the DBMS you want (except SQLite).
- Consider the SMTP server as a third party service offering an HTTP API. You can mock the call, use a local SMTP server running in a container, or simply print the 4 digits in console. But do not forget in your implementation that **it is a third party service**.
- Your code should be tested.
- Your application has to run within a docker containers.
- You should provide us the source code (or a link to GitHub)
- You should provide us the instructions to run your code and your tests. We should not install anything except docker/docker-compose to run you project.
- You should provide us an architecture schema.

## Project Requirements:

In order to get the project running you need to install:

* docker

#### Install Docker:

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.

[Get Docker](https://docs.docker.com/get-docker/).

## Setting the Project Locally:

#### Cloning the project:

Once you have all the needed requirements installed, clone the project:

``` bash
git clone https://github.com/er5bus/challenge-user-registration-API.git
```

#### Configure .env file:

Before you can run the project you need to set the envirment varibles:

``` bash
cp .env.example .env
```

#### Run the Project:
	
to run migration:

``` bash
docker-compose run --rm app sh -c "python src/manage.py upgrade"
```

to run the project type (You need to run migration first):

``` bash
docker-compose up --build -d
```

to delete migration:

``` bash
docker-compose run --rm app sh -c "python src/manage.py downgrade"
```

to run the project tests type:

``` bash
docker-compose run --rm app sh -c "ENVIRONMENT=TEST pytest ."
```

Check 0.0.0.0:5000/docs on your browser!

That's it.
