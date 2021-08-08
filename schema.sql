CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    firstname TEXT,
    password TEXT,
    role TEXT
);

CREATE TABLE families (
    id SERIAL PRIMARY KEY,
    family_name TEXT,
    code TEXT
 );

CREATE TABLE familymembers ( 
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES users,
    family_id INTEGER REFERENCES families
);
