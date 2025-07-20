#!/bin/bash
git add .
git commit -m "Auto deploy from orchestrator"
git push origin main
gcloud compute ssh warmwind-agent --command="cd ~/repo && git pull && python3 agent.py"
