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
 "keywords": ["i", "love", "you"]
}
```

***sample response***

```json
{
  "error": false,
  "news": [
    {
      "content": "Day Three of Tech 911 here-to-answer-your-questions week, and Im barreling through reader comments as if it were my job. Which it is. It is my job, and I love helping out as best I can. Remember, if you have a question about the tech of working from home, bec… [+5095 chars]",
      "ranking": 0.8,
      "reference": "https://lifehacker.com/why-does-my-work-laptop-have-slower-wifi-than-my-other-1842489912",
      "title": "Why Does My Work Laptop Have Slower Wifi Than My Other Devices?"
    },
    {
      "content": "It is possible that, while stocking up to stay home, you purchased too much of one particular item. I did this with eggs. It all happened so fast: I was at my local restaurant supply store, buying a normal amount (four pounds) of butter, when I was suddenly m… [+3043 chars]",
      "ranking": 0.78,
      "reference": "https://skillet.lifehacker.com/so-you-bought-too-many-eggs-1842454706",
      "title": "So, You Bought Too Many Eggs"
    },
    {
      "content": "Its obvious that Meathead Goldwyn knows a lot about meatbut it must be said that after nearly half a century of eating and drinking for a living, he knows a lot of other things, too. His site, AmazingRibs.com, is not only a font of BBQ and meat-centric grilli… [+14793 chars]",
      "ranking": 0.0,
      "reference": "https://skillet.lifehacker.com/im-meathead-goldwyn-of-amazingribs-and-this-is-how-i-ea-1842364465",
      "title": "I'm Meathead Goldwyn of AmazingRibs and This Is How I Eat"
    }
  ]
}
```
## Author
**(Abass Makinde)** - <abs4real16.ma@gmail.com>

## License
[MIT](https://choosealicense.com/licenses/mit/)