DROP TABLE if exists MCP;
DROP TABLE if exists DHT;
DROP TABLE if exists SS;
CREATE TABLE MCP (
    voltage TEXT NOT NULL
);
CREATE TABLE DHT (
    celsius INTEGER NOT NULL,
    fahrenheit INTEGER NOT NULL,
    humidity INTEGER NOT NULL
);
CREATE TABLE SS (
    gate INTEGER NOT NULL,
    envelope INTEGER NOT NULL,
    audio INTEGER NOT NULL
);