CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    name TEXT,
    password TEXT,
    role TEXT
);

CREATE TABLE families (
    id SERIAL PRIMARY KEY,
    familyname TEXT UNIQUE,
    code TEXT
 );

CREATE TABLE familymembers (
    id SERIAL PRIMARY KEY,
    family_id INTEGER,
    member_id INTEGER,
    FOREIGN KEY (family_id) REFERENCES families,
    FOREIGN KEY (member_id) REFERENCES users
    ON DELETE CASCADE
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER,
    doer_id INTEGER,
    task TEXT,
    deadline DATE,
    done BOOLEAN DEFAULT false,
    FOREIGN KEY (creator_id) REFERENCES users,
    FOREIGN KEY (doer_id) REFERENCES users
    ON DELETE CASCADE
);