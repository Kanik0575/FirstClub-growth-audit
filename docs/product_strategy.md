# Product Strategy Memo

## Question

How should FirstClub improve qualified install-to-first-order conversion and repeat behavior without diluting its quality-first brand into generic discount-led quick commerce?

## Short Answer

Make trust visible earlier, protect it harder, and measure it like a growth loop.

FirstClub's strongest differentiation is not only that users can get groceries in minutes. It is that users believe the products are cleaner, safer, more curated, and more worth trusting. The product should turn that belief into measurable activation, repeat, recovery, category width, and city expansion.

## What Changed After 1M+ Orders

At early stage, the main question is: "Will users try this?"

After 1M+ orders, the sharper question is: "Can FirstClub become a weekly household habit while keeping the quality promise intact?"

That means the growth system should optimize for:

- Qualified activation, not raw installs.
- Trust-led conversion, not blind discounting.
- Issue-free first orders and fast recovery.
- Category-width repeat behavior.
- Contribution LTV:CAC by PIN and city.
- Expansion demand captured before a ClubHouse launches.

## Product Principles

1. **Every onboarding question must change the next screen.**
   If FirstClub asks for diet, household, kids, and trust preferences, the app should immediately show why that data mattered.

2. **Quality proof should be productized, not buried in brand copy.**
   A product card should answer: tested for what, free from what, selected why, sourced from where, and good for whom.

3. **A first-order incentive should create memory.**
   A flat discount is forgettable. A high-quality A2 milk, zero-maida bread, pesticide-free fruit, or clean-label kids snack can become a tangible quality memory.

4. **Operational defects are trust defects.**
   Missing/wrong/spoiled items must be solved with a premium recovery system because FirstClub sells confidence.

5. **Retention should be measured by category width.**
   A user who only buys one premium item is sampling FirstClub. A user who buys across dairy, produce, bakery, staples, and kids food is shifting household habit.

6. **Expansion should be demand-led.**
   Unserviceable PINs should produce apartment-level demand heatmaps, not rage browsing.

## Recommended Roadmap

### Days 0-14: Measurement + Serviceability

- Define north-star tree: qualified first-order users who repeat within 30 days.
- Instrument install, PIN check, serviceability, onboarding, Trust Match, proof card, first order, issue, recovery, category width, and referral events.
- Move PIN/serviceability before full onboarding.
- Create a premium waitlist state for unavailable PINs with apartment request, category intent, product proof, and launch notification.
- Fix obvious conversion leaks: failed search, dead banner taps, and category backtracks.

Success metrics:

- `pin_checked_before_signup_pct`
- `waitlist_submit_rate`
- `search_to_cart_rate`
- `dead_banner_tap_rate`
- `unserviceable_user_negative_feedback_rate`

### Days 15-30: Trust Match + Hero SKU

- Build a "Curated for your household" bridge after onboarding.
- Run Hero SKU trust-unlock vs. flat discount for premium serviceable PINs.
- Segment by household type, diet, trust signals, acquisition channel, city, and PIN tier.
- Add inventory guardrails so the Hero SKU does not create stockout or substitution risk.

Success metrics:

- `onboarding_to_cart_add_rate`
- `time_to_first_cart_add`
- `i2fo_7d`
- `first_order_aov`
- `d7_repeat_rate`
- `incentive_cost_per_first_order`

### Days 31-60: Recovery + Category Width

- Add issue taxonomy for missing, wrong, damaged, spoiled, late, substitution, and subscription/accounting defects.
- Launch instant make-good rules for high-confidence cases.
- Add SLA timers and follow-up prompts after recovery.
- Nudge users from first-order category into complementary categories.

Success metrics:

- `issue_to_resolution_minutes`
- `issue_user_d7_repeat_rate`
- `negative_review_rate_after_issue`
- `categories_in_first_3_orders`
- `d30_repeat_rate`

### Days 61-90: Quality Passport + City Playbook

- Add Quality Passport modules to product cards and PDPs.
- Connect ClubHouse transparency to the app journey.
- Build referral prompts after quality moments, not during cold onboarding.
- Build city-launch scorecards for new markets: micro-market density, apartment demand, supply reliability, defect rate, support readiness, and hero SKU assortment.

Success metrics:

- `quality_passport_expand_rate`
- `premium_sku_card_to_cart_rate`
- `proof_view_to_repeat_rate`
- `referral_invites_per_activated_user`
- `launch_day_first_orders_by_waitlist_pin`

## North-Star Metric

**Qualified first-order users who repeat within 30 days.**

Why this is better than raw first orders:

- Filters out unserviceable installs.
- Rewards conversion that does not destroy trust.
- Keeps retention and operating quality in the same conversation.
- Prevents a discount-heavy acquisition spike from looking like product-market pull.

## Dashboard I Would Build

| Area | Metric | Why |
| --- | --- | --- |
| Serviceability | `serviceable_install_share` | Separates real conversion opportunity from out-of-area curiosity |
| Activation | `serviceable_install_to_first_cart_add` | Measures whether qualified users find value |
| Conversion | `i2fo_7d` | Core activation output |
| Trust | `issue_free_first_order_rate` | Quality promise must survive first delivery |
| Recovery | `issue_user_d7_repeat_rate` | Measures whether FirstClub repairs trust |
| Retention | `categories_in_first_3_orders` | Early household habit proxy |
| Economics | `contribution_ltv_cac_by_pin` | Keeps growth quality honest |

## Why This Should Matter To FirstClub

FirstClub is trying to own a premium trust position in a speed-obsessed market. That is powerful, but fragile. The product experience must repeatedly prove:

- We know what quality means.
- We know why this product is right for your household.
- We will fix it fast if we break your trust.
- We can repeat this city by city without making the experience feel generic.

That is the growth system I would want to help build.
