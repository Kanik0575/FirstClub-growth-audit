# Experiment Backlog

Scoring model: ICE = Impact x Confidence / Effort.

Each experiment is written like something a growth/product intern could help ship: hypothesis, what ships, primary metric, secondary metrics, and guardrails.

## 1. PIN-First Waitlist 2.0

Hypothesis: Checking PIN before full onboarding reduces a bad trust moment for unserviceable users and improves waitlist intent.

Control: User completes full onboarding before seeing serviceability wall.

Variant: User checks PIN first. If unserviceable, they see a premium waitlist with product proof, launch notification, category-intent capture, and "request my apartment" CTA.

Primary metric: `pin_to_waitlist_submit_rate`

Secondary metrics:

- `pin_checked_before_signup_pct`
- `waitlist_apartment_density`
- `unserviceable_negative_feedback_rate`
- `launch_day_first_orders_from_waitlist`

Guardrails:

- Serviceable onboarding start rate.
- False unavailable PIN rate.
- Notification opt-out rate.

## 2. Trust Match Onboarding Bridge

Hypothesis: Showing a personalized shelf after onboarding increases browse-to-cart conversion because users can see that their preferences changed the app.

Example:

- User selects kids + pesticide-free + no artificial additives.
- Bridge shows fruits, kids snacks, A2 dairy, and breads with proof copy explaining why each item fits.

Primary metric: `onboarding_to_cart_add_rate`

Secondary metrics:

- `time_to_first_cart_add`
- `trust_match_card_click_rate`
- `first_order_aov`
- `d7_repeat_rate`

Guardrails:

- Onboarding skip rate.
- Time to homepage.
- Shelf dismiss rate.

## 3. Hero SKU Trust-Unlock

Hypothesis: A high-quality free SKU creates a stronger first-order memory than a flat discount and can reduce incentive cost.

Control: Rs. 100-150 off first order.

Variant: Free hero SKU added to first cart, such as A2 milk, zero-maida bread, pesticide-free fruit, or clean-label kids snack.

Primary metric: `i2fo_7d`

Secondary metrics:

- `d7_repeat_rate`
- `first_order_aov`
- `hero_sku_repeat_purchase_rate`
- `incentive_cost_per_first_order`

Guardrails:

- Contribution margin per first order.
- Stock availability.
- Substitution rate.
- Abuse/refund risk.

## 4. Quality Passport Cards

Hypothesis: Specific product proof improves conversion for premium-priced SKUs by reducing value doubt.

Variant proof modules:

- "Tested for"
- "Free from"
- "Why this SKU won"
- "Best for"
- "Source or brand story"

Primary metric: `premium_sku_card_to_cart_rate`

Secondary metrics:

- `quality_passport_expand_rate`
- `pdp_view_to_cart_rate`
- `price_comparison_exit_rate`

Guardrails:

- Card clutter.
- PDP bounce.
- Proof freshness and claim accuracy.

## 5. Missing-Item Recovery OS

Hypothesis: Instant make-good for missing/wrong/spoiled items preserves repeat behavior among users who experience a defect.

Product components:

- Issue taxonomy.
- Photo optional but encouraged.
- Instant refund or replacement choice for common cases.
- Visible SLA timer.
- Follow-up after resolution.
- SKU, picker, and ClubHouse-level defect tagging.

Primary metric: `issue_user_d7_repeat_rate`

Secondary metrics:

- `issue_to_resolution_minutes`
- `support_contact_rate_per_order`
- `negative_review_rate_after_issue`
- `reorder_rate_after_resolution`

Guardrails:

- Refund abuse.
- Support cost/order.
- Auto-credit false positives.

## 6. Subscription Ledger

Hypothesis: Transparent membership and wallet accounting reduces negative reviews and support contacts.

Product components:

- Paid balance.
- Used balance.
- Earned gifts.
- Gift eligibility progress.
- Renewal date.
- Cancellation state.
- Refund rules.

Primary metric: `subscription_support_contact_rate`

Secondary metrics:

- `subscription_cancellation_rate`
- `wallet_ledger_view_rate`
- `gift_eligibility_dispute_rate`
- `subscription_review_sentiment`

Guardrails:

- Subscription conversion rate.
- Renewal rate.

## 7. Search Defect Sprint

Hypothesis: Fixing failed search, dead banners, and category backtracks creates immediate conversion lift without incremental discounting.

Product components:

- Top 100 failed queries.
- Dead-banner tap logging.
- Category backtrack tracking.
- Weekly defect burndown with owner and status.

Primary metric: `search_to_cart_rate`

Secondary metrics:

- `zero_result_search_rate`
- `dead_banner_tap_rate`
- `category_backtrack_rate`
- `browse_to_cart_rate`

Guardrails:

- Search latency.
- Irrelevant recommendation rate.

## 8. Category-Width CRM

Hypothesis: Users who buy from 3+ categories in their first 3 orders retain better than users who remain in one category.

Example nudges:

- Bread first order -> butter, cheese, eggs.
- Dairy first order -> fruits, breakfast staples.
- Snacks first order -> high-protein or kids food.
- Produce first order -> staples and oils.

Primary metric: `d30_repeat_rate`

Secondary metrics:

- `categories_in_first_3_orders`
- `second_order_aov`
- `crm_click_to_add_rate`
- `unsubscribe_rate`

Guardrails:

- Discount dependency.
- Push opt-out rate.
- Over-messaging complaints.

## 9. ClubHouse Proof Loop

Hypothesis: Making the ClubHouse concept visible in-app improves trust and repeat among quality-conscious households.

Variants:

- "Packed from your Bellandur ClubHouse" card.
- Hygiene/process video.
- Visit booking CTA.
- Batch or picker proof for fresh produce.

Primary metric: `proof_view_to_repeat_rate`

Secondary metrics:

- `clubhouse_card_click_rate`
- `fresh_produce_repeat_rate`
- `trust_score_after_order`

Guardrails:

- Content fatigue.
- Operational readiness to expose proof.

## 10. Post-Aha Referral

Hypothesis: Referral prompts work better after a quality moment than during cold onboarding.

Trigger moments:

- First 5-star rating.
- First issue-free repeat order.
- Hero SKU reorder.
- Issue resolved with positive feedback.
- Category-width milestone.

Primary metric: `referral_invites_per_activated_user`

Secondary metrics:

- `invite_to_install_rate`
- `referred_i2fo_rate`
- `referred_d30_repeat_rate`

Guardrails:

- Referral discount leakage.
- Low-quality referred installs.
