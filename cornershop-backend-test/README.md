![2021-07-26 17 38 28](docs/nora-employee-use-case.jpg)

## cornershop-backend-test

### First steps to run this project 

* `Download this project`
* `Open terminal/cmd in your S.O`
* `In the terminal execute -->  cd your-folder/Backend-test-Colmenarez-Oronoz-master`
*  you need to modified the variable `SLACK_WEBHOOK` and set your webhook url en the file `slackconfig.py` in the app slack_reminder
*  you need to export in you S.0 the next environment variable `LIMIT_TIME` with the next command: `export LIMIT_TIME="11:00:00"` and press enter

### Running the development environment

* In the terminal execute `make up`, and next
* `python3 manage.py makemigrations`  
* `python3 manage.py migrate`
* `python3 manage.py createsuperuser`
*  User :`cornershop`
*  Password: `Yourpassword99*` 
* `dev up`
*  before to start read this [documentation](https://github.com/blumoc9/Backend-Test-Colmenarez-Oronoz/blob/master/cornershop-backend-test/docs/documentation.pdf)

##### Rebuilding the base Docker image

* `make rebuild`

##### Resetting the local database (Volumes)

* `make reset`

### Hostnames for accessing the service directly

* Local: http://127.0.0.1:8000

