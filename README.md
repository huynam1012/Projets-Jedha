[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
   <a href="https://github.com/huynam1012/Projets-Jedha">
    <img src="https://yt3.ggpht.com/a/AATXAJx-EbvNy-M6OTC3IRISPg-tJMRKzAXl_B8EmZTf=s900-c-k-c0xffffffff-no-rj-mo" alt="Logo" width="100" height="100">
  </a>
  <h3 align="center">Huy-Nam TRAN's projects</h3>

  <p align="center">
    Class : dsmft-paris-14<br />
    Final exam's date : Janvier, 19th 2022
    <br />
    <a href="hhttps://github.com/huynam1012/Projets-Jedha"><strong>Explore the 6 projects for 6 blocks »</strong></a>
    <br />
    <br />
    ·
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of projects</summary>
  <ol>
    <li><a href="Blocks 1: Kayak">Project 1 # Kayak</a></li>
    <li><a href="Blocks 2: Speed Dating">Project 2 # Speed Dating</a></li>
    <li><a href="Blocks 3: Machine Learning">Project 3 # Uber Pickups</a></li>
    <li><a href="#Blocks 4: Disaster Tweets">Projet 4 # Disaster Tweet</a></li>
    <li><a href="#Blocks 5: Deployment">Projet_5 # Wine-O-Meter</a></li>
    <li><a href="#Blocks 6: Start-up">Projet_6 # Projet final: Start-up Prediction</a></li>
  </ol>
</details>
<br />

<!-- PROJECT 1  -->
## <a href="https://github.com/huynam1012/Projets-Jedha/blob/main/Bloc%201_Kayak/Plan_your_trip_with_Kayak_Huy-Nam%20TRAN_FR.ipynb" target="_blank">Project 1: Kayak</a>

Project 🚧

The marketing team needs help on a new project. After doing some user research, the team discovered that 70% of their users who are planning a trip would like to have more information about the destination they are going to.

In addition, user research shows that people tend to be defiant about the information they are reading if they don't know the brand which produced the content.

Therefore, Kayak Marketing Team would like to create an application that will recommend where people should plan their next holidays. The application should be based on real data about:

    Weather.
    Hotels in the area.

The application should then be able to recommend the best destinations and hotels based on the above variables at any given time.
Goals 🎯

As the project has just started, your team doesn't have any data that can be used to create this application. Therefore, your job will be to:

    Scrape data from destinations.
    Get weather data from each destination.
    Get hotels' info about each destination.
    Store all the information above in a data lake.
    Extract, transform and load cleaned data from your datalake to a data warehouse.


<!-- PROJECT 2  -->
## <a href="https://github.com/huynam1012/Projets-Jedha/blob/main/Bloc%202_Speed%20dating/01-Project_speed_dating_Huy-Nam%20TRAN_FR.ipynb" target="_blank">Project 2: Speed Dating</a>

Challenge description

We will start a new data visualization and exploration project. Your goal will be to try to understand love! It's a very complicated subject so we've simplified it. Your goal is going to be to understand what happens during a speed dating and especially to understand what will influence the obtaining of a second date.

This is a Kaggle competition on which you can find more details here :

<a href="https://www.kaggle.com/annavictoria/speed-dating-experiment#Speed%20Dating%20Data%20Key.doc" target="_blank">Speed Dating Dataset</a>

Take some time to read the description of the challenge and try to understand each of the variables in the dataset. Help yourself with this from the document : Speed Dating - Variable Description.md
Rendering

To be successful in this project, you will need to do a descriptive analysis of the main factors that influence getting a second appointment.

Over the next few days, you'll learn how to use python libraries like seaborn, plotly and bokeh to produce data visualizations that highlight relevant facts about the dataset.

For today, you can start exploring the dataset with pandas to extract some statistics.



<!-- PROJECT 3  -->
## <a href="https://github.com/huynam1012/Projets-Jedha/blob/main/Bloc%203_Machine%20learning/Uber/01-Uber_Pickups_Huy-Nam_TRAN_FR.ipynb" target="_blank">Project 3: UBER Pickups</a>

Company's Description 📇
Uber is one of the most famous startup in the world. It started as a ride-sharing application for people who couldn't afford a taxi. Now, Uber expanded its activities to Food Delivery with Uber Eats, package delivery, freight transportation and even urban transportation with Jump Bike and Lime that the company funded.

The company's goal is to revolutionize transportation accross the globe. It operates now on about 70 countries and 900 cities and generates over $14 billion revenue! 😮
Project 🚧

One of the main pain point that Uber's team found is that sometimes drivers are not around when users need them. For example, a user might be in San Francisco's Financial District whereas Uber drivers are looking for customers in Castro.

(If you are not familiar with the bay area, check out Google Maps)

Eventhough both neighborhood are not that far away, users would still have to wait 10 to 15 minutes before being picked-up, which is too long. Uber's research shows that users accept to wait 5-7 minutes, otherwise they would cancel their ride.

Therefore, Uber's data team would like to work on a project where their app would recommend hot-zones in major cities to be in at any given time of day.
Goals 🎯

Uber already has data about pickups in major cities. Your objective is to create algorithms that will determine where are the hot-zones that drivers should be in. Therefore you will:

    Create an algorithm to find hot zones.
    Visualize results on a nice dashboard.


<!-- PROJECT 4  -->
## <a href="https://github.com/huynam1012/Projets-Jedha/blob/main/Bloc%203_Machine%20learning/Uber/01-Uber_Pickups_Huy-Nam_TRAN_FR.ipynb" target="_blank">Project 4: Disaster_tweets</a>

Project description: https://www.kaggle.com/c/nlp-getting-started

    
<!-- PROJECT 5  -->
## <a href="https://github.com/huynam1012/Projets-Jedha/blob/main/Bloc%205_Deployment/Test_Endpoint_Huy-Nam_TRAN.ipynb" target="_blank">Project 5: Wine-o-meter</a>

Machine Learning in production

Wine-o-meter is a future unicorn application. It allows wine producers to predict the quality score of their wine based on physicochemical inputs. The startup behind this innovation is convinced about its ability to disrupt the world of wine. 🍷
Project 🚧

The data-science team has worked together on creating the best model predicting the quality score (from 0 to 10) of multiple wines. The next step is to include this model into the mobile application. The development team is expecting an API endpoint in order to request the model and display the result inside the application.

Your job is to put the trained model into production. Hopefully, the team provided you their work:

    a model.joblib which is the trained model pickled (saved using joblib library),
    the notebook used to train the model (Model_Training.ipynb) and the dataset (winequality.csv), so you can have a look,
    a test notebook (Test_Endpoint.ipynb) so you can assert that your endpoint is meeting the requirements.

Goals 🎯

Your mission is to put this model into production by building an API. To succeed you need to:

    provide a /predict endpoint,
    provide a small documentation for the developer team at the index of your website.

In the following link, we describe the technical expectations: https://wine-hnt.herokuapp.com

<!-- PROJECT 6  -->
## <a href="https://raw.githubusercontent.com/huynam1012/Projets-Jedha/main/Bloc%206_Projet%20Start-up/Presentation_Huy%20Nam%20Tran%2C%20Said%20%2C%20Amir%20%2C%20Matthieu%20Verrecchia.pdf" target="_blank">Project 6: Start-up Prediction</a>

This is the final project as a Jedha student. The object of the project is development an application that allows to predict the success of startups based on some characteristics.

In the following link, we describe the technical expectations: https://predictstartup.herokuapp.com


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/huy-nam-tran/
