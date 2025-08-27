from pydantic import BaseModel, Field, field_validator
from typing import Optional

class DataFrameValidator(BaseModel):
    Organizador: int = Field(..., description="Identificador sequencial da linha",nullable=True)
    Ano_Mes: str = Field(..., description="Ano e mês no formato 'YYYY | Mês'")
    Dia_da_Semana: str = Field(..., description="Dia da semana")
    Tipo_Dia: str = Field(..., description="Se é dia útil, feriado, etc.")
    Objetivo: str = Field(..., description="Objetivo da campanha (ex: Leads)")
    Date: str = Field(..., description="Data da observação (dd/mm/yyyy)")
    AdSet_name: str = Field(..., description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(..., description="Valor gasto na campanha")
    Link_clicks: Optional[float] = Field(None, description="Quantidade de cliques no link",nullable=True)
    Impressions: Optional[float] = Field(None, description="Quantidade de impressões",nullable=True)
    Conversions: Optional[float] = Field(None, description="Número de conversões",nullable=True)
    Segmentacao: Optional[str] = Field(None, alias="Segmentação", description="Tipo de segmentação utilizada",nullable=True)
    Tipo_de_Anúncio: str = Field(None, alias="Tipo_de_Anúncio", description="Formato do anúncio (ex: Estático, Vídeo)", nullable=True)
    Fase: Optional[str] = Field(None, description="Etapa da campanha (ex: 2º Lançamento | Leads",nullable=True)

    @field_validator("Link_clicks", "Impressions", "Conversions")
    def must_be_positive(cls, v):
        if v is not None and v <0:
            raise ValueError("O valor deve ser maior ou igual à zero")
        return v