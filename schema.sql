CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    pword TEXT
);

CREATE TABLE infos (
    id SERIAL PRIMARY KEY,
    users_id INTEGER,
    website TEXT,
    username TEXT,
    pw TEXT,
    FOREIGN KEY (users_id) REFERENCES users
    ON DELETE CASCADE
);