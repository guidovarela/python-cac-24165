CREATE DATABASE IF NOT EXISTS maradona;

CREATE TABLE `curso-24165`.`alumnos` ( `dni` INT(11) NOT NULL ,  `nombre` VARCHAR(30) NOT NULL ,  `apellido` VARCHAR(30) NOT NULL ,  `fecha_nac` DATE NOT NULL ) ENGINE = MyISAM;

/* modificar base de datos */
CREATE DATABASE d10s / DROP DATABASE maradona

/* modificar tabla */
RENAME TABLE `d10s`.`alumnos` TO `d10s`.`alumnado`;

ALTER TABLE `alumnos` ADD `id` INT NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (`id`); 
describe alumnado
/* elimina */
DROP TABLE alumnado
/* vaciar  */
truncate TABLE alumnado;

/* DDL */


INSERT INTO `alumnos` (`id`, `dni`, `nombre`, `apellido`, `fecha_nac`) VALUES (NULL, '32222222', 'Juan ', 'Perez', '1990-05-20');
INSERT INTO `alumnos` (`id`, `dni`, `nombre`, `apellido`, `fecha_nac`) VALUES (0, '32456775', 'Maria', 'Lopez', '1991-05-21') 

INSERT INTO `curso-24165`.`alumnos` VALUES (0, '3446687', 'Teresa', 'Cancelarich', '1972-05-21') 

UPDATE `alumnos` SET `dni` = '22446687' WHERE `alumnos`.`id` = 3; 

DELETE FROM `alumnos` WHERE `alumnos`.`id` = 1

SELECT dni, nombre FROM `alumnos` 
SELECT dni, nombre FROM `alumnos` WHERE id > 2
