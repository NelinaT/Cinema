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









