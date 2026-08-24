# E.164 Phone Number Formatting Guide

## What is E.164?

E.164 is the international standard format for phone numbers. All phone numbers passed to VoiceOfAI (`toNumber`, `fromNumber`, `phone`, `recipient_phone_number`) MUST be formatted in E.164.

## Structure

A standard E.164 phone number includes:
1. `+` prefix
2. Country calling code
3. Area code (without leading zeroes)
4. Subscriber number

Max total length: 15 digits (excluding `+`).

## Examples

| Region | Input Format | E.164 Standard Format |
|---|---|---|
| **United States / Canada** | `(415) 555-1234` | `+14155551234` |
| **India** | `098765 43210` | `+919876543210` |
| **United Kingdom** | `07911 123456` | `+447911123456` |
| **Australia** | `0412 345 678` | `+61412345678` |
| **Germany** | `030 1234567` | `+49301234567` |

## Validation Rules

- Must begin with `+`
- Contain digits only after `+` (no spaces, hyphens, brackets, or dots)
- Do not include national trunk prefixes (e.g. drop leading `0` in UK/India/Australia)
