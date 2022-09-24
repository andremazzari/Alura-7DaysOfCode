Alura - 7 Days Of Code
==============================

This project consists of data science challenges provided by [Alura](https://alura.com.br). During one week, one challenge per day was sent to the participants.

The tasks acomplished in each day are the following:
- **Day 1:** The first day was devoted to cleaning and transforming data (**Data Wrangling**). For this end, it was used data from [CEAPS](https://www12.senado.leg.br/transparencia/dados-abertos-transparencia/dados-abertos-ceaps) (Quota for the Exercise of Parliamentary Activity by Senators) regarding the expenditure of Brazilian senators. This envolved searching for null values, casting the type of columns, finding and fixing incorrect line breaks in csv files, among others.  

- **Day 2:** The objective of the second day was to find interesting information in the datasets and to tell a story about them (**storytelling**). I tried to answer some questions: What are the total expenditure values in each year ? What about the total value separated by type of expenditure ? And the total expenditure in each month ? What is the higgest value for a indiviual expenditure ? Which senator expended the most and which expended the less ? To answer these question, different plots were made.

- **Day 3:** In the third day, it was used **[Facebook's Prophet](https://facebook.github.io/prophet/)** to forecast the future senate's expenditure. For this, the data from 2008 to 2021 was joined and used to train the models, which was then used to predict the expenditure of the first months of 2022. The **Augmented Dickey-Fuller test** was used to verify if the **time series** was **stationary**. Since the original time series was not stationary, the first differences method was applied to solve this problem. The relative difference between the real and predicted values of expenditure for the first three months 2022 was less than 5%.

- **Day 4:** The fourth consisted in creating a **recommendation system** using the [MovieLens](https://grouplens.org/datasets/movielens/100k/) dataset ml-100k, which contains 100,000 ratings (1-5) from 943 users on 1682 movies. To buld the recommendation models, 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
