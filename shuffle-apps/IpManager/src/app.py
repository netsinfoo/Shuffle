from phpipam_client import PhpIpamClient, GET, PATCH
import sys
import json
import requests

from walkoff_app_sdk.app_base import AppBase

class IpManager(AppBase):
    __verison__= " 0.0.2"
    app_name = "IpManager"
    
    def __init__(self, redis, logger, console_logger=None):
                
        super().__init__(redis, logger, console_logger)
        
        
    def get_info(self, client_ip, url, app_id, token):
        
        ipam = PhpIpamClient(url, app_id, token, encryption=True)
                
        consulta =  ipam.get('/addresses/search/'+ client_ip +'/')
        
        return consulta
    
    def testa_retorno(self, nome):
        welcome = "Seja bem vindo ao shuffle " + nome
        return welcome
        
if __name__ == "__main__":
    IpManager.run()
    
    
    
    
    
