# Funny Project.

create .env file 

```
BOT_TOKEN=xxx
```

## Build Image
* first build the Repo

``` bash
docker build -t funny_project .
```

* Then create .env file:

```
touch .env
```

* And need to set the __BOT_TOKEN__ env in .env file:

```
BOT_TOKEN=xxx
```
## Run Image
```
docker run --env-file .env funny_project
```

_Tnx From AHZ :)))_
