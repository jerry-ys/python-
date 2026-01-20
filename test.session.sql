-- @block
USE airbnb;

-- @block
SHOW DATABASES;

-- @block
CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    country VARCHAR(2)
);

-- @block
INSERT INTO users(email,bio,country)
VALUE(
    'hello@world.com',
    'i love strangers!',
    'US'
);

-- @block
INSERT INTO users(email,bio,country)
VALUES
    ('chillo@world.com','foo','US'),
    ('hola@munda.com','bar','MX'),
    ('bonjour@monde.com','baz','FR');

-- @block
SELECT * FROM users;

-- @block
SELECT email,id FROM users
ORDER BY id ASC
LIMIT 2;

-- @block
SELECT email,id,country FROM users

WHERE country = 'US'
AND email LIKE 'h%'

ORDER BY id DESC
LIMIT 2;

-- @block
CREATE INDEX email_index ON users(email);

-- @block
CREATE TABLE Rooms(
    id INT AUTO_INCREMENT,
    street VARCHAR(255),
    owner_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (owner_id) REFERENCES users(id)
);

-- @block
INSERT INTO rooms (owner_id,street)
VALUES
    (1,'san diego sailboat'),
    (1,'nantucket cottage'),
    (1,'vail cabin'),
    (1,'sf cardboard box');

-- @block
SELECT * FROM users
INNER JOIN rooms
ON Rooms.owner_id = Users.id;

-- @block
SELECT * FROM users
LEFT JOIN rooms
ON Rooms.owner_id = Users.id;

-- @block
SELECT * FROM users
RIGHT JOIN rooms
ON Rooms.owner_id = Users.id;

-- @block
SELECT
    Users.id AS user_id,
    Rooms.id AS room_id,
    email,
    street
FROM users
INNER JOIN rooms ON Rooms.owner_id = Users.id

-- @block
CREATE TABLE Bookings(
    id INT AUTO_INCREMENT,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY (guest_id) REFERENCES Users(id),
    FOREIGN KEY (room_id) REFERENCES Rooms(id)
);

-- @block
SELECT
    guest_id,
    street,
    check_in
FROM bookings
INNER JOIN Rooms ON Rooms.owner_id = guest_id
WHERE guest_id = 1

-- @block
DROP TABLE Users;
DROP DATABASE airbnb;

