-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 05-08-2026 a las 08:15:54
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_finanzas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `finanzas`
--

CREATE TABLE `finanzas` (
  `Id` int(11) NOT NULL,
  `Usuario` varchar(100) NOT NULL,
  `Tipo` varchar(100) NOT NULL,
  `Categoria` varchar(100) NOT NULL,
  `Monto` int(11) NOT NULL,
  `Descripcion` varchar(100) NOT NULL,
  `Fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `finanzas`
--

INSERT INTO `finanzas` (`Id`, `Usuario`, `Tipo`, `Categoria`, `Monto`, `Descripcion`, `Fecha`) VALUES
(1, 'leonel sifuentes', 'ingreso', 'SUELDO', 1001, 'aumento de 1 peso', '2026-08-03'),
(2, 'leonel sifuentes', 'gasto', 'COMIDA', 65, 'hamborguesaaa', '2026-08-03'),
(3, 'leonel sifuentes', 'gasto', 'TRANSPORTE', 30, 'camion', '2026-08-03'),
(4, 'leonel sifuentes', 'gasto', 'SERVICIOS', 400, 'luz', '2026-12-31'),
(5, 'leo', 'ingreso', 'SUELDO', 10000, 'sueldo', '2022-12-12'),
(6, 'leo', 'gasto', 'COMIDA', 19, 'amborguesa', '2002-02-02'),
(7, 'leo', 'gasto', 'TRANSPORTE', 13, 'camion', '2024-01-23');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  `telefono` varchar(100) NOT NULL,
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `usuario`, `nombre`, `correo`, `contrasena`, `telefono`, `fecha_registro`) VALUES
(1, 'leo', 'leonel ivan sifuentes zaragoza', 'leonel@gmail.com', '$2b$12$YB13Ck/gDobWsh20sJhmwOde4bY8iLmvkGWGg5CgKF8luTq5f5hU2', '6182590911', '2026-08-05 00:10:22');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `finanzas`
--
ALTER TABLE `finanzas`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `finanzas`
--
ALTER TABLE `finanzas`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
