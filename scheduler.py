import schedule, time
from agents import writer

def job():
    print("[Scheduler] Running scheduled task...")
    writer.generate()

def run():
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
