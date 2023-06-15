
use heroku_a193cf3c95f45fc;

create table amostras (
  id int auto_increment primary key,
  o3 float,
  co float,
  no2 float,
  so2 float,
  mp10 float,
  mp25 float
);

INSERT INTO amostras (o3, co, no2, so2, mp10, mp25) 
VALUES (%s, %s, %s, %s, %s, %s);

DELETE FROM amostras WHERE id = %s

UPDATE amostras 
SET o3 = %s, co = %s, no2 = %s, so2 = %s, mp10 = %s, mp25 = %s 
WHERE id = %s
