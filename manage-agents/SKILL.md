---
name: manage-agents
description: "List, inspect, patch, update, or delete existing VoiceOfAI voice agents. Use when inspecting configured agents, modifying prompts or voices, backing up settings, or deleting agents."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Manage VoiceOfAI Agents

## Endpoints

- **List Agents:** `GET https://voice.voiceofai.co.in/api/v1/agents?type={type}`
- **Get Agent:** `GET https://voice.voiceofai.co.in/api/v1/agents/{agent_id}`
- **Update Agent:** `PATCH https://voice.voiceofai.co.in/api/v1/agents/{agent_id}`
- **Delete Agent:** `DELETE https://voice.voiceofai.co.in/api/v1/agents/{agent_id}`

## Workflows

### 1. List Agents
```bash
python3 manage-agents/scripts/list_agents.py
```

### 2. Inspect Single Agent
```bash
curl -H "Authorization: Bearer $VOICEOFAI_API_KEY" \
  https://voice.voiceofai.co.in/api/v1/agents/AGENT_ID
```

### 3. Update Agent Settings
```bash
curl -X PATCH -H "Authorization: Bearer $VOICEOFAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"systemPrompt": "Updated prompt text...", "temperature": 0.5}' \
  https://voice.voiceofai.co.in/api/v1/agents/AGENT_ID
```

### 4. Delete Agent
> ⚠️ **Warning:** Deleting an agent is permanent and pauses any campaigns using it.
```bash
curl -X DELETE -H "Authorization: Bearer $VOICEOFAI_API_KEY" \
  https://voice.voiceofai.co.in/api/v1/agents/AGENT_ID
```
