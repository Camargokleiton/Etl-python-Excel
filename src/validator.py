from pydantic import BaseModel, Field
from typing import Optional

class DataFrameValidator(BaseModel):
    Organizador: int = Field(..., description="Identificador sequencial da linha")
    Ano_Mes: str = Field(..., description="Ano e mês no formato 'YYYY | Mês'")
    Dia_da_Semana: str = Field(..., description="Dia da semana")
    Tipo_Dia: str = Field(..., description="Se é dia útil, feriado, etc.")
    Objetivo: str = Field(..., description="Objetivo da campanha (ex: Leads)")
    Date: str = Field(..., description="Data da observação (dd/mm/yyyy)")
    AdSet_name: str = Field(..., description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(..., description="Valor gasto na campanha")
    Link_clicks: Optional[float] = Field(None, description="Quantidade de cliques no link")
    Impressions: Optional[float] = Field(None, description="Quantidade de impressões")
    Conversions: Optional[float] = Field(None, description="Número de conversões")
    Segmentacao: str = Field(..., alias="Segmentação", description="Tipo de segmentação utilizada")
    Tipo_de_Anuncio: str = Field(..., alias="Tipo_de_Anúncio", description="Formato do anúncio (ex: Estático, Vídeo)")
    Fase: str = Field(..., description="Etapa da campanha (ex: 2º Lançamento | Leads")