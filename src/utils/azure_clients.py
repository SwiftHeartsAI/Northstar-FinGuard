from openai import AzureOpenAI
from langsmith.wrappers import wrap_openai
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

from src.utils.config import settings

# Factory functions: create and return an object of the AzureOpenAI or SearchClient class, using the 
# settings from the config module. This allows for easy access to these clients throughout the application 
# without needing to repeatedly instantiate them with the same configuration.

# wrap_openai logs each model call (prompt, response, token usage) to LangSmith when
# LANGSMITH_TRACING=true; with tracing off it passes calls straight through.
def get_azure_openai_client():
    return wrap_openai(AzureOpenAI(
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
        api_key=settings.AZURE_OPENAI_API_KEY,
        api_version=settings.AZURE_OPENAI_API_VERSION,
    ))


def get_search_client():
    return SearchClient(
        endpoint=settings.SEARCH_ENDPOINT,
        index_name=settings.SEARCH_INDEX_NAME,
        credential=AzureKeyCredential(settings.SEARCH_KEY),
    )