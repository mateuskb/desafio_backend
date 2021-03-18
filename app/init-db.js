db = db.getSiblingDB("desafio");
db.users.drop();

db.users.insertMany([
    {
        "nome": "Roberto Filipe Figueiredo",
        "cpf": "41882728564",
        "celular": "6526332774",
        "score": 300,
        "negativado": false
    },
    {
        "nome": "Bernardo Martins", 
        "cpf": "23401976516", 
        "celular": "81977468400", 
        "score": 879, 
        "negativado": true
    }
]);