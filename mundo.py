import xmlrpc.client
import csv
import numpy as np

class Supervisor:
    
    modelPath = ''
    port = ''
    server = None
    modelName = ''
    scopeRef = ''
    scopes = None
    
    def __init__(self):
        self.modelPath = r"C:\Users\57322\Desktop\Supervisor"
        self.port = "1080"
        self.server = xmlrpc.client.Server('http://localhost:' + self.port + '/RPC2')
        self.modelName = 'buckboost'
        self.scopeRef = 'Scope'
        self.scopePath = self.modelName + '/' + self.scopeRef
        self.server.plecs.load(self.modelPath + '/' + self.modelName + '.plecs')
        self.server.plecs.scope( self.scopePath, 'ClearTraces')
        
    def simular(self, numIrr):
        
        opts = {'ModelVars' : {'irr' : numIrr/1000}}
        self.server.plecs.simulate(self.modelName, opts)
        print(self.server.plecs.get(self.modelName + '/Scope'))
        

        
        
        with open(self.modelPath+"\Data.csv", 'r') as f:
            self.scopes = list(csv.reader(f, delimiter=","))
            
        self.scopes = np.array(self.scopes[1:], dtype=np.float)


            
    def getData(self):
        
        return self.scopes