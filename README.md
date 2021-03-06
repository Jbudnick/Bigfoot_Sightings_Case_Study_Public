
# Natural Language Processing / Unsupervised Learning Case Study - Bigfoot Sightings
<p align="center">
   <img src="/images/Bigfoot_Harry.gif">
</p>

In this project I worked with several data scientists to examine Bigfoot datasets of reported sightings from all over the USA and Canada. The data came from a text based JSON file, and we were able to cluster the data into categories based on words that have been used. We found that the highest prevalence of sightings comes from the Pacific Northwest.

![](/images/sighting_map.png)

![](/images/sighting_map_canada.png)


# Data Import and Exploratory Data Analysis

![](/images/Top_States_sightings_bar.png)

11.6% (The majority) of reported sightings occurred in Washington.

![](/images/Top_Months_sightings_bar.png)

The majority of Canadian Sightings occurred in British Columbia.

![](/images/Top_Canada_Sightings.png)


![](/images/Top_Years_sightings_line.png)

* Many entries for years in the data were not precise. This data was ommitted from this plot.
* 2017 was ommitted - only 2 sightings - assuming data was extracted early 2017

# Text Processing Pipeline
To clean and process our data, we followed the following procedure.

1. Convert `json` data to pandas `DataFrame` with following columns:
    * 'year'
    * 'season'
    * 'month'
    * 'date'
    * 'state'
    * 'county'
    * 'location details'
    * 'nearest town'
    * 'nearest road'
    * 'observed'
    * 'also noticed'
    * 'other witnesses'
    * 'other stories'
    * 'time and conditions'
    * 'environment'
1. Clean text data
    * Lowercase
    * Remove punctuation
    * Lemmatize (WordNet)
    * Remove stop words
        * Added some stop words (Ex. "sasquatch", "bigfoot", etc.)
1. Created TF-IDF Matrix
1. Used NMF to infer topics
    * Extracted top words for each topic 



# ML algorithms for analysis
Algorithm chosen: Non-Neagative Matrix Factorization (NMF)<br><br>
We chose NMF because it allows us to easily interpret the impact each word has in creating the infered topics. It also allows us to easily assign a topic to each document based on how heavily that document loads onto a given topic. Furthermore, we were not concerened with our latent topics being orthoganal, so the increase in interpretability of the weights outweighed being able to interpret the amount of variance each topic explained. 
        

# Tuning and evaluating model
We took an iterative approach to tuning our model in which we mainly tuned the stop words list and the amount of latent topics. We started by running NMF with n_components = 3. We then looked at the top words associated with each topic. We found that the topics offered little description of the sighting because the top words were generic. We removed the words we viewed as non descriptive from our analysis by adding them to the stop words list. We continued through this process until we were satisfied that the topics' top words gave insight to how the sighting unfolded. As we were adding words to our stop words list we were also increasing and decreasing the n_components. We settled on five topics because we noticed that the top words for the five topics appeared to be describing the activity the observer was engaged in when the sightings occured (Hiking, Camping, Hunting/Winter, Home-Sighting, Driving)


# Results

## Observations

### Topics & Features

Based on observations in the data, topics and features were analyzed using 10 words and 5 topics.

|   Topic # | Word #0   | Word #1   | Word #2   | Word #3   | Word #4   | Word #5   | Word #6   | Word #7   | Word #8   | Word #9   |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|         0 | tree      | just      | deer      | wood      | trail     | area      | river     | friend    | got       | bear      |
|         1 | heard     | sound     | scream    | loud      | night     | sounded   | tent      | noise     | howl      | animal    |
|         2 | track     | print     | inch      | snow      | footprint | toe       | picture   | trail     | area      | size      |
|         3 | house     | dog       | window    | door      | outside   | said      | night     | went      | ran       | home      |
|         4 | road      | car       | saw       | creature  | driving   | tall      | hair      | arm       | highway   | dark      |

### Topic Names
|   Topic # | Name   |
|-----------|-----------|
|         0 | Hiking      |
|         1 | Camping     |
|         2 | Hunting/Winter     |
|         3 | Home-Sighting     | 
|         4 | Driving      |

![](/images/Observations.png)

#### Topic 0: Hiking
<p align="center">
   <img src="/images/wordcloud_topic0.png">
</p>

#### Topic 1: Camping
<p align="center">
   <img src="/images/wordcloud_topic1.png">
</p>

#### Topic 2: Hunting/Winter
<p align="center">
   <img src="/images/wordcloud_topic2.png">
</p>

#### Topic 3: Home-Sighting
<p align="center">
   <img src="/images/wordcloud_topic3.png">
</p>

#### Topic 4: Driving
<p align="center">
   <img src="/images/wordcloud_topic4.png">
</p>

<br>

## Time and Conditions

### Topics & Features

Times and Conditions were grouped together in the database, so all values were unique. NMF was used to classify the words used into topics and this was used to determine the time of day or weather condition of when the sightings occurred. 

|   Topic # | Word #0   | Word #1   | Word #2   | Word #3   | Word #4   | Word #5       | Word #6   | Word #7   |
|-----------|-----------|-----------|-----------|-----------|-----------|---------------|-----------|-----------|
|         0 | night     | late      | moon      | cool      | midnight  | summer        | 11pm      | clear     |
|         1 | sunny     | warm      | clear     | hot       | bright    | noon          | degree    | cloud     |
|         2 | pm        | 10        | 11        | 1100      | 900       | approximately | 400       | 800       |
|         3 | morning   | early     | evening   | mid       | late      | overcast      | sun       | cold      |
|         4 | afternoon | late      | early     | mid       | evening   | overcast      | cloudy    | 200       |
|         5 | clear     | dark      | weather   | sky       | light     | dusk          | moon      | evening   |
|         6 | day       | bright    | summer    | mid       | middle    | nice          | noon      | sun       |

### Topic Names

|   Topic # | Name      |
|-----------|-----------|
|         0 | Late Night|
|         1 | Midday    |
|         2 | Evening   |
|         3 | Morning   | 
|         4 | Cloudy    |
|         5 | Dark      |
|         6 | Light     |

![](/images/TimeConditions.png)

It looks like the majority of the sightings occurred during the evening, and/or while it was dark outside, but the sightings occurred at all times of day and under a wide variety of conditions.

