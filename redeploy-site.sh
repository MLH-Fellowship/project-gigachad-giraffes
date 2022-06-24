cd flask-portfolio

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate

python3 pip install -r requirements.txt

tmux new-session -d -s flask-portfolio 'source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'
