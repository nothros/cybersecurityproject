CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    name TEXT,
    password TEXT,
    role TEXT,
    visible BOOLEAN DEFAULT true
);

CREATE TABLE families (
    id SERIAL PRIMARY KEY,
    familyname TEXT UNIQUE,
    code TEXT,
    visible BOOLEAN DEFAULT true
);

CREATE TABLE familymembers (
    id SERIAL PRIMARY KEY,
    member_id INTEGER,
    family_id INTEGER,
    FOREIGN KEY (member_id) REFERENCES users,
    FOREIGN KEY (family_id) REFERENCES families
    ON DELETE CASCADE
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER,
    doer_id INTEGER,
    task TEXT,
    deadline DATE,
    done BOOLEAN DEFAULT false,
    task_status TEXT DEFAULT 'tekemättä',
    FOREIGN KEY (creator_id) REFERENCES users
    ON DELETE CASCADE,
    FOREIGN KEY (doer_id) REFERENCES users
    ON DELETE CASCADE
);