# Anatolian Bistro & Market

![Am I Responsive](docs/am-i-responsive.PNG)

***Oğuzhan Akça***

💻 [Visit live website](https://anatolian-bm-0079c230f935.herokuapp.com/)  
(Ctrl + click to open in new tab)



## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Device & Browser compatibility](#device-testing--browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About

Anatolian Bistro & Market is a fictional Turkish restaurant where users can book a table, read the blog and can also buy some Turkish products.
<hr>

### User Goals

- Booking a table
- Finding a restaurant that offers good food and nice atmosphere.
- Find location and contact address of the restaurant
- Reading Blog
- Purchasing products from market

### Site Owner Goals

- Allowing users to book table online
- Showing and selling their available products
- Providing users an application that easy to navigate
- Promote the business
- Fully responsive and accessible
<hr>

## User Experience

### Target Audience
- Users who wants to book a table easily
- People looking for a place to have dinner
- Users who wants to purchase turkish products
- Users who wants to share their idea and opinions
- Users who wants to taste of Turkish Cuisine

### User Requirements and Expectations

- Fully responsive
- Accessible
- A welcoming design
- Contact information
- Accessibility
- Design and content that will not tire the reader's eyes
- Links that work as they should

## User Stories

### Users

1. As a User, I want to use navigation so that I can navigate through website easily.
2.	As a User, I want to make a reservation online so that I can ensure a table is available when I visit.
3.	As a User, I want to find social accounts of business so that I can visit their accounts.
4.	As a User, I want to find a contact us page so that I can get in touch with business.
5.	As a User, I want to view the opening hours and contact details so that I know when the business is open and how to contact them via phone and socials.
6.	As a User, I want to book a table selecting a date and time so that I can reserve my table.
7.	As a User, I want to add additional informations to my booking so that business can be prepared better.
8.  As a User, I want to list my bookings so that I can see when did i book last time.
9. As a User, I want to get informed when my booking status changed so that I know if its cancelled or not.
10. As a User, I want to make an account so that I can use all the features.
11. As a User, I want to login so that I can book a table.
12. As a User, I want to reset my password once i forget.
13. As a User, I want to view the site's blog so that I can learn additional information and read articles.
14. As a User, I want to search posts so that I can find the post i want faster.
15. As a User, I want to post on blog.
16. As a User, I want to edit or delete my post.
17. As a User, I want to comment on posts.
18. As a User, I want to search and filter products.

### Admin
19.	As an Admin, I want to log in so that I can access the back end of the site.
20.	As an Admin, I want to add and remove products.
21. As an Admin, I want to accept or reject bookings so that I can avoid double bookings.
22. As an Admin, I want to add,read, update and remove posts.
23. As an Admin, I want to add,read, update and remove comments.

### Site Owner  
24. As a Site Owner, I can provide a fully responsive site for my customers so that they have a good user experience.
25. As a Site Owner, I can validate data entered into my site so that all submitted data is correct to avoid errors.
26. As a Site Owner, I can provide information about my business.


### Kanban, Epics & User Stories
- GitHub Kanban was used to track user stories
- Epics were created using the milestones feature
- Todo, In Progress, Done headings were used in the kanban

<details><summary>Epics</summary>

![Epics](docs/features/epics.png)
![Epic 1](docs/features/epic-1.png)
![Epic 3](docs/features/epic-3.png)
![Epic 4](docs/features/epic-4.png)
![Epic 5](docs/features/epic-5.png)
![Epic 6](docs/features/epic-6.png)
![Epic 7](docs/features/epic-7.png)
</details>

<details><summary>User Stories</summary>

![User stories](docs/features/user-stories.png)

</details>

<details><summary>Kanban</summary>

![Kanban](docs/features/kanban.png)

</details>

## Design

### Colours

For the color theme, I used restaurant logo's background color as the reference. After some research I decided to use the Cappucino Color Palette which fits pretty good with restaurant's logo.

The colors I wanted to stay close to  [Cappucino Color Palette](https://www.color-hex.com/color-palette/389)
<details><summary>See colour pallet</summary>
<img src="docs/colors.png">
</details>

### Fonts

Vollkorn, PT Sans, Oswald and Abril Fatface fonts used from [Google Fonts](https://fonts.google.com/)

### Structure

#### Website pages

The site was designed for the user to be familiar with the layout such as a navigation bar along the top of the pages and a dropdown menu button for smaller screen.

The footer contains all social media links that the business has so the user can visit any social media site and follow the business there to expand the businesses followers, likes and shares.

- The site consists of the following pages:
  - Homepage : Welcomes users and shows the features of the website.
  - About Us : Gives information about business, its history. Also contains contact addresses and form.
  - Booking : Allows users to book a table from site. Users can also see their booking history with paginated view. For admin users, it shows every booking that has done by users.
  - Booking Success : Gives information to users when they successfully book a table.
  - Blog : Allows users to view posts and create posts.
  - Create Post : Logged in users can create post.
  - Update Post : Users can edit and delete their own posts.
  - Post Details : Users can read the full post. They can also comment.
  - Shop : Users can view products.
  - All Products : Users can view, filter and search all products.
  - Login : Allows users to login with their account.
  - Register : Allows the user to regiser so they can use features
  - Password Recovery : Allows users to reset their password once they forgot.
  - 404 : Error page to display if a 404 error is raised

#### Database

- Built with Python and the Django framework with a database of a Postgres for the deployed Heroku version(production)

<details><summary>Show diagram</summary>
<img src="docs/database-model.png">
</details>


##### User Model
The User Model contains the following:
- id
- username
- password
- email
- first_name
- last_name
- date_joined
- is_superuser

##### Post Model
The Post Model contains the following:
- id
- title
- author (Foreign Key : User)
- category
- content
- created_at
- status
- updated_at

##### Comment Model
The Comment Model contains the following:
- id
- post (Foreign Key : Post)
- author (Foreign Key : User)
- body
- approved
- created_at

##### Booking Model
The Booking Model contains the following:
- id
- created_date
- requested_date
- requested_time
- user (Foreign Key : User)
- status
- guests
- message
- phone

##### Product Model
The Product Model contains the following:
- id
- name
- description
- category
- image
- price
- stock
- sold
- on_sale
- created_at
- updated_at

##### Cart Model
The Cart Model contains the following:
- id
- user (Foreign Key : User)
- created_at
- updated_at

##### CartItem Model
The CartItem Model contains the following:
- id
- cart (Foreign Key : Cart)
- product (Foreign Key : Product)
- quantity


### Wireframes
The wireframes were created by Balsamiq
<details><summary>Homepage</summary>
<img src="docs/wireframes/homepage.jpg">
</details>

<details><summary>About Us</summary>
<img src="docs/wireframes/about-us.jpg">
</details>

<details><summary>Booking</summary>
<img src="docs/wireframes/booking.jpg">
</details>

<details><summary>Shop Homepage</summary>
<img src="docs/wireframes/shop-homepage.jpg">
</details>

<details><summary>All Products</summary>
<img src="docs/wireframes/all-products.jpg">
</details>

<details><summary>Product Detail</summary>
<img src="docs/wireframes/product-detail.jpg">
</details>

<details><summary>My Cart</summary>
<img src="docs/wireframes/my-cart.jpg">
</details>

<details><summary>Blog Homepage</summary>
<img src="docs/wireframes/blog-homepage.jpg">
</details>

<details><summary>Post Detail</summary>
<img src="docs/wireframes/post-detail.jpg">
</details>

<details><summary>Create Post</summary>
<img src="docs/wireframes/create-post.jpg">
</details>

<details><summary>Update Post</summary>
<img src="docs/wireframes/update-post.jpg">
</details>

<details><summary>Log In</summary>
<img src="docs/wireframes/log-in.jpg">
</details>

<details><summary>Sign Up</summary>
<img src="docs/wireframes/register.jpg">
</details>

<details><summary>Password Recovery</summary>
<img src="docs/wireframes/password-recovery.jpg">
</details>

<details><summary>Reset Password</summary>
<img src="docs/wireframes/reset-password.jpg">
</details>


## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django


### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.3.3](https://getbootstrap.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- [Allauth](https://docs.allauth.org/en/latest/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [CI Python Linter](https://pep8ci.herokuapp.com/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

## Features

### Home page
- Home page includes nav bar, main body and a footer

<details><summary>Homepage</summary>

<img src="docs/features/feature-homepage.png">
</details>


### Navigation
- Custom logo for the business
- Fully Responsive
- On small screens switches to dropdown menu
- Indicates login/logout in status
- Displayed on all pages

<details><summary>Navigation</summary>

<img src="docs/features/feature-navigation-1.png">
<img src="docs/features/feature-navigation-2.png">
<img src="docs/features/feature-navigation-3.png">

</details>

### Footer
- Contains social media links
- Displayed across all pages

<details><summary>Footer</summary>

<img src="docs/features/feature-footer.png">

</details>


### Sign up / Register
- Allow users to create an acoount
- Has validation for empty fields
- Sends validation mail after successful registration

<details><summary>Sign Up</summary>

<img src="docs/features/feature-signup.png">

</details>


### Login
- Allows users to access their account
- Users must validate their account with the email they get to use their account
- Required for site features

<details><summary>Login</summary>

<img src="docs/features/feature-login.png">

</details>


### Password Recovery
- Allows users to reset their password once they forgot
- Users gets an email to recover their password.
- Email link lasts 1 hour.

<details><summary>Password Recovery</summary>

<img src="docs/features/feature-password-recovery-1.png">
<img src="docs/features/feature-password-recovery-2.png">

</details>


### Logout
- Allows the user to securely log out
- Ask user if they are sure they want to log out

<details><summary>Logout</summary>

<img src="docs/features/feature-signout.png">

</details>


### Booking
- Allows the user to book a table using the booking form
- User must be logged in to access page.
- Users can view their paginated booking records. Every page contains 5 bookings.
- After successful booking, users will get email that contains their booking information
- Bookings must be confirmed by the business.
- Users will get email whenever their booking status changes.

<details><summary>Booking</summary>

<img src="docs/features/feature-booking-1.png">
<img src="docs/features/feature-booking-2.png">

</details>


### Blog
- The blog displays each post made by a staff member or users
- User must be logged in to access page.
- Paginations is used to display 7 posts per page.
- Users can click a post to view its content.
- Users can search posts by their title.
- Users can click "Create Post" to access create post page.
  
<details><summary>Blog</summary>

<img src="docs/features/feature-blog.png">

</details>


### Post Detail
- User must be logged in to access page.
- Displays the clicked post content.
- Also shows the comments below the post.
- Users can make comment to every post.

<details><summary>Post Detail</summary>

<img src="docs/features/feature-post-detail-1.png">
<img src="docs/features/feature-post-detail-2.png">

</details>


### Create & Edit Post
- Allows logged in users to create post
- Users can use rich template to decorate their posts.
- Everyone can comment a post.
- Post owners can edit or delete their posts after they create.
  
<details><summary>Create & Edit Post</summary>

<img src="docs/features/feature-create-post.png">
<img src="docs/features/feature-edit-post.png">

</details>


### Comments
- Users must be logged in to comment.
- Users can comment under every post.
  
<details><summary>Comments</summary>

<img src="docs/features/feature-comment.png">

</details>


### Contact Us
- Displayed in Abous Us page.
- Contact infos such as phone, address are displayed
- A Google Map is embedded with the address for users to use
- Users can send message to business with contact form without requiring creating account.
  
<details><summary>Contact Us</summary>

<img src="docs/features/feature-contact-us.png">

</details>


### Shop
- Users must be logged in to access page.
- Displays the products business selling.
- Users can filter products by their category.
- Users can search products by their name.
- Users can order products by name and sold amount.
- Still in development.
  
<details><summary>Shop</summary>

<img src="docs/features/feature-shop-1.png">
<img src="docs/features/feature-shop-2.png">
<img src="docs/features/feature-shop-3.png">

</details>


## Validation

The W3C Markup Validation Service
<details><summary>Homepage</summary>
<img src="docs/validation/html/homepage.png">
</details>

<details><summary>About Us</summary>
<img src="docs/validation/html/about.png">
</details>

<details><summary>Booking</summary>
<img src="docs/validation/html/booking.png">
</details>

<details><summary>Booking Success</summary>
<img src="docs/validation/html/booking_success.png">
</details>

<details><summary>Blog</summary>
<img src="docs/validation/html/blog.png">
</details>

<details><summary>Create Post</summary>
<img src="docs/validation/html/create_post.png">
</details>

<details><summary>Update Post</summary>
<img src="docs/validation/html/update_post.png">
</details>

<details><summary>Post Detail</summary>
<img src="docs/validation/html/post_detail.png">
</details>

<details><summary>Login</summary>
<img src="docs/validation/html/login.png">
</details>

<details><summary>Signup</summary>
<img src="docs/validation/html/signup.png">
</details>

<details><summary>Logout</summary>
<img src="docs/validation/html/signout.png">
</details>

<details><summary>Forgot Password</summary>
<img src="docs/validation/html/forgot_password.png">
</details>

<details><summary>Password Recover</summary>
<img src="docs/validation/html/password_reset_form.png">
<img src="docs/validation/html/password_reset_mailsent.png">
<img src="docs/validation/html/password_reset_badtoken.png">
<img src="docs/validation/html/password_reset_form.png">
</details>

<details><summary>Shop</summary>
<img src="docs/validation/html/shop.png">
</details>

<details><summary>All Products</summary>
<img src="docs/validation/html/all_products.png">
</details>

<details><summary>Product Detail</summary>
<img src="docs/validation/html/product_detail.png">
</details>

<details><summary>My Cart</summary>
<img src="docs/validation/html/my_cart.png">
</details>

<details><summary>Add Cart Success</summary>
<img src="docs/validation/html/add_cart_success.png">
</details>

<details><summary>404</summary>
<img src="docs/validation/html/404.png">
</details>

<hr>


### CSS Validation
The W3C Jigsaw CSS Validation Service

<details><summary>Style.css</summary>
<img src="docs/validation/css/css_validation.png">
</details>
<hr>


### PEP8 Validation
CI Python Linter was used to check the code for PEP8 requirements.

<details><summary>About - apps.py</summary>
<img src="docs/validation/pep8/about_apps.png">
</details>

<details><summary>About - forms.py</summary>
<img src="docs/validation/pep8/about_forms.png">
</details>

<details><summary>About - urls.py</summary>
<img src="docs/validation/pep8/about_urls.png">
</details>

<details><summary>About - views.py</summary>
<img src="docs/validation/pep8/about_views.png">
</details>

<details><summary>Anatolian_bm - forms.py</summary>
<img src="docs/validation/pep8/anatolian_forms.png">
</details>

<details><summary>Blog - admin.py</summary>
<img src="docs/validation/pep8/blog_admin.png">
</details>

<details><summary>Blog - apps.py</summary>
<img src="docs/validation/pep8/blog_apps.png">
</details>

<details><summary>Blog - forms.py</summary>
<img src="docs/validation/pep8/blog_forms.png">
</details>

<details><summary>Blog - models.py</summary>
<img src="docs/validation/pep8/blog_models.png">
</details>

<details><summary>Blog - blog_tags.py</summary>
<img src="docs/validation/pep8/blog_tags.png">
</details>

<details><summary>Blog - urls.py</summary>
<img src="docs/validation/pep8/blog_urls.png">
</details>

<details><summary>Blog - views.py</summary>
<img src="docs/validation/pep8/blog_views.png">
</details>

<details><summary>Booking - admin.py</summary>
<img src="docs/validation/pep8/booking_admin.png">
</details>

<details><summary>Booking - apps.py</summary>
<img src="docs/validation/pep8/booking_apps.png">
</details>

<details><summary>Booking - forms.py</summary>
<img src="docs/validation/pep8/booking_forms.png">
</details>

<details><summary>Booking - models.py</summary>
<img src="docs/validation/pep8/booking_models.png">
</details>

<details><summary>Booking - signals.py</summary>
<img src="docs/validation/pep8/booking_signals.png">
</details>

<details><summary>Booking - booking_tags.py</summary>
<img src="docs/validation/pep8/booking_tags.png">
</details>

<details><summary>Booking - urls.py</summary>
<img src="docs/validation/pep8/booking_urls.png">
</details>

<details><summary>Booking - utils.py</summary>
<img src="docs/validation/pep8/booking_utils.png">
</details>

<details><summary>Booking - views.py</summary>
<img src="docs/validation/pep8/booking_views.png">
</details>

<details><summary>Shop - admin.py</summary>
<img src="docs/validation/pep8/shop_admin.png">
</details>

<details><summary>Shop - apps.py</summary>
<img src="docs/validation/pep8/shop_apps.png">
</details>

<details><summary>Shop - forms.py</summary>
<img src="docs/validation/pep8/shop_forms.png">
</details>

<details><summary>Shop - models.py</summary>
<img src="docs/validation/pep8/shop_models.png">
</details>

<details><summary>Shop - urls.py</summary>
<img src="docs/validation/pep8/shop_urls.png">
</details>

<details><summary>Shop - views.py</summary>
<img src="docs/validation/pep8/shop_views.png">
</details>


<hr>


### Lighthouse

Performance, best practices and SEO was tested using Lighthouse.

#### Desktop
<details><summary>About Us</summary>
<img src="docs/validation/lighthouse/about-us-desktop.png">
</details>

<details><summary>All Products</summary>
<img src="docs/validation/lighthouse/all-products-desktop.png">
</details>

<details><summary>Blog</summary>
<img src="docs/validation/lighthouse/blog-homepage-desktop.png">
</details>

<details><summary>Booking</summary>
<img src="docs/validation/lighthouse/booking-desktop.png">
</details>

<details><summary>Create Post</summary>
<img src="docs/validation/lighthouse/create-post-desktop.png">
</details>

<details><summary>Homepage</summary>
<img src="docs/validation/lighthouse/homepage-desktop.png">
</details>

<details><summary>Login</summary>
<img src="docs/validation/lighthouse/log-in-desktop.png">
</details>

<details><summary>My Cart</summary>
<img src="docs/validation/lighthouse/my-cart-desktop.png">
</details>

<details><summary>Post Detail</summary>
<img src="docs/validation/lighthouse/post-detail-desktop.png">
</details>

<details><summary>Product Detail</summary>
<img src="docs/validation/lighthouse/product-detail-desktop.png">
</details>

<details><summary>Shop</summary>
<img src="docs/validation/lighthouse/shop-homepage.png">
</details>

<details><summary>Signup</summary>
<img src="docs/validation/lighthouse/sign-up-desktop.png">
</details>


#### Mobile
<details><summary>About Us</summary>
<img src="docs/validation/lighthouse/about-us-mobile.png">
</details>

<details><summary>All Products</summary>
<img src="docs/validation/lighthouse/all-products-mobile.png">
</details>

<details><summary>Blog</summary>
<img src="docs/validation/lighthouse/blog-homepage-mobile.png">
</details>

<details><summary>Booking</summary>
<img src="docs/validation/lighthouse/booking-mobile.png">
</details>

<details><summary>Create Post</summary>
<img src="docs/validation/lighthouse/create-post-mobile.png">
</details>

<details><summary>Homepage</summary>
<img src="docs/validation/lighthouse/homepage-mobile.png">
</details>

<details><summary>Login</summary>
<img src="docs/validation/lighthouse/log-in-mobile.png">
</details>

<details><summary>My Cart</summary>
<img src="docs/validation/lighthouse/my-cart-mobile.png">
</details>

<details><summary>Post Detail</summary>
<img src="docs/validation/lighthouse/post-detail-mobile.png">
</details>

<details><summary>Product Detail</summary>
<img src="docs/validation/lighthouse/product-detail-mobile.png">
</details>

<details><summary>Shop</summary>
<img src="docs/validation/lighthouse/shop-mobile.png">
</details>

<details><summary>Signup</summary>
<img src="docs/validation/lighthouse/sign-up-mobile.png">
</details>
<hr>

### Wave
WAVE was used to test the websites accessibility.

<details><summary>About</summary>
<img src="docs/validation/wave/about.png">
</details>

<details><summary>Add Cart Success</summary>
<img src="docs/validation/wave/add_cart_success.png">
</details>

<details><summary>All Products</summary>
<img src="docs/validation/wave/all_products.png">
</details>

<details><summary>Blog</summary>
<img src="docs/validation/wave/blog.png">
</details>

<details><summary>Booking</summary>
<img src="docs/validation/wave/booking.png">
</details>

<details><summary>Booking Success</summary>
<img src="docs/validation/wave/booking_success.png">
</details>

<details><summary>Create Post</summary>
<img src="docs/validation/wave/create_post.png">
</details>

<details><summary>Homepage</summary>
<img src="docs/validation/wave/homepage.png">
</details>

<details><summary>Login</summary>
<img src="docs/validation/wave/login.png">
</details>

<details><summary>My Cart</summary>
<img src="docs/validation/wave/my_cart.png">
</details>

<details><summary>Post Detail</summary>
<img src="docs/validation/wave/post_detail.png">
</details>

<details><summary>Product Detail</summary>
<img src="docs/validation/wave/product_detail.png">
</details>

<details><summary>Shop</summary>
<img src="docs/validation/wave/shop.png">
</details>

<details><summary>Signout</summary>
<img src="docs/validation/wave/signout.png">
</details>

<details><summary>Signup</summary>
<img src="docs/validation/wave/signup.png">
</details>

<details><summary>Update Post</summary>
<img src="docs/validation/wave/update_post.png">
</details>


## Testing

### Manual testing

1. As a User, I can use navigation so that I can navigate through website easily.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the links in the navigation bar | Navigated to the link| Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-1.png">

</details>

2. As a User, I want to make a reservation online so that I can ensure a table is available when I visit.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 | Click Booking in navigation bar | Navigate to booking page | Works as expected |
 | Scroll down to page for booking form | Fill the "Book a Table" form | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-2-1.png">
<img src="docs/user-story-test/user-story-2-2.png">

</details>

3.	As a User, I can find social accounts of business so that I can visit their accounts.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Scroll down in any page to find footer | All social media links will be showed| Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-3.png">

</details>

4.	As a User, I can find a contact us page so that I can get in touch with business.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'About Us' link in the navigation bar, scroll to bottom of page | Find "Contact Us" form and fill | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-4-1.png">
<img src="docs/user-story-test/user-story-4-2.png">

</details>

5.	As a User, I can view the opening hours and contact details so that I know when the business is open and how to contact them via phone and socials.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'About Us' link in the navigation bar, scroll down to bottom of page | Find map and business information | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-4-1.png">
<img src="docs/user-story-test/user-story-5-2.png">

</details>

6. As a User, I can book a table selecting a date and time so that I can reserve my table.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Booking' link in the navigation bar, scroll down to find Book a Table form| Choose Date and Time  | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-6-1.png">
<img src="docs/user-story-test/user-story-6-2.png">

</details>

7. As a User, I can add additional informations to my booking so that business can be prepared better.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Booking' link in the navigation bar, scroll down to find Book a Table form| Fill the form  | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-7.png">

</details>

8. As a User, I can list my bookings so that I can see when did i book last time.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Booking' link in the navigation bar | Booking list will display all bookings made| Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-8.png">

</details>

9. As a User, I want to get informed when my booking status changed so that I know if its cancelled or not.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Check Emails | When booking status changed, user gets an email | Works as expected |


<details><summary></summary>
<img src="docs/user-story-test/user-story-9-1.png">
<img src="docs/user-story-test/user-story-9-2.png">

</details>

10. As a User, I can make an account so that I can use all the features.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click "Sign Up" in the navigation bar | Enter account details | Works as expected |
| After successful entry, user will get validation email | Validate Email | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-10-1.png">
<img src="docs/user-story-test/user-story-10-2.png">


</details>

11. As a User, I can login so that I can book a table.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click "Sign In" in the navigation bar | Enter account data | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-11.png">


</details>

12. As a User, I can reset my password once i forget.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click "Sign In" in the navigation bar | Enter account data | Works as expected |
| Click "Forgot Password?" button | Enter account's email | Works as expected |
| Receive password recovery link in email | Use recovery link to reset password | Works as expected |


<details><summary></summary>
<img src="docs/user-story-test/user-story-12-1.png">
<img src="docs/user-story-test/user-story-12-2.png">
<img src="docs/user-story-test/user-story-12-3.png">
<img src="docs/user-story-test/user-story-12-4.png">


</details>

13. As a User, I can view the site's blog so that I can learn additional information and read articles.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click "Blog" in the navigation bar, login to account if you didn't | View blog | Works as expected |


<details><summary></summary>
<img src="docs/user-story-test/user-story-13.png">


</details>

14. As a User, I can search posts so that I can find the post i want faster.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click "Blog" in navigation bar | Type the word you want to search in "Search Post" input area then press Search button | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-14.png">

</details>

15. As a User, I want to post on blog.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click "Blog" in navigation bar then click "Create a Post" button | Enter post content | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-15-1.png">
<img src="docs/user-story-test/user-story-15-2.png">



</details>

16.  As a User, I want to edit or delete my post.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click "Blog" in navigation bar then click the post you've posted | Click the edit button | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-16-1.png">
<img src="docs/user-story-test/user-story-16-2.png">

</details>

17. As a User, I want to comment on posts.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on a post you want to comment, scroll down to the end | Enter your comment and submit  | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-17.png">

</details>

18. As a User, I want to search and filter products.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click "Shop" in navigation bar then click "All Products" | Use filter and search area | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-18.png">

</details>

19.	As an Admin, I can log in so that I can access the back end of the site.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click "Sign In" in navigation bar  | Login to your admin account | Works as expected |
| Click "Admin Panel" in navigation bar  | Navigate to Admin site | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-19.png">

</details>

20. As an Admin, I can add products.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From the admin panel, select Products | Navigate to products page | Works as expected |
| Click "Add Products" button and add the product you want | Add product | Works as expected |


<details><summary></summary>
<img src="docs/user-story-test/user-story-20-1.png">
<img src="docs/user-story-test/user-story-20-2.png">
<img src="docs/user-story-test/user-story-20-3.png">

</details>

21. As an Admin, I can remove products.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From the admin panel, select Products and click the checkbox near the products you want to delete | Choose "Delete" action | Works as expected |


<details><summary></summary>
<img src="docs/user-story-test/user-story-21.png">

</details>

22. As an Admin, I can accept or reject bookings so that I can avoid double bookings.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From the admin panel, select Bookings and click the booking you want to take action | Confirm or Cancel booking | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-22-1.png">
<img src="docs/user-story-test/user-story-22-2.png">


</details>

23. As an Admin, I can add,read, update and remove posts.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From the admin panel, select Posts and click the post you want to take action | Create, Read, Update or Delete the post | Works as expected |


<details><summary></summary>
<img src="docs/user-story-test/user-story-23-1.png">
<img src="docs/user-story-test/user-story-23-2.png">

</details>

24. As an Admin, I can add,read, update and remove comments.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From the admin panel, select Posts and click the post you want to take action | Create, Read, Update or Delete the post | Works as expected |

<details><summary></summary>
<img src="docs/user-story-test/user-story-24.png">

</details>



### Device Testing & Browser compatibility

The following devices and browsers were used to test my site:

- Google Chrome
- Safari
- Iphone 6S
- Ipad Mini

<hr>


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| In "Create a Post" page, mobile devices has lots of space to scroll down| Still working on it |

<hr>


### Heroku Deployment

The website was deployed to [Heroku](https://www.heroku.com/) using the following process:

1. Login or create an account at [Heroku](https://www.heroku.com/)

<img src="docs/heroku/heroku-1.jpg">

2. Click on New > Create new app in the top right of the screen.

<img src="docs/heroku/heroku-2.jpg">

3. Decide an app name and select location, then click 'create app'.

<img src="docs/heroku/heroku-3.jpg">

4. Move to the deploy tab and select GitHub Connect.

<img src="docs/heroku/heroku-4.jpg">

5. Log in to your GitHub account when prompted and give permission for it.

6. Under the Deployment Method, select the repository that you want to be connected to the Heroku app.

<img src="docs/heroku/heroku-5.jpg">

7. Move to the Settings tab.

<img src="docs/heroku/heroku-6.jpg">

8. Scroll down to the config vars section, and add config vars:

<img src="docs/heroku/heroku-7.png">

9. Once you have set up the config vars, scroll down to buildpacks and add the Python buildpacks to your app and make sure that when they are displayed, they appear in the order:

<img src="docs/heroku/heroku-8.jpg">

10. Navigate back to the Deploy tab.
11. In the 'manual deploy' section beneath this, make sure the branch selected is 'main' and click deploy branch.

<img src="docs/heroku/heroku-9.png">

12. Select automatic deploys to allow Heroku to build the site with new changes each time changes are pushed to GitHub.

<img src="docs/heroku/heroku-10.jpg">

13. The site should now be built and Heroku should provide a url for the built site.

This repository can be forked using the following process:

1. On the repository's page, go to the top-right of the page underneath the dark ribbon.
2. Click on the fork button
3. You can now work on a fork of this project.

This repository can be cloned using the following process:

1. Go to this repository's page on GitHub.
2. Click on the code button (not the one in the navbar, but the one right above the file list).
3. Select an option, HTTPS, SSH, GitHub CLI.
4. Copy the url below to your clipboard.
5. Open Git Bash/your IDE terminal.
6. Ensure the directory you are working in is the correct one you want to paste the project into.
7. Type the command '$ git clone'
8. Paste the URL of the repository after this.
9. Hit enter on your keyboard and the project will be cloned.
<hr>

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
<hr>

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.
<hr>


## Credits

### Images

- Product images : [Migros](https://www.migros.com.tr/)
- Homepage Images : [Pexels](https://www.pexels.com/), [FreeImages](https://www.freeimages.com/), [Pixabay](https://pixabay.com/)

### Code

[Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
Custom Forms : [Allauth](https://docs.allauth.org/en/latest/), [Stackoverflow](https://stackoverflow.com/)

<hr>

## Acknowledgements

I would like to take the opportunity to thank my mentor Mo Shami for his guidance and support.