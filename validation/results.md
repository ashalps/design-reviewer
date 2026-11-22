# Validation results — 1.1.0

Date: 2026-11-22.

## Automated checks

The release process runs the standard-library package validator against the working folder, clean distribution folder and extracted ZIP. It checks required files, local links, skill metadata, eight shared operating contracts, matching category weights, JSON validity, seven score fixtures, four invalid-input cases, shared graphic-design guidance and the fictional example's 74/100 score with 95% coverage.

The release process also compares every archived file byte-for-byte against the clean distribution and verifies the archive file list. The accompanying release-checks.json records the outcome of the completed runs.

## Beginner-path desk check

The README leads with one path: attach general instructions, attach the design/link, paste the request. It then shows expected output with a fictional example and offers category-only choices. Technical validation is explicitly maintainer-only. Relative links are checked in the extracted package, so no working-folder paths are needed.

This is an authoring-agent desk check, not a usability study with new users. The inherited category walkthroughs are synthetic instruction checks, not real-design audits or independent model evaluations.

## Limits

No real design was audited and no cross-model benchmark was run. Actual usefulness and repeatability need a pilot with real designs. The separate installed skill-creator validator previously could not run because its PyYAML dependency was unavailable; the package's standard-library metadata checks run independently. No external dependency was installed.
