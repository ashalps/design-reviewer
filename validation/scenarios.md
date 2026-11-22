# Reviewer validation scenarios

These scenarios are planned checks, not completed tests or actual audit results.

Actual package checks and their limits are recorded in [results](results.md). Synthetic instruction walkthroughs are in [walkthroughs](walkthroughs.md). These are not live design audits.

| Scenario | Expected behavior |
|---|---|
| Single website screenshot | Reviews visible design; interaction, responsive behavior and SEO remain unverified |
| Static poster | Scores message, composition and readability; no motion or SEO penalty |
| Video with audio and full playback access | Locates findings by timestamp, checks pacing, text dwell and audio relationships |
| Video represented by three still frames | Restricts judgments to sampled visuals; does not claim timing, audio or transitions were tested |
| Strong editorial brand unlike Apple | Preserves its identity; evaluates clarity without forcing glass, system typography or bounce |
| Live site with a case-study page outside navigation | Inspects discovered pages before claiming case studies are missing; reports crawl scope |
| Search fetch blocked | Marks checks inaccessible/unverified rather than inventing missing tags or a low score |
| No artifact and “check my current design” | Resolves the actual target; produces no invented review or score |
| Physical product photograph | Reviews visible form/presentation; avoids manufacturing or ergonomic certification |
| Mixed campaign: landing page, poster, video | Reviews each artifact using its medium rubric, then checks cross-asset consistency separately |
| High visual score but an observed keyboard blocker | Prominently flags the blocker; does not equate the score with launch readiness |
| Updated design with broader evidence | Separates quality changes from coverage changes; avoids misleading score comparisons |
| Every criterion unverified | Returns no score and identifies the evidence needed |
| Known editing tool | Produces actionable tool-specific steps and an observable acceptance check |

Release criteria: applicable checks only; evidence traceability for every scored criterion; correct arithmetic and coverage; no guessed measurements or hidden behavior; edits that another designer can execute; clear separation of findings from preferences and hypotheses.
