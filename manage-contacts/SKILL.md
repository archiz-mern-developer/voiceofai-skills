---
name: manage-contacts
description: "Create, list, search, update, delete, or bulk-import CRM contacts in VoiceOfAI. Enriched with call history, lead scores, and sentiment analysis."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Manage VoiceOfAI CRM Contacts

## Endpoints

- **List Contacts:** `GET https://voice.voiceofai.co.in/api/v1/contacts?page={page}&pageSize={pageSize}`
- **Create Contact:** `POST https://voice.voiceofai.co.in/api/v1/contacts`
- **Get Contact Details:** `GET https://voice.voiceofai.co.in/api/v1/contacts/{contact_id}`
- **Update Contact:** `PUT https://voice.voiceofai.co.in/api/v1/contacts/{contact_id}`
- **Delete Contact:** `DELETE https://voice.voiceofai.co.in/api/v1/contacts/{contact_id}`
- **Bulk Import Contacts:** `POST https://voice.voiceofai.co.in/api/v1/contacts/bulk-import`

## Single Contact Schema

```json
{
  "phone": "+14155551234",
  "firstName": "John",
  "lastName": "Doe",
  "email": "john@example.com",
  "company": "Acme Corp",
  "tags": ["vip", "leads"],
  "customFields": {
    "account_number": "ACC123"
  }
}
```

## Helper Scripts

Create one contact:
```bash
python3 manage-contacts/scripts/create_contact.py \
  --phone "+14155551234" \
  --first-name "John" \
  --last-name "Doe"
```

Bulk import contacts:
```bash
python3 manage-contacts/scripts/bulk_import_contacts.py \
  --json-file "contacts.json"
```
