ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
# Upload .pub to github

git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
