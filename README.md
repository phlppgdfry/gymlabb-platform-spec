# 💪 GymLabb — Fitness Coaching Platform Specification

![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Type](https://img.shields.io/badge/Type-Product%20Specification-purple)
![Domain](https://img.shields.io/badge/Domain-Fitness%20Tech%20%7C%20B2C-green)
![Role](https://img.shields.io/badge/Role-Business%20Analyst%20%7C%20Product%20Owner-blue)

> **Product vision:** GymLabb is a B2C fitness coaching platform connecting individuals with certified coaches. It delivers a structured training, nutrition, and accountability system — combining the personal touch of 1:1 coaching with the scale and convenience of a digital platform.

---

## 📌 Product Overview

**Target users:**
- **Client:** Motivated individuals (25–45) who want structure, accountability, and expert guidance beyond generic fitness apps
- **Coach:** Certified personal trainers managing 10–50 remote clients, currently juggling WhatsApp + spreadsheets + PDFs

**Core problem being solved:**

| For Clients | For Coaches |
|---|---|
| Generic apps don't adapt to their specific goals | Managing 30+ clients via WhatsApp is unsustainable |
| No accountability or expert feedback loop | No centralized platform for programs, check-ins, and billing |
| Nutrition and training are siloed | No visibility into client progress without manual check-in |

---

## 🎯 Product Goals (OKRs)

**Objective 1 — Deliver measurable client results**
- KR1: 70% of active clients report goal progress by Week 8
- KR2: Average client retention > 16 weeks
- KR3: NPS > 45 by Month 6

**Objective 2 — Make coaches 10x more efficient**
- KR1: Coach manages 2x more clients with same time investment
- KR2: < 15 min admin time per client per week (vs ~45 min currently)
- KR3: Coach churn < 5% per quarter

**Objective 3 — Sustainable revenue model**
- KR1: 60% of clients on monthly subscription (vs pay-per-session)
- KR2: Average coach GMV > €2,000/month by Month 6
- KR3: Platform take rate: 15%

---

## 📦 Epic Overview

### EPIC 1 — Training OS

**Goal:** Clients follow personalized training programs; coaches assign, adjust, and review with minimal friction.

| User Story | Priority | Description |
|---|---|---|
| US-T01 | Must | Client views daily workout with sets, reps, rest times, and demo video |
| US-T02 | Must | Client logs completed sets with actual weights/reps |
| US-T03 | Must | Coach creates programs from exercise library (500+ exercises) |
| US-T04 | Must | Coach assigns program to client with start date |
| US-T05 | Should | Client sees progress chart (volume, max weight) per exercise over time |
| US-T06 | Should | Coach receives notification when client completes a session |
| US-T07 | Could | AI suggests program adjustment based on logged performance trend |

**Key acceptance criteria (US-T02):**
- Logging UI completable in < 30 seconds per set
- Autosaves every set (no data loss if app closes)
- Rest timer starts automatically after set logged
- Previous session's weights pre-filled as placeholder

---

### EPIC 2 — Nutrition OS

**Goal:** Clients track macros; coaches set targets and monitor adherence without manual data collection.

| User Story | Priority | Description |
|---|---|---|
| US-N01 | Must | Coach sets daily macro targets per client (protein / carbs / fats / calories) |
| US-N02 | Must | Client logs meals via barcode scan or manual entry |
| US-N03 | Must | Client sees daily macro progress (ring chart) |
| US-N04 | Should | Coach views client's weekly nutrition adherence in dashboard |
| US-N05 | Should | Platform supports multiple nutrition phases (cut / bulk / maintain) |
| US-N06 | Could | AI generates 7-day meal plan matching macro targets |

---

### EPIC 3 — Onboarding & Intake

**Goal:** Client is matched to the right coach and starts their first program within 24 hours of signup.

**7-Step Intake Flow:**

```
Step 1: Goal Selection
        → Fat loss / Muscle gain / Athletic performance / General health

Step 2: Current Situation
        → Training frequency, experience level, available equipment

Step 3: Lifestyle & Constraints
        → Work schedule, injury history, dietary restrictions

Step 4: Metrics
        → Height, weight, age, goal weight / body composition target

Step 5: Coach Matching
        → Algorithm suggests 3 coaches based on specialty + availability

Step 6: Trial Session Booking
        → 30-min intro call with chosen coach (Calendly integration)

Step 7: Program Assignment
        → Coach assigns first program; client gets "welcome kit" email
```

**Acceptance criteria:**
- Intake completable in < 5 minutes
- Progress auto-saved; resumable if app closed
- Coach receives intake summary PDF before intro call
- Client matched within 24 hours of completing intake

---

### EPIC 4 — Community & Retention

**Goal:** Keep clients engaged and accountable beyond the coach-client relationship.

| Feature | Priority | Description |
|---|---|---|
| Weekly check-in | Must | Client answers 5 structured questions (sleep, energy, adherence, mood, note to coach) |
| Milestone badges | Should | Auto-awarded: First session, 4-week streak, 10kg lifted PR, etc. |
| Leaderboard | Could | Opt-in; weekly training volume ranking within coach's client group |
| Push notifications | Must | Smart reminders: workout due, macro goal update, check-in due |
| Coach message | Must | In-app messaging (async); coach can send voice notes |

---

### EPIC 5 — Coach Dashboard

**Goal:** Coach has a single view of all clients, with priority alerts for who needs attention.

**Dashboard components:**

| Component | Data Shown |
|---|---|
| Client list | Name, photo, current phase, last activity, risk flag |
| Attention required | Clients with missed check-ins > 5 days or low adherence |
| Weekly summary | Sessions completed, macros logged, messages received across all clients |
| Program calendar | Who is in what week of which program |
| Revenue | Monthly GMV, upcoming renewals, subscription health |

**Priority flags (auto-generated):**
- 🔴 No activity in 7+ days
- 🟡 Macro adherence < 60% this week
- 🟢 Personal best logged — praise prompt sent to coach

---

## 🔧 Technical Requirements

### Tech Stack Recommendation

| Layer | Solution | Rationale |
|---|---|---|
| Mobile (client) | Swift / SwiftUI (iOS first) | Native performance, haptic feedback, HealthKit integration |
| Mobile (coach) | SwiftUI + iPad layout | Multi-client management benefits from larger screen |
| Backend | Supabase (PostgreSQL + Auth + Realtime) | Row-level security; realtime check-in notifications |
| Payments | RevenueCat | Subscription lifecycle management; StoreKit 2 abstraction |
| Coaching ops | Everfit (white-labeled) | Exercise library, program builder, client management |
| Notifications | APNs (push) + Resend (email) | Standard stack; deliverability focus |
| Analytics | Mixpanel | Event-based; funnel analysis for retention work |

### Non-Functional Requirements

| Requirement | Target |
|---|---|
| App launch time | < 1.5 seconds |
| Workout log sync | < 500ms (optimistic UI) |
| Offline support | Last 7 days of program accessible offline |
| Data security | GDPR compliant; health data encrypted at rest (AES-256) |
| Uptime | > 99.5% (excluding planned maintenance) |

---

## 📁 Repository Structure

```
gymlabb-platform-spec/
│
├── README.md                          ← You are here
├── ProductVision.md                   ← Full vision doc (1-pager for investors)
│
├── epics/
│   ├── EPIC1_Training_OS.md           ← 12 user stories, ACs, wireframe refs
│   ├── EPIC2_Nutrition_OS.md          ← 8 user stories, macro tracking spec
│   ├── EPIC3_Onboarding.md            ← 7-step intake flow, matching algorithm
│   ├── EPIC4_Community.md             ← Retention mechanics, notification spec
│   └── EPIC5_Coach_Dashboard.md       ← Dashboard spec, priority flag logic
│
└── wireframes/
    ├── client_home_screen.md          ← Annotated wireframe description
    ├── workout_logging_flow.md
    ├── coach_dashboard.md
    └── onboarding_flow.md
```

---

## 🗓 Phased Roadmap

| Phase | Scope | Timeline | Success Metric |
|---|---|---|---|
| Phase 1 — MVP | Training OS + Onboarding + Coach Dashboard | Months 1–4 | 10 coaches, 50 clients onboarded |
| Phase 2 — Nutrition | Nutrition OS + Check-in system | Months 5–7 | 70% clients logging macros weekly |
| Phase 3 — Community | Badges + Leaderboard + Push optimization | Months 8–10 | Retention Week 8 > 70% |
| Phase 4 — AI | Smart suggestions + Churn prediction | Months 11–14 | Coach admin time < 15 min/client/week |

---

*Product specification by Philippe Godfroy — Business Analyst / Product Owner Portfolio*
