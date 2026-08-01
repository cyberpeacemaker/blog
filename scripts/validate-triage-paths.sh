#!/bin/bash
set -euo pipefail

# Validate that changed files in a triage diff stay within trusted vault paths.
# Core/ is intentionally excluded — operational rolling docs; see Core/Core.md.
# Usage: validate-triage-paths.sh [base_ref]
#   base_ref defaults to origin/main (compares origin/main..HEAD)

BASE_REF="${1:-origin/main}"

if ! git rev-parse --verify "$BASE_REF" >/dev/null 2>&1; then
  echo "Error: base ref not found: $BASE_REF"
  exit 1
fi

HAS_CHANGES=0

while IFS= read -r -d '' path; do
  HAS_CHANGES=1
  case "$path" in
    Inbox/*.md|00-Meta/*.md|00-Meta/*.canvas|01-NSM-Malcolm/*.md|02-Threat-Hunting-DFIR/*.md|03-AI-Agents/*.md|03-AI-Agents/*/*.md|04-Dev-Environment/*.md|04-Dev-Environment/*/*.md|05-Software-Engineering/*.md|06-Design-Creative/*.md|07-Productivity-Work/*.md|08-Career-Presentations/*.md|09-Personal/*.md|scripts/vault-graph.json|scripts/finish-ai-task.sh|scripts/validate-triage-paths.sh|.github/workflows/triage-validation.yml|.github/workflows/mark-cursor-triage-pr-ready.yml|.github/PULL_REQUEST_TEMPLATE.md)
      ;;
    *)
      echo "Error: File outside trusted triage paths: $path"
      exit 1
      ;;
  esac
done < <(git -c core.quotePath=false diff --name-only -z "$BASE_REF"..HEAD)

if [[ "$HAS_CHANGES" -eq 0 ]]; then
  echo "No changed files between $BASE_REF and HEAD."
  exit 0
fi

echo "All changed files are within trusted triage paths."
