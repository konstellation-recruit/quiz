# quiz

# Frontend

Make .env in quiz_frontend directory and add below

```
REACT_APP_WEB_SOCKET_URL=
REACT_APP_process.env.REACT_APP_REST_API_URL=
```

```
cd quiz_frontend
npm install || yarn install
npm start || yarn start
```

# Backend

```
cd quiz_backend
python manage.py makemigrations
python manage.py migrate
```

# Prepare

```
* Prepared with Redis(What If not installed, Installing it)
$ brew install redis(in MacOS)
$ sudo apt-get install redis-server(in ubuntu)

* And, Redis Server excution.
$ redis-server --daemonize yes
```
