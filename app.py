"""
FirstClub Growth OS
===================
A product + growth proof-of-work case study for FirstClub's quality-led
quick-commerce wedge.

Built by Kanik Kumar, CS '27, BITS Pilani.
All company metrics are public-source references or synthetic estimates for
experiment planning. No private FirstClub data is used.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


ROOT = Path(__file__).parent


def money(value: float) -> str:
    return f"Rs. {value:,.0f}"


def pp(value: float) -> str:
    return f"{value:.1f}%"


def signed_money(value: float) -> str:
    sign = "+" if value >= 0 else ""
    return f"{sign}{money(value)}"


def render_card(title: str, body: str, accent: str = "green") -> None:
    st.markdown(
        f"""
        <div class="fc-card fc-card-{accent}">
            <h3>{title}</h3>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_badges(items: list[str]) -> None:
    html = "".join(f'<span class="fc-pill">{item}</span>' for item in items)
    st.markdown(html, unsafe_allow_html=True)


st.set_page_config(
    page_title="FirstClub Growth OS",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
        :root {
            --fc-green: #10382a;
            --fc-green-2: #226048;
            --fc-mint: #e9f4ed;
            --fc-cream: #fbf7ef;
            --fc-amber: #d9822b;
            --fc-blue: #245477;
            --fc-red: #a94442;
            --fc-ink: #17211c;
            --fc-muted: #5b6861;
            --fc-border: #d9e3dd;
        }
        .block-container {
            padding-top: 1.7rem;
            padding-bottom: 2.4rem;
            max-width: 1320px;
        }
        h1, h2, h3 {
            letter-spacing: 0;
        }
        .fc-hero {
            display: grid;
            grid-template-columns: minmax(0, 1.4fr) minmax(260px, 0.7fr);
            gap: 22px;
            align-items: end;
            background: linear-gradient(135deg, #10382a 0%, #1e6046 58%, #245477 100%);
            border-radius: 8px;
            padding: 30px 34px;
            color: #fff;
            margin-bottom: 16px;
            box-shadow: 0 16px 42px rgba(17, 31, 24, 0.16);
        }
        .fc-hero h1 {
            font-size: clamp(2.0rem, 4vw, 3.2rem);
            line-height: 1.02;
            margin: 0 0 10px 0;
            color: #fff;
        }
        .fc-hero p {
            margin: 0;
            color: #edf6f0;
            font-size: 1.02rem;
            line-height: 1.45;
            max-width: 780px;
        }
        .fc-hero-stat {
            border: 1px solid rgba(255,255,255,0.22);
            border-radius: 8px;
            padding: 14px 15px;
            background: rgba(255,255,255,0.09);
            margin-top: 8px;
        }
        .fc-hero-stat strong {
            display: block;
            color: #fff;
            font-size: 1.38rem;
            line-height: 1.1;
        }
        .fc-hero-stat span {
            display: block;
            color: #d8ebe1;
            font-size: 0.82rem;
            margin-top: 4px;
        }
        .fc-pill {
            display: inline-block;
            border: 1px solid rgba(16, 56, 42, 0.18);
            border-radius: 999px;
            padding: 5px 10px;
            margin: 4px 6px 7px 0;
            color: #10382a;
            background: #fbfcfa;
            font-size: 0.82rem;
            font-weight: 650;
        }
        .fc-card {
            border: 1px solid var(--fc-border);
            border-radius: 8px;
            padding: 17px 18px 16px 18px;
            background: #ffffff;
            min-height: 150px;
        }
        .fc-card h3 {
            color: #10382a;
            font-size: 1.02rem;
            margin: 0 0 8px 0;
        }
        .fc-card p {
            color: #46534c;
            margin: 0;
            font-size: 0.94rem;
            line-height: 1.45;
        }
        .fc-card-blue h3 { color: #245477; }
        .fc-card-amber h3 { color: #9b5517; }
        .fc-card-red h3 { color: #a94442; }
        .fc-callout {
            background: #f7fbf8;
            border-left: 5px solid #10382a;
            border-radius: 6px;
            padding: 15px 17px;
            color: #26362e;
            margin: 13px 0;
            line-height: 1.5;
        }
        .fc-warning {
            background: #fff8ed;
            border-left: 5px solid #d9822b;
            border-radius: 6px;
            padding: 15px 17px;
            color: #3f3021;
            margin: 13px 0;
            line-height: 1.5;
        }
        .fc-source {
            font-size: 0.82rem;
            color: #6c786f;
        }
        .metric-container [data-testid="stMetricValue"] {
            color: #10382a;
        }
        div[data-testid="stDataFrame"] {
            border-radius: 8px;
        }
        @media (max-width: 820px) {
            .fc-hero {
                grid-template-columns: 1fr;
                padding: 24px 22px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="fc-hero">
        <div>
            <h1>FirstClub Growth OS</h1>
            <p>
                A board-ready product and growth case study for FirstClub after its
                1M-order scale-up: how to turn quality trust into first orders,
                repeat behavior, better recovery, and stronger city expansion.
            </p>
        </div>
        <div>
            <div class="fc-hero-stat"><strong>1.2M+</strong><span>orders reported by Moneycontrol in Mar 2026</span></div>
            <div class="fc-hero-stat"><strong>2L+</strong><span>customers and Rs. 1,500 AOV reported publicly</span></div>
            <div class="fc-hero-stat"><strong>Week 1</strong><span>job-ready operating assets, not a generic teardown</span></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

render_badges(
    [
        "Built by Kanik Kumar",
        "BITS Pilani CS '27",
        "Research snapshot: May 2026",
        "Public data + synthetic model",
        "Product, growth, ops, CRM",
    ]
)


COMPANY_SIGNALS = pd.DataFrame(
    [
        {
            "Signal": "Current positioning",
            "Public evidence": "Official site frames FirstClub as groceries users do not have to second guess, with trusted/tasted/tested curation, 200+ harmful ingredients left out, and a ClubHouse concept.",
            "Why it matters": "Quality cannot stay as brand copy. It must appear in launch, browse, cart, delivery, and recovery moments.",
            "Source": "FirstClub website",
        },
        {
            "Signal": "Scale reset",
            "Public evidence": "Moneycontrol reported 1.2M+ orders, 15M units shipped, 2L+ customers, roughly Rs. 1,500 AOV, and 45% CMGR.",
            "Why it matters": "At this scale the problem shifts from proving demand to protecting repeat trust and contribution quality.",
            "Source": "Moneycontrol",
        },
        {
            "Signal": "Funding and expansion pressure",
            "Public evidence": "Moneycontrol reported talks to raise USD 50-60M at around a USD 250M valuation, with expansion planned across major Indian cities.",
            "Why it matters": "The operating system needs repeatable city launch playbooks, not one-off growth hacks.",
            "Source": "Moneycontrol",
        },
        {
            "Signal": "Early economics",
            "Public evidence": "TechCrunch reported Rs. 1,050 AOV, 60% repeat purchase, 4,000+ curated SKUs, 60% exclusive products, 70% women customers, and Rs. 15L household income.",
            "Why it matters": "The strongest users are likely household trust buyers. Segment around family, food safety, and premium pantry behavior.",
            "Source": "TechCrunch",
        },
        {
            "Signal": "Android acquisition signal",
            "Public evidence": "AppBrain listed roughly 360k total downloads, 100,000+ Play downloads, and 4.33 rating from about 3k ratings.",
            "Why it matters": "Enough top-of-funnel exists to justify activation, support, and lifecycle experiments instead of only more paid installs.",
            "Source": "AppBrain",
        },
        {
            "Signal": "iOS trust base",
            "Public evidence": "Apple App Store listing shows high rating volume and reviews that praise curated quality while surfacing service, discovery, and subscription pain.",
            "Why it matters": "Reviews are a leading indicator of whether the quality promise survives real operations.",
            "Source": "Apple App Store",
        },
        {
            "Signal": "Product surface maturity",
            "Public evidence": "Recent App Store version notes mention product ratings/recommendations, reorder improvements, and commonly purchased together.",
            "Why it matters": "The app is ready for preference-led personalization and category-width loops, not just static merchandising.",
            "Source": "Apple App Store",
        },
        {
            "Signal": "Category tailwind",
            "Public evidence": "IBEF/CareEdge reported quick-commerce GOV of Rs. 64,000 crore in FY25, projected to reach Rs. 2,00,000 crore by FY28.",
            "Why it matters": "The market is large enough for a premium wedge. FirstClub does not have to win by copying the speed war.",
            "Source": "IBEF",
        },
        {
            "Signal": "Consumer need",
            "Public evidence": "PwC India reported 84% of Indian consumers view food safety as a vital driver.",
            "Why it matters": "Trust communication should be specific, measurable, and repeated in app moments.",
            "Source": "PwC India",
        },
    ]
)


SOURCE_LINKS = {
    "FirstClub website": "https://www.firstclub.co.in/",
    "FirstClub Standard": "https://www.firstclub.site/banned-ingredients",
    "Moneycontrol": "https://www.moneycontrol.com/news/business/startup/firstclub-in-talks-to-raise-50-million-from-peak-xv-sofina-and-others-doubling-valuation-in-under-six-months-13851304.html",
    "Moneycontrol launch": "https://www.moneycontrol.com/news/business/startup/ex-flipkart-execs-firstclub-launches-high-quality-curated-platform-to-target-top-10-of-indian-consumers-13107863.html",
    "TechCrunch": "https://techcrunch.com/2025/09/03/firstclub-bucks-indias-speed-obsession-quickly-triples-valuation-to-120m-with-premium-approach/",
    "IBEF": "https://www.ibef.org/news/quick-commerce-orders-soar-to-rs-64-000-crore-us-7-47-billion-in-fy25-to-touch-rs-2-00-000-crore-us-23-34-billion-by-fy28",
    "PwC India": "https://www.pwc.in/press-releases/2025/84-of-indian-consumers-seek-safer-healthier-food-choices-pwc-report.html",
    "Apple App Store": "https://apps.apple.com/in/app/firstclub-quality-in-minutes/id6744534743",
    "AppBrain": "https://www.appbrain.com/app/firstclub-quality-in-minutes/com.firstclub.app",
}


REVIEW_THEMES = pd.DataFrame(
    [
        {
            "Theme": "Quality and clean-label trust",
            "Sentiment": "Positive",
            "Observed evidence": "Users praise clean food, premium products, organic/fresh options, and curated selection.",
            "Product implication": "Show proof cards, test results, banned-ingredient reasons, and source stories in browse.",
            "Priority": 5,
        },
        {
            "Theme": "Curated discovery",
            "Sentiment": "Positive",
            "Observed evidence": "Some users like that FirstClub feels curated instead of endless.",
            "Product implication": "Lean into editorial shelves and fewer, better choices instead of copying commodity q-commerce.",
            "Priority": 4,
        },
        {
            "Theme": "Missing, wrong, or spoiled items",
            "Sentiment": "Negative",
            "Observed evidence": "Public reviews mention missing items, wrong orders, and rotten produce.",
            "Product implication": "Add picker verification, photo proof, instant make-good, and issue tagging by SKU and ClubHouse.",
            "Priority": 5,
        },
        {
            "Theme": "Support speed and empathy",
            "Sentiment": "Negative",
            "Observed evidence": "Some users complain that customer care is slow or hard to resolve through.",
            "Product implication": "Measure support SLA by defect type and auto-credit common high-confidence cases.",
            "Priority": 5,
        },
        {
            "Theme": "Subscription and wallet clarity",
            "Sentiment": "Negative",
            "Observed evidence": "Reviews call out locked money, gift eligibility, wallet balance, and renewal confusion.",
            "Product implication": "Create a transparent membership ledger: paid, used, gift-earned, expiry, cancellation, and refund rules.",
            "Priority": 4,
        },
        {
            "Theme": "Search, dead taps, and category mapping",
            "Sentiment": "Negative",
            "Observed evidence": "Users report that discovery can be messy and banners do not always behave as expected.",
            "Product implication": "Track failed search, banner dead taps, and category backtracks; fix top defects weekly.",
            "Priority": 4,
        },
        {
            "Theme": "Price/value comparison",
            "Sentiment": "Negative",
            "Observed evidence": "Some reviews compare FirstClub with BigBasket, Amazon, Blinkit, and Instamart on value.",
            "Product implication": "Avoid generic discounting; explain quality premium and use samples to create trust memory.",
            "Priority": 3,
        },
    ]
)


FUNNEL_AUDIT = pd.DataFrame(
    [
        {
            "Stage": "Install / launch",
            "Current risk": "The promise is memorable, but the first viewport does not yet prove it with products or test evidence.",
            "Opportunity": "Use a hero SKU, banned-ingredient proof, or ClubHouse quality story before phone input.",
            "Metric": "launch_to_pin_check",
            "Severity": 3,
        },
        {
            "Stage": "Serviceability",
            "Current risk": "Unserviceable users can complete onboarding before learning they cannot order.",
            "Opportunity": "Move PIN/serviceability before rich onboarding and convert out-of-area users into high-intent waitlist demand.",
            "Metric": "pin_checked_before_signup_pct",
            "Severity": 5,
        },
        {
            "Stage": "Onboarding",
            "Current risk": "Age, household, diet, and trust data may not visibly alter the next screen.",
            "Opportunity": "Show a Trust Match bridge with products that explain why they were chosen.",
            "Metric": "onboarding_to_cart_add_rate",
            "Severity": 5,
        },
        {
            "Stage": "Browse",
            "Current risk": "Premium catalog can still feel like a commodity quick-commerce grid.",
            "Opportunity": "Add concise proof: tested for, free from, source, why this won, best for whom.",
            "Metric": "premium_sku_card_to_cart_rate",
            "Severity": 4,
        },
        {
            "Stage": "First cart",
            "Current risk": "Flat discounting makes FirstClub sound like the players it wants to differentiate from.",
            "Opportunity": "Replace blanket discount with Hero SKU trust-unlock for high-intent cohorts.",
            "Metric": "i2fo_7d",
            "Severity": 4,
        },
        {
            "Stage": "First order ops",
            "Current risk": "Missing/wrong/spoiled items are existential because the brand sells confidence.",
            "Opportunity": "Create premium recovery: picker proof, instant refund/replacement, and issue-to-SKU learning.",
            "Metric": "issue_to_resolution_minutes",
            "Severity": 5,
        },
        {
            "Stage": "Repeat",
            "Current risk": "A one-category user is still sampling, not shifting household habit.",
            "Opportunity": "Move users into three categories by order three with contextual reorder and bundles.",
            "Metric": "categories_in_first_3_orders",
            "Severity": 4,
        },
        {
            "Stage": "Advocacy",
            "Current risk": "Referral too early can feel like a growth ask before the quality moment has landed.",
            "Opportunity": "Trigger referral after the first 5-star delivery, repeat order, or successful recovery.",
            "Metric": "referrals_per_activated_user",
            "Severity": 3,
        },
    ]
)


EXPERIMENTS = pd.DataFrame(
    [
        {
            "Bet": "PIN-first waitlist 2.0",
            "Hypothesis": "Checking PIN before full onboarding reduces bad trust moments and turns unserviceable traffic into expansion demand.",
            "Ships": "PIN gate, apartment request, product proof, launch notification consent.",
            "Primary metric": "pin_to_waitlist_submit_rate",
            "Guardrail": "Lower serviceable onboarding start rate",
            "Impact": 8,
            "Confidence": 8,
            "Effort": 3,
            "Horizon": "0-14 days",
            "Owner": "Growth + Product",
        },
        {
            "Bet": "Trust Match bridge",
            "Hypothesis": "A shelf based on household, diet, and trust signals increases cart-add because the user sees that preferences mattered.",
            "Ships": "Post-onboarding shelf with matched products and reasons.",
            "Primary metric": "onboarding_to_cart_add_rate",
            "Guardrail": "Time to homepage and skipped onboarding rate",
            "Impact": 9,
            "Confidence": 7,
            "Effort": 5,
            "Horizon": "15-30 days",
            "Owner": "Product + Catalog",
        },
        {
            "Bet": "Hero SKU trust-unlock",
            "Hypothesis": "A free high-proof SKU creates stronger memory than flat discount and can lower incentive cost for premium PINs.",
            "Ships": "Cohort-level free SKU in cart, inventory guardrails, repeat tracking.",
            "Primary metric": "i2fo_7d",
            "Guardrail": "Gross margin, substitution, stockout, abuse",
            "Impact": 8,
            "Confidence": 6,
            "Effort": 4,
            "Horizon": "15-30 days",
            "Owner": "Growth",
        },
        {
            "Bet": "Quality Passport cards",
            "Hypothesis": "Specific proof on product cards increases conversion for premium-priced SKUs.",
            "Ships": "Free-from, tested-for, source, why selected, best-for modules.",
            "Primary metric": "premium_sku_card_to_cart_rate",
            "Guardrail": "Card clutter and PDP bounce",
            "Impact": 7,
            "Confidence": 7,
            "Effort": 4,
            "Horizon": "31-60 days",
            "Owner": "Product + Design",
        },
        {
            "Bet": "Missing-item recovery OS",
            "Hypothesis": "Instant make-good preserves second-order conversion among users who experience a defect.",
            "Ships": "Issue taxonomy, auto-refund/replacement, SLA timer, ClubHouse defect learning.",
            "Primary metric": "issue_user_d7_repeat_rate",
            "Guardrail": "Refund abuse and support cost/order",
            "Impact": 9,
            "Confidence": 8,
            "Effort": 6,
            "Horizon": "31-60 days",
            "Owner": "Product + Ops",
        },
        {
            "Bet": "Subscription ledger",
            "Hypothesis": "Transparent membership and wallet accounting reduces negative reviews and support contacts.",
            "Ships": "Ledger for paid, used, gifts, expiry, renewal, cancellation, refund.",
            "Primary metric": "subscription_support_contact_rate",
            "Guardrail": "Subscription conversion rate",
            "Impact": 7,
            "Confidence": 7,
            "Effort": 5,
            "Horizon": "31-60 days",
            "Owner": "Product + Support",
        },
        {
            "Bet": "Search defect sprint",
            "Hypothesis": "Fixing failed search, dead banners, and category backtracks creates immediate conversion lift.",
            "Ships": "Top 100 failed queries, dead-tap logging, weekly defect burndown.",
            "Primary metric": "search_to_cart_rate",
            "Guardrail": "Search latency and irrelevant recommendations",
            "Impact": 6,
            "Confidence": 8,
            "Effort": 3,
            "Horizon": "0-30 days",
            "Owner": "Product + Engineering",
        },
        {
            "Bet": "Category-width CRM",
            "Hypothesis": "Users buying from 3+ categories in first 3 orders retain better than one-category samplers.",
            "Ships": "Next-best-category nudges after first order and reorder bundles.",
            "Primary metric": "d30_repeat_rate",
            "Guardrail": "Unsubscribe rate and discount dependency",
            "Impact": 7,
            "Confidence": 6,
            "Effort": 4,
            "Horizon": "31-60 days",
            "Owner": "CRM + Growth",
        },
        {
            "Bet": "ClubHouse proof loop",
            "Hypothesis": "Visible hygiene and process proof makes the ClubHouse concept a retention asset.",
            "Ships": "Packed-from card, process content, optional visit CTA, picker proof.",
            "Primary metric": "proof_view_to_repeat_rate",
            "Guardrail": "Content fatigue",
            "Impact": 6,
            "Confidence": 5,
            "Effort": 5,
            "Horizon": "61-90 days",
            "Owner": "Brand + Product",
        },
        {
            "Bet": "Post-aha referral",
            "Hypothesis": "Referral works better after a quality moment than during cold onboarding.",
            "Ships": "Referral prompt after 5-star delivery, repeat order, or positive recovery.",
            "Primary metric": "referral_invites_per_activated_user",
            "Guardrail": "Referral discount leakage",
            "Impact": 6,
            "Confidence": 6,
            "Effort": 3,
            "Horizon": "61-90 days",
            "Owner": "Growth",
        },
    ]
)
EXPERIMENTS["ICE"] = (EXPERIMENTS["Impact"] * EXPERIMENTS["Confidence"] / EXPERIMENTS["Effort"]).round(1)


EVENT_TAXONOMY = pd.DataFrame(
    [
        {
            "Event": "app_launch",
            "Properties": "source, campaign, device, city_guess, app_version",
            "Why it matters": "Top-of-funnel quality and release health by acquisition channel.",
        },
        {
            "Event": "pin_checked",
            "Properties": "pin, serviceable, city, clubhouse_id, eta_bucket",
            "Why it matters": "Separates true I2FO from unserviceable curiosity.",
        },
        {
            "Event": "waitlist_requested",
            "Properties": "pin, apartment, intent_category, notification_channel",
            "Why it matters": "Creates city-expansion demand heatmaps.",
        },
        {
            "Event": "onboarding_step_completed",
            "Properties": "step_name, skipped, time_spent_sec, sequence_position",
            "Why it matters": "Quantifies which questions earn their friction.",
        },
        {
            "Event": "trust_signal_selected",
            "Properties": "signal, household_type, diet_type, kids_present",
            "Why it matters": "Enables personalization and cohort recommendations.",
        },
        {
            "Event": "trust_match_card_viewed",
            "Properties": "matched_signal, sku_count, shelf_rank, source_step",
            "Why it matters": "Measures whether users notice the onboarding-to-homepage bridge.",
        },
        {
            "Event": "quality_passport_expanded",
            "Properties": "sku_id, proof_type, category, brand, price_bucket",
            "Why it matters": "Shows which proof increases confidence for premium SKUs.",
        },
        {
            "Event": "hero_sku_added",
            "Properties": "sku_id, treatment, cost, perceived_value, cohort",
            "Why it matters": "Tracks incremental conversion and incentive economics.",
        },
        {
            "Event": "order_issue_reported",
            "Properties": "issue_type, sku_id, order_value, photo_added, clubhouse_id",
            "Why it matters": "Identifies trust-breaking operational defects.",
        },
        {
            "Event": "issue_resolved",
            "Properties": "resolution_type, minutes_to_resolution, credit_amount, agent_type",
            "Why it matters": "Connects service recovery to repeat behavior.",
        },
        {
            "Event": "category_width_milestone",
            "Properties": "categories_count, order_number, first_category, crm_source",
            "Why it matters": "Early proxy for household habit depth and D30 retention.",
        },
        {
            "Event": "referral_prompt_shown",
            "Properties": "trigger, customer_segment, credit_value, order_number",
            "Why it matters": "Moves referral to proven quality moments.",
        },
    ]
)


ROADMAP = pd.DataFrame(
    [
        {
            "Window": "Days 0-14",
            "Workstream": "Measurement",
            "Deliverable": "Define north-star tree, funnel dashboard, serviceability analytics, review taxonomy, and defect taxonomy.",
            "Success signal": "Leadership can see where qualified users drop and what breaks trust.",
        },
        {
            "Window": "Days 0-14",
            "Workstream": "Growth",
            "Deliverable": "Ship PIN-first waitlist and fix top search/dead-banner defects.",
            "Success signal": "Higher waitlist submit rate and search-to-cart rate.",
        },
        {
            "Window": "Days 15-30",
            "Workstream": "Product",
            "Deliverable": "Launch Trust Match bridge for kids/family, high-protein, and clean-label cohorts.",
            "Success signal": "Lift in cart-add and lower time-to-first-cart.",
        },
        {
            "Window": "Days 15-30",
            "Workstream": "Growth",
            "Deliverable": "Run Hero SKU incentive against flat discount in premium PIN cohorts.",
            "Success signal": "I2FO and D7 repeat lift with lower incentive spend/order.",
        },
        {
            "Window": "Days 31-60",
            "Workstream": "Ops/Product",
            "Deliverable": "Missing-item recovery OS with instant make-good, SLA timer, and ClubHouse defect learning.",
            "Success signal": "Faster resolution and better repeat among issue reporters.",
        },
        {
            "Window": "Days 31-60",
            "Workstream": "CRM",
            "Deliverable": "Category-width lifecycle nudges after first order.",
            "Success signal": "More users reach 3 categories by order three.",
        },
        {
            "Window": "Days 61-90",
            "Workstream": "Expansion",
            "Deliverable": "City launch scorecard and micro-market playbook for apartment clusters.",
            "Success signal": "Launch readiness measured before marketing spend scales.",
        },
        {
            "Window": "Days 61-90",
            "Workstream": "Brand/Product",
            "Deliverable": "Quality Passport and ClubHouse proof loop across browse, cart, and post-delivery.",
            "Success signal": "Higher premium SKU conversion and stronger review sentiment.",
        },
    ]
)


LIFECYCLE_JOURNEYS = pd.DataFrame(
    [
        {
            "Cohort": "Installed, no PIN",
            "Trigger": "No PIN check within 12 hours",
            "Message angle": "Check if your home is inside the quality delivery zone.",
            "Action": "Deep link to PIN check",
            "Metric": "pin_check_rate",
        },
        {
            "Cohort": "Unserviceable",
            "Trigger": "PIN unavailable",
            "Message angle": "Vote for your apartment and preview what will launch first.",
            "Action": "Apartment request + category intent",
            "Metric": "waitlist_submit_rate",
        },
        {
            "Cohort": "Onboarded, no cart",
            "Trigger": "No add-to-cart in first session",
            "Message angle": "Your Trust Match picks are ready.",
            "Action": "Open personalized shelf",
            "Metric": "onboarding_to_cart_add_rate",
        },
        {
            "Cohort": "Cart abandoned",
            "Trigger": "Cart idle for 2 hours",
            "Message angle": "Your quality sample is reserved for today.",
            "Action": "Resume cart with Hero SKU",
            "Metric": "cart_to_order_rate",
        },
        {
            "Cohort": "First order delivered issue-free",
            "Trigger": "Delivery + 3 hours",
            "Message angle": "Rate your first quality experience.",
            "Action": "Rating + next-best-category",
            "Metric": "second_order_rate",
        },
        {
            "Cohort": "First order had issue",
            "Trigger": "Issue reported",
            "Message angle": "We will fix this fast.",
            "Action": "Instant refund/replacement choice",
            "Metric": "issue_user_d7_repeat_rate",
        },
        {
            "Cohort": "3+ categories in first 3 orders",
            "Trigger": "Category-width milestone",
            "Message angle": "Invite a household like yours.",
            "Action": "Post-aha referral",
            "Metric": "referral_invites_per_activated_user",
        },
    ]
)


CITY_PLAYBOOK = pd.DataFrame(
    [
        {
            "Step": "Micro-market score",
            "Question": "Which PINs have dense premium households, apartment clusters, school/office adjacency, and food-safety intent?",
            "Output": "PIN priority score and apartment launch list",
        },
        {
            "Step": "Supply promise",
            "Question": "Can the ClubHouse support fresh, dairy, bakery, kids, snacks, and staples with defect rate under target?",
            "Output": "Launch assortment and no-go SKUs",
        },
        {
            "Step": "Trust content",
            "Question": "Which 25 SKUs prove FirstClub's quality difference fastest in this city?",
            "Output": "Hero shelf, sampling plan, and proof copy",
        },
        {
            "Step": "Demand seeding",
            "Question": "Which apartments and communities should receive concierge waitlist + referral campaigns?",
            "Output": "Apartment captain list and WhatsApp/CRM plan",
        },
        {
            "Step": "Launch guardrails",
            "Question": "Are substitutions, missing items, support SLA, and ETA accuracy stable before marketing scales?",
            "Output": "City health dashboard",
        },
    ]
)


PRDS = {
    "Trust Match onboarding bridge": {
        "Problem": "FirstClub collects useful preference data, but the user does not immediately see how that data changes the product experience.",
        "MVP": "After onboarding, show a single personalized shelf with 8-12 SKUs, each tagged with the selected trust signal it satisfies.",
        "User story": "As a parent who selected kids and pesticide-free, I should instantly see safe fruits, kids snacks, dairy, and breads chosen for my household.",
        "Success": "onboarding_to_cart_add_rate, time_to_first_cart_add, first_order_aov, d7_repeat_rate",
        "Guardrail": "Skip rate, time to homepage, over-personalization complaints",
    },
    "Quality Passport": {
        "Problem": "Premium-priced SKUs need more evidence than a product name and discount badge.",
        "MVP": "Add compact proof modules to cards/PDP: tested for, free from, selected why, source, best for.",
        "User story": "As a value-conscious buyer, I should understand why this bread/milk/snack deserves a premium within 3 seconds.",
        "Success": "premium_sku_card_to_cart_rate, quality_passport_expand_rate, price_comparison_exit_rate",
        "Guardrail": "Visual clutter, PDP bounce, SKU proof freshness",
    },
    "Recovery OS": {
        "Problem": "A missing or spoiled item damages FirstClub more than it damages commodity q-commerce because trust is the core promise.",
        "MVP": "Issue taxonomy, photo optional, refund/replacement choice, SLA timer, auto-credit for high-confidence cases.",
        "User story": "As a first-order user with a defect, I should feel FirstClub protected my trust without needing to chase support.",
        "Success": "issue_to_resolution_minutes, issue_user_d7_repeat_rate, negative_review_after_issue_rate",
        "Guardrail": "Refund abuse, support cost/order, false-positive auto-credit",
    },
    "Subscription ledger": {
        "Problem": "Membership or wallet confusion can turn a loyal premium customer into a public detractor.",
        "MVP": "Single ledger with paid, used, earned gift, renewal, cancellation, expiry, and refund states.",
        "User story": "As a member, I should always know what I paid, what I used, what I earned, and what expires.",
        "Success": "subscription_support_contact_rate, cancellation_reason_clarity, review sentiment",
        "Guardrail": "Subscription conversion and renewal rate",
    },
}


with st.sidebar:
    st.header("Simulator controls")
    st.caption("Directional model for activation, retention, incentive spend, and recovery.")

    monthly_installs = st.slider("Monthly new installs", 5_000, 250_000, 75_000, 5_000)
    serviceable_share = st.slider("Serviceable install share", 25, 100, 62, 1)
    onboarding_completion = st.slider("Onboarding completion", 20, 95, 60, 1)
    control_i2fo = st.slider("Control I2FO from onboarded users", 5, 45, 17, 1)
    trust_match_lift = st.slider("Trust Match I2FO lift", 0, 50, 16, 1)
    hero_lift = st.slider("Hero SKU I2FO lift", 0, 60, 18, 1)
    proof_card_lift = st.slider("Quality Passport cart lift", 0, 30, 7, 1)
    cpi = st.number_input("Blended CPI", 10, 300, 70, 5)
    flat_discount = st.number_input("Flat discount cost/order", 0, 500, 120, 10)
    hero_sku_cost = st.number_input("Hero SKU cost/order", 10, 200, 45, 5)
    first_order_aov = st.number_input("Control first-order AOV", 300, 2_500, 1_050, 25)
    variant_aov = st.number_input("Variant first-order AOV", 300, 3_000, 1_200, 25)
    contribution_margin = st.slider("Contribution margin/order", 5, 35, 15, 1)
    control_d30 = st.slider("Control D30 repeat", 5, 70, 34, 1)
    d30_lift = st.slider("Variant D30 repeat lift", 0, 50, 12, 1)
    issue_rate = st.slider("First-order issue rate", 1, 15, 5, 1)
    recovery_lift = st.slider("Recovery repeat lift after issue", 0, 50, 18, 1)
    repeat_orders_90d = st.slider("90-day repeat orders from retained users", 1, 25, 7, 1)


serviceable_installs = int(monthly_installs * serviceable_share / 100)
users_onboarded = int(serviceable_installs * onboarding_completion / 100)

control_first_orders = int(users_onboarded * control_i2fo / 100)
combined_i2fo_lift = (1 + trust_match_lift / 100) * (1 + hero_lift / 100) * (1 + proof_card_lift / 300)
variant_i2fo = min(control_i2fo * combined_i2fo_lift, 95)
variant_first_orders = int(users_onboarded * variant_i2fo / 100)

marketing_spend = monthly_installs * cpi
control_incentive_spend = control_first_orders * flat_discount
variant_incentive_spend = variant_first_orders * hero_sku_cost

control_cac = (marketing_spend + control_incentive_spend) / max(control_first_orders, 1)
variant_cac = (marketing_spend + variant_incentive_spend) / max(variant_first_orders, 1)

control_margin_order = first_order_aov * contribution_margin / 100
variant_margin_order = variant_aov * contribution_margin / 100
variant_d30 = min(control_d30 * (1 + d30_lift / 100), 95)

control_issue_users = int(control_first_orders * issue_rate / 100)
variant_issue_users = int(variant_first_orders * issue_rate / 100)
control_retained = int(control_first_orders * control_d30 / 100)
variant_base_retained = int(variant_first_orders * variant_d30 / 100)
recovered_repeat_users = int(variant_issue_users * (control_d30 / 100) * (recovery_lift / 100))
variant_retained = variant_base_retained + recovered_repeat_users

control_ltv = control_margin_order + (control_d30 / 100) * repeat_orders_90d * control_margin_order
variant_ltv = variant_margin_order + (variant_d30 / 100) * repeat_orders_90d * variant_margin_order
control_ltv_cac = control_ltv / max(control_cac, 1)
variant_ltv_cac = variant_ltv / max(variant_cac, 1)


tab_brief, tab_market, tab_teardown, tab_experiments, tab_simulator, tab_lifecycle, tab_assets = st.tabs(
    [
        "Executive memo",
        "Market & reviews",
        "Product teardown",
        "Growth bets",
        "Simulator",
        "Lifecycle & city",
        "PM artifacts",
    ]
)


with tab_brief:
    st.subheader("Board-ready thesis")
    st.markdown(
        """
        <div class="fc-callout">
        FirstClub's wedge is not speed. It is trusted quality at quick-commerce convenience.
        After crossing the 1M-order scale line, the product-growth problem becomes sharper:
        make quality proof visible before checkout, protect trust after defects, and build
        repeatable city/category loops that do not depend on generic discounting.
        </div>
        """,
        unsafe_allow_html=True,
    )

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.metric("Modeled I2FO lift", f"{variant_i2fo - control_i2fo:.1f} pp")
    with k2:
        st.metric("CAC delta", money(variant_cac - control_cac), delta=f"{money(control_cac)} control")
    with k3:
        st.metric("D30 repeat delta", f"{variant_d30 - control_d30:.1f} pp")
    with k4:
        st.metric("LTV:CAC delta", f"{variant_ltv_cac - control_ltv_cac:.2f}x")

    st.markdown("#### What I would tell the Product/Growth Head")
    b1, b2, b3 = st.columns(3)
    with b1:
        render_card(
            "1. Make trust measurable",
            "Do not let quality stay as a tagline. Instrument quality proof views, issue-free first order rate, recovery repeat, and category-width behavior.",
            "green",
        )
    with b2:
        render_card(
            "2. Spend incentives on memory",
            "A Hero SKU can create a first-order quality memory while costing less than blanket discounting in selected premium PIN cohorts.",
            "amber",
        )
    with b3:
        render_card(
            "3. Treat ops defects as product debt",
            "Missing, wrong, or spoiled items should update SKU, picker, ClubHouse, support, and repeat-risk systems in one loop.",
            "blue",
        )

    st.markdown("#### North-star metric tree")
    metric_tree = pd.DataFrame(
        [
            ["North star", "Qualified first-order users who repeat within 30 days", "Balances acquisition with trust and habit"],
            ["Activation", "Serviceable install to first cart add", "Filters unserviceable installs and measures intent"],
            ["Conversion", "I2FO within 7 days", "Core growth funnel output"],
            ["Trust", "Issue-free first order rate", "Critical for a quality-first brand"],
            ["Recovery", "Issue users who repeat within 7 days after make-good", "Measures whether FirstClub can repair trust"],
            ["Retention", "Categories bought in first 3 orders", "Proxy for household grocery habit depth"],
            ["Economics", "Contribution LTV:CAC by PIN cohort", "Prevents vanity conversion from subsidy-heavy cohorts"],
        ],
        columns=["Layer", "Metric", "Why it matters"],
    )
    st.dataframe(metric_tree, width="stretch", hide_index=True)


with tab_market:
    st.subheader("Fresh public context")
    st.dataframe(COMPANY_SIGNALS, width="stretch", hide_index=True)

    st.markdown("#### Source map")
    for source, link in SOURCE_LINKS.items():
        st.markdown(f"- [{source}]({link})")

    st.markdown("#### Review intelligence")
    col_left, col_right = st.columns([1.05, 1])
    with col_left:
        sentiment_counts = REVIEW_THEMES.groupby("Sentiment").size().reset_index(name="Themes")
        fig = px.pie(
            sentiment_counts,
            names="Sentiment",
            values="Themes",
            color="Sentiment",
            color_discrete_map={"Positive": "#2f6b4f", "Negative": "#a94442"},
            hole=0.48,
        )
        fig.update_layout(height=330, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig, width="stretch")
    with col_right:
        fig2 = px.bar(
            REVIEW_THEMES.sort_values("Priority"),
            x="Priority",
            y="Theme",
            color="Sentiment",
            orientation="h",
            color_discrete_map={"Positive": "#2f6b4f", "Negative": "#a94442"},
        )
        fig2.update_layout(height=330, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig2, width="stretch")

    st.dataframe(REVIEW_THEMES, width="stretch", hide_index=True)
    st.caption(
        "Review themes are manually synthesized from public App Store/AppBrain evidence and app-store snippets. They are not a statistical scrape."
    )


with tab_teardown:
    st.subheader("Install-to-first-order teardown")
    st.dataframe(FUNNEL_AUDIT, width="stretch", hide_index=True)

    st.markdown("#### Severity map")
    fig = px.bar(
        FUNNEL_AUDIT,
        x="Severity",
        y="Stage",
        color="Severity",
        orientation="h",
        color_continuous_scale=["#dceee2", "#d9822b", "#a94442"],
        range_x=[0, 5],
    )
    fig.update_layout(height=405, margin=dict(l=20, r=20, t=30, b=20), coloraxis_showscale=False)
    st.plotly_chart(fig, width="stretch")

    st.markdown("#### App evidence")
    image_rows = [
        ("00_splash_login.jpeg", "Splash/login: quality promise appears, but no concrete product proof yet."),
        ("04_food_trust_preferences_.jpeg", "Trust preferences: high-value segmentation data is collected."),
        ("08_homepage_.jpeg", "Homepage/serviceability: unserviceable users may see the wall after onboarding."),
        ("09_categories_aisles.jpeg", "Aisles: catalog depth is strong; product storytelling can work harder."),
    ]
    cols = st.columns(4)
    for col, (filename, caption) in zip(cols, image_rows):
        path = ROOT / filename
        with col:
            if path.exists():
                st.image(str(path), caption=caption, width="stretch")
            else:
                st.caption(caption)

    st.markdown(
        """
        <div class="fc-warning">
        The product principle I would defend hardest: every extra onboarding question
        must earn its keep by changing what the user sees next. Otherwise it is
        friction disguised as personalization.
        </div>
        """,
        unsafe_allow_html=True,
    )


with tab_experiments:
    st.subheader("Prioritized growth/product bets")
    st.dataframe(
        EXPERIMENTS.sort_values("ICE", ascending=False),
        width="stretch",
        hide_index=True,
    )

    fig = px.scatter(
        EXPERIMENTS,
        x="Effort",
        y="Impact",
        size="Confidence",
        color="Horizon",
        hover_name="Bet",
        text="Bet",
        size_max=36,
        color_discrete_sequence=["#10382a", "#d9822b", "#245477", "#8b3a3a"],
    )
    fig.update_traces(textposition="top center")
    fig.update_layout(height=560, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig, width="stretch")

    st.markdown("#### Experiment brief")
    selected = st.selectbox("Choose a bet", EXPERIMENTS.sort_values("ICE", ascending=False)["Bet"])
    row = EXPERIMENTS[EXPERIMENTS["Bet"] == selected].iloc[0]
    st.markdown(
        f"""
        <div class="fc-card">
            <h3>{row['Bet']} - ICE {row['ICE']}</h3>
            <p><strong>Hypothesis:</strong> {row['Hypothesis']}</p>
            <p><strong>What ships:</strong> {row['Ships']}</p>
            <p><strong>Primary metric:</strong> {row['Primary metric']}</p>
            <p><strong>Guardrail:</strong> {row['Guardrail']}</p>
            <p><strong>Horizon:</strong> {row['Horizon']} | <strong>Owner:</strong> {row['Owner']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


with tab_simulator:
    st.subheader("Activation, retention, and economics simulator")
    st.caption("Directional synthetic model. It shows product-growth thinking, not FirstClub internal numbers.")

    col_a, col_b = st.columns(2)
    with col_a:
        funnel_control = go.Figure(
            go.Funnel(
                y=["Installs", "Serviceable", "Onboarded", "First orders", "D30 repeat"],
                x=[monthly_installs, serviceable_installs, users_onboarded, control_first_orders, control_retained],
                textinfo="value+percent previous",
                marker={"color": ["#6d7f74", "#507c62", "#2f6b4f", "#1f5a40", "#10382a"]},
            )
        )
        funnel_control.update_layout(title="Control: generic first-order discount", height=390, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(funnel_control, width="stretch")
    with col_b:
        funnel_variant = go.Figure(
            go.Funnel(
                y=["Installs", "Serviceable", "Onboarded", "First orders", "D30 repeat"],
                x=[monthly_installs, serviceable_installs, users_onboarded, variant_first_orders, variant_retained],
                textinfo="value+percent previous",
                marker={"color": ["#8c7b65", "#ba8748", "#d9822b", "#e9a249", "#f2bd6d"]},
            )
        )
        funnel_variant.update_layout(title="Variant: Trust Match + Hero SKU + Recovery OS", height=390, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(funnel_variant, width="stretch")

    k1, k2, k3, k4, k5 = st.columns(5)
    with k1:
        st.metric("Extra first orders", f"{variant_first_orders - control_first_orders:,}")
    with k2:
        st.metric("CAC", money(variant_cac), delta=money(variant_cac - control_cac), delta_color="inverse")
    with k3:
        st.metric("Incentive saved", money(control_incentive_spend - variant_incentive_spend))
    with k4:
        st.metric("90D LTV/user", money(variant_ltv), delta=signed_money(variant_ltv - control_ltv))
    with k5:
        st.metric("LTV:CAC", f"{variant_ltv_cac:.2f}x", delta=f"{variant_ltv_cac - control_ltv_cac:.2f}x")

    econ = pd.DataFrame(
        [
            ["Monthly installs", f"{monthly_installs:,}", f"{monthly_installs:,}"],
            ["Serviceable installs", f"{serviceable_installs:,}", f"{serviceable_installs:,}"],
            ["Onboarded users", f"{users_onboarded:,}", f"{users_onboarded:,}"],
            ["I2FO rate", pp(control_i2fo), pp(variant_i2fo)],
            ["First orders", f"{control_first_orders:,}", f"{variant_first_orders:,}"],
            ["First-order issue users", f"{control_issue_users:,}", f"{variant_issue_users:,}"],
            ["D30 repeat rate", pp(control_d30), pp(variant_d30)],
            ["D30 repeat users", f"{control_retained:,}", f"{variant_retained:,}"],
            ["Incentive cost/order", money(flat_discount), money(hero_sku_cost)],
            ["Total incentive spend", money(control_incentive_spend), money(variant_incentive_spend)],
            ["CAC incl. CPI + incentive", money(control_cac), money(variant_cac)],
            ["90D contribution LTV/user", money(control_ltv), money(variant_ltv)],
            ["90D LTV:CAC", f"{control_ltv_cac:.2f}x", f"{variant_ltv_cac:.2f}x"],
        ],
        columns=["Metric", "Control", "Variant"],
    )
    st.dataframe(econ, width="stretch", hide_index=True)

    st.markdown("#### Break-even sensitivity")
    lifts = np.arange(0, 65, 5)
    ratios = []
    for lift in lifts:
        trial_i2fo = min(control_i2fo * (1 + lift / 100) * (1 + trust_match_lift / 100), 95)
        trial_orders = max(int(users_onboarded * trial_i2fo / 100), 1)
        trial_cac = (marketing_spend + trial_orders * hero_sku_cost) / trial_orders
        trial_d30 = min(control_d30 * (1 + d30_lift / 100), 95)
        trial_ltv = variant_margin_order + (trial_d30 / 100) * repeat_orders_90d * variant_margin_order
        ratios.append(trial_ltv / trial_cac)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=lifts,
            y=[control_ltv_cac] * len(lifts),
            mode="lines",
            name="Control",
            line=dict(color="#10382a", dash="dash"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=lifts,
            y=ratios,
            mode="lines+markers",
            name="Hero SKU variant",
            line=dict(color="#d9822b"),
        )
    )
    fig.update_layout(
        title="How much I2FO lift is needed for Hero SKU economics to beat flat discount?",
        xaxis_title="Hero SKU I2FO lift",
        yaxis_title="90D LTV:CAC",
        height=380,
        margin=dict(l=20, r=20, t=50, b=30),
    )
    st.plotly_chart(fig, width="stretch")


with tab_lifecycle:
    st.subheader("Lifecycle CRM and city expansion")
    st.markdown(
        """
        <div class="fc-callout">
        FirstClub's growth loops should be sequenced around moments of trust:
        serviceability, personalization, first quality proof, issue recovery, category width,
        and post-aha referrals.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Lifecycle journeys")
    st.dataframe(LIFECYCLE_JOURNEYS, width="stretch", hide_index=True)

    st.markdown("#### City launch playbook")
    st.dataframe(CITY_PLAYBOOK, width="stretch", hide_index=True)

    st.markdown("#### PIN tier strategy")
    tiers = pd.DataFrame(
        [
            ["Premium family PINs", "High household density, kids, school zones", "Trust Match + kids/food-safety shelf", "Family repeat, category width"],
            ["Young professional PINs", "Office/PG density, high protein, snacks", "Hero SKU + meal/snack discovery", "I2FO, reorder frequency"],
            ["Mixed value PINs", "Higher price comparison, lower trust premium", "Compare sample vs cash discount", "Contribution LTV:CAC"],
            ["New city waitlist PINs", "High apartment requests before launch", "Concierge pre-launch community campaign", "Launch-day first orders"],
        ],
        columns=["PIN cohort", "Signal", "Best treatment", "Primary readout"],
    )
    st.dataframe(tiers, width="stretch", hide_index=True)


with tab_assets:
    st.subheader("PM assets")

    st.markdown("#### Event taxonomy")
    st.dataframe(EVENT_TAXONOMY, width="stretch", hide_index=True)

    st.markdown("#### 30-60-90 day plan")
    st.dataframe(ROADMAP, width="stretch", hide_index=True)

    st.markdown("#### Mini PRD")
    selected_prd = st.selectbox("Choose asset", list(PRDS.keys()))
    prd = PRDS[selected_prd]
    st.markdown(
        f"""
        <div class="fc-card">
            <h3>{selected_prd}</h3>
            <p><strong>Problem:</strong> {prd['Problem']}</p>
            <p><strong>MVP:</strong> {prd['MVP']}</p>
            <p><strong>User story:</strong> {prd['User story']}</p>
            <p><strong>Success metrics:</strong> {prd['Success']}</p>
            <p><strong>Guardrails:</strong> {prd['Guardrail']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
