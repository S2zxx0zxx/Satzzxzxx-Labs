# Satzzxzxx Labs — independent technology studio

**Official public site:** https://s2zxx0zxx.github.io/Satzzxzxx-Labs/

Satzzxzxx Labs is the umbrella identity for independent software products, future applications, public open-source work, maintainership, technical articles, research, and evidence-based app/website reviews. This is not a claim that a legal company has been incorporated.

## Explore

- [Products](https://s2zxx0zxx.github.io/Satzzxzxx-Labs/products/): FinCo-Pilot, UNILOOP, OpenXdrive and future verified projects.
- [Open source](https://s2zxx0zxx.github.io/Satzzxzxx-Labs/open-source/): maintained repositories, upstream attribution, contribution standards.
- [Journal](https://s2zxx0zxx.github.io/Satzzxzxx-Labs/blog/): technical articles with a review and publication process.
- [Research](https://s2zxx0zxx.github.io/Satzzxzxx-Labs/research/): technical experiments and evidence.
- [App and website reviews](https://s2zxx0zxx.github.io/Satzzxzxx-Labs/reviews/): methodology, conflicts, corrections.
- [About](https://s2zxx0zxx.github.io/Satzzxzxx-Labs/about/) and [Contact](https://s2zxx0zxx.github.io/Satzzxzxx-Labs/contact/).

## Engineering

The website is a zero-backend GitHub Pages static project using the **existing original** HTML/CSS/JS visual design. New pages reuse the same stylesheet; no framework or paid CMS is required.

Run `python3 scripts/verify_site.py` for local checks before a PR. A GitHub Actions workflow runs this validation on changes and main.

- `data/catalog.json`: versioned source of truth for published routes, current projects, statuses and attribution.
- `docs/ARCHITECTURE.md`: boundaries and future scale.
- `docs/EDITORIAL_POLICY.md`: review and publication process.
- `CONTRIBUTING.md`: maintainer workflow.
- `SECURITY.md`: private vulnerability reporting boundaries.

Draft blog articles are explicitly **noindex** and omitted from the sitemap and feed. No fake case studies, user metrics, endorsements or product-readiness claims are published.

GitHub owner names are not legal entities. Moving repositories or changing the GitHub Pages hostname is outside this release and needs verified permissions and redirects.
