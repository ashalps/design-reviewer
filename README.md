# Design Review Studio

Version 1.1.0 — ready-to-share instructions for reviewing designs with an AI assistant.

## Start here — three simple steps

1. Attach [GENERAL-REVIEW.md](GENERAL-REVIEW.md) to your AI chat. If file uploads are unavailable, paste its contents.
2. Attach your design image, PDF or video, or provide its website link. The AI needs the ability to view that type of content.
3. Copy this request:

> Use these instructions to review my design. It is for [audience] and should help them [understand or do something]. Give me a score, explain the most important improvements, and tell me how to make each edit. Preserve my existing brand. Do not change the design yet.

You do **not** need to install anything, run Python or fill in a technical form. If you do not know the audience or goal yet, say so; the AI can clarify what matters.

## What you will receive

- A score out of 100 and the percentage of checks the AI could complete.
- What works well and should be kept.
- The most important improvements, with locations and reasons.
- Practical editing steps and a way to check each improvement.

**A high score with low coverage is incomplete evidence.** For example, a screenshot can show layout, but cannot prove that buttons or keyboard navigation work.

See a [fictional example review](examples/poster-review.md). It illustrates the output; it is not a real design audit or a promise of identical results from every AI.

## Want only one category?

Attach one of these files instead of the general file. Each works on its own:

| Your design | File to use |
|---|---|
| Website or landing page | [Website](categories/website.md) |
| App screens or product interface | [Product UI](categories/product-ui.md) |
| Poster, ad or social graphic | [Poster and social](categories/poster-and-social.md) |
| Video or animation | [Video and motion](categories/video-and-motion.md) |
| Logo or brand identity | [Brand and logo](categories/brand-and-logo.md) |
| Slides, report or document | [Presentation and document](categories/presentation-and-document.md) |
| Physical product or packaging | [Product and packaging](categories/product-and-packaging.md) |

If unsure, use the general file. These are instructions for the AI; you do not need to read every rule yourself.

## Useful follow-up requests

> Compare these two versions using the same criteria. Recommend one and explain why.

> Recheck my updated design against your previous review. Show what improved and what remains.

> Turn the suggested edits into step-by-step instructions for [Figma / Canva / my codebase / my video editor].

> Create a design brief for [idea] using the appropriate category. Do not score it before a design exists.

## Using the whole folder with a coding agent

Give the agent access to this folder and say: “Use SKILL.md to review [design/link].” [SKILL.md](SKILL.md) selects the relevant instructions. Skill discovery and installation differ by host; no automatic installation is included.

The AI's abilities still matter: screenshots need image understanding; a live-site review needs browser access; video pacing and sound need playback/audio access. If it cannot inspect something, it must say so. Optional specialist tools can improve evidence, but no paid tool is required.

## Maintainer information — optional

The package includes [scoring rules](references/scoring.md), [research sources](references/research-sources.md), [review template](templates/review-report.md) and [editing template](templates/builder-handoff.md). The [project brief](templates/project-brief.json) is optional and intended for repeat workflows.

To validate the package, open a terminal in this folder and run `python3 scripts/validate-package.py`, or `py scripts/validate-package.py` on Windows with Python installed. Only the Python standard library is needed. This is a maintainer check, not a setup step for users.

See [validation results](validation/results.md) for the checks actually run and their limits. Automated package checks do not prove subjective design quality or consistency across AI models.

Five foundations inform this toolkit: Ashal Design Checker, Apple Design, Animation Vocabulary, SEO/GEO/AEO and Graphic Design Thinking. Original source skills remain unchanged. This folder does not publish, install or automatically edit your designs.
