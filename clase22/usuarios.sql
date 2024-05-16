-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-06-2020 a las 21:31:35
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `webmaster`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `ocupacion` varchar(30) DEFAULT NULL,
  `edad` int(100) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombre`, `apellido`, `ocupacion`, `edad`, `email`) VALUES
(0, 'Sandra', 'Gonzalez', 'Empleada', 26, 'sandragon@yahoo.com.ar'),
(1, 'Roxana', 'Pereyra', 'Estudiante', 22, 'roxi_pereyra@gmail.com'),
(2, 'Mariano', 'Gasior', 'Estudiante', 22, 'mar501@hotmail.com'),
(3, 'Ingrid', 'Bermudez', 'Ama de casa', 28, 'ingridberz@yahoo.com.ar'),
(4, 'Victoria', 'Godoy', 'Abogada', 27, 'vicus80@hotmail.com'),
(5, 'Ornella', 'Riccio', 'Estudiante', 21, 'nelariccio@yahoo.com.ar'),
(6, 'Felipe', 'Rodriguez', 'Comerciante', 31, 'feliperod@hormail.com'),
(7, 'Gisela', 'Lardo', 'Docente', 24, 'glardo@hotmail.com'),
(8, 'Rodrigo', 'Obrogozo', 'Ama de casa', 28, 'r.obregozo@hotmail.com'),
(9, 'Mariano', 'Golluccio', 'Empleado', 33, 'marianogolluccio@hotmail.com'),
(10, 'Florencia', 'Baldacchino', 'Estudiante', 23, 'marflorb@yahoo.com.ar'),
(11, 'Pablo', 'Solis', 'Empleado', 30, 'pablitosolis@yahoo.com.ar'),
(12, 'Eugenia', 'Sinclair', NULL, 27, 'mariusinclair@hotmail.com'),
(13, 'Anabella', 'Gatti', 'Estudiante', 22, 'anabellagatti@hotmail.com'),
(14, 'Soledad', 'Spandonari', 'Comerciante', 32, 'solzimer@hotmail.com'),
(15, 'Ignacio', 'Dominguez', 'Estudiante', 23, 'dominacho@hotmail.com'),
(16, 'Gabriel', 'Rodriguez', 'Empleado', 26, 'rodriguez_ga@hotmail.com'),
(17, 'Jimena', 'Morillo', 'Arquitecta', 31, 'majimori@hotmail.com'),
(18, 'Martin', 'Sanchez', 'Estudiante', 29, 'tityms@yahoo.com.ar'),
(19, 'Francisco', 'Lopez', 'Empleado', 27, 'flopez@hotmail.com'),
(20, 'Agustina', 'Farina', NULL, 21, 'agustinafarina@hotmail.com'),
(21, 'Margarita', 'Pando', 'Psicologa', 31, 'mmpando@gmail.com'),
(22, 'Luis', 'Panelli', 'Arquitecto', 28, 'luisgym@gmail.com'),
(23, 'Jorgelina', 'Perales', 'Docente', 25, 'mjorgelinap@hotmail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
