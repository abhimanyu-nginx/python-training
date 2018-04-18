A simple flask service that calculates the median of integers added in last minute.

## Endpoints

- /put (POST): Store an integer for one minute. Expects a JSON object in the following structure:

```json
{
    "param": <integer>
}
```

- /median (GET): calculates median request for all integers received over the last minute. Returns a JSON object in the following format:

```json
{
    "median": <median>
}
```

## Testing

```
    python test_app.py
```

```
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"param":4}' http://localhost:5000/app/api/v1.0/put
```

```
    $ curl -i http://localhost:5000/app/api/v1.0/median
```

### Improvements

- Right now everything is in memory, can use database
- Can extend dev, staging and production context
- Improved error handling and authentication
- Logging
