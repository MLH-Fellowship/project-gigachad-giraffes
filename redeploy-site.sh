#!/bin/bash
systemctl daemon-reload
cd flask-portfolio
git fetch && git reset origin/main --hard
systemctl restart myportfolio
