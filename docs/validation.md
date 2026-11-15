# Validation evidence

Validation date: 15 November 2026. Fixtures represent June 2026 and are intentionally frozen. No historical business outcomes are inferred from this validation.

## Recorded local result

Python 3.15.2: **18 tests passed**. Chromium: **8 tests passed**. JavaScript syntax checks and Python compilation passed. The report command reproduced the committed synthetic baseline.

## Automated checks

- `make check`: Python unit/integration tests, HTTP round trips, invalid input, read/export round trip, durable state, stale-write rejection, simultaneous updates and audit-failure rollback; Python compilation; JavaScript syntax checks.
- `npm run test:e2e`: eight Chromium tests covering served brand assets, filters/empty state, responsive layouts at 390/768/1440 px, the domain workflow with reload persistence, and the public showcase.
- `make report`: baseline JSON and CSV generated from the same domain calculations used by the browser.

Domain coverage: Volume, fractional and impossible set counts, weekly session cap, check-in validation and reopening coach review.

## Browser review

The Browser plugin is not available in this environment, so the final review uses the repository Playwright suite and the shared Playwright browser. The core flow was exercised through real forms and buttons against the local Python server. Reload persistence, visible success and rejection messages, record selection and mobile document width were checked. Screenshots are actual rendered pages, not design mockups.

1. Select Emma Vermeer and save a squat session with 3 sets × 8 reps × 40 kg. Weekly logged volume becomes 960 kg.
2. Submit a fictional weekly check-in with sleep, energy and a note. Mark the check-in reviewed as the coach.
3. Reload and select Emma again to verify the session and review state persist. Submit another check-in to reopen review.

See [desktop screenshot](preview.png), [mobile screenshot](mobile.png), and the current [GitHub Actions run](https://github.com/phlppgdfry/gymlabb-platform-spec/actions/workflows/demo.yml). The badge reports the remote result; this document describes the checks, not an invented production certification.

## Final release checks

The final pass adds regression coverage for negative numeric CSV values, formula-leading text and a failed snapshot refresh after a version conflict. The conflict error remains visible, form inputs survive and controls are re-enabled without a script error. The versioned release is linked from the public setup section.

## Limits of the evidence

The suite tests a local single-workspace product with synthetic records. It does not establish external integration reliability, real user outcomes, scale, production security, legal compliance or clinical validity. One trusted workspace demonstrates both coach and client actions. No authentication, tenant isolation, native iOS app, nutrition tracking, billing, notifications, offline mobile sync or HealthKit integration is delivered.
