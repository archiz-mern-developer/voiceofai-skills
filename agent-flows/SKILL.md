---
name: agent-flows
description: "Export visual flow graphs (JSON nodes, edges, variables) from 'flow'-type agents, or replace an existing flow configuration. Use when backing up visual graph agents or restoring flow templates."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Export & Import Visual Agent Flows

## Endpoints

- **Export Flow Graph:** `GET https://voice.voiceofai.co.in/api/v1/agents/{agent_id}/flow`
- **Import Flow Graph:** `PUT https://voice.voiceofai.co.in/api/v1/agents/{agent_id}/flow`

## Flow Graph Object Structure

```json
{
  "flow": {
    "name": "Payment Flow",
    "nodes": [
      {
        "id": "node_1",
        "type": "speak",
        "data": { "text": "Please confirm your invoice number." }
      },
      {
        "id": "node_2",
        "type": "input",
        "data": { "variable": "invoice_num" }
      }
    ],
    "edges": [
      { "id": "edge_1", "source": "node_1", "target": "node_2" }
    ],
    "variables": {
      "invoice_num": null
    }
  }
}
```

## Helper Script

Export flow to file:
```bash
python3 agent-flows/scripts/export_flow.py --agent-id "AGENT_UUID" --output "flow_backup.json"
```

Import flow from file:
```bash
curl -X PUT -H "Authorization: Bearer $VOICEOFAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @flow_backup.json \
  https://voice.voiceofai.co.in/api/v1/agents/AGENT_UUID/flow
```
