-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           10.4.11-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.0.0.6468
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para placa
CREATE DATABASE IF NOT EXISTS `placa` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `placa`;

-- Copiando estrutura para tabela placa.cargo
CREATE TABLE IF NOT EXISTS `cargo` (
  `idCargo` int(11) NOT NULL AUTO_INCREMENT,
  `Cargos` varchar(45) NOT NULL,
  PRIMARY KEY (`idCargo`),
  UNIQUE KEY `Cargos_UNIQUE` (`Cargos`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela placa.cargo: ~1 rows (aproximadamente)
INSERT IGNORE INTO `cargo` (`idCargo`, `Cargos`) VALUES
	(1, 'Admin');

INSERT IGNORE INTO `cargo` (`idCargo`, `Cargos`) VALUES
	(2, 'Gerente');

INSERT IGNORE INTO `cargo` (`idCargo`, `Cargos`) VALUES
	(2, 'Funcionario');

-- Copiando estrutura para view placa.consulta
-- Criando tabela temporária para evitar erros de dependência de VIEW
CREATE TABLE `consulta` (
	`idPessoa` INT(11) NOT NULL,
	`Nome` VARCHAR(45) NOT NULL COLLATE 'utf8_general_ci',
	`Sobrenome` VARCHAR(45) NOT NULL COLLATE 'utf8_general_ci',
	`Documentos_idDocumentos` INT(11) NOT NULL,
	`Endereco_idEndereco` INT(11) NOT NULL,
	`RG` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`CPF` BIGINT(11) NULL,
	`Estado` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`Cidade` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`CEP` BIGINT(13) NULL,
	`Rua` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`Complemento` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`idVeiculo` INT(11) NULL,
	`Placa` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`Modelo` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`Marca` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`idTelefone` INT(11) NULL,
	`telefone` VARCHAR(12) NULL COLLATE 'utf8_general_ci',
	`idrelacao` INT(11) NULL,
	`User` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`Senha` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`Cargo_idCargo` INT(11) NULL
) ENGINE=MyISAM;

-- Copiando estrutura para tabela placa.dispositivo
CREATE TABLE IF NOT EXISTS `dispositivo` (
  `idDispositivo` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Dispositivo` varchar(45) NOT NULL,
  `Nome` varchar(50) NOT NULL,
  `In_Out` TINYINT(4) NOT NULL,
  PRIMARY KEY (`idDispositivo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 CHARSET=utf8;

-- Copiando dados para a tabela placa.dispositivo: ~0 rows (aproximadamente)
INSERT IGNORE INTO `dispositivo` (`idDispositivo`, `Dispositivo`, `Nome`, `In_Out`) VALUES
	(1, 'http://192.168.15.2:8080/videofeed', 'cel', 0);


-- Copiando estrutura para tabela placa.documentos
CREATE TABLE IF NOT EXISTS `documentos` (
  `idDocumentos` int(11) NOT NULL AUTO_INCREMENT,
  `RG` varchar(45) NOT NULL,
  `CPF` bigint(11) DEFAULT NULL,
  PRIMARY KEY (`idDocumentos`),
  UNIQUE KEY `RG_UNIQUE` (`RG`),
  UNIQUE KEY `CPF_UNIQUE` (`CPF`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela placa.documentos: ~1 rows (aproximadamente)
INSERT IGNORE INTO `documentos` (`idDocumentos`, `RG`, `CPF`) VALUES
	(1, '00000000', 0);

-- Copiando estrutura para tabela placa.endereco
CREATE TABLE IF NOT EXISTS `endereco` (
  `idEndereco` int(11) NOT NULL AUTO_INCREMENT,
  `Estado` varchar(45) NOT NULL,
  `Cidade` varchar(45) NOT NULL,
  `CEP` bigint(13) NOT NULL,
  `Rua` varchar(45) NOT NULL,
  `Complemento` varchar(45) NOT NULL,
  PRIMARY KEY (`idEndereco`),
  UNIQUE KEY `idEndereco_UNIQUE` (`idEndereco`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela placa.endereco: ~1 rows (aproximadamente)
INSERT IGNORE INTO `endereco` (`idEndereco`, `Estado`, `Cidade`, `CEP`, `Rua`, `Complemento`) VALUES
	(1, 'X', 'X', 0, 'X', 'X');

-- Copiando estrutura para tabela placa.log
CREATE TABLE IF NOT EXISTS `log` (
	`idLog` INT(11) NOT NULL AUTO_INCREMENT,
	`Data_hora` DATETIME NOT NULL,
	`CodigoLeitura` VARCHAR(45) NOT NULL COLLATE 'utf8_general_ci',
	`Status` TINYINT(4) NOT NULL,
	`Veiculo_idVeiculo` INT(11) NULL DEFAULT NULL,
	`Dispositivo_idDispositivo` INT(10) UNSIGNED NOT NULL,
  `Caminho` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	PRIMARY KEY (`idLog`) USING BTREE,
	INDEX `fk_Log_Veiculo1_idx` (`Veiculo_idVeiculo`) USING BTREE,
	INDEX `fk_Log_Dispositivo1_idx` (`Dispositivo_idDispositivo`) USING BTREE,
	CONSTRAINT `fk_Log_Dispositivo1` FOREIGN KEY (`Dispositivo_idDispositivo`) REFERENCES `dispositivo` (`idDispositivo`) ON UPDATE NO ACTION ON DELETE CASCADE,
	CONSTRAINT `fk_Log_Veiculo1` FOREIGN KEY (`Veiculo_idVeiculo`) REFERENCES `veiculo` (`idVeiculo`) ON UPDATE NO ACTION ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela placa.log: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela placa.login
CREATE TABLE IF NOT EXISTS `login` (
  `idLogin` int(11) NOT NULL AUTO_INCREMENT,
  `User` varchar(45) NOT NULL,
  `Senha` varchar(45) NOT NULL,
  `Pessoa_idPessoa` int(11) NOT NULL,
  `Cargo_idCargo` int(11) NOT NULL,
  PRIMARY KEY (`idLogin`),
  UNIQUE KEY `User_UNIQUE` (`User`),
  KEY `fk_Login_Pessoa1_idx` (`Pessoa_idPessoa`),
  KEY `fk_Login_Cargo1_idx` (`Cargo_idCargo`),
  CONSTRAINT `fk_Login_Cargo1` FOREIGN KEY (`Cargo_idCargo`) REFERENCES `cargo` (`idCargo`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_Login_Pessoa1` FOREIGN KEY (`Pessoa_idPessoa`) REFERENCES `pessoa` (`idPessoa`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela placa.login: ~1 rows (aproximadamente)
INSERT IGNORE INTO `login` (`idLogin`, `User`, `Senha`, `Pessoa_idPessoa`, `Cargo_idCargo`) VALUES
	(1, 'a', 'a', 1, 1);

-- Copiando estrutura para tabela placa.pessoa
CREATE TABLE IF NOT EXISTS `pessoa` (
  `idPessoa` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `Sobrenome` varchar(45) NOT NULL,
  `Documentos_idDocumentos` int(11) NOT NULL,
  `Endereco_idEndereco` int(11) NOT NULL,
  PRIMARY KEY (`idPessoa`),
  KEY `fk_Pessoa_Documentos1_idx` (`Documentos_idDocumentos`),
  KEY `fk_Pessoa_Endereco1_idx` (`Endereco_idEndereco`),
  CONSTRAINT `fk_Pessoa_Documentos1` FOREIGN KEY (`Documentos_idDocumentos`) REFERENCES `documentos` (`idDocumentos`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_Pessoa_Endereco1` FOREIGN KEY (`Endereco_idEndereco`) REFERENCES `endereco` (`idEndereco`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela placa.pessoa: ~1 rows (aproximadamente)
INSERT IGNORE INTO `pessoa` (`idPessoa`, `Nome`, `Sobrenome`, `Documentos_idDocumentos`, `Endereco_idEndereco`) VALUES
	(1, 'Admin', 'Admin', 1, 1);

-- Copiando estrutura para tabela placa.relacao
CREATE TABLE IF NOT EXISTS `relacao` (
  `idrelacao` int(11) NOT NULL AUTO_INCREMENT,
  `Pessoa_idPessoa` int(11) NOT NULL,
  `Veiculo_idVeiculo` int(11) NOT NULL,
  PRIMARY KEY (`idrelacao`),
  KEY `fk_relacao_Pessoa_idx` (`Pessoa_idPessoa`),
  KEY `fk_relacao_Veiculo1_idx` (`Veiculo_idVeiculo`),
  CONSTRAINT `fk_relacao_Pessoa` FOREIGN KEY (`Pessoa_idPessoa`) REFERENCES `pessoa` (`idPessoa`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_relacao_Veiculo1` FOREIGN KEY (`Veiculo_idVeiculo`) REFERENCES `veiculo` (`idVeiculo`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela placa.relacao: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela placa.telefone
CREATE TABLE IF NOT EXISTS `telefone` (
  `idTelefone` int(11) NOT NULL AUTO_INCREMENT,
  `telefone` varchar(12) DEFAULT NULL,
  `Pessoa_idPessoa` int(11) NOT NULL,
  PRIMARY KEY (`idTelefone`),
  UNIQUE KEY `idTelefone_UNIQUE` (`idTelefone`),
  UNIQUE KEY `telefone_UNIQUE` (`telefone`),
  KEY `fk_Telefone_Pessoa1_idx` (`Pessoa_idPessoa`),
  CONSTRAINT `fk_Telefone_Pessoa1` FOREIGN KEY (`Pessoa_idPessoa`) REFERENCES `pessoa` (`idPessoa`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela placa.telefone: ~1 rows (aproximadamente)
INSERT IGNORE INTO `telefone` (`idTelefone`, `telefone`, `Pessoa_idPessoa`) VALUES
	(1, '0', 1);

-- Copiando estrutura para tabela placa.veiculo
CREATE TABLE IF NOT EXISTS `veiculo` (
  `idVeiculo` int(11) NOT NULL AUTO_INCREMENT,
  `Placa` varchar(45) NOT NULL,
  `Modelo` varchar(45) NOT NULL,
  `Marca` varchar(45) NOT NULL,
  PRIMARY KEY (`idVeiculo`),
  UNIQUE KEY `idVeiculo_UNIQUE` (`idVeiculo`),
  UNIQUE KEY `Placa_UNIQUE` (`Placa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela placa.veiculo: ~0 rows (aproximadamente)

-- Copiando estrutura para view placa.consulta
-- Removendo tabela temporária e criando a estrutura VIEW final
DROP TABLE IF EXISTS `consulta`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `consulta` AS SELECT Pessoa.*, Documentos.RG, Documentos.CPF, Endereco.Estado, Endereco.Cidade, Endereco.CEP, 
        Endereco.Rua, Endereco.Complemento, veiculo.idVeiculo, veiculo.Placa, Veiculo.Modelo, Veiculo.Marca, telefone.idTelefone, telefone.telefone, relacao.idrelacao, login.`User`, login.Senha, login.Cargo_idCargo FROM Pessoa
        left JOIN Documentos ON Pessoa.Documentos_idDocumentos = Documentos.idDocumentos
        left JOIN Endereco ON Pessoa.Endereco_idEndereco = Endereco.idEndereco
        left JOIN relacao ON pessoa.idPessoa = relacao.Pessoa_idPessoa
        left JOIN Veiculo ON relacao.Veiculo_idVeiculo = veiculo.idVeiculo
        LEFT JOIN login ON login.Pessoa_idPessoa = pessoa.idPessoa 
        LEFT JOIN telefone ON telefone.Pessoa_idPessoa = pessoa.idPessoa ;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
