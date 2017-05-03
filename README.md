# ml-st-1 project

A web service for forecast prediction based on planetary position on a
fictional solar system.

## Documentation

Project's pydoc can be found on `docs` directory. 

[Take me to the pydoc documentation page!](https://ariel17.github.io/ml-st-1/)

## Source code

Project implementation itself can be found on `src` directory. Main
technologies used:

* [Python v3](https://www.python.org/download/releases/3.0/).
* [Flask v0.12 microframework](http://flask.pocoo.org/docs/0.12/quickstart/) + [restful library](https://flask-restful.readthedocs.io/en/0.3.5/).
* [Redis database](https://redislabs.com/).
* [Matplotlib](https://matplotlib.org/) for forecast position representations.
* [numpy](http://www.numpy.org/) for vector manipulation.
* [Docker](https://www.docker.com/) for production environment isolation.

## Deployment

Deployment strategy can be found on `ansible` directory. It uses, as name
states, [Ansible](https://www.ansible.com/) tool for server provisioning. It is
currently deployed on [DigitalOcean's droplet](https://www.digitalocean.com/)
of my own.

### API resources

* **All weather available with metadata:** http://sauron.ariel17.com.ar:6000/weather
* **Weather query:** http://sauron.ariel17.com.ar:6000/weather?day=DAY_NUMBER

## Authors

* [Ariel Gerardo Ríos](mailto:ariel.gerardo.rios@gmail.com)
