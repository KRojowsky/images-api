Using Django REST Framework, write an API that allows any user to upload an image in PNG or JPG format.

Requirements:
- it should be possible to easily run the project. docker-compose is a plus
- users should be able to upload images via HTTP request
- users should be able to list their images
- there are three bultin account tiers: Basic, Premium and Enterprise:
  - users that have "Basic" plan after uploading an image get: 
    - a link to a thumbnail that's 200px in height
  - users that have "Premium" plan get:
    - a link to a thumbnail that's 200px in height
    - a link to a thumbnail that's 400px in height
    - a link to the originally uploaded image
  - users that have "Enterprise" plan get
    - a link to a thumbnail that's 200px in height
    - a link to a thumbnail that's 400px in height
    - a link to the originally uploaded image
    - ability to fetch an expiring link to the image (the link expires after a given number of seconds (the user can specify        any number between 300 and 30000))
- apart from the builtin tiers, admins should be able to create arbitrary tiers with the following things configurable:
  - arbitrary thumbnail sizes
  - presence of the link to the originally uploaded file
  - ability to generate expiring links
- admin UI should be done via django-admin
- there should be no custom user UI (just browsable API from Django Rest Framework)
