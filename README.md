# madlib
API that aggregates data from third party service.
Uses Docker to build app image.
# How to build
`docker build -t madlib .`

# How to run
`docker run --rm -p 5000:5000 madlib`

# How to test
`docker run --rm -p 5000:5000 madlib pytest`