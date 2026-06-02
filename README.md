# Personal AI Agent

A simple AI agent built with **LangChain** and **Kimi K2.5** (via NVIDIA API). It uses tools to answer questions—weather, calculator, current time, and web search.

## Tools

| Tool | Type | Description |
|------|------|-------------|
| `get_weather` | Demo | Mock weather for any city |
| `calculator` | Demo | Evaluate math expressions |
| `current_time` | Demo | Get current date and time |
| `search_web` | Real | Web search via DuckDuckGo (no API key needed) |

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up your API key

1. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```

2. Get an NVIDIA API key from [build.nvidia.com](https://build.nvidia.com/) (free tier available)

3. Edit `.env` and add your key:
   ```
   NVIDIA_API_KEY=your-nvapi-key-here
   ```

**Important:** Never commit `.env`—it contains your API key. It's already in `.gitignore`.

## Run

```bash
python agent.py
```

Type your questions and press Enter. Type `quit` or `exit` to stop.

## Example queries

- "What's the weather in Tokyo?"
- "What is 15 * 7?"
- "What time is it?"
- "What's the latest news about AI?"
- "Search for Python tutorials 2025"

## Tech stack

- **LangChain** – Agent framework
- **langchain-nvidia-ai-endpoints** – Kimi K2.5 integration
- **langchain-community** – DuckDuckGo web search
- **python-dotenv** – Load API key from `.env`

## License

MIT
