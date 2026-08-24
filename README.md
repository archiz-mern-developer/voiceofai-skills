# 🎤 VoiceOfAI Skills

Official Agent Skills for [VoiceOfAI Voice Platform](https://voice.voiceofai.co.in). Teach your AI coding assistant — Claude Code, Cursor, Codex, Antigravity, or any tool supporting the Agent Skills format — to build, deploy, test, and operate production voice agents and bulk calling campaigns in one command.

## 🚀 Quick Start & Install

Install all skills using the Agent Skills CLI:

```bash
npx skills add voiceofai-ai/skills
```

For a specific AI tool:

```bash
npx skills add voiceofai-ai/skills -a claude-code
npx skills add voiceofai-ai/skills -a cursor
npx skills add voiceofai-ai/skills -a codex
```

Install just a single skill:

```bash
npx skills add voiceofai-ai/skills --skill create-agent
```

## 🔑 Setup

Get your API key from the **VoiceOfAI Dashboard → Settings → Developer** tab and export it:

```bash
export VOICEOFAI_API_KEY="your-api-key-here"
```

Optionally set the API Base URL if using a custom environment:

```bash
export VOICEOFAI_BASE_URL="https://voice.voiceofai.co.in/api/v1"
```

## 💬 What You Can Ask Your AI Assistant

Once installed, ask your AI assistant natural language requests like:

- *"Create a VoiceOfAI voice agent for customer support with OpenAI and ElevenLabs."*
- *"Trigger a test outbound call to +14155551234 using agent ID `123e4567...`."*
- *"Upload `leads.csv` as a bulk calling campaign and launch it."*
- *"Check my VoiceOfAI credit balance and daily usage."*
- *"Get call analytics and disposition metrics for the last 30 days."*
- *"Set up a webhook to receive `call.completed` events."*
- *"Link phone number `num_987` to answer inbound calls for my receptionist agent."*

The right skill loads automatically based on your prompt.

## 📚 Available Skills

| Skill | Description |
|---|---|
| `setup-api-key` | Verify and test your `VOICEOFAI_API_KEY` against VoiceOfAI. |
| `create-agent` | Create incoming or flow voice agents (system prompts, voices, LLMs, transfer rules). |
| `manage-agents` | List, inspect, patch, export flow, or delete voice agents. |
| `make-call` | Trigger immediate or scheduled outbound calls with custom metadata. |
| `manage-calls` | List past calls, inspect transcripts/recordings, and terminate active calls. |
| `create-campaign` | Create bulk calling campaigns, import CSV contacts, start/pause execution. |
| `manage-contacts` | Create, list, search, update, or bulk-import CRM contacts. |
| `setup-incoming` | Link/unlink voice agents to phone numbers for handling inbound calls. |
| `manage-credits` | Check credit balance (minutes) and daily usage history. |
| `get-analytics` | Pull call volume, campaign performance, and account activity metrics. |
| `setup-webhook` | Register, update, test, or delete HTTP webhook event subscriptions. |
| `agent-flows` | Export and import complex visual agent flows (JSON nodes/edges). |

## 🛠️ Repository Structure

```
voiceofai-skills/
├── references/              # Platform architecture & phone format reference guides
│   ├── voiceofai-core.md
│   ├── providers-matrix.md
│   └── phone-number-formats.md
├── scripts/                 # Shared repository utilities
│   └── validate_skills.py
├── setup-api-key/           # Skill: API key setup & test
├── create-agent/            # Skill: Create agents
├── manage-agents/           # Skill: List/update/delete agents
├── make-call/               # Skill: Trigger calls
├── manage-calls/            # Skill: Inspect/hangup calls
├── create-campaign/         # Skill: Campaign creation & CSV import
├── manage-contacts/         # Skill: CRM contact management
├── setup-incoming/          # Skill: Inbound phone linking
├── manage-credits/          # Skill: Credit balance & usage
├── get-analytics/           # Skill: Call & campaign analytics
├── setup-webhook/           # Skill: Webhooks
└── agent-flows/             # Skill: Visual flow import/export
```

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
