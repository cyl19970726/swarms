from openai import OpenAI
from dotenv import load_dotenv
import os
import logging  
# 配置 logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f"Loaded API Key: {api_key}")

logger.info("API Key status: %s", "✓ Set" if api_key else "✗ Not Set")
# 如果想看到 key 的前几个字符（相对安全的方式）

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "analyze this repo code https://github.com/Uniswap/UniswapX.git"
        }
    ]
)

print(completion.choices[0].message)