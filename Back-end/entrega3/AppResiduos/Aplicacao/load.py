from .builder import *

# no shell faça
# from Aplicacao.load import *
# load_clientes()

def load_clientes():
    DiretorCliente('marcelo', 'silva'    , '123', 'cliente1@gmail.com','es', '29106080', 'vila pavão','ibiri', 'rua das bananas', '12', 'nenhuma', '49257065006' ,'1994-06-06')
    DiretorCliente('eduardo', 'santos'   , '123', 'cliente2@gmail.com','es', '29106080', 'vila pavão','ibiri', 'rua das bananas', '14', 'nenhuma', '93457469008' ,'1994-06-06')
    DiretorCliente('rodrigo', 'dias'     , '123', 'cliente3@gmail.com','es', '29106080', 'vila pavão','ibiri', 'rua das bananas', '16', 'nenhuma', '22056241056' ,'1994-06-06')
    DiretorCliente('vanessa', 'silva'    , '123', 'cliente4@gmail.com','es', '29106080', 'vila pavão','ibiri', 'rua das bananas', '18', 'nenhuma', '60435777041' ,'1994-06-06')
    DiretorCliente('marcelo', 'madureira', '123', 'cliente5@gmail.com','es', '29106080', 'vila pavão','ibiri', 'rua das bananas', '20', 'nenhuma', '59616689088' ,'1994-06-06')

    size = 10
    nome = [
        'luiz','antonio','glaydson','paulo','kleber', 'caio', 'gary', 'ana', 'jose', 'brenno'
    ]
    sobrenome = [
        'silva', 'oliveira', 'neto', 'junior', 'roque', 'guzzo', 'fernandes', 'santos', 'lima', 'rosa'
    ]
    senha = [
        '1234','1234','1234','1234','1234','1234','1234','1234','1234','1234'
    ]
    email= [
        'luiz@gmail.com', 'antonio@gmail.com', 'glaydson@gmail.com', 'paulo@gmail.com', 'kleber@gmail.com', 'caio@gmail.com', 'gary@gmail.com', 'ana@gmail.com', 'jose@gmail.com', 'brenno@gmail.com'
    ]
    estado = [
        'ES','ES','ES','ES','ES','ES','ES','ES','ES','ES'
    ]
    cep = [
        '29060270','29060270','29060270','29060270','29060270','29060270','29060270','29060270','29060270','29060270'
    ]
    cidade = [
        'vitoria','vitoria','vitoria','vitoria','vitoria','vila velha','vila velha','vila velha','vila velha','vila velha'
    ]
    bairro = [
        'pedro nolasco','ibiratiba','jeriquaquara','Pedra Branca','Cariacica','Porto de Galinhas','Gramado','Canela','morro de são paulo','Ferrosa'
    ]
    lorgadouro = [
        'logra1','logra2','logra3','logra4','logra5','logra6','logra7','logra8','logra9','logra10'
    ]
    numero = [
        '111','112','113','121','122','123','131','132','133','211'
    ]
    referencia = [
        'ref1','ref2','ref3','ref4','ref5','ref6','ref7','ref8','ref9','ref10'
    ]
    cpf = [
        '12671513111','12671513112','12671513113','12671513121','12671513122','12671513123','12671513131','12671513132','12671513133','12671513211'
    ]
    data_nascimento = [
        '1994-06-01','1994-06-02','1994-06-03','1994-06-04','1994-06-05','1994-06-06','1994-06-07','1994-06-08','1994-06-09','1994-06-10',
    ]

    for i in range(size):
        DiretorCliente(nome[i],sobrenome[i],senha[i],email[i],estado[i],cep[i],cidade[i],bairro[i],lorgadouro[i],numero[i],referencia[i],cpf[i],data_nascimento[i])

def load_motoristas():
    DiretorMotorista('Kraubler', 'Glaydson', '1234', 'motorista1@gmail.com', 'es', '29260579', 'cariacicacity', 'são jose', 'logra', '123', 'nebas', 'A-B-C-D', 'HLP-3313')
    DiretorMotorista('Lucimar', 'Ferreira', '1234', 'motorista2@gmail.com', 'es', '29264579', 'cariacicacity2', 'são jose2', 'logra', '313', 'nebas', 'C-D', 'HGP-3217')
    DiretorMotorista('Bianca', 'Raldeli', '1234', 'motorista3@gmail.com', 'es', '29260679', 'cariacicacity3', 'são jose3', 'logras', '122', 'nebas', 'D', 'HLV-1393')
    DiretorMotorista('Bianco', 'Patuzzo', '1234', 'motorista4@gmail.com', 'es', '19260679', 'cariacicacity3', 'são jose3', 'logras', '11', 'nebas', 'A', 'HLV-5490')
    DiretorMotorista('Giorno', 'Giovanna', '1234', 'motorista5@gmail.com', 'es', '92260679', 'cariacicacity', 'são jose', 'logra0', '1234', 'nabos', 'E', 'BFG-9000')

    return None

def load_empresa():
    DiretorEmpresa('Agenor','fucks','123','empresa1@gmail.com','es','29106100','vila pavão','caboclo','rua mingau','sn','ao lado do motel','18609928000133','Brasileirinhas ltda','33394433')
    DiretorEmpresa('nome1','sobrenome2','1234','empresa2@gmail.com','estado1','29106100','cidade1','bairro1','logradouro1','numeroreferencia1','cnpj1','Digital Extremes1','48615341')
    DiretorEmpresa('nome2', 'sobrenome3', '1234', 'empresa3@gmail.com', 'estado1', '29106102', 'cidade1', 'bairro1','logradouro1', 'numeroreferencia1', 'cnpj4', 'Digital Extremes4', '486135341')
    DiretorEmpresa('nome3', 'sobrenome4', '1234', 'empresa4@gmail.com', 'estado1', '29125100', 'cidade1', 'bairro0','logradouro5', 'numeroreferencia1', 'cnpj2', 'Digital Extremes2', '486115341')
    DiretorEmpresa('nome4', 'sobrenome5', '1234', 'empresa5@gmail.com', 'estado1', '291694300', 'cidade1', 'bairro02','logradour51', 'numeroreferencia1', 'cnpj3', 'Digital Extremes3', '486155341')
