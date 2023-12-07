-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2023 a las 03:43:58
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
-- Base de datos: `loginvet`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$9Vq2xMRmPcq699eMRu0r8J$gQQ+RJCpuowgQ81RH0z20+4UdF/usKQSTdHRK4u2PBc=', '2023-12-07 02:28:32.439889', 1, 'admin', '', '', '', 1, 1, '2023-12-07 00:34:36.511403'),
(2, 'pbkdf2_sha256$600000$Kx4vMl1gEVdXd9m6rmqYW1$4KSHme1m/LHQKRT8oQ2UF/E3Z4h2S52BpsaUXQirvHI=', '2023-12-07 02:28:49.011233', 0, 'miku', 'hatsune', 'miku', 'sjkdh@gmail.com', 0, 1, '2023-12-07 01:26:37.942036'),
(3, 'pbkdf2_sha256$600000$rRPRkgoosMYNQOdBLvxEzS$XMPuGAcHrx9mxs5ZOR69yIOfnsvWhDVznS+um2pCD5o=', '2023-12-07 02:21:16.837960', 0, 'hjdbhmfn', 'dhsvd', 'sddhjb', 'ddjcj@gmail.com', 0, 1, '2023-12-07 02:17:05.672819'),
(4, 'pbkdf2_sha256$600000$X2iRwLytCCbbE93CWL7tW7$0sZCXgpbKgCfu2nxGDCNfqOsy0Q56GHGgSOkRn8L6LE=', NULL, 0, 'dlkfjf', 'dhsvd', 'sddhjb', 'ddjcj@gmail.com', 0, 1, '2023-12-07 02:21:01.328848');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
