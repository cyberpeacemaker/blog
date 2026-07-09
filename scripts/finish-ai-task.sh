#!/bin/bash
set -euo pipefail

# Intended for trusted daily inbox triage runs configured to run on main.
BRANCH_NAME="$(git branch --show-current)"

if [[ "$BRANCH_NAME" != "main" ]]; then
  echo "Error: Direct-push triage must run on main, not: $BRANCH_NAME"
  exit 1
fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "Error: Working tree is dirty. Commit all changes before finishing."
  git status --short
  exit 1
fi

git fetch origin main

REMOTE_HEAD="$(git rev-parse origin/main)"
LOCAL_HEAD="$(git rev-parse HEAD)"
MERGE_BASE="$(git merge-base HEAD origin/main)"

if [[ "$LOCAL_HEAD" != "$REMOTE_HEAD" && "$MERGE_BASE" != "$REMOTE_HEAD" ]]; then
  echo "Error: origin/main has commits that are not in local main. Pull/rebase before pushing."
  exit 1
fi

CHANGED_FILES="$(git diff --name-only origin/main..HEAD)"

if [[ -z "$CHANGED_FILES" ]]; then
  echo "No local commits to push; main is already in sync with origin/main."
  exit 0
fi

while IFS= read -r path; do
  case "$path" in
    Inbox/*.md|00-Meta/*.md|00-Meta/*.canvas|01-NSM-Malcolm/*.md|02-Threat-Hunting-DFIR/*.md|03-AI-Agents/*.md|03-AI-Agents/*/*.md|04-Dev-Environment/*.md|04-Dev-Environment/*/*.md|05-Software-Engineering/*.md|06-Design-Creative/*.md|07-Productivity-Work/*.md|08-Career-Presentations/*.md|09-Personal/*.md|scripts/vault-graph.json)
      ;;
    *)
      echo "Error: Refusing direct push because this file is outside trusted triage paths: $path"
      exit 1
      ;;
  esac
done <<< "$CHANGED_FILES"

git push -u origin main