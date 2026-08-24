# VoiceOfAI Telephony & Voice Providers Matrix

## Supported Telephony Engines

When triggering calls or creating campaigns, VoiceOfAI supports multiple engine types:

| Engine | Identifier | Description |
|---|---|---|
| **VoiceOfAI Native** | `voiceofai` | Recommended. Native high-throughput engine with minimal latency. |
| **ElevenLabs Native** | `elevenlabs` | Direct integration with ElevenLabs conversational voice stack. |
| **Plivo** | `plivo` | Global telephony provider suitable for international numbers. |
| **Twilio OpenAI** | `twilio-openai` | Twilio network combined with OpenAI Realtime API. |

## OpenAI Realtime Voices

When configuring agents with `telephonyProvider: "twilio_openai"`, choose from:

- `alloy`
- `echo`
- `shimmer`
- `ash`
- `ballad`
- `coral`
- `sage`
- `verse`
- `cedar`
- `marin`

## ElevenLabs Voices

When using `elevenLabsVoiceId`, pass any valid 20-character ElevenLabs Voice ID string (e.g. `21m00Tcm4TlvDq8ikWAM`).

## Voice Parameters

- `temperature`: float between `0.0` and `2.0` (default `0.7`)
- `voiceStability`: float between `0.0` and `1.0` (default `0.5`)
- `voiceSimilarityBoost`: float between `0.0` and `1.0` (default `0.75`)
- `voiceSpeed`: float between `0.5` and `2.0` (default `1.0`)
- `maxDurationSeconds`: max length of call in seconds (default `600`)
