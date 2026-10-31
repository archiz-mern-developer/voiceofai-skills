---
name: get-analytics
description: "Pull aggregated call stats, campaign performance comparison metrics, or account-wide dashboard summaries using MCP tools. Use when evaluating call performance, answer rates, or campaign costs."
license: MIT
compatibility: Requires VoiceOfAI MCP server connection (FastMCP / voiceofai).
metadata:
  mcp:
    server: voiceofai
    tools:
      - get_call_analytics
      - get_campaign_analytics
      - get_analytics_summary
---

# Get VoiceOfAI Analytics & Metrics

## Overview

Retrieve performance metrics, call conversion analytics, and cross-campaign evaluations using the `voiceofai` MCP tools.

## Available MCP Tools

### 1. `get_call_analytics`
Get aggregated statistics on phone calls, including answer rates, average call duration, outcome distribution, and daily trends.

**Arguments:**
- `days` (integer, optional, default `30`): Lookback period in days (1 to 90).

**Example Tool Invocation:**
```json
{
  "name": "get_call_analytics",
  "arguments": {
    "days": 30
  }
}
```

**Returned Data Structure:**
```json
{
  "totalCalls": 1250,
  "totalMinutes": 3480.5,
  "answerRate": 0.74,
  "averageDurationSeconds": 167,
  "outcomes": {
    "completed": 850,
    "voicemail": 180,
    "busy": 90,
    "failed": 30,
    "no_answer": 100
  },
  "dailyTrend": [
    { "date": "2026-10-30", "calls": 52, "minutes": 145.2 }
  ]
}
```

---

### 2. `get_campaign_analytics`
Compare performance across all bulk calling campaigns, including total contacts, dial count, answer rate, completion rate, and credit cost.

**Arguments:** None

**Example Tool Invocation:**
```json
{
  "name": "get_campaign_analytics",
  "arguments": {}
}
```

**Returned Data Structure:**
```json
{
  "campaigns": [
    {
      "campaignId": "cmp_987e6543-e21b-12d3-a456-426655440000",
      "name": "Q4 Reactivation Outreach",
      "totalContacts": 500,
      "callsPlaced": 500,
      "answeredCalls": 370,
      "answerRate": 0.74,
      "completedRate": 0.68,
      "totalCreditsUsed": 1120.0
    }
  ]
}
```

---

### 3. `get_analytics_summary`
Fetch a high-level executive dashboard summary comparing total volume, campaign metrics, credit spend, and success rates against the previous period.

**Arguments:**
- `days` (integer, optional, default `30`): Lookback period in days (1 to 90).

**Example Tool Invocation:**
```json
{
  "name": "get_analytics_summary",
  "arguments": {
    "days": 7
  }
}
```

**Returned Data Structure:**
```json
{
  "period": { "days": 7 },
  "totalCalls": 312,
  "totalMinutes": 890.0,
  "callsChangePercent": 14.5,
  "activeCampaigns": 2,
  "activeAgents": 4,
  "creditBalance": {
    "available": 450.5,
    "total": 465.5
  }
}
```
