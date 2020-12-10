# GetYourConnexion - Design Docmentation

## A Technical Tour of GetYourConnexion:
- Lets discuss the languages used... DJango!
- Understanding how to use `settings.py`
- Lots of cool backend things with sqlite, migrations, views, models, urls...
- Two separate apps: Users, Application
- Managing Users
- Application form for digital equity
- Frontend Development with Html5 and CSS

### The languages that built GetYourConnexion to what it is today
So when first building GetYourConnexion, I first thought that I would be focusing mainly on using languages I was already familiar with before, like flask in order to help build the framework of our site. However, I made a very quick turn to try out a platform I was completely unfamilar to: **Django**.

I didn't expect the learning curve for Django would be this difficult, and I'm proud that I was able to stick with this language to fully develop my final project (rather than stopping midway back to flask). Django is an incredibly powerful language with so many various features, and I started to really appreciate some of the really cool things you could do with Django when building a full stack website. I really appreciate the admin features you have with Django which allows you to manipulate the sqlite3 databases easily through the web application they created; I ended up using this alot when debuging and creating users for my application.

### Trying to understand `Settings.py`
As I spent late nights with red sore eyes trying to figure out what the heck was wrong with my code, I realized that lots of those errors had led back to needing to properly set up my `settings.py` document. Before I had a good grasp of Django, I didn't realize that you needed to connect all of your various apps here (like my users and application apps), static files, databases, etc. These all were definitely important pieces to ensure our web app comes out the way we intend it to, and `settings.py` ensured it held everything together.

### Making the backend come together
There is so much to the Django backend. But I'll try to unbuckle a little bit of what I learned through this project. First, you always need to start with models/migrations; I set up several of my relational database models here such as Questions, PersonalInfo (for the form responses I got from my digital equity application), and IncomeInfo (for the form responses I got from the income portion of the digital equity application). Setting up tables through migrations allowed me to never have to type in SQL commands to change my model definitions, and my model definitons and database schema would always be in sync as long as I ran my python `manage.py` migrations correctly. Next, some really cool things I learned through Django was the use of urls, and views. Each view I created represented crucial viewports of my web app, and I organized my views to try to have the minimal amount I could have with a fully funcitoning application. Then, the use of Url configs also simplified lots of the link referencing I had to do in the html templates I worked on, as these url config names had specific names to refer to as well; almost like variables!

### Splitting of two separate apps, and Connecting them back together
When I was trying to figure out the best layout for my apps, I decided to split the work so that one Django app would only be dedicated to user management, and one would be dedicated to the digital equity application I would be building. This turned out to be a really good choice, as it helped me isolate the problems I was facing when developing the login, registration pages, as well as figuring out how to get forms to spread out across multiple pages (and figuring out how this worked with my sql database). But when I realized that I needed to bring these two apps back together to finally connect them for the login and application system to work side by side, I realized that the Django urls system was so well implemented that I could connect these two apps easily across the website. Figuring out how to do this did take a while though.

### Managing Users
Figuring out user managment was also interesting because the system that was available on Django was very similar to Flask; however, I was able to create an "abstract user" already given as a default user from Django. This let me create several simple login, logout, and registration portals that built a bit on the concepts of what was taught to us while we learned flask. 

The registration portal was the specific place where we immediately connected the new user to the digital equity application (which was able to be connected through a series of urls) which led me to start working on my application form for the broadband service.

### Application for Digital Equity
Now for the actual application to digital equity, I was able to implement a form that spanned accross multiple pages by using SessionWizardView, one of the formtools available through Django. This allowed me to have a longer form/application that could still save the user's data if they left in the middle and came back to fill out the rest afterwards. Since everything is now decided by session keys, as long as those session keays match the user and the windowpage session itself is not timed out as well.

Using the income and personal information provided from this application, I could then store this data into our sqlite3 database and calculate whether or not the person applying were eligible for other similar programs in the City of Fort Collins as well.

### Frontend Development
For the frontend design, I tried using Figma to wireframe out my design, but ended up having to convert all of that into html5 and CSS. Trying to make these conversions were definitely much more of a pain than I had expected as it was difficult to represent my designs exactly through those CSS styling factors. However I do know now most of the important CSS Selectors, and I realize now how encompassing CSS is in creating various stylesheets! Although design was probably most low stakes portion when completing this project, I must say that when I fully incorporated CSS, thats when my website truly looked like it was coming alive!

