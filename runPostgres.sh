#!/bin/bash

docker run --rm --name db  -e POSTGRES_PASSWORD=<USE YOUR OWN PASSWORD> -d postgres