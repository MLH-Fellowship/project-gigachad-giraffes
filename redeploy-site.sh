#!/bin/bash

systemctl daemon-reload

cd ~/project-gigachad-giraffes

git fetch && git reset origin/main --hard

systemctl restart myportfolio