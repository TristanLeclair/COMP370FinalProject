# Unveiling the Media Tapestry: A Comprehensive Analysis of Movie Coverage

## Introduction

Welcome to our data science project. Our goal is to delve into the world of media coverage for movies, with a specific focus on "Killers of the Flower Moon" and its comparison to other intriguing titles. In this README, you'll find details on our motivations, installation guidelines, data sources, results, and insights gained from analyzing media narratives around these films.

## Abstract

This project revolves around an in-depth analysis of media coverage for the movie "Killers of the Flower Moon" in comparison to ten other notable films. Leveraging data from newsapi.org, our exploration spans various topics such as box office performance, awards, production, and more. Key findings indicate a distinct pattern in coverage, with "Killers of the Flower Moon" standing out in topics like streaming, awards, and production. This README encapsulates our journey, providing a glimpse into the world of media representation for these cinematic creations.

## Data

We've decided to look at all the wide-releases that had a top 5 domestic weekend gross since Nov 24th 2023 inclusive according to [the-numbers.com](the-numbers.com). The list includes re-releases.

### Data Source

We gathered a dataset of 490 English articles from newsapi.org, focusing on movies like "Killers of the Flower Moon" and its counterparts. To refine our search, we used specific keywords, ensuring relevance to our selected films.

### Data Description

Each article contained essential attributes, including source, author, title, description, URL, publication date, and content. Despite an initial query yielding 4,451 articles, API constraints limited us to extracting a total of 490.

### Data Quality and Missing Values

Our dataset exhibited high quality, with only one article marked as "[Removed]" by the API, subsequently removed from the dataset.

### Data Exploration

A preliminary exploration revealed insights into article sources, title/description lengths, and distribution across topics like box office, streaming, awards, production, plot/performances, and promotion.

## Results

### Typology:

We created 2 typologies of the articles based on the movies and topics they covered. The typologies are as follows (abridged, the full descriptions are in the [report](./Killers_of_the_Flower_Moon_Media_Coverage.pdf)):

| Movie | Description |
| --- | --- |
| Movie titile | Articles that mention the movie title |
| Not Mentioned | Articles that do not mention the movie title (e.g articles that are about movies but were cropped in the data before mentioning the name of the movie) |
| Not Relevant | Articles that aren't about movies (e.g an article about Napoleon Bonaparte, the person, not the movie) |

| Topic | Description |
| --- | --- |
| Box Office | Articles that mention the box office performance of a movie |
| Streaming/home-viewing | Articles that mention the streaming/home-viewing performance of a movie |
| Awards | Articles that mention awards that movie, and/or its actors, received |
| Production | Articles that mention the production of a movie |
| Plot/Performances | Articles that mention the plot or performances of a movie |
| Promotion | Articles that mention the promotion of a movie |
| Movie only mentioned | Articles that only mention a movie, but not any of the topics above |

### Movie Coverage:

"Killers of the Flower Moon" dominated with 96 mentions, followed by "Hunger Games: The Ballad of Songbirds and Snakes" (87), and "The Marvels" (76).

### Topic Distribution:

Box Office (36.4%) and Plot/Performances (26.6%) were prominent topics. "Killers of the Flower Moon" exhibited high relative coverage in Streaming, Awards, and Production, but less in Promotion and Box Office.

### TF-IDF:

Top words by TF-IDF for each topic unveiled nuanced insights into media emphasis on different aspects of these films.

## Discussion Section:

### Relative Coverage:

"Killers of the Flower Moon" represented 17.6% of all movie articles, displaying a hierarchy in media coverage among the selected films.

### Aspects Covered:

Media interest varied; while box office performance received less coverage for "Killers of the Flower Moon," awards and streaming generated more attention than average.

### Underrepresentation:

"Thanksgiving" and "After Death" lacked coverage, potentially impacting the overall representation of movies in the dataset.

# Overview of the repository

Explore the project's structure, installation guidelines and test procedures.

## Installation and Setup

### Python

*Optional: create a virtual environment*
`python -m venv venv`

Install dependencies:
`python -m pip install -r requirements.txt`

### API Keys

Please create a file named `creds.py` in the root directory of the project and add the following lines:

```Python
API_KEY = "<your-api-key-goes-here>"
```

### Tests

#### Running tests

The test folder contains unit tests for the project. To run them, use the following command:
```bash
make run_tests
```

#### Adding tests

The tests folder mimics the structure of the project.
Tests for `src` should be placed in `tests/src`, tests for `scripts` should be placed in `tests/scripts`, etc. 

**Don't forget to add `__init__.py` files to *all* of the folders you create inside `tests/` or they won't be automatically discovered.**

To add a new test or to test a new module, create a new file in the tests folder with the name `test_<name>.py` and add the following code:

```Python
import unittest

class Test<Name>(unittest.TestCase):
    def test_<name>(self):
        # Test code goes here
        pass

if __name__ == '__main__':
    unittest.main()
```

## Code structure
```
.
├── assignment_description
├── data
│   ├── coded
│   ├── interim
│   │   └── keywords
│   ├── processed
│   └── raw
│       └── movies
├── notebooks
├── scripts
│   └── python
├── src
│   └── common
│   └── data
└── tests
    └── src
        └── common
```

## Contributors

- [Tristan Leclair-Vani](https://github.com/TristanLeclair) : All other writing and testing of code for gathering, processing and analysing the data, including data exploration notebooks and creation of graphs. Repository structure and README. Introduction and Data sections of report.
- [Jean-Alexandre Nolin](https://github.com/JANolin) : Methods, Discussions for the topics focused on by the media, Formatting, Introduction, Bug finder of tested code.
- [Juan Rodriguez](https://github.com/JiRodriguez2411) : Results, Discussions
- [Michael Almanza](https://github.com/MichaelAlmanza) : Code for TF-IDF, results and discussion for TF-IDF, typology section of report, process and retrieval for choosing which movies to include.
- Everyone: Discussions, report, open-coding, typology refinement, and project management.

## Acknowledgements

### Libraries

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [notebook](https://jupyter.org/)
