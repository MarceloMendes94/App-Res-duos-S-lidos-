from .builder import *
from .models import EmpresaCupom,Cupom

# faça
# python3 manage.py shell
# from Aplicacao.load import *
# load_clientes()

def load_clientes():
    DiretorCliente('marcelo', 'silva'    , '123', 'cliente1@gmail.com'  ,'es', '29106080', 'vila pavão' ,'ibiri', 'rua das bananas', '12', 'nenhuma', '49257065006' ,'1994-06-06')
    DiretorCliente('eduardo', 'santos'   , '123', 'cliente2@gmail.com'  ,'es', '29106080', 'vila pavão' ,'ibiri', 'rua das bananas', '14', 'nenhuma', '93457469008' ,'1994-06-06')
    DiretorCliente('rodrigo', 'dias'     , '123', 'cliente3@gmail.com'  ,'es', '29106080', 'vila pavão' ,'ibiri', 'rua das bananas', '16', 'nenhuma', '22056241056' ,'1994-06-06')
    DiretorCliente('vanessa', 'silva'    , '123', 'cliente4@gmail.com'  ,'es', '29106080', 'vila pavão' ,'ibiri', 'rua das bananas', '18', 'nenhuma', '60435777041' ,'1994-06-06')
    DiretorCliente('marcelo', 'madureira', '123', 'cliente5@gmail.com'  ,'es', '29106080', 'vila pavão' ,'ibiri', 'rua das bananas', '20', 'nenhuma', '59616689088' ,'1994-06-06')
    DiretorCliente('luiz'   ,'silva'     , '123', 'cliente6@gmail.com'  ,'es','29060170' , 'vitoria'    ,'pedro nolasco','logra1'  ,'111','ref1','12671513111'           ,'1994-06-01')
    DiretorCliente('antonio','oliveira'  , '123', 'cliente7@gmail.com'  ,'es','29060170' , 'vitoria'    ,'ibiratiba'    ,'logra2'  ,'112','ref2','12671513112'              ,'1994-06-02')
    DiretorCliente('glaydson','neto'     , '123', 'glaydso8@gmail.com'  ,'es','29060170' , 'vitoria'    ,'jeriquaquara' ,'logra3'  ,'113','ref3','12671513113'           ,'1994-06-03')
    DiretorCliente('paulo'  ,'junior'    , '123', 'cliente9@gmail.com'  ,'es','29060170' , 'vitoria'    ,'Pedra Branca' ,'logra4'  ,'121','ref4','12671513121'           ,'1994-06-04')
    DiretorCliente('kleber' ,'roque'     , '123', 'cliente10@gmail.com' ,'es','29060170' , 'vitoria'    ,'Cariacica'    ,'logra5'  ,'122','ref5','12671513122'              ,'1994-06-05')
    DiretorCliente('caio'   ,'guzzo'     , '123', 'cliente11@gmail.com' ,'es','29060210' , 'vila velha' ,'Porto de Galinhas','logra6','123','ref6','12671513123'   ,'1994-06-06')
    DiretorCliente('gary'   ,'fernandes' , '123', 'cliente12@gmail.com' ,'es','29060210' , 'vila velha' ,'Gramado'      ,'logra7'  ,'131','ref7','12671513131'             ,'1994-06-07')
    DiretorCliente('ana'    ,'santos'    , '123', 'cliente13@gmail.com' ,'es','29060220' , 'vila velha' ,'Canela'       ,'logra8'  ,'132','ref8','12671513132'              ,'1994-06-08')
    DiretorCliente('jose'   ,'lima'      , '123', 'cliente14@gmail.com' ,'es','29060250' , 'vila velha' ,'morro de são paulo','logra9','133','ref9','12671513133'  ,'1994-06-09')
    DiretorCliente('brenno' ,'rosa'      , '123', 'cliente15@gmail.com' ,'es','29060280' , 'vila velha' ,'Ferrosa'      ,'logra10' ,'211','ref10','12671513211'           ,'1994-06-10')

def load_motoristas():
    DiretorMotorista('Bianco', 'Patuzzo', '123', 'moto1@gmail.com', 'es', '19260679', 'cariaci', 'são jose3', 'logras', '11', 'nebas', 'A', 'HLV5490')
    DiretorMotorista('paulo', 'Patuzzo' , '123', 'moto2@gmail.com', 'es', '19260679', 'cariaci', 'são jose3', 'logras', '11', 'nebas', 'A', 'HLV5490')
    DiretorMotorista('icaro', 'Patuzzo' , '123', 'moto3@gmail.com', 'es', '19260679', 'cariaci', 'são jose3', 'logras', '11', 'nebas', 'A', 'HLV5490')
    DiretorMotorista('Bianco', 'junior' , '123', 'moto4@gmail.com', 'es', '19260679', 'cariaci', 'são jose3', 'logras', '11', 'nebas', 'A', 'HLV5490')

def load_empresa():
    DiretorEmpresa('Agenor','fucks','123','empresa1@gmail.com','es','29106100','vila pavão','caboclo','rua mingau','sn','ao lado do motel','18609928000133','Brasileirinhas ltda','33394433')

def load_empresa_and_cupom():
    #IFOOD
    ifood = EmpresaCupom(nome='Ifood',imagem='/static/img/ifood.png')
    ifood.save()
    cupom_01 = Cupom(empresa=ifood,valor=10.0)
    cupom_01.save() 
    cupom_02 = Cupom(empresa=ifood,valor=20.0)
    cupom_02.save()
    #HBO GO     
    hbogo = EmpresaCupom(nome='HBOgo',imagem='/static/img/hbogo.png')
    hbogo.save()
    cupom_03 = Cupom(empresa=hbogo,valor=35.0)
    cupom_03.save()
    #NETFLIX
    netflix = EmpresaCupom(nome='Netflix',imagem='/static/img/netflix.png')
    netflix.save()
    cupom_04 = Cupom(empresa=netflix,valor=25.0)
    cupom_04.save(0)
    #UBER
    spotify = EmpresaCupom(nome='Spotify',imagem='/static/img/spotify.png')
    spotify.save()
    cupom_05 = Cupom(empresa=spotify,valor=10.0)
    cupom_05.save()

    uber = EmpresaCupom(nome='Uber',imagem='/static/img/uber.png')
    uber.save()
    cupom_06 = Cupom(empresa=uber,valor=10.0)
    cupom_06.save()
    cupom_07 = Cupom(empresa=uber,valor=20.0)
    cupom_07.save()
    cupom_08 = Cupom(empresa=uber,valor=30.0)
    cupom_08.save()
    


def load_all():
    load_clientes()
    load_empresa()
    load_motoristas()