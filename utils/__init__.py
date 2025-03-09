import os
import dotenv

# wonky to be put here... need to investigate how OLLAMA_HOST works
OLLAMA_HOST = 'http://ollama:11434'

if not os.path.exists('master.env'):
    raise Exception('master.env not found, please put your tavily API key inside: TAVILY_API_KEY="tvly-dev-..."')
dotenv.load_dotenv('master.env')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')