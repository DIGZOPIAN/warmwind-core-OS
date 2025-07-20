import yaml, subprocess, openai
from agents import scraper, deployer, writer

with open('config.yaml') as f:
    config = yaml.safe_load(f)

def ask_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": config["llm_prompt"]},
                  {"role": "user", "content": prompt}],
        api_key=config["openai_key"]
    )
    return response['choices'][0]['message']['content']

def parse_and_execute(command):
    intent = ask_llm(f"What actions should be triggered by: {command}")
    if "scrape" in intent: scraper.run()
    if "deploy" in intent: deployer.push()
    if "write article" in intent: writer.generate()
    print("[✔] Completed:", intent)

if __name__ == "__main__":
    import sys
    parse_and_execute(" ".join(sys.argv[1:]))
