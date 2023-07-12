# Single Table Design Recipe Template

## 1. Extract nouns from the user stories or specification

Nouns:

artist, name, genre
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| artist                | name, genre         |

Name of the table (always plural): `albums`

Column names: `name`, `genre`

## 3. Decide the column types

```

id: SERIAL
name: text
genre: text
```

## 4. Write the SQL

SQL to add to exist database

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  title text,
  release_year text
);




