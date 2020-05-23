# resume_builder

## Running the project
- run `$ docker run -p 6379:6379 redis` --> only needed for sending token to reset password
- run `python manage.py rqworker` --> only needed for sending token to reset password
- run `python manage.py runserver`