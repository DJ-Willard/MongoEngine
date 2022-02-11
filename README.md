# MongoEngine Example

This is an example of MongoEngine in action.

It's a simple Flask blog app, where you can insert articles, update, delete and view them.

You can find the data schemas in `database/` and the RESTful resources defined in `resources/`.

**You need MongoDB running for this to work.**

## Getting Started

Run MongoDB locally at port 5000 (or alternatively modify the port and host in `app.py`), install the dependencies, and run.

## Requirements
```
pip install flask pymongo mongoengine
```

## Authors
Created by Ali Hassani for [CIS 322](https://classes.cs.uoregon.edu/22W/cis322/).