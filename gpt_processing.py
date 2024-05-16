from openai import OpenAI
import yaml

key = "hah"

with open("config.yaml", 'r') as file:
    data = yaml.safe_load(file)
    key = data["token"]

client = OpenAI(api_key = key)

def commentate(stats):
    #return "BANG"
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", 
                     "content":  "Given the past stats, commentate with this live play-by-play update in a live nba game, pretending you're the commentator: " + stats}]
    )
    return response.choices[0].message.content.strip()

