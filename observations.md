# FirstClub Funnel Teardown — Detailed Observations

> **Date of analysis:** May 2026
> **Device:** Android (Samsung), Bijnor UP PIN (unserviceable) + Bangalore PIN comparison
> **App version:** Latest on Google Play Store

---

## Screen 0: Splash / Login

**What I see:**
- Full-screen dark green splash with FIRSTCLUB logo
- Tagline: "Real quality. Delivered in minutes."
- Login with mobile number (+91 pre-filled)
- "Skip →" in top right corner (small, easy to miss)
- Terms and Privacy Policy checkbox pre-checked

**Growth observations:**
- The "Skip →" button is a good practice (lets users browse first) — one of the few things FirstClub does better than Blinkit here. A Substack reviewer (Disha Bhatia) specifically praised this.
- However, the login screen doesn't explain WHY they need my number. Zepto shows "Get exclusive deals" next to login. FirstClub just asks.
- No social login (Google/Apple) — adds friction for users who don't want to share phone number yet.
- The dark green is distinctive but the splash screen doesn't preview any products. Missed opportunity to show the quality promise visually.

---

## Screen 1: Name Input

**What I see:**
- Progress bar (1 of 5 steps, green)
- Icon of an ID card
- "What should we call you?" with text input
- "Got a referral code? (optional)" link below
- "Continue" button (greyed out until name entered)
- "Skip" in top right

**Growth observations:**
- Asking name first is personal and warm. Good.
- The referral code is buried as a secondary link. If referral is a key acquisition channel (the JD mentions "Program designs like referral, mechanics, and measurement"), this placement severely underperforms.
- Compare to CRED: referral code is prominent with "Get ₹X" reward messaging. FirstClub's "optional" framing discourages input.
- **Opportunity:** If I were a growth intern, I'd test moving the referral code to post-first-order (when the user has experienced quality) rather than pre-onboarding (when they have zero context).

---

## Screen 2: Age Selection

**What I see:**
- "What is your age?"
- Four chips: 18-25 yrs (emoji: person), 26-35 yrs (emoji: briefcase), 36-45 yrs (emoji: house), 46+ yrs (emoji: star)
- "Confirm" button

**Growth observations:**
- The age brackets are clearly designed for household income segmentation. 36-45 = peak earning + kids at home = highest LTV potential. The emojis confirm this: house = settled family.
- But does this data change anything in the app? If not, it's a wasted screen.
- **Hypothesis:** If 36-45 users see "Family Favorites" and 18-25 users see "Quick Meals for One," this screen pays for itself. If everyone sees the same homepage, delete this screen.
- This adds ~5 seconds of friction. At scale, that's thousands of drop-offs.

---

## Screen 3: Gender + Household

**What I see:**
- "We'd love to know more about you"
- Gender: Male / Female / Prefer not to say
- "Who do you order for?" with multi-select: Just me / Flatmates / Spouse / Kids / Pets / Parents / Others
- Progress bar shows 4 of 5 complete

**Growth observations:**
- The household question is HIGH-VALUE for a grocery app. A "Spouse + Kids" user orders differently from "Just me + Flatmates."
- But again — only if it's used downstream.
- "Pets" is interesting — it hints at future category expansion (pet food). Smart forward-thinking, but currently premature if there's no pet category.
- Gender is less useful for grocery. Could be used for marketing copy personalization at most.
- **Opportunity:** The "Kids" signal should trigger a fundamentally different homepage — baby food, pesticide-free vegetables, no-preservative snacks. This is where FirstClub's clean-label promise has the strongest emotional resonance.

---

## Screen 4: Food Habits + Trust Signals

**What I see:**
- "Bring out the foodie in you!"
- "What are your food habits?" multi-select: Vegetarian, Non-Vegetarian, Eggetarian, Vegan, Gluten free, Keto/low carb, High protein
- "What builds your trust in a product?" multi-select: Organic, Palm oil free, Pesticide free, No artificial additives, Hormone free, None of the above
- "Finish Setup" button

**Growth observations:**
- This is the MOST IMPORTANT onboarding screen. It directly maps to FirstClub's banned-ingredients positioning and clean-label differentiation.
- The trust signals (organic, pesticide-free, no additives, hormone-free) are exactly what separates FirstClub from Blinkit/Zepto. If this data personalizes the experience, it's a retention gold mine.
- "None of the above" option for trust signals is revealing — it captures users who don't care about clean-label, which helps FirstClub understand their addressable market.
- **Critical gap:** After selecting "High protein + No artificial additives," I expected the homepage to reflect these choices. It didn't. The homepage was generic.

---

