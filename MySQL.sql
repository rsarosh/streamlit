CREATE DATABASE `streamlit` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;


CREATE TABLE `Users` (
  `UserId` varchar(255) NOT NULL,
  `Password` varchar(32) NOT NULL,
  `CreatedTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`UserId`),
  UNIQUE KEY `UserId_UNIQUE` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DELIMITER $$
CREATE   PROCEDURE `CheckUser`( IN _userId varchar(255), IN _password varchar(32), out _result int )
BEGIN 
		
    declare _User varchar(255);
		SELECT UserId into _User FROM Users WHERE `Password` = _password  AND UserId = _userId AND `Active` = 1;
        IF (isnull(_User)) THEN  
			BEGIN
				SET _result = 0;
			END;
		ELSE
        BEGIN
				SET _result = 1;
		END;
        END IF;
    END$$
DELIMITER ;


DELIMITER $$
CREATE   PROCEDURE `SaveUser`( IN _userId VARCHAR (255),
							 IN _password VARCHAR(32))
BEGIN 
	IF EXISTS 
		(SELECT * FROM Users
			WHERE UserId = _userId) THEN
    BEGIN 
		UPDATE Users 
			SET 
            Password = _password, CreatedTime = now() 
				WHERE UserId = _userId and Active = 1; 
	END;
    ELSE 
		INSERT INTO Users (UserId, password, CreatedTime, Active) Values ( _userId, _password, now(), 1);
    END if;
    
    SELECT * FROM Users WHERE UserId = _userId; 
    
END$$
DELIMITER ;

/* Insert dummy data */
DELIMITER ;
CALL SaveUser('admin','admin')