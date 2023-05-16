-- MySQL Script generated by MySQL Workbench
-- Mon May 15 19:40:00 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema foodxperian
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema foodxperian
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `foodxperian` DEFAULT CHARACTER SET utf8mb4 ;
USE `foodxperian` ;

-- -----------------------------------------------------
-- Table `foodxperian`.`TipoDocumento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`TipoDocumento` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`TipoDocumento` (
  `idTipoDocumento` INT NOT NULL,
  `nombreTipoDocumento` VARCHAR(45) NULL,
  PRIMARY KEY (`idTipoDocumento`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`DatosDomicilio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`DatosDomicilio` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`DatosDomicilio` (
  `idDatosDomicilio` INT NOT NULL,
  `ciudad` VARCHAR(45) NULL,
  `localidad` VARCHAR(45) NULL,
  `barrio` VARCHAR(45) NULL,
  `direccion` VARCHAR(45) NULL,
  `descripcionDomicilio` VARCHAR(200) NULL,
  PRIMARY KEY (`idDatosDomicilio`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`Usuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`Usuario` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`Usuario` (
  `idUsuario` INT NOT NULL,
  `nombreUsuario` VARCHAR(45) NULL,
  `apellidoUsuario` VARCHAR(45) NULL,
  `numeroIdentificacion` INT NULL,
  `Celular` INT NULL,
  `TipoDocumento_idTipoDocumento` INT NOT NULL,
  `DatosDomicilio_idDatosDomicilio` INT NOT NULL,
  PRIMARY KEY (`idUsuario`),
  INDEX `fk_Usuario_TipoDocumento1_idx` (`TipoDocumento_idTipoDocumento` ASC) VISIBLE,
  INDEX `fk_Usuario_DatosDomicilio1_idx` (`DatosDomicilio_idDatosDomicilio` ASC) VISIBLE,
  CONSTRAINT `fk_Usuario_TipoDocumento1`
    FOREIGN KEY (`TipoDocumento_idTipoDocumento`)
    REFERENCES `foodxperian`.`TipoDocumento` (`idTipoDocumento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_DatosDomicilio1`
    FOREIGN KEY (`DatosDomicilio_idDatosDomicilio`)
    REFERENCES `foodxperian`.`DatosDomicilio` (`idDatosDomicilio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`TipoMetodoPago`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`TipoMetodoPago` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`TipoMetodoPago` (
  `idTipoMetodoPago` INT NOT NULL,
  `nombreTipoMetodoPago` VARCHAR(45) NULL,
  PRIMARY KEY (`idTipoMetodoPago`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`TipoEstadoEntrega`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`TipoEstadoEntrega` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`TipoEstadoEntrega` (
  `idTipoEstadoEntrega` INT NOT NULL,
  `nombreTipoEstadoEntrega` VARCHAR(45) NULL,
  PRIMARY KEY (`idTipoEstadoEntrega`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`TiempoEntrega`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`TiempoEntrega` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`TiempoEntrega` (
  `idTiempoEntrega` INT NOT NULL,
  `cantidadTiempoEntrega` INT NULL,
  `descripcionTiempoEntregacol1` VARCHAR(200) NULL,
  PRIMARY KEY (`idTiempoEntrega`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`EstadoEntrega`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`EstadoEntrega` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`EstadoEntrega` (
  `idEstadoEntrega` INT NOT NULL,
  `TipoEstadoEntrega_idTipoEstadoEntrega` INT NOT NULL,
  `Usuario_idUsuario` INT NOT NULL,
  `Factura_idFactura` INT NOT NULL,
  `DatosDomicilio_idDatosDomicilio` INT NOT NULL,
  `TiempoEntrega_idTiempoEntrega` INT NOT NULL,
  PRIMARY KEY (`idEstadoEntrega`),
  INDEX `fk_EstadoEntrega_TipoEstadoEntrega1_idx` (`TipoEstadoEntrega_idTipoEstadoEntrega` ASC) VISIBLE,
  INDEX `fk_EstadoEntrega_Usuario1_idx` (`Usuario_idUsuario` ASC) VISIBLE,
  INDEX `fk_EstadoEntrega_Factura1_idx` (`Factura_idFactura` ASC) VISIBLE,
  INDEX `fk_EstadoEntrega_DatosDomicilio1_idx` (`DatosDomicilio_idDatosDomicilio` ASC) VISIBLE,
  INDEX `fk_EstadoEntrega_TiempoEntrega1_idx` (`TiempoEntrega_idTiempoEntrega` ASC) VISIBLE,
  CONSTRAINT `fk_EstadoEntrega_TipoEstadoEntrega1`
    FOREIGN KEY (`TipoEstadoEntrega_idTipoEstadoEntrega`)
    REFERENCES `foodxperian`.`TipoEstadoEntrega` (`idTipoEstadoEntrega`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_EstadoEntrega_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario`)
    REFERENCES `foodxperian`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_EstadoEntrega_Factura1`
    FOREIGN KEY (`Factura_idFactura`)
    REFERENCES `foodxperian`.`Factura` (`idFactura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_EstadoEntrega_DatosDomicilio1`
    FOREIGN KEY (`DatosDomicilio_idDatosDomicilio`)
    REFERENCES `foodxperian`.`DatosDomicilio` (`idDatosDomicilio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_EstadoEntrega_TiempoEntrega1`
    FOREIGN KEY (`TiempoEntrega_idTiempoEntrega`)
    REFERENCES `foodxperian`.`TiempoEntrega` (`idTiempoEntrega`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`EstadoPedido`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`EstadoPedido` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`EstadoPedido` (
  `idEstadoPedido` INT NOT NULL,
  `nombreEstadoPedido` VARCHAR(45) NULL,
  `EstadoEntrega_idEstadoEntrega` INT NOT NULL,
  PRIMARY KEY (`idEstadoPedido`),
  INDEX `fk_EstadoPedido_EstadoEntrega1_idx` (`EstadoEntrega_idEstadoEntrega` ASC) VISIBLE,
  CONSTRAINT `fk_EstadoPedido_EstadoEntrega1`
    FOREIGN KEY (`EstadoEntrega_idEstadoEntrega`)
    REFERENCES `foodxperian`.`EstadoEntrega` (`idEstadoEntrega`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`Pedido`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`Pedido` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`Pedido` (
  `idPedido` INT NOT NULL,
  `fechaCreacion` DATETIME(6) NULL,
  `Usuario_idUsuario` INT NOT NULL,
  `EstadoPedido_idEstadoPedido` INT NOT NULL,
  PRIMARY KEY (`idPedido`),
  INDEX `fk_Pedido_Usuario1_idx` (`Usuario_idUsuario` ASC) VISIBLE,
  INDEX `fk_Pedido_EstadoPedido1_idx` (`EstadoPedido_idEstadoPedido` ASC) VISIBLE,
  CONSTRAINT `fk_Pedido_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario`)
    REFERENCES `foodxperian`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Pedido_EstadoPedido1`
    FOREIGN KEY (`EstadoPedido_idEstadoPedido`)
    REFERENCES `foodxperian`.`EstadoPedido` (`idEstadoPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`TipoEstadoPago`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`TipoEstadoPago` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`TipoEstadoPago` (
  `idTipoEstadoPago` INT NOT NULL,
  `nombreTipoEstadoPagocol` VARCHAR(45) NULL,
  PRIMARY KEY (`idTipoEstadoPago`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`Factura`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`Factura` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`Factura` (
  `idFactura` INT NOT NULL,
  `valorPedido` INT NULL,
  `fechafactura` DATETIME(6) NULL,
  `TipoMetodoPago_idTipoMetodoPago` INT NOT NULL,
  `Pedido_idPedido` INT NOT NULL,
  `TipoEstadoPago_idTipoEstadoPago` INT NOT NULL,
  PRIMARY KEY (`idFactura`),
  INDEX `fk_Factura_TipoMetodoPago_idx` (`TipoMetodoPago_idTipoMetodoPago` ASC) VISIBLE,
  INDEX `fk_Factura_Pedido1_idx` (`Pedido_idPedido` ASC) VISIBLE,
  INDEX `fk_Factura_TipoEstadoPago1_idx` (`TipoEstadoPago_idTipoEstadoPago` ASC) VISIBLE,
  CONSTRAINT `fk_Factura_TipoMetodoPago`
    FOREIGN KEY (`TipoMetodoPago_idTipoMetodoPago`)
    REFERENCES `foodxperian`.`TipoMetodoPago` (`idTipoMetodoPago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Factura_Pedido1`
    FOREIGN KEY (`Pedido_idPedido`)
    REFERENCES `foodxperian`.`Pedido` (`idPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Factura_TipoEstadoPago1`
    FOREIGN KEY (`TipoEstadoPago_idTipoEstadoPago`)
    REFERENCES `foodxperian`.`TipoEstadoPago` (`idTipoEstadoPago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`Notificacion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`Notificacion` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`Notificacion` (
  `idNotificacion` INT NOT NULL,
  `EstadoEntrega_idEstadoEntrega` INT NOT NULL,
  PRIMARY KEY (`idNotificacion`),
  INDEX `fk_Notificacion_EstadoEntrega1_idx` (`EstadoEntrega_idEstadoEntrega` ASC) VISIBLE,
  CONSTRAINT `fk_Notificacion_EstadoEntrega1`
    FOREIGN KEY (`EstadoEntrega_idEstadoEntrega`)
    REFERENCES `foodxperian`.`EstadoEntrega` (`idEstadoEntrega`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foodxperian`.`RegistroMensajes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `foodxperian`.`RegistroMensajes` ;

CREATE TABLE IF NOT EXISTS `foodxperian`.`RegistroMensajes` (
  `idRegistroMensajes` INT NOT NULL,
  `Usuario_idUsuario` INT NOT NULL,
  `nombres` VARCHAR(45) NULL,
  `apellidos` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `celular` INT NULL,
  `mensaje` VARCHAR(400) NULL,
  PRIMARY KEY (`idRegistroMensajes`),
  INDEX `fk_RegistroMensajes_Usuario1_idx` (`Usuario_idUsuario` ASC) VISIBLE,
  CONSTRAINT `fk_RegistroMensajes_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario`)
    REFERENCES `foodxperian`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;