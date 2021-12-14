<div id="top"></div>

[![LinkedIn][linkedin-shield]][https://www.linkedin.com/in/satta-sundar-talukdar-9923661a6/]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Auction App</h3>

  <p align="center">
    An app to create and bid auctions.
    <br />
    <a href=https://github.com/SST-Bappu/Auction/tree/main/auction><strong>Explore the files »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#challenges">Challenges in each step</a>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is an Auction Site like eBay. On this site, anybody can signup using their email address. There is no complex authentication. When somebody enters their email address at the login screen, if the user with the email address already exists it logs the user in and shows a dashboard for the user. If the email address does not exist, a user will be created with the email address and the user logs in. 
This is an assessment project assigned by TakaSchool.







### Built With



* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com)
* [Chart.js](https://www.chartjs.org/)
* [PostgreSQL](https://www.postgresql.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Challenges

The instruction given in each step is very much conceptual here. Anyone without having a clean clear concept on Django user model, authentication systems, decorator etc. has to go through some bumpy ride.


### Challenges I faced in each step

#### Step-1
Basically, Django has a built-in user model which takes a name as its username and required field. But here I am told to let the user sign in with user mail without any registration. So I had to override the Django default user model to make the user mail as its username and to let the user sign in without any password as well. 

#### Step-2
Here I just retrieve all the auctions from the database and view them on the user end. There are two different dashboards. One shows all the auctions and the other filters the auctions posted by the logged-in user only.
##### Packages: Pillow (To upload photo)

#### Step-3
Here users can bid for a particular auction and can see others bids as well.

#### Step-4
Every auction will only be available for a specific time only. So no user can bid once an auction expires. I took the system date to check whether the auction is expired or not.

#### Step-5
Challenging, very challenging step and I have a very vague idea of the concept. I personally not satisfied with my progress in this step. It seems I have to use some time series analysis packages such as matplotlib or panda. But the problem is I couldn't just integrate the data we have with the instructions. In my professional approach, I take more time in such challenges.

#### Step-6
I did not spend that much time on this section. I relied on Bootstrap classes. 

#### Step-7
Finally I deployed it on Heroku. I made some mistakes initially which takes a lot of mine. Very tedious...!
That also results some random commits on git at the end.

#### Step-8
And here I go. I am about to be done. Working on the README file. I was assigned this project at midnight on 12th December(This day is recognized as "Digitial Bangladesh Day". Interesting...!). I started working on it on the morning of 13th December. But unfortunately, The electric supply was interrupted for the whole day here in Gazipur (Joydebpur) on that day. So I had to start it in the evening. And now I am all set to submit it at 12.30 AM on 14th December. 
Looking forward to solving many more such......

<p align="right">(<a href="#top">back to top</a>)</p>



