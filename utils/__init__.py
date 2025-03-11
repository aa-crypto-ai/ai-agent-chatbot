import os
import dotenv

if not os.path.exists('master.env'):
    raise Exception('master.env not found, please put your tavily API key inside: OPENROUTERAI_API_KEY=="sk-or-v1-..."')
dotenv.load_dotenv('master.env')
OPENROUTERAI_API_KEY = os.getenv('OPENROUTERAI_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')