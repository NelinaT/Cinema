This is a fullstack web project. Only for a month I succeeded to do a cinema booking system. I created a page with all the movies and info about them. When you click on movie you are redirected to a page where you can see more info and choose a projection with time,price and type of hall that is suitable for you. After choosing your projection, than you go to the next page where you choose your seat. You can see the hall as available seat are in green, broken ones in grey and the booked are marked in red. After you choose your seat you choose how to pay by card or cash and after that a ticket for this projection i being generated. Every ticket is unique and has movie title, seat, type of hall and qr code. 
Depending on the role people can log as admin, personal or clients.


HOW TO RUN IT:

All you need is to dowload the code and write the following comand in the terminal:  
python manage.py runserver

Then the site will operate on localhost:8000.

This page should be shown in the browser:

![image](https://github.com/NelinaT/Cinema/assets/90975870/569ad6f4-a40c-4259-b149-3492266086f4)

When you click on a movie, the site will redirect you to sign in:

![image](https://github.com/NelinaT/Cinema/assets/90975870/00397707-42c5-4ef0-8966-72aecd06279c)

You can choose to register as Customer by clicking the sing up link:

![image](https://github.com/NelinaT/Cinema/assets/90975870/761e8400-16b3-475d-b6b7-065e6bc8c33b)

The registration checks if there is a username like this and many standarts for the pasword. 
After you complete your resistration you will be redirected to the sign in form. You enter your cardentionlas and now you shoul be logged as customer and you will see the index page:

![image](https://github.com/NelinaT/Cinema/assets/90975870/3333173b-9dc9-4071-856f-5af8301e2e24)

you will see at the top right corner will be a loggout option:
![image](https://github.com/NelinaT/Cinema/assets/90975870/e08ec9e6-9603-490c-806b-ee853935c9ff)

Now as you are logged in you can do many stuff:
  - if you click on a movie you will be redirected to the next page with more info about it:
   
    ![image](https://github.com/NelinaT/Cinema/assets/90975870/ff56e762-2c52-4971-ba35-f0273ea0aea6)
    
  - When you click on "Projections" you will se all the projections of this movie:
   
    ![image](https://github.com/NelinaT/Cinema/assets/90975870/430127c6-cfcd-47d9-970c-0278bd0c3d2d)
    
  - Now you can choose the one projection that suits you the best and then choose your seat/seats:
  - 
    ![image](https://github.com/NelinaT/Cinema/assets/90975870/7e464a4d-f94c-4f0c-8e8a-97afac58f8cc)

     Here you can see 3 colours of seats. Green means it is available, gray - already booked and red - the admin blocked it (might be broken).
    When you press on the green one it highlightes in orange, which means you marked those seats and want to book them. If you want to change it hust clich again on it and it will be green again.
    The total amount is being calculated automaticly based on how many seats you have chosen. ( So if one projection costs 10 lv than 5 tickets will cost 50 lv)
    
    - After you choosed you seats you press continue, choose a payment method and your ticket will be generated:
    - 
    - ![image](https://github.com/NelinaT/Cinema/assets/90975870/3ea31c8c-6d18-4c50-8968-4caf3445e92b)
      
       ![image](https://github.com/NelinaT/Cinema/assets/90975870/fb934f7e-f1c3-4894-b3f2-4a603e3f1b4b)

    - to see you tickets you can press the link "here" or "My tickets which is at the top right corner
    - Here you can see all your tickets:
    - ![image](https://github.com/NelinaT/Cinema/assets/90975870/25b5f115-21ad-45c7-8175-7c2ad17acf70)

 So this are the funtionalities grom a Customer profile;

 Now lets see what you can do with stuff profile:
1. Only the admin can give stuff status to the accounts.
2. For admin role it is basically the same with a few differences:
  - they are suposed to sell the tickets phisicaly at the cinema, so their priorities are mainly the upcoming projections. That's why they do not see details about the movies. They see the program for the upcomming projections filtered by day and ordered by hours.
  - ![image](https://github.com/NelinaT/Cinema/assets/90975870/922afa1e-4ecc-4823-b4a8-5a4c3a48dbfa)
  - They have access to admin account but only view mode:
    ![image](https://github.com/NelinaT/Cinema/assets/90975870/d24d3eb0-dc58-4725-9ee3-5a2c67b252e7)

Admin account:
The Admin can in the site has the same rules as the Customer, but he has a full access to the admin panel and can make changes there;
He can:
  -creat hall and change it's name and type
  
  ![image](https://github.com/NelinaT/Cinema/assets/90975870/f2c8b608-3646-4055-9ac3-f026ea3c1e2c)

  - creat movies and change it's properties

    ![image](https://github.com/NelinaT/Cinema/assets/90975870/d497db7d-a65e-4c8c-8be2-b7a0fb37a7e3)

  - creat projections and change it's properties

    ![image](https://github.com/NelinaT/Cinema/assets/90975870/9e4551b3-5be9-4aa4-b682-190b2b9d5371)
    
  -  block them if they shouldn't be used
    ![image](https://github.com/NelinaT/Cinema/assets/90975870/934d9e6a-38b1-4ec5-b26a-c567af9114e9)

  - creat grops and gives roles to the users

    ![image](https://github.com/NelinaT/Cinema/assets/90975870/f1d60ee1-90b2-4624-83c0-c6df9f9aae31)

Implemented rules:
1. When creating a hall, the seats are automaticaly created, according to what tyoe is the hall.
2. When creating a projection:
    - admin can't creat a projection if there is another one at this time and hall
    - admin can't creat a projection if the movie in that hall did not finished
    - admin can't creat a projection if the new projection ends during another projection in this hall
    - admin can't creat a projection if there are less than 20 minutes before or after another projection
    
3. The page "Agenda":
   - is vissible only for people with role "Sales"
   - the program is ordered by the time of the projections per each day
     
4. The images of the seats in the hall are clickable when they can be booked and not if they are taken or broken
5. All tickets have unique QR codes that consist detail about there projection such as name of movie, hall, time, seat etc...

Technoligies:
  - Python + Django
  - SQLite
  - Front-end(html, css, bootstrap, js, jQuery)
  - additional modules acording to the needs of the project

Additional Notes:
 - I created the seats with Python Turtle, insted with frontend tecgologies,because this project is from a University course about Python and I wanted to show that I can do it with it.   

    













