import yaml, subprocess, openai, json, datetime
from agents import scraper, deployer, writer, telegram_bot, wallet_monitor

with open('config.yaml') as f:
    config = yaml.safe_load(f)

def log_memory(event):
    with open("memory.json", "r+") as memfile:
        data = json.load(memfile)
        data["last_run"] = str(datetime.datetime.now())
        data["agent_logs"].append(event)
        memfile.seek(0)
        json.dump(data, memfile, indent=2)
        memfile.truncate()

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
    log_memory({"input": command, "intent": intent})
    if "scrape" in intent: scraper.run()
    if "deploy" in intent: deployer.push()
    if "write article" in intent: writer.generate()
    if "telegram" in intent: telegram_bot.run()
    if "wallet" in intent: wallet_monitor.run()
    print("[✔] Completed:", intent)

if __name__ == "__main__":
    import sys
    parse_and_execute(" ".join(sys.argv[1:]))
