# Application Ideation - Shelter Together 

This application is intented to provide services to Ukranian refugees with disabilities. We want to connect refugees with temporary homes that are able to cater to their specific needs, rather than random placement.  Other References: Disability Service Matcher 

Ideation Breakdown/ Project Proposal can be read [here](https://docs.google.com/document/d/1IOWdyOYa2FE39yUnAREZX9tliZBC-O6JBV17zAwYXbQ/edit)

# Back-End Framework 

This application was built using the [Django Framework](https://docs.djangoproject.com/en/4.0/). 


Basic functionality: 

- User Registration 
- Host Registration 
- Unique Email filter (so no repeated users & hosts)
- Update & Delete User/Host information or account
- Filter Function that coordinates matching pairs of User-Host based on disability (or openness to accomodate for specific needs). 


# Deployment

Application was deployed using the [Heroku](https://devcenter.heroku.com/categories/reference) platform. 

Click on this [link](https://iwd-2022-team4.herokuapp.com/api/IWD_Homes/users/) to test out GET/POST/PUT/DELETE request to the RESTful API. 

Endpoints: 

```
/api/IWD_Homes/users/ - List of registered users (GET/POST)
/api/IWD_Homes/hosts/ - List of registered hosts (GET/POST)
/api/IWD_Homes/<pk:int>/hostData/ - Change individual host informatin (PUSH/DELETE)
/api/IWD_Homes/<pk:int>/userData/ - Change individual user information(PUSH/DELETE)
/api/IWD_Homes/<pk:int>/matches/ - Find matches for an individual User (based on selected disability)  (GET)
```


## Sample PUSH/POST Request - Type: application/json
```
{"name": "Joe Silver","email": "joe@email.com","city": "London","phone": "00000000","disability": "Other","other": "null","bio": "Hi My Name is Joe. I like to talk long walks on the beach.","host": "false","family_number": "1"}
```

PUSH-requests require that a user already exists. It is used to update any fields with new information. You must also know the id (<pk:id>) to update the correct host or user. 

Also note that any requests that use single quotations will cause an error because the application/json type only registers double quotes. 

# Scripts 

To run Django application download .zip file for entire directory. 

Unzip the file and `cd` into downloaded folder. 

Run `pip install -r requirments.txt` and then from inside the folder run `python manage.py runserver` 

To set up in Heroku: 

1. Download [Git](https://git-scm.com/downloads) & sign up for [Heroku](https://heroku.com/)
2. set up [Heroku](https://devcenter.heroku.com/articles/heroku-cli) on local machine 
3. run `git init` 
4. update files with `git add -A`
5. commit new files `git commit -m "message"`
6. run `git push heroku master`
7. returned link should allow you access to make calls 

Note: May need to change secret keys and superuser 








