# Learning Python Day 2: Connecting to the database

## Description

`web.py ` is connecting us to the browser.
`routes.py` allows us to use GET and POST routes.
`db.py` is connected to the database and can do basic CRUD

## Setup

Create the following table and name the database `pyex`.

```SQL
CREATE TABLE "employees" (
    "id" serial PRIMARY KEY,
    "name" varchar(50)
);
```