This is a full-stack web project. In just one month, I succeeded in creating a cinema booking system. I developed a page that lists all the movies along with detailed information about them. When you click on a movie, you are redirected to a page where you can see more information and choose a projection with time, price, and type of hall that suits you. After selecting your projection, you proceed to the next page where you choose your seat. You can see the hall layout with available seats marked in green, broken ones in grey, and booked seats in red. Once you select your seat, you choose how to pay, either by card or cash. After the payment is processed, a ticket for the chosen projection is generated. Each ticket is unique and includes the movie title, seat, type of hall, and a QR code.
Depending on their role, users can log in as admin, staff, or clients.


HOW TO RUN IT:

All you need to do is download the code and run the following command in the terminal:

    ~python manage.py runserver~

Then the site will operate on localhost:8000.

This page should be displayed in the browser:

![image](https://github.com/NelinaT/Cinema/assets/90975870/569ad6f4-a40c-4259-b149-3492266086f4)

When you click on a movie, the site will redirect you to sign in:

![image](https://github.com/NelinaT/Cinema/assets/90975870/00397707-42c5-4ef0-8966-72aecd06279c)

You can choose to register as a Customer by clicking the sign-up link:

![image](https://github.com/NelinaT/Cinema/assets/90975870/761e8400-16b3-475d-b6b7-065e6bc8c33b)

The registration process checks if the username is available and enforces various password standards. 
After completing your registration, you will be redirected to the sign-in form. Enter your credentials, and you should now be logged in as a customer, allowing you to see the index page:

![image](https://github.com/NelinaT/Cinema/assets/90975870/3333173b-9dc9-4071-856f-5af8301e2e24)

At the top right corner, you will see a logout option:

![image](https://github.com/NelinaT/Cinema/assets/90975870/e08ec9e6-9603-490c-806b-ee853935c9ff)

Now that you are logged in, you can do many things:
  - If you click on a movie, you will be redirected to the next page with more info about it:
   
    ![image](https://github.com/NelinaT/Cinema/assets/90975870/ff56e762-2c52-4971-ba35-f0273ea0aea6)
    
  - When you click on "Projections," you will see all the projections of this movie.
   
    ![image](https://github.com/NelinaT/Cinema/assets/90975870/430127c6-cfcd-47d9-970c-0278bd0c3d2d)
    
  - You can then choose the projection that suits you best and select your seat/seats:
    
    ![image](https://github.com/NelinaT/Cinema/assets/90975870/7e464a4d-f94c-4f0c-8e8a-97afac58f8cc)

     In the seat selection page:
        Seats are color-coded: green for available, gray for booked, and red for blocked (possibly broken).
      Clicking on a green seat will highlight it in orange, indicating selection. Clicking again will unselect it, reverting it to green.
      The total amount is calculated automatically based on the number of seats chosen. For example, if one ticket costs 10 lv, then 5 tickets will amount to 50 lv.
    
    This interface allows you to conveniently select and book seats for your chosen movie projection.

    
    After choosing your seats:
    
      - Press "Continue" to proceed to the payment page.
    
      - Choose your preferred payment method (card or cash).
    
      - Your ticket will be generated automatically, including details such as movie title, selected seats, type of hall, and a QR code.

     ![image](https://github.com/NelinaT/Cinema/assets/90975870/3ea31c8c-6d18-4c50-8968-4caf3445e92b)
      
       ![image](https://github.com/NelinaT/Cinema/assets/90975870/fb934f7e-f1c3-4894-b3f2-4a603e3f1b4b)

    - To view your tickets just click on the link "here" or "My tickets" located at the top right corner.
    - You will be able to see all your purchased tickets in this section.
    - ![image](https://github.com/NelinaT/Cinema/assets/90975870/25b5f115-21ad-45c7-8175-7c2ad17acf70)

So these are the functionalities from customer profile.

 Now lets see what you can do with stuff profile:
1. Only the admin can give stuff status to the accounts.
2. For admin role it is basically the same with a few differences:
  - they are suposed to sell the tickets physically at the cinema, so their priorities are mainly the upcoming projections.
    That's why they do not see details about the movies.
    They see the program for the upcomming projections filtered by day and ordered by hours.
    
   ![image](https://github.com/NelinaT/Cinema/assets/90975870/922afa1e-4ecc-4823-b4a8-5a4c3a48dbfa)
   
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
     
     [image](https://github.com/NelinaT/Cinema/assets/90975870/934d9e6a-38b1-4ec5-b26a-c567af9114e9)

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
5. All tickets have unique QR codes that consist details about the projection such as name of movie, hall, time, seat etc...

Technoligies:
  - Python + Django
  - SQLite
  - Front-end(html, css, bootstrap, js, jQuery)
  - additional modules acording to the needs of the project

Additional Notes:
 - I created the seats with Python Turtle, instead of with frontend technologies, because this project is from a University course about Python and I wanted to show that I can do it with it.

    













