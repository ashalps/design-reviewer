# Synthetic instruction walkthroughs

Reviewed against version 1.1.0 on 2026-11-22 by the authoring agent. These are desk checks using text-only scenarios, not independent model executions, real screenshots or actual scored design audits. No artifact quality score is assigned.

| Category/input scenario | Instruction path and expected handoff | Desk-check result |
|---|---|---|
| Website: desktop screenshot; no browser/source | Review visible hierarchy; mark mobile, keyboard, semantics, search and performance unverified. Handoff identifies a visible region, never an invented CSS selector. | Explicitly covered by shared evidence rules and website procedure |
| Product UI: booking screen with supplied error state | Trace only visible states; do not infer successful booking. Specify label/error changes with recovery acceptance checks; preserve approved components. | Covered by task/state instructions and required output |
| Poster: approved luxury brand, small-text concern | Assess intended viewing size and brief; use approximate size proposals unless source values exist. Preserve the brand rather than impose system fonts/glass. | Covered by poster procedure and brand safeguards |
| Video: three stills, no audio | Inspect framing/type only; mark dwell time, pacing, captions-versus-speech and audio unverified. Request time mapping before frame-number edits. | Covered by video procedure; no fake timecodes required |
| Brand/logo: wordmark only | Assess supplied rendering; monochrome/small-size performance stays unverified until inspected. No trademark claim. | Covered by logo procedure |
| Presentation: opening and conclusion only | Identify sampled pages; do not assert middle-section narrative or chart accuracy. Handoff requests evidence pages before conclusions about them. | Covered by presentation procedure |
| Packaging: front photograph only | Review visible front hierarchy; unseen panels, dieline, bleed and physical usability remain unverified. | Covered by packaging procedure |
| General vs category: same poster evidence | General and poster use identical contract and weights. General has less medium-specific detail; it must not claim equivalent inspection depth automatically. | Arithmetic/contract parity checked by validator; behavioral equivalence not independently benchmarked |
| RTL campaign with brand mark and mixed digits | Check language order/shaping and directional controls; do not automatically mirror logos or every icon. | Shared rule appears in all eight portable files |
| A/B posters and later revision | Compare shared criteria, justify winner only with evidence, then track changed findings at equivalent scope. | Explicit compare/recheck mode in all portable files |
| No artifact, inaccessible URL or no visual tool | Request artifact or mark checks unverified. Source-only work is labeled; no invented visual score. | Explicit no-evidence policy |
| Strong average with one critical task blocker | Display critical finding independently of numeric average; no launch certification. | Explicit severity rule |

Remaining empirical validation: run the toolkit on actual artifacts in target AI hosts, evaluate editing usefulness with a designer, and measure review consistency across repeated runs. These require real input artifacts and cannot be established by package tests.
