# holy_sounds
# Holy Sounds Website

Welcome to the README file for the Holy Sounds Band website. This document will guide you through 
the steps necessary to build and run the application using both virtual environment (venv) and Docker.
The Holy Sounds website is designed to showcase the details, music,events, and contact information for
the soulful and melodious Holy Sounds band from Johannesburg, South Africa.

## Table of Contents
### Getting Started
    - Prerequisites
    - Installation
### Running the Application
    - Using Virtual Environment (venv)
    - Using Docker
### Accessing the Website
### Customization
### Contact

## Getting Started
### Prerequisites
    Before you begin, make sure you have the following prerequisites installed:
    - Python (>= 3.6)
    - Docker (optional, if you want to use Docker for deployment)
### Installation
1. Clone the repository:
    bash
    _**Copy code**_
    git clone https://github.com/your-username/holy-sounds-website.git
    cd holy-sounds-website
2. Create a virtual environment (venv):
    bash
    _**Copy code**_
    python3 -m venv venv
3. Activate the virtual environment:
    On macOS and Linux:
    bash
    _**Copy code**_
    source venv/bin/activate
   
    On Windows:
    bash
   _**Copy code**_
    venv\Scripts\activate
4. Install the required packages:
    bash
    _**Copy code**_
    pip install -r requirements.txt

## Running the Application
### Using Virtual Environment (venv)
 1.   Make sure your virtual environment is activated.
 2.   CD to holy_sounds_website
 3.   If you need to build the docker image again then follow these commands:               
      bash
      _**Copy code**_
      docker build -t holy_sounds_website ./
      docker run -d -p 8000:8000 holy_sounds_website
 4.  The website should now be accessible at http://8000:8000/ in your web browser.
 6.  To stop the development server, press Ctrl + C in the terminal.
### Using Docker
 1. Make sure your docker desktop is active
 2. Login to dockerhub
 3. Pull the  docker image:
    bash
      _**Copy code**_
    docker pull sinqo/holy_sounds_website
4. Run the image:
5. Option for portal choose 8000 then run
6. After running the image click on the website 8000:8000  this will take you to web page and you see the image.

## Accessing the Website
   Once the application is running, you can access the Holy Sounds website by opening your web browser and
   navigating to **'http://8000:8000/'**.

## Customization
   To make this website your own, follow these steps:
1.  Replace the placeholder content in **'templates/index.html'** with your own band details, music, and events.
2.  Update the navigation links in the header of **'index.html** to match your website structure.
3.  Customize the CSS styles by editing **'assets/styles.css.'**

## Contact
    If you have any questions or need further assistance, please feel free to reach out to us:
    
    Email:Sinqobilekent@gmail.com
    LinkedIn:Holy Sounds Band LinkedIn Profile.

    This project was created by [Sinqobile Kanty Moluli].

Contributor 1 - [Owner]

        
