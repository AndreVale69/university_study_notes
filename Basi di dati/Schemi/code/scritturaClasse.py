"""
Si vuole salvare in un file una tabella delle spese definita come:
table spese{
    data DATE,
    voce VARCHAR,
    importo Decimal
}
In questo paragrafo si rappresenta la tabella come
un oggetto di una classe e si usa JSON per salvare.
Inoltre gli importi sono rappresentati come Decimal.
"""
# ############################################################
# IMPORT
import datetime
import decimal
import json
import re

# ############################################################

# Classi o funzioni di servizio
pattern = re.compile("^\d{2,2}/\d{2,2}/\d{4,4}$")
def creaDict(data, voce, importo):
    """
    Ritorna un dict formato con gli argomenti.\n
    Formato: {'data':<data>, 'voce':<voce>, 'importo':<importo>}.\n
    Fa il check sul formato data e su importo che
    deve essere Decimal.
    """
    if not isinstance(data, str) or not pattern.match(data):
        print("Data non e' nel formato dd/mm/aaaa")
        exit()
    if not isinstance(importo, decimal.Decimal) and not isinstance(importo, str):
        print("Importo deve essere un Decimal o una stringa che rappresenta un importo.")
        exit()
    return {'data':data, 'voce':voce, 'importo':decimal.Decimal(importo)}

class Spese:
    """
    L'attributo 'tabella' rappresenta le spese organizzate come dict(primaryKey, riga).\n
    La primaryKey e' data dalla coppia (data, voce).\n
    La riga e' un dict creato dal metodo creaDict().\n
    L'attributo 'ultimaModifica' rappresenta il timestamp dell'ultima modifica.
    """
    def __init__(self, inputTab = {}, istante = datetime.datetime.now()):
        self.tabella = dict(inputTab)
        self.ultimaModifica = istante

    def makeKey(data, voce):
        return data + "_%_" + voce
    
    def add(self, data, voce, importo):
        self.tabella[Spese.makeKey(data, voce)] = creaDict(data, voce, importo)
        self.ultimaModifica = datetime.datetime.now()
        return importo
    
    def remove(self, data, voce):
        del self.tabella[Spese.makeKey(data, voce)]
        self.ultimaModifica = datetime.datetime.now()

    def get(self, data, voce):
        return self.tabella[self.makeKey(data, voce)]
    
    def items(self):
        return self.tabella.items()

# ############################################################
# Crea la tabella e aggiungo dati
tab = Spese()
tab.add("24/02/2016", "Stipendio", "0.1")
tab.add("24/02/2016", 'Stipendio "Bis"', "0.1")
tab.add("24/02/2016", 'Stipendio "Tris"', "0.1")
tab.add("24/02/2016", "Affitto", "-0.3")
# Stampo la tabella da memoria
print('=' * 50)
print("|{:10s}|{: <20}|{: >10s}|"
      .format("Data", "Voce", "Importo"))
print('-' * 50)
for riga in tab.tabella.values():
    print("|{:10s}|{: <20}|{: >10.2f}|"
          .format(riga['data'], riga['voce'], riga['importo']))
    print('=' * 50)

# Calcoli il totale degli importi
tot = decimal.Decimal(0)
for riga in tab.tabella.values():
    tot += riga['importo']
print("La somma e' {:.20f}".format(tot))

# Salvataggio in un file
class MyEncoder(json.JSONEncoder):
    """ Codifica gli oggetti di tipo Decimal, Date o Spese. """
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        if isinstance(o, Spese):
            return {"tabella": o.tabella, 
                    "ultimaModifica": o.ultimaModifica}
        return json.JSONEncoder.default(self, o)
    
# Salvo la tabella in un file
nomeFile = 'database.json'
with open(nomeFile, mode='w', encoding='utf-8') as file:
    json.dump(tab, file, cls=MyEncoder, indent=4)

def myDecoder(jsonObj):
    """ Decodifica oggetti di tipo Spesa. """
    if 'tabella' in jsonObj:
        tab = jsonObj['tabella']
        istante = datetime.datetime.strptime(jsonObj['ultimaModifica'], "%Y-%m-%dT%H:%M:%S.%f")
        return Spese(tab, istante)
    else:
        return jsonObj
    
# Leggo dal file la tabella e la pongo in una nuova variabile
with open(nomeFile, mode='r', encoding='utf-8') as file:
    tab1 = json.load(file, object_hook=myDecoder, parse_float=decimal.Decimal)

# Calcolo il totale sulla nuova tabella
tot1 = decimal.Decimal(0)
for riga in tab1.tabella.values():
    tot1 += riga['importo']
if tot == tot1:
    print("I due totali sono uguali!")
if tot == 0:
    print("Eureka!!")
else:
    print("Ops... il totale non e' corretto!")