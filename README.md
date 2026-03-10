# Grok + DigitalOcean Gradient AI Platform (ADK) Demo

Run Grok-powered AI agents on **DigitalOcean's Gradient AI Platform** using the **Agent Development Kit (ADK)** — with full observability, tracing, and easy deployment.

This repo shows a minimal, production-ready example of integrating **xAI's Grok** (via the OpenAI-compatible API) into a Gradient ADK agent. Grok inference runs remotely via api.x.ai while the agent code and hosting live on DigitalOcean.

**Why this combo?**
- Gradient ADK = free preview compute + built-in tracing/evals/RAG tools
- Grok = strong reasoning, large context (up to 2M tokens on grok-4-1-fast-reasoning), truthful style
- Zero infra management: deploy in minutes, pay only for xAI usage

**Status (March 2026)**: Grok is **not** natively listed in Gradient's serverless inference catalog yet, but integrates perfectly using the OpenAI SDK with custom base URL + your xAI API key.

## Features Demonstrated

- Async Grok call using `openai` SDK (Responses API style)
- ADK `@entrypoint` + `@trace_llm` for observability
- Local dev with hot reload
- One-command deploy to DigitalOcean
- Environment variable secrets handling (.env → DO runtime)

## Prerequisites

1. **DigitalOcean Account**
   - Enable **Gradient AI Platform** preview (Account → Feature Preview)
   - Personal Access Token with `genai` Write + `project` Read scopes  
     → https://cloud.digitalocean.com/account/api/tokens

2. **xAI / Grok API**
   - API key from https://console.x.ai/team/default/api-keys
   - Add billing/credits if needed

3. **Local Setup**
   - Python 3.10+
   - `pip install gradient-adk openai python-dotenv`

## Quick Start (Local)

```bash
# 1. Clone & enter repo
git clone https://github.com/YOUR_USERNAME/grok-gradient-adk-demo.git
cd grok-gradient-adk-demo

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env (never commit!)
cat << EOF > .env
DIGITALOCEAN_API_TOKEN=do_pat_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
XAI_API_KEY=xai-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
EOF

# 4. Initialize ADK project (if starting fresh; skips if files exist)
gradient agent init --force  # optional

# 5. Run locally (with hot reload & verbose logs)
gradient agent run --dev --verbose
