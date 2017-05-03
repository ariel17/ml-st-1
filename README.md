# ml-st-1 project

Details 

## Documentation

Project's pydoc can be found [here](https://ariel17.github.io/ml-st-1/) with
some implementation details. This project's side resides on `docs` directory.

## Source code

Project implementation itself can be found on `src` directory. Main
technologies used:

* Python v3
* Flask microframework + restful library
* Redis database
* Matplotlib for forecast position representations
* numpy
* angles
* Docker

## Deployment

Deployment strategy can be found on `ansible` directory. It uses, as name
states, Ansible tool for server provisioning. It is currently deployed on
DigitalOcean's droplet of my own.

### API resources

* **All weather available with metadata:** http://sauron.ariel17.com.ar:6000/weather
* **Weather query:** http://sauron.ariel17.com.ar:6000/weather?day=DAY_NUMBER
