-- Cities by States
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states on states.id = cities.state_id;
