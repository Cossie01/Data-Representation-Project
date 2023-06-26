# Data-Representation-Project
<h1> Get Thirsty!</h1>
<h3>Welcome to Get Thirsty! A Flask-based voting system that settles the age-old question of which Tea is the best. Users can vote for their favorite tea, view the results, and explore tea categories using an external API.</h3>

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)



## Installation

1. Clone the repository:
   ![clone](/static/Images/gitclone.png)

2. Install the required dependencies:
   ![requirements](/static/Images/pip_install.png)

3. Set up the SQL database by executing the provided SQL scripts.

4. Configure the database connection in the `config.py` file.

5. Start the Flask server:
   ![application.py](/static/Images/python_application.png)

6. Open your web browser and access the application at [http://localhost:5000](http://localhost:5000).


## Usage

**Vote for your favorite tea:**

1. Navigate to the homepage.
2. Choose your preferred tea from the available options.
3. Click the "Vote" button to submit your vote.
4. You will be redirected to a thank you page with a carousel effect.
5. The `/vote/<teaname>` endpoint is rate-limited to 1 request per minute per IP address.

**View the voting results:**

- From the thank you page, click the "View Results" button.
- The total votes will be displayed in both table and chart form.

**Play the tea song:**

- On the results page, click the "Play Tea Song" button to start playing the tea-themed song.
- Click the same button to turn off the music.

**Explore tea categories using an external API:**

- On the results page, click the "Explore Tea Categories" button.
- This will connect to an external API that provides information, images, and relevant data for various tea categories.

**Note:** Usage limits are in place to ensure fair access and prevent abuse.
- The `/tea` endpoint is rate-limited to 10 requests per minute per IP address.
- The `/vote/<teaname>` endpoint is rate-limited to 1 request per minute per IP address.


## Features

- CRUD operations through a REST API using Flask.
- SQL database integration for storing and retrieving voting data.
- AJAX calls to perform CRUD operations and update the web interface dynamically.
- Voting system to settle the debate on the best tea.
- Results page displaying total votes in table and chart form.
- Carousel effect on the thank you page.
- Tea song that can be played and turned off.
- Integration with an external API for exploring tea categories.