## Screen 5: Homepage — Unserviceable PIN (Bijnor, UP)

**What I see:**
- "Unserviceable" tag in red (top left)
- Address shows "02, Malti Nagar, Bijnor, ..."
- "Refer & Earn" button (top right)
- Search bar with rotating suggestions
- Category pills: All / Mango / Fresh / Milk&Bread / Groceries / Snacks
- **"We're not in your area yet"** banner with "Request your apartment" CTA
- "Meanwhile, take a look around" divider
- Full-screen popup: "Upgrade to high quality protein — No added sugar or preservatives" with Cosmix, Whole Truth, SuperYou Pro products
- "Buy Now" button on popup (can't actually buy)

**Growth observations:**
- The protein popup on a non-serviceable user is actively harmful. I can't buy anything, and you're showing me a promotional popup? This is a Blinkit-style growth hack that doesn't belong here.
- The "Request now" button for waitlist is good — but it should be Step 1 of the entire flow, not Step 6.
- "Meanwhile, take a look around" is an attempt to retain the unserviceable user, but browsing a catalog you can't purchase from creates frustration, not intent.
- **The Fix:** Serviceability check should happen BEFORE phone number input. If unserviceable → show a beautiful waitlist page with "Here's what's waiting for you" product showcase + email/PIN notification. Don't put them through 5 onboarding screens first.

---

## Screen 6-9: Homepage — Browsing Experience (Unserviceable but browsable)

**Breads Section:**
- Sub-categories: Everyday Breads, Whole Wheat, Sourdough, Indian Breads, Artisanal Breads
- Products: The Health Factory Zero Maida Protein Bread (₹85), Member's Pick Protein Bread (₹75, was ₹89)
- "Everyday Breads: The daily essential that never gets old" — good copy

**High Protein Picks:**
- Paneer (56g protein), Milk (25g protein), Yogurt, Bread — with protein callouts
- This is strong category merchandising. The nutrition data IS the differentiation.

**Best of Cheese:**
- Vallombrosa Mozzarella (₹288), Begum Victoria Smoked Gouda (₹637), Dlecta Cream Cheese (₹189)
- Premium SKUs. No "why this is special" context. Just name + price.
- **Opportunity:** Add one-line stories. "Begum Victoria — smoked in small batches in Pondicherry." This is the discovery gap the Substack reviewer identified.

**Vegan Dairy:**
- 137 Degrees Almond Milk (₹429), Health on Plants Chickpea Tofu (₹175), Only Earth Oat Milk (₹266)
- Niche but important. Shown to ALL users — should be prioritized for users who selected "Vegan" in onboarding.

**Newly Launched:**
- Herbs & Co Cheese Garlic Bread (₹99, was ₹125), Butter Garlic Toast (₹69, was ₹95)
- Good discount framing showing old vs. new price.

**All Categories Page (Aisles tab):**
- Left sidebar: Featured / Fruits & Vegetables / Dairy & Eggs / Breads & Bakery / Staples / Snacks & Beverages
- Right content: Brand tiles (Kaara Puram Snacks, Cosmix, Member's Pick, Ice-creams)
- Sub-sections: Mango Junction, Fresh Fruits & Veggies
- This is the navigation structure Blinkit/Zepto uses (split-view). Works well.

**"Your Usuals" Tab (Order Again):**
- "No orders yet. Your previously bought items will show here."
- "Start Shopping" CTA
- **Problem:** Showing an empty primary nav tab on Day 0 makes the app feel hollow. Zepto hides this tab until you have order history. FirstClub should either:
  - Hide it for new users, OR
  - Replace it with "Trending with new members" or "Most reordered items"

---

## Overall Funnel Score

| Dimension | Score (1-10) | Notes |
|-----------|:---:|-------|
| Onboarding friction | 4/10 | Too many steps before value delivery |
| Data collection usefulness | 8/10 | Excellent questions for segmentation |
| Data activation (personalization) | 2/10 | Collected data appears unused |
| Serviceability handling | 2/10 | Critical — check should be Step 0 |
| Homepage merchandising | 7/10 | Strong category depth, good pricing |
| Product storytelling | 4/10 | Minimal context on why products are special |
| First-order incentive | 5/10 | Standard discount — doesn't showcase quality |
| Empty state handling | 3/10 | "Your Usuals" tab feels hollow on Day 0 |
| Brand consistency | 6/10 | Protein popup contradicts curated promise |

**Overall I2FO Readiness: 4.5/10**

The product catalog is excellent. The onboarding data collection is smart. But the bridge between them — personalization, storytelling, and a quality-first first-order experience — is missing. That's the growth opportunity.
