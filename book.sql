/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `IDnumber` int NOT NULL AUTO_INCREMENT,
  `BookTitle` varchar(100) DEFAULT NULL,
  `BookAuthor` varchar(100) DEFAULT NULL,
  `BookGenre` varchar(100) DEFAULT NULL,
  `BookPrice` int DEFAULT NULL,
  `BookQuantity` int DEFAULT NULL,
  PRIMARY KEY (`IDnumber`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `book` (`IDnumber`, `BookTitle`, `BookAuthor`, `BookGenre`, `BookPrice`, `BookQuantity`) VALUES
(40, 'The Dark Tower: The Gunslinger', 'Stephen King', 'Fantasy', 36, 6);
INSERT INTO `book` (`IDnumber`, `BookTitle`, `BookAuthor`, `BookGenre`, `BookPrice`, `BookQuantity`) VALUES
(42, 'Contact', 'Carl Sagan', 'Fantasy', 20, 80);
INSERT INTO `book` (`IDnumber`, `BookTitle`, `BookAuthor`, `BookGenre`, `BookPrice`, `BookQuantity`) VALUES
(49, 'Cosmos', 'Carl Sagan', 'Science', 14, 20);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;