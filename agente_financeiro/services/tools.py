from langchain.agents import tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.utilities import GoogleSerperAPIWrapper  # Atualizado
import yfinance as yf
import numpy as np

@tool
def pesquisa_mercado(query: str) -> str:
    """Pesquisa informações financeiras atuais como cotações, notícias e tendências"""
    try:
        search = GoogleSerperAPIWrapper()
        return search.run(f"site:bloomberg.com OR site:investing.com {query}")
    except Exception as e:
        return f"Erro na pesquisa: {str(e)}"

@tool
def calcular_investimento(principal: float, taxa: float, anos: int) -> str:
    """Calcula retorno de investimentos com juros compostos"""
    try:
        montante = principal * (1 + taxa/100) ** anos
        return f"Investimento inicial: R${principal:,.2f}\nTaxa anual: {taxa}%\nPeríodo: {anos} anos\nMontante final: R${montante:,.2f}"
    except Exception as e:
        return f"Erro no cálculo: {str(e)}"

@tool
def analise_risco(ticker: str, periodo: str = "1y") -> str:
    """Analisa risco de um ativo com base em dados históricos"""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=periodo)
        returns = hist['Close'].pct_change().dropna()
        volatility = returns.std() * np.sqrt(252)  # Volatilidade anualizada
        return f"Análise de risco para {ticker}:\nRetorno médio diário: {returns.mean():.2%}\nVolatilidade anualizada: {volatility:.2%}"
    except Exception as e:
        return f"Erro na análise: {str(e)}"