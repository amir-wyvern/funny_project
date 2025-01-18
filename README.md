# ___Funny Project.___



## _Build Image_
* _first build the Repo_

``` bash
docker build -t funny_project .
```

* _Then create .env file:_

```
touch .env
```

* _And need to set the __BOT_TOKEN__ env in .env file:_

```
BOT_TOKEN=xxx
```
## _Run Image_
```
docker run --env-file .env funny_project
```

_Tnx From AHZ :)))_
