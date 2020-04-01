# Learning Python Day 2: Connecting to the database

## Description

- `web.py ` is connecting us to the browser.
- `routes.py` allows us to use GET and POST routes.
- `db.py` is connected to the database and can do basic CRUD

## Setup

Create the following table and name the database `pyex`.

```SQL
CREATE TABLE "employees" (
    "id" serial PRIMARY KEY,
    "name" varchar(50)
);
```

## Links that were helpful!

For installation:
- https://flask.palletsprojects.com/en/1.1.x/installation/

For connecting to browsers:
- https://www.youtube.com/watch?v=mqhxxeeTbu0

For CRUD:
- https://www.youtube.com/watch?v=s_ht4AKnWZg

- https://wiki.postgresql.org/wiki/Psycopg2_Tutorial

- https://www.youtube.com/watch?v=2PDkXviEMD0