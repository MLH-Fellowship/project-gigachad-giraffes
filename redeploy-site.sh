#!/bin/bash
systemctl daemon-reload
cd flask-portfolio
git fetch && git reset origin/main --hard
source env1/bin/activate
pip install -r requirements.txt
systemctl restart myportfolio
