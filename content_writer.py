import openai

def generate():
    topic = "Benefits of AI-driven automation"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Write a blog post about {topic}"}],
        api_key="sk-openai-key-placeholder"
    )
    print("[Writer] Post Generated:\n", response["choices"][0]["message"]["content"])
