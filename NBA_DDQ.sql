--
-- Table structure for table `Players`
--
DROP TABLE IF EXISTS `Players`;
CREATE TABLE `Players` (
  `player_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `speciality` varchar(255) NOT NULL,
  `team` varchar(255) NOT NULL,
  `salary` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `birthday` date NOT NULL,
  `primary_position` varchar(255) NOT NULL,
  `secondary_position` varchar(255) NULL,
  `fg` decimal(5,2) NOT NULL,
  `ft` decimal(5,2) NOT NULL,
  `ppg` decimal(5,2) NOT NULL,
  `rpg` decimal(5,2) NOT NULL,
  `apg` decimal(5,2) NOT NULL,
  `spg` decimal(5,2) NOT NULL,
  `bpg` decimal(5,2) NOT NULL,
  `tpg` decimal(5,2) NOT NULL,
	PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
--
-- Populating data for the table `Players`
--
INSERT INTO `Players` (`first_name`, `last_name`, `speciality`, `team`, `salary`, `height`,
`weight`, `birthday`, `primary_position`, `secondary_position`, `fg`, `ft`, `ppg`,
`rpg`, `apg`, `spg`, `bpg`, `tpg`) VALUES
('Lebron', 'James', 'dunking','Lakers', 39219566, 206, 
250, '1984-12-30', 'SF', 'PG', 51.3, 69.8, 25.0, 7.7, 7.8, 1.1, 0.6, 3.7),
('Stephen', 'Curry', 'shooting', 'Warriors', 43006362, 188, 
190, '1988-03-14', 'PG', 'SG', 48.2, 91.6, 32.0, 5.5, 5.8, 1.2, 0.1, 3.4),
('James', 'Harden', 'passing', 'Nets', 41254920, 196, 
220, '1989-08-26', 'PG', 'SG', 46.6, 86.1, 24.6, 7.9, 10.8, 1.2, 0.8, 4.0),
('Giannis', 'Antetokounmpo', 'dunking', 'Nets', 41254920, 196, 
220, '1989-08-26', 'PG', 'SG', 46.6, 86.1, 24.6, 7.9, 10.8, 1.2, 0.8, 4.0),
('Karl-Anthony', 'Towns', 'defense', 'Timberwolves', 29467800, 211, 
248, '1995-11-25', 'C', NULL, 48.6, 85.9, 24.8, 10.6, 4.5, 0.8, 1.1, 3.2);
--
-- Table structure for table `Teams`
--
DROP TABLE IF EXISTS `Teams`;
CREATE TABLE `Teams` (
  `team_id` int(11) NOT NULL AUTO_INCREMENT,
  `team_name` varchar(255) NOT NULL,
  `total_fines` int(11) NOT NULL,
  `salary_available` int(11) NOT NULL,
  `best_player` varchar(255) NOT NULL REFERENCES `Players` (`last_name`),
	PRIMARY KEY (`team_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
--
-- Populating data for the table `Teams`
--
INSERT INTO `Teams` (`team_name`, `total_fines`, `salary_available`, `best_player`) VALUES
('Lakers', 1000000, 0, 'James'),
('Nets', 0, 20000, 'Harden'),
('Heat', 100, 1000000, 'Butler'),
('Raptors', 250, 6678, 'Siakam'),
('Warriors', 234324, 567, 'Curry');
--
-- Table structure for table `Head_Coaches`
--
DROP TABLE IF EXISTS `Head_Coaches`;
CREATE TABLE `Head_Coaches` (
  `coach_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `team` varchar(255) NOT NULL REFERENCES `Teams` (`team_name`),
	PRIMARY KEY (`coach_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
--
-- Populating data for the table `Head_Coaches`
--
INSERT INTO `Head_Coaches` (`first_name`, `last_name`, `team`) VALUES
('Frank', 'Vogel', 'Lakers'),
('Stevel', 'Nash', 'Nets'),
('Erik', 'Spoelstra', 'Heat'),
('Nick', 'Nurse', 'Raptors'),
('Steve', 'Kerr', 'Warriors');
--
-- Table structure for table `Trainers`
--
DROP TABLE IF EXISTS `Trainers`;
CREATE TABLE `Trainers` (
  `trainer_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `speciality` varchar(255) NOT NULL REFERENCES `Players` (`speciality`),
	PRIMARY KEY (`trainer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
--
-- Populating data for the table `Trainers`
--
INSERT INTO `Trainers` (`first_name`, `last_name`, `speciality`) VALUES
('Magic', 'Johnson', 'passing'),
('Michael', 'Jordan', 'shooting'),
('Kareem', 'Abdul-Jabar', 'dunking'),
('Reggie', 'Miller', 'shooting'),
('Gary', 'Payton', 'defense');
--
-- Table structure for table `Stadiums`
--
DROP TABLE IF EXISTS `Stadiums`;
CREATE TABLE `Stadiums` (
  `stadium_id` int(11) NOT NULL AUTO_INCREMENT,
  `stadium_name` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `team` varchar(255) NOT NULL REFERENCES `Teams` (`team_name`),
  `state` varchar(255) NOT NULL,
	PRIMARY KEY (`stadium_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
--
-- Populating data for the table `Stadiums`
--
INSERT INTO `Stadiums` (`stadium_name`, `city`, `team`, `state`) VALUES
('Scotiabank Arena', 'Toronto', 'Raptors', 'Ontario'),
('STAPLES Center', 'Los Angeles', 'Lakers', 'California'),
('FTX Arena', 'Miami', 'Heat', 'Florida'),
('Barclays Center', 'Brooklyn', 'Nets', 'New York'),
('Chase Center', 'Golden State', 'Warriors', 'California');
--
-- Table structure for table `Players_Trainers`
--
DROP TABLE IF EXISTS `Players_Trainers`;
CREATE TABLE `Players_Trainers` (
  `player_rel_id` int(11) NOT NULL REFERENCES `Players` (`player_id`),
  `player_last_name` varchar(255) NOT NULL REFERENCES `Players` (`last_name`),
  `trainer_rel_id` int(11) NOT NULL REFERENCES `Trainers` (`trainer_id`),
  `trainer_last_name` varchar(255) NOT NULL REFERENCES `Trainers` (`last_name`),
	PRIMARY KEY (`player_rel_id`, `trainer_rel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
-- --
-- -- Populating data for the table `Players_Trainers`
-- --
INSERT INTO `Players_Trainers` (`player_rel_id`, `player_last_name`, `trainer_rel_id`, `trainer_last_name`) VALUES

((SELECT `player_id` FROM `Players` WHERE `last_name` = 'Curry'),
(SELECT `last_name` FROM `Players` WHERE `last_name` = 'Curry'),
(SELECT `trainer_id` FROM `Trainers` WHERE `last_name` = 'Miller'),
(SELECT `last_name` FROM `Trainers` WHERE `last_name` = 'Miller')),

((SELECT `player_id` FROM `Players` WHERE `last_name` = 'Harden'),
(SELECT `last_name` FROM `Players` WHERE `last_name` = 'Harden'),
(SELECT `trainer_id` FROM `Trainers` WHERE `last_name` = 'Johnson'),
(SELECT `last_name` FROM `Trainers` WHERE `last_name` = 'Johnson')),

((SELECT `player_id` FROM `Players` WHERE `last_name` = 'Towns'),
(SELECT `last_name` FROM `Players` WHERE `last_name` = 'Towns'),
(SELECT `trainer_id` FROM `Trainers` WHERE `last_name` = 'Payton'),
(SELECT `last_name` FROM `Trainers` WHERE `last_name` = 'Payton'));
