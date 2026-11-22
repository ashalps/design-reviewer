# Scoring 1.1.0

The operating contract in every standalone reviewer is authoritative. Category weights sum to 100 and are split equally over listed subcriteria. Assess at subcriterion level; do not treat a partially inspected category as fully verified.

Record each subcriterion as observed (rating 0–5), unverified (null rating) or N/A (null rating), with positive weight. Remove N/A weights from applicable weight, retain unverified weights in applicable weight. Only observed weights contribute to score. Use half-up rounding, not language-dependent banker's rounding.

Score = floor(100 × sum(w × r / 5) / observed weight + 0.5).
Coverage = floor(100 × observed weight / applicable weight + 0.5).
Provisional when unrounded coverage <70%. No observed weight: no score. No applicable weight: no coverage.

Example: observed weight 60, earned weight 45, applicable weight 100 → 75/100, 60% coverage, provisional. N/A is excluded, not rewarded. Unknown evidence is not failure.

Comparison requires the same rubric version and shared evidence scope. Show full-scope results separately when coverage differs. Do not compare visual design score directly to a Lighthouse result or average SEO into visual design. Confidence, severity and effort are separate fields.

The validator contains an executable reference calculator and synthetic test cases. Scores remain reasoned editorial judgments, not objective measurements of business success.

