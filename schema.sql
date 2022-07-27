DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fullname TEXT NOT NULL,
    bio TEXT NOT NULL
);