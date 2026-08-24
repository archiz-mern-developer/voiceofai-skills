---
name: setup-api-key
description: "Verify, test, and troubleshoot a VoiceOfAI API key (VOICEOFAI_API_KEY). Use when starting a VoiceOfAI project, setting up authentication, diagnosing 401 or 403 unauthorized errors, or checking API health."
license: MIT
compatibility: Requires internet access and VOICEOFAI_API_KEY.
metadata:
  openclaw:
    requires:
      env:
        - VOICEOFAI_API_KEY
    primaryEnv: VOICEOFAI_API_KEY
---

# Setup VoiceOfAI API Key

## Core Facts

- **Default Base URL:** `https://voice.voiceofai.co.in/api/v1`
- **Auth Header:** `Authorization: Bearer $VOICEOFAI_API_KEY`
- **Health / Smoke Test Endpoint:** `GET /health` or `GET /credits/balance`
- API keys are created in the VoiceOfAI Dashboard under **Settings → Developer**.
- Keep your API key secret. Never commit it to git or publicly expose it.

## Quick Setup Steps

1. Check if `VOICEOFAI_API_KEY` is set in your environment:
   ```bash
   echo $VOICEOFAI_API_KEY
   ```
2. If not set, export your key:
   ```bash
   export VOICEOFAI_API_KEY="agl_sk_..."
   ```
3. Test your key with the helper script:
   ```bash
   python3 setup-api-key/scripts/verify_key.py
   ```

## Script Usage

```bash
python3 setup-api-key/scripts/verify_key.py
```
Outputs JSON indicating whether the API key is valid, along with status code and message.
