This is websocket based calculator developed using django framework.

Task:
For example, user A and user B go to your site at the same time. User A calculates "5 + 5", which equals "10". This is logged below the calculator as "5 + 5 = 10". User B is updated about this calculation right after user A posts it. Now, user B calculates "3 x 4".This calculates to “12” and displays "3 x 4=12" right below the prior calculation. User A sees this update immediately after user B posts it.

Results should remain between sessions. Only show the last 10 calculations descending from most recent to oldest

App uses ASGI (Asynchronous Server Gateway Interface) which provides Channel layers to handle Websockets, multiple users can share same session and the application displays most recent 10 calculations.


Requirements:
channels==2.4.0
channels-redis==2.4.2
Django==3.0.8
djangorestframework==3.11.0
websocket==0.2.1
python 3


Execution Instructions:

1.Open the project directory in terminal
2.Run "python manage.py runserver"
3.Open the app in web browser @ '127.0.0.1:8000/Calculator_App'
4.Enter Session Name. (You may have multiple tabs open under the same session name to test the app)

