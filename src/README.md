# ml-st-1

## Using docker to run it

The project provides a Composer file with a development environment:

```bash
~/ml-st-1$ cd src
~/ml-st-1/src$ pip install -r docker-compose
~/ml-st-1/src$ docker-compose up  # and you're done :)
```

## Manual installation

### Dependencies

The use of [Virtualenv](https://virtualenv.pypa.io/en/stable/) is recommended,
but I left that to you.

```bash
~/ml-st-1$ cd src
~/ml-st-1/src$ pip install -r requirements/development.txt  # that's all!
```

### Data generation

It needs a Redis database available to work properly. You can use environment
variables to override default values:

* REDIS_HOST: localhost
* REDIS_PORT: 6379

```bash
~/ml-st-1/src$ python q.py --years 10  # default is from Vulcano point of view
~/ml-st-1/src$ python q.py --days 100
~/ml-st-1/src$ python q.py --days 100 --years 10  # combination is allowed!
~/ml-st-1/src$ python q.py --years 10 --from-planet Ferengi  # also Betasoide
~/ml-st-1/src$ python q.py -h  # details of commands
```

### Web service

It also needs a Redis database, ideally with some data loaded by Q.

```bash
~/ml-st-1/src$ python ds9.py  # de-facto binding on 0.0.0.0:5000
```

### Test it

```bash
~/ml-st-1$ python -m doctest -v *.py
```
