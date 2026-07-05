from pydantic import BaseModel

class ViaCepResponse(BaseModel):
    cep: str
    logradouro: str
    complemento: str
    bairro: str
    localidade: str
    uf: str
    estado: str | None = None
    regiao: str | None = None
    igbe: str
    gia: str | None = None
    ddd: str
    siafi: str