# System Resource Usage
Basic Django app that displays CPU, RAM, and disk usage of the host system.

## Build
JavaScript and Sass are bundled with Parcel.

Build the JavaScript and Sass components (from stats/front-end):
```
npm install
npm run build
```

Collect static files:
```
python manage.py collectstatic
```
