# FirstClub Growth OS

**A product + growth proof-of-work case study for FirstClub's install-to-first-order, trust, retention, and city-expansion engine.**

Built by **Kanik Kumar, CS '27, BITS Pilani** as a public product-growth case study.

> FirstClub's hard problem is not just faster grocery delivery. It is making quality feel trustworthy at quick-commerce frequency.
>
> This project is what I would want to contribute in Week 1: identify the highest-leverage trust gaps, turn them into measurable experiments, and connect product decisions to retention, recovery, and unit economics.

---

## Live Project

- **Streamlit app:** https://firstclub-growth-audit-banzuk7s95qjwqyataqdfs.streamlit.app
- **GitHub:** https://github.com/Kanik0575/FirstClub-growth-audit

---

## What Changed In This Version

This version upgrades the project from a funnel teardown into a fuller **Growth OS**:

- Fresh May 2026 public research, including FirstClub's reported 1.2M+ orders, 15M units, 2L+ customers, Rs. 1,500 AOV, funding/expansion signals, App Store evidence, and AppBrain Android signal.
- A 1M-order scale diagnosis: the problem is no longer only trial; it is trust, repeat, recovery, and city playbook repeatability.
- A richer Streamlit app with tabs for executive memo, market/reviews, product teardown, experiment portfolio, simulator, lifecycle/city expansion, and PM assets.
- Prioritized experiments with hypotheses, what ships, primary metrics, guardrails, owners, horizons, and ICE scores.
- A simulator connecting activation, first-order conversion, D30 repeat, recovery, incentive spend, CAC, and contribution LTV:CAC.
- PM artifacts: event taxonomy, 30-60-90 day roadmap, mini PRDs, lifecycle CRM, and city launch playbook.

---

## Core Thesis

FirstClub's wedge is **trusted quality at quick-commerce convenience**.

Public positioning, app-store reviews, and reported business metrics all point in the same direction:

- The brand promise is quality-first, with 200+ harmful ingredients left out and stronger ingredient/product verification.
- Reported customer economics are meaningfully different from commodity quick commerce: public reporting cites 1.2M+ orders, 2L+ customers, Rs. 1,500 AOV, and strong monthly growth.
- Reviews praise clean-label quality and curation, but negative reviews cluster around missing items, support speed, subscription/accounting clarity, search/discovery friction, and price/value comparison.

The product opportunity:

> Make quality trust visible before the first checkout, then protect that trust after the first order.

---

## What This Repo Includes

| File | Purpose |
| --- | --- |
| `app.py` | Interactive FirstClub Growth OS: research, review intelligence, funnel teardown, experiment portfolio, simulator, lifecycle/city playbook, and PM assets |
| `observations.md` | Original screen-by-screen teardown from the FirstClub onboarding and browse journey |
| `docs/market_research.md` | Public research synthesis with source links |
| `docs/product_strategy.md` | Product/growth strategy memo |
| `docs/experiment_backlog.md` | Prioritized experiment briefs |
| `requirements.txt` | Python dependencies |
| `*.jpeg` | App screenshots used as funnel evidence |

---

## The Growth Bets

1. **PIN-first waitlist 2.0**
   Move serviceability before rich onboarding. Turn unavailable PINs into expansion demand, not frustration.

2. **Trust Match onboarding bridge**
   Use household, diet, and trust-signal data to show a personalized shelf before the generic homepage.

3. **Hero SKU trust-unlock**
   Test a free, high-proof SKU against a flat first-order discount for premium PIN cohorts.

4. **Quality Passport cards**
   Productize proof on cards and PDPs: tested for, free from, source, selected why, and best for.

5. **Missing-item recovery OS**
   Treat defects as product moments. Missing/wrong/spoiled items should trigger fast make-good and learning loops.

6. **Subscription ledger**
   Make paid, used, earned, gift, expiry, renewal, and refund states transparent.

7. **Search defect sprint**
   Track failed searches, dead banner taps, and category backtracks; fix the top defects weekly.

8. **Category-width CRM**
   Move users from one trusted category into three categories by order three.

---

## Run Locally

```bash
git clone https://github.com/Kanik0575/FirstClub-growth-audit
cd FirstClub-growth-audit
pip install -r requirements.txt
streamlit run app.py
```

---

## Public Sources Used

- [FirstClub official website](https://www.firstclub.co.in/)
- [FirstClub Standard / banned ingredients](https://www.firstclub.site/banned-ingredients)
- [Moneycontrol: FirstClub funding, orders, customers, AOV, expansion](https://www.moneycontrol.com/news/business/startup/firstclub-in-talks-to-raise-50-million-from-peak-xv-sofina-and-others-doubling-valuation-in-under-six-months-13851304.html)
- [Moneycontrol: FirstClub launch and positioning](https://www.moneycontrol.com/news/business/startup/ex-flipkart-execs-firstclub-launches-high-quality-curated-platform-to-target-top-10-of-indian-consumers-13107863.html)
- [TechCrunch: FirstClub Series A and operating metrics](https://techcrunch.com/2025/09/03/firstclub-bucks-indias-speed-obsession-quickly-triples-valuation-to-120m-with-premium-approach/)
- [IBEF / CareEdge quick commerce market data](https://www.ibef.org/news/quick-commerce-orders-soar-to-rs-64-000-crore-us-7-47-billion-in-fy25-to-touch-rs-2-00-000-crore-us-23-34-billion-by-fy28)
- [PwC India Voice of the Consumer 2025](https://www.pwc.in/press-releases/2025/84-of-indian-consumers-seek-safer-healthier-food-choices-pwc-report.html)
- [Apple App Store listing and reviews](https://apps.apple.com/in/app/firstclub-quality-in-minutes/id6744534743)
- [AppBrain Android listing](https://www.appbrain.com/app/firstclub-quality-in-minutes/com.firstclub.app)

---

## Important Note

This is a public-data project. The simulator uses directional assumptions to show product and growth reasoning. It does **not** claim access to FirstClub's internal funnel, cost, retention, or customer data.
