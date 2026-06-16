# Security Notes

Before publishing this repository, verify that no private credentials are committed.

## Do Not Commit

- Hugging Face access tokens
- Google Drive private paths containing personal or institutional information
- API keys
- Cloud credentials
- Large model weights
- Local cache directories

## What Was Cleaned

The uploaded notebooks contained hard-coded Hugging Face tokens. In this GitHub-ready package, token strings were replaced and notebook outputs were cleared.

## Recommended Action

If any token was ever stored in a notebook or shared file, revoke it from the provider account and create a new token.
