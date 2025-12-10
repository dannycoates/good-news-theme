# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Good News Theme is a VSCode and Zed editor theme extension featuring light and dark variants with a minimalist color palette emphasizing readability through monochromatic text and subtle color highlights.

The light theme is inspired by newspaper and book print marked up with colored highlighter markers and blue ink pen.

The dark theme is inspired by vintage computer monochrome CRT monitors with an amber tint and warm beiges.

## Commands

```bash
# Package VSCode extension (.vsix file)
npm run package
```

## Architecture

### VSCode Themes
- `themes/Good News-color-theme.json` - Light theme
- `themes/Good News Dark-color-theme.json` - Dark theme

Theme files contain:
- `colors` - UI element colors (editor, tabs, sidebar, etc.)
- `semanticTokenColors` - Language-aware token styling (requires `semanticHighlighting: true`)
- `tokenColors` - TextMate scope-based syntax highlighting

### Zed Theme
- `zed/good-news.json` - Contains both light and dark themes in a single file following Zed's schema

### Icon Theme
- `icons/file-icon-theme.json` - File icon definitions and mappings
- `icons/*.svg` - Icon assets

## Color Palette

The theme uses a 4-shade foreground hierarchy for semantic differentiation:

| Level | Light | Dark | Usage |
|-------|-------|------|-------|
| Primary | `#252627` | `#fceee0` | Definitions, constants, tags, numbers |
| Secondary | `#6c6f72` | `#b2a092` | Variables, types, strings |
| Tertiary | `#9a9a99` | `#908377` | Keywords, operators |
| Subdued | `#bebebd` | `#564c43` | Punctuation, brackets |

**Backgrounds:**
- Light: `#f0f0ef`
- Dark: `#202122`

## Typography Conventions

- **Bold**: Definitions (function declarations, constructors, type definitions)
- **Italic**: Calls/references (function calls, self/this, attributes)
- **Normal**: Everything else

Combined with the 4-shade hierarchy:
- `function.definition` → bold, primary
- `function` (calls) → italic, primary
- `keyword` → normal, tertiary
- `punctuation` → normal, subdued

## Token Scope Reference

See `token-scopes-reference.md` for comprehensive documentation of TextMate scopes, VSCode semantic tokens, and tree-sitter captures used by Zed.
