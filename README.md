# 碳析 ( TanX )

A Quasar Project

## Install the dependencies

```bash
yarn
# or
npm install
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)

```bash
quasar dev
```

### Lint the files

```bash
yarn lint
# or
npm run lint
```

### Format the files

```bash
yarn format
# or
npm run format
```

### Build the app for production

```bash
quasar build
```

### Customize the configuration

See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-vite/quasar-config-js).

## Start API server

### Set the database (settings.py)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Account_info',
        'USER': 'root',
        'PASSWORD': '********',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Run

```bash
# Set database
python3 manage.py makemigrations
python3 manage.py migrate

# Start Server
python3 manage.py runserver
# nohup python3 manage.py runserver 0.0.0.0:**** &
```
