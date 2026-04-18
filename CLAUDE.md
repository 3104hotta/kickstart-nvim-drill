# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is a Neovim drill practice workbook (練習帳) designed to help beginners become intermediate Neovim users. It uses [kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim) as the base configuration.

- **Target**: Neovim beginners progressing to intermediate level
- **Neovim version**: 0.12.1 (latest)
- **Base config**: kickstart.nvim with `Space` as the leader key

## Repository Contents

- `nvim_engineer_reference.md` — Comprehensive Japanese-language reference for kickstart.nvim keybindings, covering movement, editing patterns, Telescope, LSP, Git (gitsigns), and recommended `init.lua` settings
- Drill exercises and sample code files (to be added)

## Key Design Decisions

**Language**: Documentation and drill content is written in Japanese (日本語).

**Scope**: Content is scoped to kickstart.nvim defaults — avoid documenting keybindings or behaviors that require plugins beyond what kickstart.nvim ships with.

**Drill philosophy**: Exercises should be practical and reinforce the "verb + noun" operator/motion pattern central to Vim's editing model. Workflow sections (like the ones in the reference doc) are preferred over isolated keybinding lists.
