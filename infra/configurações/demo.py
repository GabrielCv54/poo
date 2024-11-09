class OlaMUndo:
    def __enter__(self):
        print('Estou entrando')
  
    def __exit__(self,exc_type, exc_val , exc_tb):
        print('estou saindo')


with OlaMUndo() as ola:
    print('Estou aqui ')