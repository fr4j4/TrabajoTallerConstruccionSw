/*insert into actor_character (actor_id,character_id,movie_id) values
(4,4,11)
*/
/*
select peliculas filtrado por actor
select movies.* from movies join actor_character where  movies.id=actor_character.movie_id and actor_character.actor_id=1

select actores filtrados por peliculas
select actors.* from actors join actor_character where  actor_character.actor_id=actors.id and actor_character.movie_id=1
*/
