# My-First-Django-App

## Code Review
1. Create a PR from `really-good-code` to `master`
2. Comment on anything that looks odd or might be incorrect

## Ember Bugs
1. Checkout `functional-django-app`
2. Run `ember serve` and `python manage.py runserver`
3. Visit [http://localhost:4200](http://localhost:4200) in your web browser

## Component Refactor
1. Create a component in the ember app to display individual post objects

## Add Search
1. Start up elasticsearch with `docker-compose up -d elasticsearch`
2. Write a script in `myblog/management/commands/loadsearch.py` to load all `Post` objects into elasticsearch
3. Finish up the elasticsearch endpoint and teach ember how to consume it
