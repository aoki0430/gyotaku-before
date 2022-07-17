docker-compose build
docker-compose up -d
heroku create hoge
runtime.txt
requirements.txt
Procfile
git subtree push --prefix app/flaskapp/ heroku master

Compiled slug size: 625.5M is too large (max is 500M)
heroku plugins:install heroku-repo
heroku repo:gc --app <アプリ名>
heroku repo:purge_cache --app <アプリ名>

https://qiita.com/kimisyo/items/e73844cf1ff46e2f26c5