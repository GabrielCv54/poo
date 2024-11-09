from infra.repositorio.individuos_repositorio import IndividuoRepository

repositorio=IndividuoRepository()

data= repositorio.select()

print(data)