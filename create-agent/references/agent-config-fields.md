# VoiceOfAI Agent Field Reference

## Core Agent Fields

- `name` (string, required): Human-readable name.
- `type` (string, required): `"incoming"` or `"flow"`. Immutable once created.
- `systemPrompt` (string): Complete system instructions guiding the AI behavior.
- `personality` (string): Core persona summary (used in flow agents).
- `voiceTone` (string): Tone guide (e.g. `"friendly, empathetic, professional"`).
- `firstMessage` (string): Spoken immediately upon call answer. Supports dynamic tokens (e.g. `"Hi {first_name}"`).
- `language` (string): Language ISO code (`"en"`, `"hi"`, `"es"`, `"fr"`, `"de"`).
- `llmModel` (string): LLM choice (`"gpt-4o-mini"`, `"gpt-4o"`, `"claude-3-5-sonnet"`).
- `temperature` (float): Creativity tuning (`0.0` to `2.0`, default `0.7`).
- `elevenLabsVoiceId` (string): ElevenLabs Voice ID string.
- `voiceStability` (float): ElevenLabs stability (`0.0` to `1.0`).
- `voiceSimilarityBoost` (float): ElevenLabs clarity/similarity boost (`0.0` to `1.0`).
- `voiceSpeed` (float): Speech rate multiplier (`0.5` to `2.0`).
- `knowledgeBaseIds` (array of strings): UUIDs of linked RAG knowledge documents.
- `transferEnabled` (boolean): Enable live call transfer.
- `transferPhoneNumber` (string): E.164 phone number to transfer call to.
- `transferMessage` (string): Spoken before transfer occurs.
- `detectLanguageEnabled` (boolean): Enable dynamic multi-language switching.
- `endConversationEnabled` (boolean): Allow AI to hang up when goal is reached.
- `appointmentBookingEnabled` (boolean): Enable native calendar integration.
- `maxDurationSeconds` (integer): Auto-hangup limit in seconds.
- `telephonyProvider` (string): `"twilio"`, `"plivo"`, or `"twilio_openai"`.
- `openaiVoice` (string): `"alloy"`, `"echo"`, `"shimmer"`, `"ash"`, `"ballad"`, `"coral"`, `"sage"`, `"verse"`, `"cedar"`, `"marin"`.
