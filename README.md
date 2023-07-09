# Data-Representation-Project

## Get Thirsty!
Welcome to Get Thirsty! A Flask-based voting system that settles the age-old question of which Tea is the best. Users can vote for their favorite tea, view the results, and explore tea categories using an external API.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

1. Clone the repository:
    ```
    git clone <repository_link>
    ```
    Example clone command: ![clone](Project.py/static/Images/gitclone.PNG)

2. Navigate to the project directory and install the required dependencies:
    ```
    cd Data-Representation-Project
    pip install -r requirements.txt
    ```
    Example command: ![requirements](Project.py/static/Images/pip_install.PNG)

3. Set up the SQL database by executing the provided SQL scripts found in the `voteDAO.py` file.

4. Configure the database connection in the `dbconfig.py` file.

5. Start the Flask server:
    ```
    python application.py
    ```
    Example command: ![application.py](Project.py/static/Images/python_application.PNG)

6. Open your web browser and access the application at [http://localhost:5000](http://localhost:5000).

7. It is also hosted on PythonAnywhere at [ciaraosull.pythonanywhere.com/loginPage](https://ciaraosull.pythonanywhere.com/loginPage).

## Usage

**Note:** Some endpoints are rate-limited to prevent abuse.
- The `/tea` endpoint is rate-limited to 10 requests per minute per IP address.
- The `/vote/<teaname>` endpoint is rate-limited to 1 request per minute per IP address.

Follow the steps below to use the application:

**User Login:**
1. Navigate to the login page (/loginPage)
2. Enter a valid email address (includes @ symbol).
3. Enter a password (at least 6 characters, with at least one uppercase, one lowercase, and one number).
4. Click "Submit" to log in.

**Vote for your favorite tea:**
1. Navigate to the voting page (/vote)
2. Choose your preferred tea from the available options.
3. Click on your preferred tea to cast your vote. The vote count will increase by 1.
4. Click "Submit" to submit your vote. You'll be redirected to a thank you page with a carousel effect.

**Thank you for Voting page:**
1. This page loads after voting (/thankyou)
2. The carousel effect begins 1 second after the page loads.
3. Click "See Results" to view the final voting outcome.

**View the voting results:**
1. From the thank you page, click "View Results" (/results)
2. Voting results are displayed in both table and chart form.

**Play the Tea Song:**
- On the results page, click "Play Tea Song" to start playing a tea-themed song.
- Click the same button again to stop the music.

**Explore Tea Categories using an external API:**
- On the results page, click "More Tea Info". 
- This connects to an external API that provides information, images, and relevant data for various tea categories.
- The API used is available at [boonakitea.cyclic.app](https://boonakitea.cyclic.app/).

## Features

- CRUD operations through a REST API using Flask.
- SQL database integration for storing and retrieving voting data.
- AJAX calls for dynamic web interface updates.
- Voting system to determine the best tea in Ireland.
- Carousel effect on the thank you page.
- Results page displaying total votes in table and chart format.
- An interactive tea song feature.
- Integration with an external API for exploring tea categories.

