USE `curso-24165`;

SELECT nombre, apellido, ocupacion FROM `usuarios` WHERE edad > 30 and edad < 50

# comentario
/* comentario */
-- comentario

SELECT nombre, apellido, ocupacion, edad 
FROM `usuarios`
WHERE edad BETWEEN 30 and 50
ORDER BY edad ASC; 

USE `curso-24165`;

SELECT id_usuario,nombre, apellido FROM `usuarios` LIMIT 10
SELECT id_usuario,nombre, apellido FROM `usuarios` LIMIT 5,10 ORDER BY apellido ASC

SELECT id_usuario,nombre, apellido, edad
FROM `usuarios`
WHERE apellido LIKE "%Gonz%" 


SELECT id_usuario,nombre, apellido, edad
FROM `usuarios`
WHERE ocupacion IN("estudiante","desarrollador") 
WHERE apellido LIKE "%z%"

SELECT id_usuario,nombre, apellido, edad
FROM `usuarios`
WHERE ocupacion IN("estudiante","desarrollador") or apellido LIKE "%z%"
ORDER by apellido

SELECT id_usuario,nombre, apellido, edad FROM `usuarios` WHERE ocupacion NOT IN("estudiante","desarrollador") or apellido NOT LIKE "%z%" ORDER by apellido

SELECT * FROM `usuarios` WHERE ocupacion IS null ORDER by apellido
SELECT * FROM `usuarios` WHERE ocupacion IS NOT null ORDER by apellido

/* JOIN */
SELECT * FROM alumnos JOIN cursos

SELECT * FROM `alumnos` as alu JOIN cursos as cur ON alu.idCurso = cur.idCurso 

SELECT * FROM `alumnos` as alu LEFT JOIN cursos as cur ON alu.idCurso = cur.idCurso 

SELECT curso FROM `alumnos` as alu RIGHT JOIN cursos as cur ON alu.idCurso = cur.idCurso 