from openai import OpenAI
client = OpenAI(
    base_url="https://api.chatanywhere.tech/v1",
)

print(client._version)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.8,
    max_tokens=60,
    messages=[
        {"role": "system", "content": "You are a creative AI."},
        {"role": "user", "content": "请给我的花店起个名"},
    ],
)

print(response.choices[0].message.content)
