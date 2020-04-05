CREATE DATABASE db_detran
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE tb_proprietario (
	CodProprietario serial,
	TipoProprietario CHAR(1),
	Nome varchar(255),
	DataNascimento DATE,
	CodEndereco integer,
	Cpf varchar(11),
	Sexo CHAR(1),
	Email varchar(40),
	Telefone varchar(20),
	Cnpj CHAR(18),
	InscricaoEstadual char(15),
	RazaoSocial varchar(255),
	AtividadeEconomica varchar(255),
	SituacaoCadastral varchar(255),
	RegimeApuracao varchar(255),
	CONSTRAINT tb_proprietario_pk PRIMARY KEY (CodProprietario)
);



CREATE TABLE tb_veiculos (
	PlacaVeiculo CHAR(7) NOT NULL,
	Chassi CHAR(17),
	Renavam CHAR(11),
	Fabricante varchar(50),
	Modelo varchar(50),
	Cor varchar(20),
	AnoFabricacao integer,
	CodStatus integer,
	CodProprietario integer,
	VeiculoAdaptado BOOLEAN,
	CONSTRAINT tb_veiculos_pk PRIMARY KEY (PlacaVeiculo)
);



CREATE TABLE tb_status (
	CodStatus serial,
	Descricao VARCHAR(80) NOT NULL,
	CONSTRAINT tb_status_pk PRIMARY KEY (CodStatus)
);



CREATE TABLE tb_veiculos_irregulares (
	PlacaVeiculo CHAR(7) NOT NULL,
	TipoIrregularidade integer,
	Data DATE,
	CONSTRAINT tb_veiculos_irregulares_pk PRIMARY KEY (PlacaVeiculo)
);



CREATE TABLE tb_tipo_irregularidade (
	TipoIrregularidade serial,
	Descricao VARCHAR(80) NOT NULL,
	CONSTRAINT tb_tipo_irregularidade_pk PRIMARY KEY (TipoIrregularidade)
);



CREATE TABLE tb_veiculos_roubados (
	PlacaVeiculo CHAR(7) NOT NULL,
	NumeroBoletim CHAR(11) NOT NULL,
	Data DATE,
	CONSTRAINT tb_veiculos_roubados_pk PRIMARY KEY (PlacaVeiculo)
);



CREATE TABLE tb_endereco (
	CodEndereco serial,
	Logradouro varchar(255),
	Cep CHAR(8),
	Numero varchar(6),
	Bairro varchar(40),
	Cidade varchar(80),
	SiglaEstado CHAR(2),
	CONSTRAINT tb_endereco_pk PRIMARY KEY (CodEndereco)
);



CREATE TABLE tb_estado (
	SiglaEstado CHAR(2) NOT NULL,
	Descricao varchar(255),
	CONSTRAINT tb_estado_pk PRIMARY KEY (SiglaEstado)
);



ALTER TABLE tb_proprietario ADD CONSTRAINT tb_proprietario_fk_codEndereco FOREIGN KEY (CodEndereco) REFERENCES tb_endereco(CodEndereco);

ALTER TABLE tb_veiculos ADD CONSTRAINT tb_veiculos_fk_Status FOREIGN KEY (CodStatus) REFERENCES tb_status(CodStatus);
ALTER TABLE tb_veiculos ADD CONSTRAINT tb_veiculos_fk_CodProprietario FOREIGN KEY (CodProprietario) REFERENCES tb_proprietario(CodProprietario);


ALTER TABLE tb_veiculos_irregulares ADD CONSTRAINT tb_veiculos_irregulares_fk_PlacaVeiculo FOREIGN KEY (PlacaVeiculo) REFERENCES tb_veiculos(PlacaVeiculo);
ALTER TABLE tb_veiculos_irregulares ADD CONSTRAINT tb_veiculos_irregulares_fk_TipoIrregularidade FOREIGN KEY (TipoIrregularidade) REFERENCES tb_tipo_irregularidade(TipoIrregularidade);


ALTER TABLE tb_veiculos_roubados ADD CONSTRAINT tb_veiculos_roubados_fk_PlacaVeiculo FOREIGN KEY (PlacaVeiculo) REFERENCES tb_veiculos(PlacaVeiculo);

ALTER TABLE tb_endereco ADD CONSTRAINT tb_endereco_fk_Estado FOREIGN KEY (SiglaEstado) REFERENCES tb_estado(SiglaEstado);

