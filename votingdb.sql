-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2021 at 03:35 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `votingdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `partydb`
--

CREATE TABLE `partydb` (
  `Id` int(11) NOT NULL,
  `PartyName` varchar(30) NOT NULL,
  `PartyHead` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `partydb`
--

INSERT INTO `partydb` (`Id`, `PartyName`, `PartyHead`) VALUES
(1, 'AAP', 'KG'),
(2, 'BJP', 'Modi'),
(3, 'NCL', 'Pappu'),
(4, 'dhbhbghw', 'cvbfgh');

-- --------------------------------------------------------

--
-- Table structure for table `voters`
--

CREATE TABLE `voters` (
  `Id` int(11) NOT NULL,
  `VoterName` varchar(50) NOT NULL,
  `VoterIdCard` varchar(10) NOT NULL,
  `VoterCity` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `voters`
--

INSERT INTO `voters` (`Id`, `VoterName`, `VoterIdCard`, `VoterCity`) VALUES
(1, 'Sandy', '1234567890', 'chrur'),
(2, 'meera', 'asdsa231', 'dscs'),
(3, 'Sharma', '2edsfc', '');

-- --------------------------------------------------------

--
-- Table structure for table `votes`
--

CREATE TABLE `votes` (
  `Id` int(11) NOT NULL,
  `VoteParty` varchar(30) NOT NULL,
  `VoterName` varchar(50) NOT NULL,
  `VoterIdCard` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `votes`
--

INSERT INTO `votes` (`Id`, `VoteParty`, `VoterName`, `VoterIdCard`) VALUES
(1, 'NCL', 'sandy', '1234567890');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `partydb`
--
ALTER TABLE `partydb`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `voters`
--
ALTER TABLE `voters`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `votes`
--
ALTER TABLE `votes`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `partydb`
--
ALTER TABLE `partydb`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `voters`
--
ALTER TABLE `voters`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `votes`
--
ALTER TABLE `votes`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
