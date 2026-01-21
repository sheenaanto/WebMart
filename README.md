# WebMart - E-Commerce Store Application

WebMart is a full-featured e-commerce web application built with Django and PostgreSQL which allows users to browse products,login, manage shopping carts, place orders, and manage their user accounts.

Source code can be found [here](https://github.com/sheenaanto/WebMart)

The live project can be viewed [here](https://webmart-df0a62d3a5c7.herokuapp.com/)

Table of Contents

## Purpose of the project

This project was developed as a learning exercise to demonstrate full-stack web development skills using Python with Django and PostgreSQL. It showcases practical implementation of e-commerce functionality including user authentication, product management, shopping cart operations, and order processing with a modern, responsive user interface.

## Features

- **User Authentication**: User registration, login, and dashboard
- **Product Catalog**: Browse products by categories with detailed product information
- **Shopping Cart**: Add/remove items from cart with persistent storage
- **Order Management**: Place orders and track order history
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **Admin Panel**: Django admin interface for managing products, categories, and orders
- **Toast Notifications**: User feedback with success, error, warning, and info messages

### All Users

The following pages are visible to all users, logged in or not.

<details>

<summary>Homepage (landing page)</summary>

![alt text](image.png)

#### Key Features

The landing page offers users different options:

- Navigate through categories
- Navigate through products
- View cart items
- Store
- Search for products
- Sign in
- Register

</details>

<details>
<summary>Store page</summary>

![alt text](image-2.png)

#### Key Features

Different options available are :

- Product details view option
- View cart
- Search for products
- Sign in
- Register

</details>

<details>
<summary>Products details page</summary>

![alt text](image-3.png)

#### Key Features

Different options available are :

- Navigate through categories
- Product details view option
- View cart
- Search for products
- Sign in
- Register

</details>

<details>
<summary>Carts page</summary>

![alt text](image-4.png)

#### Key Features

Different options available are :

- +/- for increase/decrease options
- Remove cart item
- checkout (Login/Register page)
- Continue shopping

</details>

<details>
<summary>login page</summary>

![alt text](image-5.png)

#### Key Features

Different options available are :

- Login button
- Sign up

</details>
<details>
<summary>Register page</summary>

![alt text](image-6.png)

#### Key Features

Different options available are :

- Enter details
- Register
- Login

</details>

### Authenticated (Logged in) Users

The following pages are only available to logged in users.

<details>

<summary>Dashboard</summary>

![alt text](image-7.png)

#### Key Features

This page shows details on:

- Total no.of orders placed
- Order history
- User details
- Logout

</details>

<details>
<summary>Checkout</summary>

![alt text](image-8.png)

#### Key Features

This page offers users different options:

- Enter billing address
- Place order
- Continue shopping
- Logout

</details>

## User Experience

This section details the key elements of the user experience (UX) design for the project, including visual design choices, color schemes, typography, and wireframes. It provides insight into the aesthetic and functional decisions made to enhance usability across different devices, ensuring a seamless and accessible experience for users.

### Design

#### Fonts/Icons

- Inter font
  This font was used throughout the project for headings and prominent text.This is a great choice for an e-commerce platform as it balances professionalism with modern aesthetics.It is a modern, clean sans-serif font that provides excellent readability for web interfaces.

- Font Awesome - Icon library
  The navbar heavily uses Bootstrap Icons for the header elements.

- Bootstrap Icons - Icon library
  Throughout the product pages and cart functionality for action-related icons.

#### Colour

The following colour palette was used in the project:

**Primary Colors**

| Color  | Hex Code  | RGB               | Usage                                      |
| ------ | --------- | ----------------- | ------------------------------------------ |
| Blue   | `#3167eb` | rgb(49, 103, 235) | Primary brand color, buttons, hover states |
| Orange | `#ff9017` | rgb(255, 144, 23) | Accent color, alerts, warnings             |
| Green  | `#00b517` | rgb(0, 181, 23)   | Success states, confirmations              |
| Red    | `#fa3434` | rgb(250, 52, 52)  | Error states, alerts                       |

**Neutral Colors**

| Color      | Hex Code  | RGB                | Usage                        |
| ---------- | --------- | ------------------ | ---------------------------- |
| White      | `#ffffff` | rgb(255, 255, 255) | Background, cards            |
| Light Gray | `#f8f9fa` | rgb(248, 249, 250) | Secondary background         |
| Dark Gray  | `#212529` | rgb(33, 37, 41)    | Text, overlays (40% opacity) |

**Gradient Variations**

- **Blue Gradient**: `rgba(49, 103, 235, 0.9)` to `rgba(33, 37, 41, 0.4)` - Used for hover effects and interactive elements
- **Green Gradient**: `rgba(0, 181, 23, 0.9)` to `rgba(33, 37, 41, 0.4)` - Success state gradients
- **Orange Gradient**: `rgba(255, 144, 23, 0.9)` to `rgba(33, 37, 41, 0.4)` - Warning state gradients
- **Red Gradient**: Similar pattern with red tones - Error state gradients

**Design Approach**

The color scheme follows a clean, modern e-commerce design with:

- **Blue** as the dominant brand color (professional, trustworthy)
- **Bright accent colors** for clear visual hierarchy and status indicators
- **Neutral backgrounds** for readability and content focus
- **Gradients** for hover effects and interactive elements

![alt text](image-10.png)

## Wireframes

These wireframes illustrate how each page is designed to adapt across various screen sizes, including Mobile, Tablet, Desktop, and Larger Screens. While the overall layout remains consistent, adjustments have been made to optimize the user experience for each viewport. Key differences include variations in button placement, layout, and card arrangements to ensure usability and visual clarity across devices.

<details>
<summary>Desktop</summary>

</details>

<details>
<summary>Tablet</summary>

</details>
<details>
<summary>Mobile</summary>

</details>

## Development Process

The development process for this project was carefully planned and documented to ensure efficient progress and transparency.

### Project Planning and Documentation Using GitHub

Userstories All user stories can be found here.Issues were posted to the board and moved from "Todo" to "In Progress" to "Done" as they were completed. MoSCoW prioritisation was applied using the labels must-have, should-have, and could-have.
[Project Board](https://github.com/users/sheenaanto/projects/17)

  <details>
<summary>Must have</summary>

</details>

<details>
<summary>Should have</summary>

</details>
<details>
<summary>Could have</summary>

</details>
<details>
<summary>Won't have</summary>

</details>

## Data Model

This section provides an overview of the data models used in the project, represented through Entity-Relationship Diagrams (ERDs) for each application.

## Data Validation

Django Widget attributes have been used to provide min and max markers for form fields ensuring only values in a certain range can be submitted.

## Testing

The Testing section covers various strategies used to ensure the application's functionality and quality

### Manual Testing

Feature Testing

### Responsiveness

All pages on the live site were tested with the default list of devices in Chrome Devtools.

### Lighthouse

The Lighthouse testing was carried out using a [chrome extension](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) .The results are displayed by page below:

<details>
<summary>Lighthouse results</summary>

</details>

## Validation Testing

### Python Validation

All python code is validated by the [Flake8 linter](https://flake8.pycqa.org/en/latest/) (installed in VSCode) and [CI Python Linter](https://pep8ci.herokuapp.com/). The exceptions to this were django migration files, urls and similar files. However, any custom models, views and forms were validated.

<details>
<summary>webmart</summary>
views.py

![alt text](image-11.png)

</details>
<details>
<summary>store</summary>
views.py

![alt text](image-12.png)

</details>
<details>
<summary>accounts</summary>
views.py

![alt text](image-13.png)

</details>
<details>
<summary>carts</summary>
views.py

![alt text](image-14.png)

</details>
<details>
<summary>orders</summary>
views.py

![alt text](image-15.png)

</details>

### JavaScript Validation

All JavaScript code is validated by the [ESLint](https://eslint.org/) (installed in VSCode) and [jshint](https://jshint.com/).

<details>
<summary>Main templete - base.html</summary>
Contains global JavaScript that runs on all pages - Bootstrap functionality and toast notifications

![alt text](image-16.png)

</details>
<details>
<summary>Checkout page - checkout.html</summary>
Contains page-specific JavaScript for order success modal display

![alt text](image-17.png)

</details>

### HTML Validation

All HTML was validating using the page source of the deployed project using [W3C Markup Validation Service](https://validator.w3.org/nu/?level=warning&doc=https%3A%2F%2Fwebmart-df0a62d3a5c7.herokuapp.com%2F). All pages were clear of all errors/warnings.

<details>
<summary>Results</summary>

![alt text](image-9.png)

</details>

### CSS Validation

The single CSS file was validated using the W3C Validation Service

<details>
<summary>Results</summary>

![alt text](image-9.png)

</details>

## Libraries and Programs Used

This section highlights the key libraries, tools, and platforms utilised throughout the development of the project. These technologies played an essential role in various aspects of the project, from wireframing and version control to deployment and testing.

Balsamiq
Balsamiq was used to wireframe all the pages in the project.
Git
Version control was implemented using Git through the GitHub terminal.
Github
GitHub was used to store the project after being pushed from Git. The cloud service GitHub Pages was used to deploy the project on the web, while GitHub Projects tracked User Stories, Epics, bugs, and other issues throughout the development.
VS code
VS code was used as the primary IDE for development, with ESLint and Flake8 linters configured for JavaScript and Python code validation, respectively.
Heroku
Heroku was used for deploying the project.

## AI Usage in Development

AI tools, specifically GitHub Copilot, were utilized in the development of this project to enhance productivity and code quality. Below is a summary of how AI assisted in various aspects:

Content & Documentation;

Leveraged AI to generate logo,icons, initial drafts for user stories and the README file.
Problem Solving & Debugging;

AI was used as a tool for fixing errors faced in python code in django .Really helped in debugging issue faced during deployment on heroku.
Conclusion:

AI served as a learning tool by:
Explaining CSS properties and Bootstrap utilities
Showing accessibility best practices
Providing multiple solution approaches for implementation challenges
AI tools like GitHub Copilot served as an efficient coding partner, helping to speed up development, reduce syntax errors, and learn best practices. However, all code was reviewed, tested, and customized to meet the specific needs of this project.

## Credits
