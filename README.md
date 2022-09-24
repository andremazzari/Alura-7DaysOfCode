Alura - 7 Days Of Code
==============================

This project consists of data science challenges provided by [Alura](https://alura.com.br). During one week, one challenge per day was sent to the participants.

The tasks accomplished each day are the following:
- **Day 1:** The first day was devoted to cleaning and transforming data (**Data Wrangling**). For this end, it was used data from [CEAPS](https://www12.senado.leg.br/transparencia/dados-abertos-transparencia/dados-abertos-ceaps) (Quota for the Exercise of Parliamentary Activity by Senators) regarding the expenditure of Brazilian senators. This involved searching for null values, casting the type of columns, and finding and fixing incorrect line breaks in CSV files, among others.  

- **Day 2:** The objective of the second day was to find interesting information in the datasets and to tell a story about them (**storytelling**). I tried to answer some questions: What are the total expenditure values each year? What about the total value separated by type of expenditure? And the total expenditure in each month? What is the highest value for an individual expenditure? Which senator expended the most and which expended the less? To answer these questions, different plots were made.

- **Day 3:** On the third day, it was used **[Facebook's Prophet](https://facebook.github.io/prophet/)** to forecast the future senate's expenditure. For this, the data from 2008 to 2021 was joined and used to train the models, which were then used to predict the expenditure for the first months of 2022. The **Augmented Dickey-Fuller test** was used to verify if the **time series** was **stationary**. Since the original time series was not stationary, the first differences method was applied to solve this problem. The relative difference between the real and predicted values of expenditure for the first three months of 2022 was less than 5%.

- **Day 4:** The fourth consisted in creating a **recommendation system** using the [MovieLens](https://grouplens.org/datasets/movielens/100k/) dataset ml-100k, which contains 100,000 ratings (1-5) from 943 users on 1682 movies. To build the recommendation models, the library [Surprise](https://surpriselib.com/) was used, which has multiple KNN-based algorithms for recommendation.

- **Day 5:** On the fifth day, the objective was to create an **API** for the recommendation model created on the fourth day. The [**Flask**](https://flask.palletsprojects.com/en/2.2.x/) library was used for this.

- **Day 6:** On the sixth day, an **A/B test** was applied to a [database](https://www.kaggle.com/datasets/zhangluyuan/ab-testing) available at Kaggle. The [statsmodels](https://www.statsmodels.org/stable/index.html} library was used to perform a Z-test.

- **Day 7:** The objective of the last day was to upload the project to some portfolio, like GitHub.

#7DaysOfCode
