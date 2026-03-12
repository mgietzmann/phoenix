#!/usr/bin/env bash
# Transcribes an audio file using OpenAI Whisper API.
# Usage: transcribe.sh <audio_file_path>
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: transcribe.sh <audio_file_path>" >&2
  exit 1
fi

FILE="$1"

if [ ! -f "$FILE" ]; then
  echo "Error: File not found: $FILE" >&2
  exit 1
fi

if [ -z "${OPENAI_API_KEY:-}" ]; then
  echo "Error: OPENAI_API_KEY is not set." >&2
  exit 1
fi

RESPONSE=$(curl -s https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "model=whisper-1" \
  -F "response_format=text" \
  -F "file=@$FILE")

echo "$RESPONSE"
