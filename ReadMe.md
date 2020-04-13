## Deltai Software Engineer - Backend test

This is an API that simulates a custom news web search engine. It can take both english and spanish word and lots more. This API has capacity to load more news from different sources but for the scope of this challenge it is limited to just three news objects.

## Installation

Ensure you have the below required softwares installed before setting up the project

- **Python** version >= 3.7.6
- **Flask**
- **mongodb**

## Configuration
After a successful installation of the above stated softwares, copy the below command to your terminal to clone the project 

```bash
git clone https://github.com/Abassade/Delt-Challenge.git
```
After cloning the project, run the command below to install all the required dependencies.

```bash
pip install -r requirements.txt
```

### Known bugs
- There are some commented codes in the project due to issues arose when trying to set up Postgres database on Heroku in which after, the database was changed to Mongodb - (model.py) file and some in (app.py) file

### The API routes Routes (Both are HTTP)
Name                                         | Endpoint
------------------------------------------- | -------------------------------------------
(**GET**) Base endpoint 

Sample call (localhost) - ```localhost:3000```

Sample call (remote) - ```https://deltai-challenge.herokuapp.com```

***sample response***
```json
{
    "error": false,
    "news": "welcome to deltai search engine"
}
```
---

#### Telco - Airtel

Name                                         | Endpoint
------------------------------------------- | -------------------------------------------
(**POST**) Search news                             | /api/news


**Search request**

The Api fetches three news from different sources based on the keywords recieved from the request.

Sample search call (localhost) - ```localhost:3000/api/news```

Sample search call (remote) - ```https://deltai-challenge.herokuapp.com/api/news```

***sample request***

```json
{
 "keywords": ["Mexico", "President"]
}
```

***sample response***

```json
{
    "error": false,
    "news": [
        {
            "content": "Chat with us in Facebook Messenger. Find out what's happening in the world as it unfolds.",
            "ranking": 1,
            "reference": "https://www.cnn.com/videos/world/2020/03/25/mexico-brazil-response-coronavirus-rivers-lead-vpx.cnn",
            "title": "Video shows Mexican president in a crowd of children during coronavirus pandemic"
        },
        {
            "content": "Ford said Tuesday won’t restart its factories in the U.S., Canada and Mexico on Monday, March 30 as the automaker had originally planned.\r\nThe company, which suspended production at its North American factories due to the continued spread of COVID-19, has dec… [+1020 chars]",
            "ranking": 1,
            "reference": "http://techcrunch.com/2020/03/24/ford-wont-restart-north-american-plants-march-30/",
            "title": "Ford won’t restart North American plants March 30"
        },
        {
            "content": "Image copyrightReutersImage caption\r\n Many checkpoints on the US-Canada border are closing\r\nThe US has suspended all non-essential traffic across its borders with both Mexico and Canada as it battles to control the coronavirus outbreak.\r\nThe curbs will go int… [+1377 chars]",
            "ranking": 1,
            "reference": "https://www.bbc.co.uk/news/world-us-canada-51980681",
            "title": "Coronavirus: US, Canada and Mexico restrict border traffic"
        }
    ]
}
```
## Author
**(Abass Makinde)** - <abs4real16.ma@gmail.com>

## License
[MIT](https://choosealicense.com/licenses/mit/)