---
name: create-campaign
description: "Create, configure, populate with CSV contacts, start, pause, or monitor bulk outbound calling campaigns. Use when setting up broadcast campaigns or batch dialing lists."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Create & Manage VoiceOfAI Campaigns

## Endpoints

- **Create Campaign:** `POST https://voice.voiceofai.co.in/api/v1/campaigns`
- **Get Campaign:** `GET https://voice.voiceofai.co.in/api/v1/campaigns/{campaign_id}`
- **Add Contacts (JSON):** `POST https://voice.voiceofai.co.in/api/v1/campaigns/{campaign_id}/contacts`
- **Upload CSV:** `POST https://voice.voiceofai.co.in/api/v1/campaigns/{campaign_id}/contacts-upload`
- **Start Campaign:** `POST https://voice.voiceofai.co.in/api/v1/campaigns/{campaign_id}/start`
- **Pause Campaign:** `POST https://voice.voiceofai.co.in/api/v1/campaigns/{campaign_id}/pause`

## Workflow

1. **Create Campaign** (starts in `draft` status):
   ```bash
   python3 create-campaign/scripts/create_campaign.py \
     --name "August Outreach" \
     --agent-id "AGENT_UUID" \
     --max-concurrent 5
   ```
2. **Upload CSV Contact List**:
   ```bash
   python3 create-campaign/scripts/upload_contacts_csv.py \
     --campaign-id "CAMPAIGN_UUID" \
     --csv-path "create-campaign/assets/sample_contacts.csv"
   ```
3. **Start Dialing**:
   ```bash
   curl -X POST -H "Authorization: Bearer $VOICEOFAI_API_KEY" \
     https://voice.voiceofai.co.in/api/v1/campaigns/CAMPAIGN_UUID/start
   ```

## CSV Format Requirements

Required Column:
- `phone` or `phone_number` (in E.164 format, e.g. `+14155551234`)

Optional Columns:
- `firstName` / `first_name`
- `lastName` / `last_name`
- `email`
- Any additional custom column becomes a dynamic parameter token (e.g. `{amount_due}`).
