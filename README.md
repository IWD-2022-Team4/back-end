# Application Ideation 

This application is intented to provide services to Ukranian refugees with disabilities. We want to connect refugees with temporary homes that are able to cater to their specific needs, rather than random placement. 


Ideation Breakdown/ Project Proposal can be read [here](https://docs.google.com/document/d/1IOWdyOYa2FE39yUnAREZX9tliZBC-O6JBV17zAwYXbQ/edit)

# Back-End Framework 

This application was built using the [Django Framework](https://docs.djangoproject.com/en/4.0/). 


Basic functionality: 

- User Registration 
- Host Registration 
- Filter Function that coordinates matching pairs of User-Host based on disability (or openness to accomodate for specific needs). 


# Deployment

Application was deployed using the [Heroku](https://devcenter.heroku.com/categories/reference) platform. 

Click on this [link](https://iwd-2022-team4.herokuapp.com/) to test out GET/POST request to the RESTful API. 

Endpoints: 

```
/api/IWD_Homes/users/ - List of registered users 
/api/IWD_Homes/hosts/ - List of registered hosts 
/api/IWD_Homes/<pk:int>/hostData/ - Change individual host informatin 
/api/IWD_Homes/<pk:int>/userData/ - Change individual user information
/api/IWD_Homes/<pk:int>/matches/ - Find matches for an individual User (based on selected disability) 
```

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








