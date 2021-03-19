import sys, os
import pymongo
from pymongo import MongoClient

BASE_PATH = os.path.abspath(__file__+ '/../../../../')
sys.path.append(BASE_PATH)

from inc.consts.consts import *
from inc.classes.db.Db import DbLib

class Users:

    def __init__(self, conn=None):
        if conn:
            self.conn = conn
        else:
            try:
                db = DbLib()
                conn = db.connect(db="desafio")
                self.conn = conn
            except:
                self.conn = False
    
    def criar(self, input):
        
        data = {
            'ok': False,
            'errors': {},
            'data': 0
        }

        # Input
        nome = ''
        cpf = ''
        celular = ''
        score = 0
        negativado = False

        # Params
        if input:
            nome = str(input['nome']) if 'nome' in input else ''
            cpf = str(input['cpf']) if 'cpf' in input else ''                
            celular = str(input['celular']) if 'celular' in input else ''    
            score = int(input['score']) if 'score' in input else 0 
            negativado = bool(input['negativado']) if 'negativado' in input else False 
        
        # Validation
        if not nome:
            data['errors']['nome'] = 'Nome não indicado.'
        
        if not cpf:
            data['errors']['cpf'] = 'Cpf não indicado.'            

        if not celular:
            data['errors']['celular'] = 'Celular não indicado.'
        
        if score < 0 or score > 1000 :
            data['errors']['score'] = 'Score invalido.'
        
        if not self.conn:
            data['errors']['conn'] = 'Erro de comunicação com o banco de dados.'

        # verfica se cpf e celular ja foram cadastrados
        resp = self._verificar_cpf_celular(cpf, celular)
        if not resp["ok"] or not resp["data"]:
            
            # junta erros se houver algum
            data["errors"] = {**data["errors"], **resp["errors"]}

        if not data['errors']:
            try:
                
                row = {
                    "nome": nome,
                    "cpf": cpf,
                    "celular": celular,
                    "score": score,
                    "negativado": negativado
                }
                resp = self.conn.users.insert_one(row)

                if not str(resp.inserted_id):
                    data["errors"]["insert"] = "Erro ao inserir usuario."
                
                if not data['errors']:
                    data['ok'] = True
                    data['data'] = str(resp.inserted_id)

            except Exception as error:
                data['errors']['conn'] = 'Erro na conexão com o banco de dados: ' + str(error)
            
            finally:
                if type(self.conn)==MongoClient:
                    self.conn.close()

        return data
    
    def criar_multiplos(self, inputs):
        
        data = {
            'ok': False,
            'errors': {},
            'data': False
        }

        # Input
        nome = ''
        cpf = ''
        celular = ''
        score = 0
        negativado = False

        # Params
        for input in inputs:
            if input:
                nome = str(input['nome']) if 'nome' in input else ''
                cpf = str(input['cpf']) if 'cpf' in input else ''                
                celular = str(input['celular']) if 'celular' in input else ''    
                score = int(input['score']) if 'score' in input else 0 
                negativado = bool(input['negativado']) if 'negativado' in input else False 
                
                # verfica se cpf e celular ja foram cadastrados
                resp = self._verificar_cpf_celular(cpf, celular)
                if not resp["ok"] or not resp["data"]:
                    
                    # junta erros se houver algum
                    data["errors"] = {**data["errors"], **resp["errors"]}

        
            # Validation
            if not nome:
                data['errors']['nome'] = 'Nome não indicado.'
            
            if not cpf:
                data['errors']['cpf'] = 'Cpf não indicado.'            

            if not celular:
                data['errors']['celular'] = 'Celular não indicado.'
            
            if score < 0 or score > 1000 :
                data['errors']['score'] = 'Score invalido.'
            
        if not self.conn:
            data['errors']['conn'] = 'Erro de comunicação com o banco de dados.'

        if not data['errors']:
            try:

                resp = self.conn.users.insert_many(inputs)

                if not data['errors']:
                    data['ok'] = True
                    data['data'] = True

            except Exception as error:
                data['errors']['conn'] = 'Erro na conexão com o banco de dados: ' + str(error)
            
            finally:
                if type(self.conn)==MongoClient:
                    self.conn.close()

        return data
    
    def verificar(self, input):
        
        data = {
            'ok': False,
            'errors': {},
            'data': 0
        }

        # Input
        cpf = ''
        celular = ''

        # Params
        if input:
            cpf = str(input['cpf']) if 'cpf' in input else ''                
            celular = str(input['celular']) if 'celular' in input else ''    
    
        # Validation
        if not cpf:
            data['errors']['cpf'] = 'Cpf não indicado.'            

        if not celular:
            data['errors']['celular'] = 'Celular não indicado.'
        
        if not self.conn:
            data['errors']['conn'] = 'Erro de comunicação com o banco de dados.'

        if not data['errors']:
            try:
                
                resp = self.conn.users.insert_many(inputs)

                if not data['errors']:
                    data['ok'] = True
                    data['data'] = True

            except Exception as error:
                data['errors']['conn'] = 'Erro na conexão com o banco de dados: ' + str(error)
            
            finally:
                if type(self.conn)==MongoClient:
                    self.conn.close()

        return data
    
    def _verificar_cpf_celular(self, cpf, celular):
        
        data = {
            'ok': False,
            'errors': {},
            'data': False
        }  
    
        # Validation
        if not cpf:
            data['errors']['cpf'] = 'Cpf não indicado.'            

        if not celular:
            data['errors']['celular'] = 'Celular não indicado.'
        
        if not self.conn:
            data['errors']['conn'] = 'Erro de comunicação com o banco de dados.'

        if not data['errors']:
            try:
                
                resp = self.conn.users.find({'cpf' : cpf, 'celular': celular}).count()

                if resp > 0:
                    data["errors"]["input"] = "Cpf e celular ja cadastrado."
                

                if not data['errors']:
                    data['ok'] = True
                    data['data'] = True

            except Exception as error:
                data['errors']['conn'] = 'Erro na conexão com o banco de dados: ' + str(error)
            
            finally:
                if type(self.conn)==MongoClient:
                    self.conn.close()

        return data


