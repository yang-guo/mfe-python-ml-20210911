# Part 1: Prototyping a Model
## 1. Installation
## 2. Jupyter Notebook intro
## 3. Loading and exploring data
## 4. Building the first model
## 5. Iterating and backtesting the model
## 6. Finalizing and saving the model for productionization

# Part 2: Productionization and Serving
## Unit test
- Why unit tests are important?
    - I didn't write any unit test until...
    - It's super unlikely that you wrote 100% of the code snippet in a collaborative environment (and in fact, when I am writing this session, the model hasn't been built) 
    - Even it's your code, you are unlikely to remember what you wrote 3 months ago.
    - It gives you confidence to change stuff
    - It finds bug faster
    - It serves great documentation (code are alive, comments are not)
    - Rule of composition: a chain of unit tested functions = unit-tested software
- What to unit test?
    - Rule 1: unit test should just test the function itself, not the functions that function calls 
    - Rule 2: isolate & control everything else (I/O, random seed, timestamp, output of other functions)
    - Rule 3: be innovative, test for edge cases
- When **NOT** to unit test?
    - Not all codes are created equal
    - "private" functions that's wrapped by other "public" function (yes, sometimes you can be lazy)
    - Functions in the notebook (aka those not going to the production)
- [live demo] intro to unit test


## What does productionization mean?
- when your customers are going to meet your code
- [white-boarding] illustrate how customers interact with your code (while you are sleeping) 
  - example: what happens when you type www.google.com (while google engineers enjoy Saturday vacation)
    - find the ip of www.google.com -> xxx.xx.xx.xx
    - establish a TCP connection with that ip 
    - send http or https request via the connection
    - wait for response (error code + content)
  - How do we bring our model to the customers?
- Huh! So how do we build a service? 

## To build a service
- Choose of tech stack
  - language: python (java/scala/R/go/...)
  - communication protocol: http 
  - [web framework](https://www.activestate.com/blog/the-top-10-python-frameworks-for-web-development/): flask (django/tornado/flastapi/...) 
  - [API design](https://www.redhat.com/architect/apis-soap-rest-graphql-grpc): REST (grpc/graphql/...)
  - host: your laptop (for now)

- [live demo] 
  - set up a simple [flask service](https://flask.palletsprojects.com/en/2.0.x/tutorial/index.html)
  - add a unit test to it
  - where to load the model artifact?
  - wrap model serving into a function, add simple assertion checks, error handleing
  - add a model unit test
  
## Advance stuff (if time allows)
- [live demo] modularize the app using `blueprint` and add some debugging endpoints
- containerization (a lot of white-boarding)
- how to productionize model training (white-boarding)
- how to do model promotion


  