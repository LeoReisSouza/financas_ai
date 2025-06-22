from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from .tools import pesquisa_mercado, calcular_investimento, analise_risco
import os

class FinancialAgentService:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0,
            model="openai/gpt-3.5-turbo", 
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
        self.tools = [pesquisa_mercado, calcular_investimento, analise_risco]
        self.agent = self._create_agent()

    def _create_agent(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Você é um especialista em finanças chamado FinBot. Responda de forma clara e profissional."),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad")
        ])
        agent = create_tool_calling_agent(self.llm, self.tools, prompt)
        return AgentExecutor(agent=agent, tools=self.tools, verbose=True)

    def query(self, question: str) -> str:
        try:
            response = self.agent.invoke({"input": question})
            return response["output"]
        except Exception as e:
            return f"Desculpe, ocorreu um erro: {str(e)}"