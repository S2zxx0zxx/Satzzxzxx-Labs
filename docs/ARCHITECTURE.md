# Satzzxzxx Labs — umbrella architecture

## Mission / permanent brand decision
Satzzxzxx Labs is the **primary umbrella identity** for the founder's current and future products, original and upstream open-source work, technical journal, research, evidence-based software reviews and collaboration. It is described publicly as an **independent technology studio / initiative**, NOT as an incorporated legal entity unless formally verified.

This website is an index and trust layer, not an OAuth, checkout, database, financial-data, or app production origin. Never merge product authentication, financial data, payments or sensitive user analytics into this static site.

## Information architecture
- Home: existing design and presentation preserved.
- /products/ and /products/<slug>/: public product portfolios; statuses and source links are mandatory.
- /open-source/: actual maintainer contributions, original projects, forks and upstream work with separate attribution.
- /blog/: technical articles; draft/publication boundary; future articles use the same design shell.
- /research/: research and methodology, hypotheses separate from verified results.
- /reviews/: independent app and website review standards, conflict disclosure, corrections; no unverified public accusations.
- /about/: identity and operator boundaries without unverifiable biographies or corporate claims.
- /contact/: verified public Github collaboration intake; no insecure public sensitive-data collection.
- /data/catalog.json: central content/project register and canonical route inventory; schema versioned.
- /sitemap.xml: only eligible published canonical static routes, never drafts.
- /feed.xml: only real, approved articles.

## Repository and organization boundaries
The Pages site currently lives in `S2zxx0zxx/Satzzxzxx-Labs`, hosted under `https://s2zxx0zxx.github.io/Satzzxzxx-Labs/`. Links to `Satzzxzxx-OSS`, `S2zxx0zxx`, and `meshishu` refer to different GitHub owners; ownership is never inferred. Forks are attributed. Future migration to an actual org-owned root Pages site requires an explicit approved move, verified domain, redirect/canonical plan and testing. This implementation does **not** rename, transfer, delete or mirror any project repository.

## Growth without operational overhead
Static HTML/CSS/JavaScript and Python stdlib validation; no analytics cookies, CMS subscription, API key, paid hosting, separate JS framework or contact form backend. A new product gets an explicit catalog entry plus its own readable profile HTML. Technical content gets a factual authored article, catalog status, relevant links, eligible sitemap entry and feed entry if published. Do not auto-publish placeholders or generate many near-identical SEO pages.

## Release gates
1. Existing design CSS and app.js unchanged unless separately reviewed.
2. Run `python3 scripts/verify_site.py` for path, canonical, publication and catalog consistency.
3. PR reviewed and CI green before merging; Pages deployment then verified by live URL.
4. Do not claim official organization affiliation/legal registration without evidence.
5. Re-check product support, repo owners, article claims, external links, corrections and security channels regularly.

## Future scale
When content becomes too large for static hand-edited pages, introduce build-time rendering from a versioned content registry, preserving the current design and canonical URL contracts. A separate CMS is optional only after editorial workload justifies it. Use verified article review states, attribution, citations, accessibility checks and private security disclosure as non-negotiable acceptance criteria.
