import os
from pathlib import PosixPath
import dotenv

# wonky to be put here... need to investigate how OLLAMA_HOST works
OLLAMA_HOST = 'http://ollama:11434'

path = PosixPath('~/.ai-agent-key/master.env').expanduser()
if not os.path.exists(path):
    raise Exception('~/.ai-agent-key/master.env not found, please run `cp sample.env ~/.ai-agent-key/master.env` and put your Tavily API key inside.')
dotenv.load_dotenv(path)
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
