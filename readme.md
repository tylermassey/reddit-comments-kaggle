# Reddit Comments Kaggle Project

For the [Reddit Comments Kaggle Project](https://www.kaggle.com/c/reddit-comments-may-2015), we are attempting to predict which Subreddit a comment originated from based on the comment's content.

## Setup

### Your dev environment

The main tools used are pandas, numpy, IPython, Jupyter, and SciKit-Learn. A complete list of dependencies is located in the ```requirements.txt``` file. You can easily install all of the dependencies by running 

```pip install -r requirements.txt```


Many people create separate python environments for all of their projects in order to keep depdencies separated. There is a great resource on how to do this [here](http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)

### Generating the dataset

If you want to generate the dataset we used in our models (and you don't want to download the CSV file in our repo, download the full dataset [here](https://www.kaggle.com/c/reddit-comments-may-2015/data), and run ```create_data_subset.py``` This will put the data subset in the "data" folder.

The subset is comprised only of comments that belong to the following list of 10 subreddits: gadgets, sports, gaming, news, history, music, funny, movies, food, and book.


## Diving in

An IPython notebook has been setup with some initial commands to load the dataset and display what it looks like. IPython is a  great tool for exploring and modifying data, and the notebook is an excellent place to get started.

While in the ```/project/``` directory, run the command below to open the notebook and start working.

```ipython project.ipynb``` 