---
name: voice-transcribe
description: Transcribes audio files to text using OpenAI Whisper. Activate automatically whenever a file path with an audio extension is referenced (.mp3, .m4a, .wav, .ogg, .flac, .webm, .mp4, .mpeg, .mpga) — transcribe first, then consume the result as you would any text content.
compatibility: Requires curl and OPENAI_API_KEY in the environment.
metadata:
  author: marcelgietzmann-sanders
  version: "1.0"
allowed-tools: Bash
---

# Voice Transcribe

## When to activate

Activate this skill automatically when:
- The user references a file path with an audio extension: `.mp3`, `.m4a`, `.wav`, `.ogg`, `.flac`, `.webm`, `.mp4`, `.mpeg`, `.mpga`
- The user asks you to "listen to", "transcribe", or "read" a voice recording or audio file

Do not wait to be asked. Transcribe first, then proceed as if you had read the content directly.

## How to transcribe

Run the bundled script with the audio file path:

```bash
.claude/skills/voice-transcribe/scripts/transcribe.sh <path_to_audio_file>
```

The script outputs the transcription as plain text to stdout.

## After transcription

Present the content naturally — do not announce "I transcribed this" or wrap it in ceremony. Treat the transcript as the content of the file, exactly as you would treat a text file the user asked you to read. If the user asked a question about the recording, answer it using the transcript.

## Error handling

- If `OPENAI_API_KEY` is not set, try sourcing `~/.bashrc` or `~/.zshrc` first (e.g., `source ~/.bashrc && ...`), then re-run. Only tell the user and stop if the key is still missing after sourcing.
- If the file does not exist, tell the user and stop.
- If the API returns an error, show the response and stop — do not retry automatically.
