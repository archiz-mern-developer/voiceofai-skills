# 🎤 VoiceOfAI Skills

Official Agent Skills for [VoiceOfAI Voice Platform](https://voice.voiceofai.co.in) using the **VoiceOfAI MCP Server** (`voiceofai`). Teach your AI coding assistant — Claude Code, Cursor, Codex, Antigravity, or any tool supporting the Agent Skills format and MCP — to build, deploy, test, and operate production voice agents and bulk calling campaigns using native MCP tools.

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

## 🔑 MCP Server Configuration

Connect your MCP client to the `voiceofai` MCP server.

### Stdio Transport (e.g. `claude_desktop_config.json` or `.mcp.json`)
```json
{
  "mcpServers": {
    "voiceofai": {
      "command": "python",
      "args": ["VoiceofAi-MCP/run_stdio.py"],
      "env": {
        "VOICEOFAI_API_KEY": "your-api-key-here",
        "VOICEOFAI_BASE_URL": "https://voice.voiceofai.co.in/api/v1"
      }
    }
  }
}
```

### HTTP / SSE Transport
Point your MCP client to the VoiceOfAI MCP server endpoint (e.g. `http://localhost:8000/sse` or `https://.../mcp`), passing your VoiceOfAI API key as the bearer token (`Authorization: Bearer <key>`).

## 💬 What You Can Ask Your AI Assistant

Once installed with the VoiceOfAI MCP server active, ask your AI assistant natural language requests like:

- *"Create a VoiceOfAI voice agent for customer support with OpenAI and ElevenLabs."*
- *"Trigger a test outbound call to +14155551234 using agent ID `123e4567...`."*
- *"Upload `leads.csv` as a bulk calling campaign and launch it."*
- *"Check my VoiceOfAI credit balance and daily usage."*
- *"Get call analytics and disposition metrics for the last 30 days."*
- *"Set up a webhook to receive `call.completed` events."*
- *"Link phone number `num_987` to answer inbound calls for my receptionist agent."*

The right skill loads automatically and directs the assistant to call the appropriate MCP tool.

## 📚 Available Skills & MCP Tools Mapping

| Skill | Primary MCP Tools | Description |
|---|---|---|
| `setup-api-key` | `health_check`, `get_credit_balance` | Verify connectivity and test authentication credentials. |
| `create-agent` | `create_agent` | Create incoming or flow voice agents (system prompts, voices, LLMs, transfer rules). |
| `manage-agents` | `list_agents`, `get_agent`, `update_agent`, `delete_agent` | List, inspect, patch, or delete voice agents. |
| `make-call` | `trigger_call` | Trigger immediate or scheduled outbound calls with custom metadata. |
| `manage-calls` | `list_calls`, `get_call`, `hangup_call` | List past calls, inspect transcripts/recordings, and terminate active calls. |
| `create-campaign` | `create_campaign`, `list_campaigns`, `get_campaign`, `add_campaign_contacts`, `upload_campaign_csv`, `start_campaign`, `pause_campaign` | Create bulk calling campaigns, import contacts, start/pause execution. |
| `manage-contacts` | `list_contacts`, `create_contact`, `get_contact`, `update_contact`, `delete_contact`, `bulk_import_contacts` | Create, list, search, update, or bulk-import CRM contacts. |
| `setup-incoming` | `list_incoming_connections`, `link_incoming_connection`, `unlink_incoming_connection` | Link/unlink voice agents to phone numbers for handling inbound calls. |
| `manage-credits` | `get_credit_balance`, `get_credit_usage` | Check credit balance (minutes) and daily usage history. |
| `get-analytics` | `get_call_analytics`, `get_campaign_analytics`, `get_analytics_summary` | Pull call volume, campaign performance, and account activity metrics. |
| `setup-webhook` | `list_webhooks`, `list_webhook_events`, `create_webhook`, `update_webhook`, `delete_webhook`, `test_webhook` | Register, update, test, or delete HTTP webhook event subscriptions. |
| `agent-flows` | `export_agent_flow`, `import_agent_flow` | Export and import visual agent flows (JSON nodes/edges/variables). |

## 🛠️ Repository Structure

```
voiceofai-skills/
├── references/              # Platform architecture & phone format reference guides
│   ├── voiceofai-core.md
│   ├── providers-matrix.md
│   └── phone-number-formats.md
├── scripts/                 # Validation utilities
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
