export interface DemoQA {
  q: string;
  a: string;
}

export const DEMO_QA: DemoQA[] = [
  {
    q: "How should I structure a hypertrophy week as a natural lifter?",
    a: "Aim for 10–20 hard sets per muscle group per week, split across 2–3 sessions, with 0–3 reps in reserve. Prioritize compound lifts early in the week and accessories later. Sleep ≥7 h and eat ~1.6 g protein/kg body weight to drive recovery.",
  },
  {
    q: "What's the difference between RPE and RIR?",
    a: "RPE (Rate of Perceived Exertion) is a 1–10 scale where 10 = absolute failure. RIR (Reps in Reserve) is the inverse — RIR 2 ≈ RPE 8. RIR tends to be easier to estimate accurately for hypertrophy work; RPE is more common for powerlifting peaking.",
  },
  {
    q: "Should beginners do cardio on lifting days?",
    a: "Low-intensity cardio (zone 2, ~150 bpm) after lifting is fine and helps recovery. Avoid hard intervals same-day same-muscle — they can blunt strength adaptations. 2–3 zone 2 sessions per week is a sweet spot for general health.",
  },
];

export const SUGGESTED_PROMPTS = [
  "How many sets per muscle per week for hypertrophy?",
  "What's a good warmup before a heavy squat day?",
  "Explain mechanical tension vs metabolic stress.",
  "Should I deload, and how often?",
  "Best macro split for a slow cut?",
];

export const DEMO_ANSWER_PREFIX = "Based on the knowledge base:";
