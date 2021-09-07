
# pysententia

[![Lifecycle:experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
[![](https://img.shields.io/github/last-commit/71point4/pysententia.svg)](https://github.com/71point4/sententia/commits/develop)

[Sententia](https://github.com/71point4/sententia) provides access to
media sentiment data from the Bureau for Economic research.

The homepage for the {sententia} python package is at
<https://github.com/71point4/pysententia>.

## Installation

### Install from PyPI

Install from PyPI.

```bash
pip3 install pysententia
```

### Install from GitHub

Install from GitHub.

```bash
install git+https://github.com/71point4/pysententia
```

## Testing

To run the test suite:

1. Set the `SENTENTIA_KEY` environment variable.
2. Launch the tests with

```bash
pytest
```

## Documentation

To build the documentation:

```bash
make -C docs/ html
```

## Set the API Key

To access the API you’ll need to first specify an API key as provided to
you by the BER.

```python
import os

key = os.getenv('SENTENTIA_KEY')
```
## The API interface

Besides providing sentiment calculations from different word-list
dictionaries, the API interface provides access to the various
permutations that is available in calculating a sentiment score (Within
text and across time):

<img src="_static/figures/aggregations.png" width="1236" style="display: block; margin: auto;" />

-   Sentiment calculation `WITHIN` the article
    -   In the API this is set by the `aggr` parameter
-   Sentiment calculation `ACCROSS` a time period
    -   This does not need to be set. API returns four aggregations:
        -   `mean_sentiment`
        -   `relative`
        -   `absolute`
        -   `sent_log`

## Usage

```python
from pysententia import sententia

sent = sententia(key = key)
```

## Sentiment Index

Get media sentiment index values for specified media source, model,
topic, dictionary, frequency, and aggregation method combination.

```python
sent.sent_index(
   source = "businessday",
   model = "model_2021-05-15",
   topic = "global",
   freq = "month",
   dict = "loughran",
   aggr = "sent_logit"
   )
```

# Count of articles that make up sentiment

Get a count of the number of articles for a specified media source, model, topic, and frequency of aggregation.

```python
sent.sent_counts(
   source = "all",
   model = "model_2021-05-15",
   topic = "global",
   freq = "week"
   )
```

# Date polarity

Get a count of the number of positive and negative articles for a specified model, topic, dictionary, aggregation method, and frequency.

```python
sent.sent_date_polarity(
   source = "all",
   model = "model_2021-05-15",
   topic = "global",
   freq = "week",
   dict = "loughran",
   aggr = "sent_logit"
   )
```

# Word polarity

Get the top 50 most frequently occurring positive and negative words for a specified model, topic, dictionary, aggregation method, and frequency. The timeframe over which these words are selected depends on the specified frequency (day = 30 days, week = 3 months, month = 6 months).

```python
sent.sent_word_polarity(
   source = "all",
   model = "model_2021-05-15",
   topic = "economy",
   freq = "day",
   dict = "loughran"
   )
```
