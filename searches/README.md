# searches

Ranked role-search shortlists produced by the `/find-roles` skill, one file per run:
`searches/<YYYY-MM-DD>.md` (with a `-2`, `-3` suffix for multiple runs in a day).

Each file lists live, currently-open roles that fit the master profile — **full-time and
part-time / contract / fractional**, each labeled by type — sorted best-fit first, with a
quick Fit band, a knockout scan, and a `/tailor-resume <url>` next-step for each.
Knockouts and weak fits are separated into a "Screened out" section.

Run a search from a Claude Code session opened on this repo:

```
/find-roles                       # full default profile (remote US + Colorado), full-time + contract
/find-roles remote HubSpot ops    # or pass filters: titles, location, comp, stage, tool
/find-roles fractional contract   # or narrow to part-time / contract / fractional work
```

Pick the strongest matches and hand them to `/tailor-resume` to build the application.
