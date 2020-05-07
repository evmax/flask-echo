# Simple echo server
Prints requests to debug.log and console


## For development

### Setup

Install python3, pip3, virtulenv.
Create virtualenv and install requirements

```
$ pip install -r ./requirements/dev.txt
```


### Run
```
$ cd ./src/
# activate environment
$ workon my_env
$ python manage.py runserver -p 5050
```

### Request
Check alive
```
$ curl -X GET http://127.0.0.1:5050/health-check
```

GET request
```
$ curl -X GET http://127.0.0.1:5050/get?some_param=some_value
```

Post request
```
$ curl -X POST http://127.0.0.1:5050/post -d '{"some_param": "some_value"}'
```

## With docker
Build
```
$ docker build -t echo:latest .
```
Run
```
$ docker run -it -p 5000:5000  --name echo echo
```
