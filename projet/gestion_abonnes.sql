-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 16 mai 2022 à 08:16
-- Version du serveur : 5.7.36
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `gestion_abonnes`
--

-- --------------------------------------------------------

--
-- Structure de la table `abonnes`
--

DROP TABLE IF EXISTS `abonnes`;
CREATE TABLE IF NOT EXISTS `abonnes` (
  `id_abonne` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(20) DEFAULT NULL,
  `prenom` varchar(20) DEFAULT NULL,
  `age` int(10) NOT NULL,
  `adresse` varchar(40) DEFAULT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `code` int(11) NOT NULL,
  PRIMARY KEY (`id_abonne`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `acces`
--

DROP TABLE IF EXISTS `acces`;
CREATE TABLE IF NOT EXISTS `acces` (
  `id_abonne` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  KEY `id_abonne` (`id_abonne`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `capteurs`
--

DROP TABLE IF EXISTS `capteurs`;
CREATE TABLE IF NOT EXISTS `capteurs` (
  `num_enregistrement` int(11) NOT NULL AUTO_INCREMENT,
  `co2` float NOT NULL,
  `temperature` float NOT NULL,
  `humidite` float NOT NULL,
  PRIMARY KEY (`num_enregistrement`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `acces`
--
ALTER TABLE `acces`
  ADD CONSTRAINT `acces_ibfk_1` FOREIGN KEY (`id_abonne`) REFERENCES `abonnes` (`id_abonne`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
