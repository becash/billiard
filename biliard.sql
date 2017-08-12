-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Хост: 127.0.0.1
-- Время создания: Фев 14 2017 г., 14:19
-- Версия сервера: 10.1.19-MariaDB
-- Версия PHP: 7.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `biliard`
--

-- --------------------------------------------------------

--
-- Структура таблицы `cards`
--

CREATE TABLE `cards` (
  `id` int(14) NOT NULL,
  `owner` varchar(32) NOT NULL,
  `discount` int(2) NOT NULL,
  `enable` int(11) NOT NULL,
  `uuid` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `cards`
--

INSERT INTO `cards` (`id`, `owner`, `discount`, `enable`, `uuid`) VALUES
(1, '123', 76, 1, 'ccbc97ee-3785-11e6-b856-3059b701a1ad'),
(2, 'becash', 12, 1, '05f884f6-3730-11e6-9272-3059b701a1ad'),
(3, 'IUra34', 7, 0, '222');

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE `orders` (
  `uuid` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `table_id` int(3) NOT NULL,
  `operator` varchar(40) COLLATE utf8_unicode_ci NOT NULL COMMENT 'uuid la operator',
  `at` int(14) NOT NULL,
  `stoptime` int(14) DEFAULT NULL,
  `payed` int(1) NOT NULL COMMENT '0-neachitat, 3-partial achitat,8-achitat dar ceva neterminat, 9 -achitat complet, inchis',
  `state` int(3) NOT NULL,
  `row_id` int(6) NOT NULL,
  `sync` int(1) NOT NULL,
  `price1` decimal(7,2) NOT NULL COMMENT 'tsena minuti',
  `price2` decimal(7,2) NOT NULL,
  `price3` decimal(7,2) NOT NULL,
  `summ_brutto` decimal(7,2) NOT NULL,
  `disc_card` varchar(14) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `disc_percent` int(2) NOT NULL,
  `summ_disc` decimal(7,2) NOT NULL,
  `summ_netto` decimal(7,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `orders`
--

INSERT INTO `orders` (`uuid`, `table_id`, `operator`, `at`, `stoptime`, `payed`, `state`, `row_id`, `sync`, `price1`, `price2`, `price3`, `summ_brutto`, `disc_card`, `disc_percent`, `summ_disc`, `summ_netto`) VALUES
('9b08fe26-f2b6-11e6-8c48-3059b701a1ad', 9, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1487077678, 1487077738, 9, 0, 2, 1, '1.17', '2.11', '3.21', '1.17', '', 0, '0.00', '1.17'),
('a769d7b4-f2b6-11e6-99a2-3059b701a1ad', 8, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1487077699, 1487077759, 9, 0, 3, 1, '1.00', '2.00', '3.00', '1.00', '', 0, '0.00', '1.00'),
('a872821c-f2b6-11e6-bedb-3059b701a1ad', 7, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1487077701, 1487077761, 9, 0, 4, 1, '1.00', '2.00', '3.00', '1.00', '', 0, '0.00', '1.00');

-- --------------------------------------------------------

--
-- Структура таблицы `payments`
--

CREATE TABLE `payments` (
  `id` int(6) NOT NULL,
  `parent_order` varchar(40) COLLATE utf8_unicode_ci NOT NULL COMMENT 'link la order UUID',
  `payment_typ` int(2) NOT NULL COMMENT 'forma oplati',
  `sum` decimal(10,2) NOT NULL COMMENT 'summa',
  `cash_reg` int(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `payments`
--

INSERT INTO `payments` (`id`, `parent_order`, `payment_typ`, `sum`, `cash_reg`) VALUES
(1, '9b08fe26-f2b6-11e6-8c48-3059b701a1ad', 0, '2.00', 1),
(2, 'a769d7b4-f2b6-11e6-99a2-3059b701a1ad', 0, '1.00', 1),
(3, 'a872821c-f2b6-11e6-bedb-3059b701a1ad', 0, '1.00', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `payments_types`
--

CREATE TABLE `payments_types` (
  `id` int(3) NOT NULL,
  `name` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `cash_reg` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `payments_types`
--

INSERT INTO `payments_types` (`id`, `name`, `cash_reg`) VALUES
(0, 'Cash', 1),
(1, 'Card', 1),
(2, 'Credit', 0),
(3, 'Transfer Bank', 0),
(101, 'Cupon', 0);

-- --------------------------------------------------------

--
-- Структура таблицы `settings`
--

CREATE TABLE `settings` (
  `id` int(3) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `value` varchar(1023) COLLATE utf8_unicode_ci NOT NULL,
  `options` varchar(127) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `settings`
--

INSERT INTO `settings` (`id`, `name`, `value`, `options`) VALUES
(10, 'triobar product', 'f43109c8-2088-11e5-a1b0-b8975a807b07', ''),
(20, 'triobar table', '26', ''),
(30, 'comapnu name', 'RED BAL', ''),
(31, 'Cod fiscal', '1234567890', ''),
(32, 'Adresa', 'Dacia 10 /1', ''),
(33, 'Mesajul din check', 'Multumim mai veniti', ''),
(34, 'Gmail sender email', 'becashka@suav.biz', ''),
(35, 'Gmail sender password', 'becashka', ''),
(36, 'Emasil receiver', 'admin@suav.biz', ''),
(40, 'save orders, days', '2', ''),
(50, 'autoclear old orders', '1', ''),
(51, 'Roll printer', 'Microsoft Print to PDF', ''),
(52, 'Roll printer exemplars', '1', ''),
(53, 'KKM Product mane', 'Joc in biliard', ''),
(54, 'KKM path & Filename', 'chech_file', ''),
(55, 'KKM nome nalogovoi gruppi', '2', ''),
(56, 'KKM nomer sectii', '4', ''),
(57, 'kkm z report', '1', ''),
(61, 'triobar sync shifts', '0', ''),
(62, 'triobar sync check', '0', ''),
(65, 'shift functional ', '1', ''),
(66, 'receive payments', '1', ''),
(67, 'new DB', '1', ''),
(70, 'period 1 start', '08', ''),
(80, 'period 2 start', '18', ''),
(90, 'period 3 start', '23', ''),
(94, 'printextended shift report', '0', ''),
(95, 'email extended shift report', '1', '');

-- --------------------------------------------------------

--
-- Структура таблицы `shift`
--

CREATE TABLE `shift` (
  `id` int(6) NOT NULL,
  `uuid` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `att` int(14) DEFAULT NULL,
  `user` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sync` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `shift`
--

INSERT INTO `shift` (`id`, `uuid`, `att`, `user`, `sync`) VALUES
(64, '57016cf0-7e9d-11e6-ac00-3059b701a1ad', 1474312492, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 0),
(65, '9ebb72ac-7e9d-11e6-b041-3059b701a1ad', 1474312612, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(66, '8f36c59e-7e9f-11e6-a913-3059b701a1ad', 1474313445, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(67, 'b672ffe4-7e9f-11e6-a461-3059b701a1ad', 1474313511, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(68, '28513336-7ea0-11e6-b65b-3059b701a1ad', 1474313702, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(69, '2bc4f6c0-7ea1-11e6-ae71-3059b701a1ad', 1474314137, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(70, '6cccd778-7ea1-11e6-bff8-3059b701a1ad', 1474314246, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(71, 'b86ad090-7ea1-11e6-923b-3059b701a1ad', 1474314373, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(72, 'fb3da4f6-7ea1-11e6-b494-3059b701a1ad', 1474314485, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(73, '1c0bd086-e8b0-11e6-b59b-3059b701a1ad', 1485975376, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(74, 'bcd750a8-e8b0-11e6-9499-3059b701a1ad', 1485975646, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(75, '43fe24e2-e8b5-11e6-8f99-3059b701a1ad', 1485977591, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(76, '8be58a90-f2b6-11e6-a18d-3059b701a1ad', 1487077653, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(77, 'd27d4b78-f2b6-11e6-8d66-3059b701a1ad', 1487077771, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(78, '05e256fa-f2b7-11e6-8db4-3059b701a1ad', 1487077857, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(79, '29cc83e4-f2b7-11e6-bb6e-3059b701a1ad', 1487077918, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1),
(80, '3504596e-f2b7-11e6-aaa3-3059b701a1ad', 1487077936, 'ba7366bc-f7dc-11e4-93ab-b8975a807b07', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `tables`
--

CREATE TABLE `tables` (
  `id` int(6) NOT NULL,
  `uuid` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `order` int(2) NOT NULL COMMENT 'poriadoc sortirovki',
  `salon` int(2) NOT NULL COMMENT 'zal',
  `enable` int(1) NOT NULL DEFAULT '0',
  `com_off` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `com_on` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `price1` decimal(7,2) NOT NULL COMMENT 'tsena minuti',
  `price2` decimal(7,2) NOT NULL,
  `price3` decimal(7,2) NOT NULL,
  `controler` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `channel` varchar(512) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `tables`
--

INSERT INTO `tables` (`id`, `uuid`, `name`, `order`, `salon`, `enable`, `com_off`, `com_on`, `price1`, `price2`, `price3`, `controler`, `channel`) VALUES
(7, '861f97b8-27cc-11e5-ac05-0060ef067993', '№03', 3, 0, 1, 'e2 04 45 02 94', 'e2 04 44 02 50', '1.00', '2.00', '3.00', 'USR', '3'),
(8, '8634fc5c-27cc-11e5-bfd0-0060ef067993', '№02', 2, 2, 1, 'e204450176', 'e2044401b2', '1.00', '2.00', '3.00', 'USR', '2'),
(9, '86444440-27cc-11e5-853e-0060ef067993', '№01', 1, 4, 1, 'e2 04 45 00 28', 'e2 04 44 00 ec', '1.17', '2.11', '3.21', 'USR-WIFI-IO-83', '1'),
(17, '8647529e-27cc-11e5-bfad-0060ef067993', '№04', 4, 0, 1, 'e2 04 45 03 ca', 'e2 04 44 03 0e', '1.00', '2.00', '3.00', 'USR', '4'),
(18, '864a60f8-27cc-11e5-bbe1-0060ef067993', '№05', 5, 0, 1, 'e2 04 45 04 49', 'e2 04 44 04 8d', '1.00', '2.00', '3.00', 'USR-WIFI-IO-83', '5'),
(19, '86538c1e-27cc-11e5-aa2f-0060ef067993', '№06', 6, 0, 1, 'e2 04 45 05 17', 'e2 04 44 05 d3', '1.00', '2.00', '3.00', 'USR', '6'),
(20, '8662d3fe-27cc-11e5-bbde-0060ef067993', '№07', 7, 0, 1, 'e2 04 45 06 f5', 'e2 04 44 06 31', '1.00', '2.00', '3.00', 'USR-WIFI-IO-83', '7'),
(21, '86752a40-27cc-11e5-8bc3-0060ef067993', '№08', 8, 0, 1, 'e2 04 45 07 ab', 'e2 04 44 07 6f', '1.00', '2.00', '3.00', 'USR-WIFI-IO-83', '8');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `uuid` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `level` int(2) NOT NULL,
  `notes` varchar(1022) COLLATE utf8_unicode_ci NOT NULL,
  `pass` varchar(127) COLLATE utf8_unicode_ci NOT NULL,
  `enable` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`uuid`, `name`, `level`, `notes`, `pass`, `enable`) VALUES
('4df129cd-a05a-11e2-95a1-001999281400', 'Triobar User', 0, '', '761111', 1),
('a8a5dc6e-23bb-11e5-9c37-b8975a807b07', 'Billiard Operator', 2, '', '1111', 1),
('ba7366bc-f7dc-11e4-93ab-b8975a807b07', 'ANDRU', 0, '', '1', 1),
('bbe583e5-f7d8-11e4-93ab-b8975a807b07', 'TUDOR', 1, '', '2222', 1);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `cards`
--
ALTER TABLE `cards`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD UNIQUE KEY `uuid` (`uuid`),
  ADD UNIQUE KEY `row_id` (`row_id`);

--
-- Индексы таблицы `payments`
--
ALTER TABLE `payments`
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `parent_order` (`parent_order`);

--
-- Индексы таблицы `payments_types`
--
ALTER TABLE `payments_types`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `shift`
--
ALTER TABLE `shift`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `uuid` (`uuid`),
  ADD KEY `uuid_2` (`uuid`),
  ADD KEY `user` (`user`);

--
-- Индексы таблицы `tables`
--
ALTER TABLE `tables`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`uuid`),
  ADD UNIQUE KEY `uuid` (`uuid`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `orders`
--
ALTER TABLE `orders`
  MODIFY `row_id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT для таблицы `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT для таблицы `payments_types`
--
ALTER TABLE `payments_types`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;
--
-- AUTO_INCREMENT для таблицы `settings`
--
ALTER TABLE `settings`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=96;
--
-- AUTO_INCREMENT для таблицы `shift`
--
ALTER TABLE `shift`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;
--
-- AUTO_INCREMENT для таблицы `tables`
--
ALTER TABLE `tables`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`parent_order`) REFERENCES `orders` (`uuid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `shift`
--
ALTER TABLE `shift`
  ADD CONSTRAINT `shift_ibfk_1` FOREIGN KEY (`user`) REFERENCES `users` (`uuid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
