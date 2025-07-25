   <h1>Walkease<h1>

## Table of Contents
- [Introduction](#introduction)
- [Purpose](#purpose)
- [Deployment](#deployment)
- [User Experience](#user-experience)
- [Design](#design)
- [Schema](#schema)
- [Colour Scheme](#colour-scheme)
- [Typography](#typography)
- [Imagery](#imagery)
- [Testing](#testing)
- [Programme Used](#programme-used)

---

## Introduction
[WalkEase](https://walkease-website-1eaae1018604.herokuapp.com/) is a fully responsive, user-friendly e-commerce website designed for selling shoes online. Built with Django, the project showcases modern development practices and a clean, modular architecture by dividing functionality into four dedicated apps:

**Store App** – Displays product listings, categories, detailed product pages, and supports customer reviews.

**Cart App** – Allows users to add, remove, and update items in their shopping cart with real-time totals and quantity controls.

**Checkout App** – Handles secure Stripe-based payment processing, order submission, and post-payment confirmation pages.

**User App** – Manages user authentication, personalized profiles, avatar uploads, and account updates.

The site emphasizes smooth user experience, secure integration with third-party APIs (Stripe and Mailgun), and robust session handling. It's styled for clarity and professionalism, with careful attention to responsiveness across all devices.


## Purpose
The goal of Walkease is to deliver a polished, user-friendly online store that showcases products with clear imagery, intuitive navigation, and a streamlined purchase process. It’s designed for small retailers who want a turnkey solution with Django’s robustness and Stripe’s reliability.




## Deployment
How to Run the Project Locally
**Github**
A Github account. Create a Github Account [here](https://github.com join).
Use the Chrome browser then follow these steps:
 1. Install the Gitpod Browser Extension for Chrome.
 2. After installation, restart the browser.
 3. Log into Gitpod with your Gitpod account.
 4. Navigate to the Project Github repository.
 5. Click the green "Gitpod" button in the top right corner of the repository
 6. This will trigger a new Gitpod workspace to be created from the code in Github where you can work locally.
 7. To work on the project code within a local IBE such as VSCode, Pycharm, etc.
Follow the link to the Project Repository
 8. Under the repository name, click "clone or download".
 9. In the clone with HTTPs section, copy the clone URL for the repository.
 10. In your local IBE, open the terminal
Change the current working directory to the location where you want the cloned directory to be made.
Type git clone, and then paste the URL you copied in Step 3: https://github.com/Farah-94/Project4-Ecommerce-website.git
Press Enter. Your local clone will be created.

**Heroku Deployment**
 1. Login to Heroku.
 2. In your Heroku dashboard, click "New" and then "Create new app".
 3. Provide a unique name for your app (e.g., walkease) and choose your region.
 4. Go to the "Resources" tab within your Heroku app.
Under Dynos, select the appropriate plan. Heroku’s Eco Dynos help you stay within a low-cost, sustainable usage model.
 5. Connect your app to Github.
 6. Navigate to the "Deploy" tab in your Heroku app dashboard.
 7. If prompted, connect your GitHub account.
Write in the search "Project4-Ecommerce-website".
Once found, click "Connect" to link your repository.
 8. After linking, scroll down in the Deploy section.
Click on the automatic deploy( automatic update after pushing code to github).
 9. Click "Deploy Branch" to manually deploy your current branch.
 10. Review the build logs to ensure that the deployment completes successfully.
https://git.heroku.com/walkease-website.git git url created.

## User Experience
### First-time Visitor

- For first-time visitors, we aim to make your initial interaction smooth and intuitive.
- The website is designed with a straightforward layout, making it easy to explore and easy to understand.
- Users can find their expected results without any hassel.
- Users can access product page in Menu, then select products.
- Users can see product details by clicking the product card.
- Users will be able to select sizes ranging from 6-9, set the quanty and add the product in cart.
- Users can adjust quantities or remove items as needed, ensuring a flexible and user-friendly shopping experience.
- Users can proceeds and go to the checkout, where they need to fill out shiiping and payment form.
- Users can see the order successfull screen message with two options continue shopping and profile after completing order.
- User can save their information in their profile.
- user can make query and complaints on the home page by using contact us form. 

### Return Visitor

- For return visitors, we focus on advertising products in more efficient ways.
- Stay informed with the latest products and special discount offers.
- User can check their prevuious order details.

### Visitor Goals

- Enable users to add products to their cart, update quantities, and remove items seamlessly, ensuring that managing their selections is both straightforward and efficient.
- Provide a secure, simple checkout process to build trust and ensure that every completed purchase is effortless.
- For frequent visitors, the site highlights the latest products and exclusive discount offers, ensuring that they stay informed and enjoy a tailored shopping experience.
- Simplify account creation and sign-in processes so that visitors can easily register, log in, and track their orders, further enhancing their engagement with our platform.

## Design
Walkease features a minimal, clean aesthetic:
- Generous whitespace to let product imagery shine.
- Consistent button styles and form inputs.
- Clear hierarchy using headings, subheadings, and highlighted call-to-action elements.

 - [index.html](walkease/store/static/store/gallery/homepage.png)
 - [productlist.html](walkease/store/static/store/gallery/productlist.png)
 - [buy_product.html](walkease/store/static/store/gallery/buy_product.png)
 - [cart.html](walkease/store/static/store/gallery/cart.png)
 - [checkout.html](walkease/store/static/store/gallery/checkout.png)
 - [order_success.html](walkease/store/static/store/gallery/order_success.png)
 - [signin.html](walkease/store/static/store/gallery/signin.png)
 - [signup.html](walkease/store/static/store/gallery/signup.png)
 - [profile.html](walkease/store/static/store/gallery/profile.png)
 - [update_profile.html](walkease/store/static/store/gallery/update_profile.png)


**Wireframes**
 - [index.html](https://www.figma.com/design/qVUeUGxCOHjgpmGoDIcCzP/Untitled?node-id=0-1&t=qt2Cb6tlq6MZQBdU-1)
 - [productlist.html](https://www.figma.com/design/qVUeUGxCOHjgpmGoDIcCzP/Untitled?node-id=4-37&t=qt2Cb6tlq6MZQBdU-1)
 - [buy_product.html](https://www.figma.com/design/qVUeUGxCOHjgpmGoDIcCzP/Untitled?node-id=5-81&t=qt2Cb6tlq6MZQBdU-1)
 - [cart.html](https://www.figma.com/design/qVUeUGxCOHjgpmGoDIcCzP/Untitled?node-id=6-103&t=qt2Cb6tlq6MZQBdU-1)
 - [checkout.html](https://www.figma.com/design/qVUeUGxCOHjgpmGoDIcCzP/Untitled?node-id=7-119&t=qt2Cb6tlq6MZQBdU-1)
 - [order_success](https://www.figma.com/design/qVUeUGxCOHjgpmGoDIcCzP/Untitled?node-id=7-143&t=qt2Cb6tlq6MZQBdU-1)



## Schema
- [Internal Schema](https://dbdiagram.io/d/6867bdeaf413ba35084e21c5)

This layout defines:

 1. Table structures
 2. Data types (int, varchar, decimal, etc.)
 3. Primary and foreign key relationships
 4. Default values and partial links

- [External Schema](https://dbdiagram.io/d/6867c67af413ba35084f7f6e)

This external schema maps the shopper’s experience across the platform

 1. Home Page (index.html) Welcomes user with promotions, featured product, and quick access to cart/login.
 2. Product List (productlist.html) Let user explore all items or filter by category, then jump into individual product details.
 3. Buy Product (buy_product.html) Shows product gallery, pricing, size options, and a form to add items to cart or leave reviews.
 4.  Cart (cart.html) Displays selected items, supports quantity edits, and links directly to checkout.
 5. Checkout (checkout.html) Summarizes the order and offers secure Stripe-based payment.
 6.  Order Success (order_success.html) Confirms purchase and shows order number, date, and item breakdown.
 7.  Profile (profile.html) Reveals personal details, past orders, and lets them update info or avatar.
 8.  Profile Update (update_profile.html) Offers a friendly form to revise details, bio, and upload a new image.


## Colour Scheme
- **Primary:** Black, white and pink
- **Accent:**rgb(97, 24, 84) for buttons and links
- **Background:** white for page backgrounds
- **Text:** black and white

## Typography
- **Headings:** “Lora”, serif, for a touch of elegance
- **Body Copy:** “Roboto”, sans-serif, for readability
- **Fallbacks:** system fonts such as Arial, Helvetica

## Imagery
- High-resolution product photos with consistent aspect ratios.
- On-page banners showcasing new arrivals or promotions.
- Placeholder graphics sourced from Unsplash and customized with brand colors.

 - [Website Home page Image](walkease/store/static/store/gallery/webfront.png)
 - [Product](walkease/store/static/store/gallery/heels.jpg)

## Testing
[Test Plan](https://1drv.ms/w/c/e1af83f369e97fb7/Ebm6ubvVfndNrFqgfDX9BNkBCy3iWzNmigQ9enYfK_vZkg?e=EYCRUs)

 - [index.html](walkease/store/static/store/gallery/index_validation.png)
 - [productlist.html](walkease/store/static/store/gallery/productlist_validation.png)
 - [buy_product.html](walkease/store/static/store/gallery/buy_product_validation.png)
 - [cart.html]()
 - [checkout.html]()
 - [order_success.html]()
 - [profile.html]()
 - [update_profile.html]()
 - [admin_profile.html]()
 - [login.html]()
 - [signup.html]()



- Stripe test cards (e.g., 4242 4242 4242 4242 for success, 4000 0000 0000 9995 for insufficient funds).


## Programme Used
-  Django 5.2.1, Python 3.12
-  HTML5, CSS3, JavaScript
-  Stripe
-  Heroku, WhiteNoise
-  Git, GitHub
-  PostgreSQL (via Heroku Postgres)
-  Freepiks
-  Formspree
-  Logo maker


