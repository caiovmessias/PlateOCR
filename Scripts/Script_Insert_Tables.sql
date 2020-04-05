INSERT INTO tb_estado(descricao, siglaestado) VALUES
('Acre', 'AC'),
('Alagoas', 'AL'),
('Amapá', 'AP'),
('Amazonas', 'AM'),
('Bahia', 'BA'),
('Ceará', 'CE'),
('Distrito Federal', 'DF'),
('Espírito Santo', 'ES'),
('Goiás', 'GO'),
('Maranhão', 'MA'),
('Mato Grosso', 'MT'),
('Mato Grosso do Sul', 'MS'),
('Minas Gerais', 'MG'),
('Pará', 'PA'),
('Paraíba', 'PB'),
('Paraná', 'PR'),
('Pernambuco', 'PE'),
('Piauí', 'PI'),
('Rio de Janeiro', 'RJ'),
('Rio Grande do Norte', 'RN'),
('Rio Grande do Sul', 'RS'),
('Rondônia', 'RO'),
('Roraima', 'RR'),
('Santa Catarina', 'SC'),
('São Paulo', 'SP'),
('Sergipe', 'SE'),
('Tocantins', 'TO');

INSERT INTO tb_status (descricao) VALUES
('Regular'),
('Irregular'),
('Roubado');

INSERT INTO tb_tipo_irregularidade (descricao) VALUES
('Documentação em atraso'),
('Infrações pendentes'),
('Licenciamento em atraso');

INSERT INTO tb_endereco (logradouro, cep, numero, bairro, cidade, siglaestado)  VALUES
('Rua Antonio Nocera', '14120000', '1079', 'Jardim Vila Nova', 'Dumont', 'SP'),
('Rua Jurece da Baixa', '19485632', '11', 'Jardim João Segundo', 'Itabuna', 'BA'),
('Avenida Treze de Pindai', '23564189', '891', 'Ignácio Meneses', 'Belo Horizonte', 'MG'),
('Rua Violo Daneze', '4523000', '587', 'Jardim Ribeiro Lopes', 'Americana', 'SP'),
('Rua Pedro Bovo', '45632000', '749', 'Loteamento Vila Bhetree', 'São Paulo', 'SP'),
('Avenida Jacinto Tovo', '78562000', '4107', 'Vila Velha', 'Porto Alegre', 'RS'),
('Rua Manoel de Deus', '14120000', '145', 'LT Zambuja Messi', 'Santa Catarina', 'SC'),
('Avenida Nossa Senhora', '89621000', '565', 'Jardim Velha Odessa', 'São Caetano', 'SP'),
('Avenida Brasil', '45523000', '862', 'Aparecida de Jesus', 'Ribeirao Preto', 'SP'),
('Rua Brooklyn Vinte', '45632000', '79', 'Nossa Barra', 'Barrinha', 'SP'),
('Rua Vinte e um de Abril', '89654000', '7419', 'Bonito Bairro', 'Olimpia', 'SP');

INSERT INTO tb_proprietario (tipoproprietario, nome, datanascimento, codendereco, cpf, sexo, email, telefone, cnpj, inscricaoestadual, razaosocial, atividadeeconomica, situacaocadastral, regimeapuracao)
VALUES
('1', 'Caio Vinicius Peçanha de Morais Messias', '1998-07-29', 1, '75225951274', 'M', 'cvinicius.dmt@gmail.com', '16981996573', '', '', '', '', '', ''),
('1', 'Adrielle Marcari', '1998-11-11', 2, '47856324852', 'F', 'adriellemarcari@gmail.com', '16981587276', '', '', '', '', '', ''),
('1', 'Vanessa Maciel da Mota', '1985-01-10', 3, '15985235766', 'F', 'vanessa.macielt@gmail.com', '16991523678', '', '', '', '', '', ''),
('1', 'Mateus Ferraz Silva', '1980-04-03', 4, '36985214778', 'M', 'mat.ferraz@outlook.com', '14974523685', '', '', '', '', '', ''),
('1', 'Jeferson Souza Pinto', '1990-10-10', 5, '47856321422', 'M', 'jef.souza@gmail.com', '25981574223', '', '', '', '', '', ''),
('1', 'Jacira Santos', '1993-08-15', 6, '74295864973', 'F', 'jacira.santos@yahoo.com', '21111210', '', '', '', '', '', ''),
('1', 'Reinaldo Aparecido Matarazzo', '1974-01-25', 7, '79465942360', 'M', 'rei.matarazzo@hotmail.com', '17986227882', '', '', '', '', '', ''),
('2', '', null, 8, '', '', 'contato@floraflor.com', '1621020238', '11098998000121', '578967976415298', 'Flora Flor Produção e Comércio de Flores Ltda', 'Produção e Comércio de Flores', 'Ativo', 'Simples Nacional'),
('2', '', null, 9, '', '', 'contato@cvmtechnology.com', '1621998573', '15219060000289', '769592496873858', 'CVM Technology Enterprises Ltda', 'Desenvolvimento de Sistemas', 'Ativo', 'Simples Nacional'),
('2', '', null, 10, '', '', 'contato@apmcenturyfilms.com', '1134150584', '13674977000210', '762230074101308', 'APM Century Films Ltda', 'Produção de Filmes', 'Ativo', 'Simples Nacional');

INSERT INTO tb_veiculos (placaveiculo, chassi, renavam, fabricante, modelo, cor, anofabricacao, codstatus, codproprietario, veiculoadaptado) VALUES
('DXA0886', 'GHAS785SEF2074KL7', '96325845620', 'Volkswagen', 'Gol Geração 4', 'Preto', 2011, 3, 1, false),
('DWQ3210', 'UIES124RFGH789JK2', '89567230090', 'Fiat', 'Argo', 'Branco', 2019, 1, 2, false),
('JHG3896', 'ASHUOK7893JSHD2SD', '76245362998', 'Fiat', 'Strada', 'Cinza', 2014, 2, 3, false),
('MBX7852', 'IOKKH2536HSJ28921', '44362718882', 'Chevrolet', 'Prisma', 'Vermelho', 2012, 2, 4 , true),
('BYP0110', '67892JAHNCMI90KSJ', '92773636270', 'Volkswagen', 'Up', 'Branco', 2019, 2, 5, false),
('UIO9087', '829KASHAHSGAB2891', '90092717289', 'Volkswagen', 'Polo', 'Cinza', 2008, 2, 6, true),
('ECO0998', '7855ASSKOKWEKS785', '15987452301', 'Audi', 'A3', 'Branco', 2019, 1, 7, false),
('GHJ7852', 'UAHWERAHSA8291823', '85236974412', 'Hyundai', 'HB20', 'Preto', 2019, 3, 8, false),
('YUI7412', 'REDFGHNS89983AH23', '78523665417', 'Kia', 'Cerato', 'Verde', 2017, 2, 9, true),
('LGB1235', '567YHJDU689KSHHC1', '89273617283', 'BMW', 'X', 'Preto', 2019, 3, 10, false);

INSERT INTO tb_veiculos_irregulares(placaveiculo, tipoirregularidade, data) VALUES
('YUI7412', 1, '2018-07-25'),
('UIO9087', 2, '2019-04-10'),
('BYP0110', 3, '2014-08-06'),
('MBX7852', 1, '2019-09-20'),
('JHG3896', 2, '2017-04-14');


INSERT INTO tb_veiculos_roubados(placaveiculo, numeroboletim, data) VALUES
('DXA0886','78598552365', '2014-10-20'),
('GHJ7852', '7412365896', '2018-02-10'),
('LGB1235', '7896541232', '2019-07-02');