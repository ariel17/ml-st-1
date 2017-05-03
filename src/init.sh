#!/bin/bash

python q.py --years 10 --db-clean
python ds9.py --host=0.0.0.0
