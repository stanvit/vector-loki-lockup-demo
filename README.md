A small stack to reporoduce the [#9251](https://github.com/vectordotdev/vector/issues/9251) issue locally.

```sh
docker-compose up -d
./post-data.py
```

When `label_cardinality` set in [the script](./post-data.py) is larger than `request.concurrency`
for the loki sink, Vector versions 0.16.0 and higher stops responding after some amount of processed
log records.
