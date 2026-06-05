"use client";

import { useState, useRef, useEffect } from "react";
import {
  Zap,
  Send,
  Loader2,
  RotateCcw,
  Sparkles,
  Dumbbell,
  Database,
  MessageSquareText,
  ArrowDown,
} from "lucide-react";
import { DEMO_QA, SUGGESTED_PROMPTS, DEMO_ANSWER_PREFIX } from "@/lib/demoData";

interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
}

export default function Page() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [demoMode, setDemoMode] = useState(false);
  const endRef = useRef<HTMLDivElement>(null);
  const composerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const send = async (text: string) => {
    const trimmed = text.trim();
    if (!trimmed || loading) return;

    const userMsg: ChatMessage = {
      id: `u-${Date.now()}`,
      role: "user",
      content: trimmed,
    };
    setMessages((m) => [...m, userMsg]);
    setInput("");
    setLoading(true);

    if (demoMode) {
      setTimeout(() => {
        const match = DEMO_QA.find((d) =>
          trimmed.toLowerCase().includes(d.q.toLowerCase().split(" ")[2] || "")
        );
        const answer = match
          ? match.a
          : `${DEMO_ANSWER_PREFIX} this is a cached demo response. For live answers, run the FastAPI backend with an OPENAI_API_KEY.`;
        setMessages((m) => [
          ...m,
          { id: `a-${Date.now()}`, role: "assistant", content: answer },
        ]);
        setLoading(false);
      }, 700);
      return;
    }

    try {
      const r = await fetch("/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: trimmed }),
      });
      if (!r.ok) throw new Error(`Request failed: ${r.status}`);
      const data = await r.json();
      setMessages((m) => [
        ...m,
        { id: `a-${Date.now()}`, role: "assistant", content: data.answer },
      ]);
    } catch (e) {
      setMessages((m) => [
        ...m,
        {
          id: `e-${Date.now()}`,
          role: "assistant",
          content:
            "Couldn't reach the backend. Switch to demo mode (button below) or start the FastAPI server.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const isEmpty = messages.length === 0;
  const scrollToComposer = () => composerRef.current?.scrollIntoView({ behavior: "smooth" });

  return (
    <div className="flex flex-col min-h-screen">
      <Nav
        demoMode={demoMode}
        onToggleDemo={() => setDemoMode((v) => !v)}
        onHome={() => {
          setMessages([]);
          setInput("");
          setDemoMode(false);
          if (typeof window !== "undefined") {
            window.scrollTo({ top: 0, behavior: "smooth" });
          }
        }}
      />

      <main className="flex-1 max-w-3xl mx-auto w-full px-4 py-8 flex flex-col gap-6">
        {isEmpty ? (
          <Hero
            onPick={send}
            onTryDemo={() => {
              setDemoMode(true);
              setTimeout(() => send(SUGGESTED_PROMPTS[0]), 50);
            }}
            scrollDown={scrollToComposer}
          />
        ) : (
          <>
            <div className="space-y-4 mb-2">
              {messages.map((m) => (
                <Bubble key={m.id} role={m.role}>
                  {m.content}
                </Bubble>
              ))}
              {loading && (
                <Bubble role="assistant">
                  <span className="inline-flex items-center gap-2 text-[var(--muted)]">
                    <Loader2 className="w-3.5 h-3.5 animate-spin text-[var(--brand-600)]" />
                    Thinking…
                  </span>
                </Bubble>
              )}
              <div ref={endRef} />
            </div>
          </>
        )}

        <Composer
          ref={composerRef}
          input={input}
          onChange={setInput}
          onSend={() => send(input)}
          loading={loading}
          demoMode={demoMode}
          onReset={() => setMessages([])}
          showReset={!isEmpty}
        />
      </main>

      <Footer />
    </div>
  );
}

function Nav({
  demoMode,
  onToggleDemo,
  onHome,
}: {
  demoMode: boolean;
  onToggleDemo: () => void;
  onHome: () => void;
}) {
  return (
    <nav className="border-b border-[var(--border)] bg-[var(--surface)]/80 backdrop-blur-md sticky top-0 z-40">
      <div className="max-w-3xl mx-auto px-4 h-16 flex items-center justify-between">
        <button
          onClick={onHome}
          className="flex items-center gap-2.5 group focus:outline-none focus-visible:ring-2 focus-visible:ring-[var(--brand-500)] rounded-lg p-1 -m-1"
          aria-label="Back to home"
          type="button"
        >
          <div className="w-9 h-9 rounded-xl bg-[var(--foreground)] text-[var(--brand-300)] flex items-center justify-center group-hover:scale-105 transition-transform">
            <Zap className="w-5 h-5" fill="currentColor" />
          </div>
          <div className="leading-tight text-left">
            <div className="font-display text-xl group-hover:text-[var(--brand-700)] transition-colors">Kinetic</div>
            <div className="text-[10px] uppercase tracking-[0.18em] text-[var(--muted-2)]">
              RAG personal trainer
            </div>
          </div>
        </button>
        <button
          onClick={onToggleDemo}
          className={`text-xs font-semibold px-3 py-1.5 rounded-full transition-all ${
            demoMode
              ? "bg-[var(--brand-100)] text-[var(--brand-700)]"
              : "bg-transparent text-[var(--muted)] hover:bg-[var(--surface-2)]"
          }`}
        >
          {demoMode ? "● Demo mode" : "Demo mode off"}
        </button>
      </div>
    </nav>
  );
}

function Hero({
  onPick,
  onTryDemo,
  scrollDown,
}: {
  onPick: (s: string) => void;
  onTryDemo: () => void;
  scrollDown: () => void;
}) {
  return (
    <div className="text-center py-8 fade-up">
      <p className="text-xs uppercase tracking-[0.22em] text-[var(--brand-600)] font-semibold mb-4">
        ✦ Retrieval-augmented coach
      </p>
      <h1 className="font-display text-5xl md:text-6xl leading-[0.95] mb-5">
        Train with answers
        <br />
        <span className="text-[var(--brand-600)]">that have receipts.</span>
      </h1>
      <p className="text-[var(--muted)] max-w-md mx-auto mb-8 leading-relaxed">
        Ask anything about training, recovery and nutrition. Kinetic grounds every
        answer in a curated knowledge base — no &ldquo;as a large language model&rdquo; vibes.
      </p>

      <div className="flex items-center justify-center gap-2 flex-wrap mb-10">
        <button
          onClick={onTryDemo}
          className="inline-flex items-center gap-2 bg-[var(--foreground)] hover:bg-[var(--brand-700)] text-white px-5 py-2.5 rounded-full text-sm font-medium transition-all shadow-md"
        >
          <Sparkles className="w-3.5 h-3.5" />
          See demo
        </button>
        <button
          onClick={scrollDown}
          className="inline-flex items-center gap-2 bg-transparent border border-[var(--border-strong)] hover:border-[var(--brand-500)] text-[var(--foreground)] px-5 py-2.5 rounded-full text-sm font-medium transition-all"
        >
          Ask anything <ArrowDown className="w-3.5 h-3.5" />
        </button>
      </div>

      {/* Suggested prompts */}
      <div className="flex flex-wrap gap-2 justify-center">
        {SUGGESTED_PROMPTS.map((p) => (
          <button
            key={p}
            onClick={() => onPick(p)}
            className="text-xs text-[var(--muted)] hover:text-[var(--brand-700)] bg-[var(--surface)] hover:bg-[var(--brand-50)] border border-[var(--border)] px-3 py-1.5 rounded-full transition-all"
          >
            {p}
          </button>
        ))}
      </div>

      {/* Process strip */}
      <div className="mt-14 grid grid-cols-3 gap-3 fade-up-2">
        {[
          { icon: MessageSquareText, label: "Ask", desc: "Plain-language question" },
          { icon: Database, label: "Retrieve", desc: "Pull from knowledge base" },
          { icon: Dumbbell, label: "Answer", desc: "Grounded, practical reply" },
        ].map((s) => (
          <div
            key={s.label}
            className="bg-[var(--surface)] border border-[var(--border)] rounded-xl p-4 text-left"
          >
            <s.icon className="w-4 h-4 text-[var(--brand-600)] mb-2" />
            <div className="font-semibold text-sm text-[var(--foreground)]">{s.label}</div>
            <div className="text-xs text-[var(--muted)] mt-0.5">{s.desc}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

function Bubble({ role, children }: { role: "user" | "assistant"; children: React.ReactNode }) {
  const isUser = role === "user";
  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div className={`max-w-[85%] flex flex-col gap-1.5 ${isUser ? "items-end" : "items-start"}`}>
        {!isUser && (
          <span className="text-[10px] uppercase tracking-[0.18em] font-semibold text-[var(--brand-600)] pl-1">
            Coach
          </span>
        )}
        <div
          className={`rounded-2xl px-4 py-3 text-sm leading-relaxed ${
            isUser
              ? "bg-[var(--foreground)] text-white rounded-br-sm shadow-md"
              : "bg-[var(--surface)] border border-[var(--border)] text-[var(--foreground)] shadow-sm rounded-bl-sm"
          }`}
        >
          {children}
        </div>
      </div>
    </div>
  );
}

interface ComposerProps {
  input: string;
  onChange: (s: string) => void;
  onSend: () => void;
  loading: boolean;
  demoMode: boolean;
  onReset: () => void;
  showReset: boolean;
}

import { forwardRef } from "react";

const Composer = forwardRef<HTMLDivElement, ComposerProps>(function Composer(
  { input, onChange, onSend, loading, demoMode, onReset, showReset },
  ref
) {
  return (
    <div ref={ref} className="sticky bottom-4 fade-up-3">
      <div className="bg-[var(--surface)] border border-[var(--border-strong)] rounded-2xl shadow-[var(--shadow-soft)] p-3">
        {showReset && (
          <div className="flex justify-end mb-1">
            <button
              onClick={onReset}
              className="inline-flex items-center gap-1.5 text-xs text-[var(--muted)] hover:text-[var(--brand-700)] px-2 py-1"
            >
              <RotateCcw className="w-3 h-3" />
              New session
            </button>
          </div>
        )}
        <div className="flex items-end gap-3">
          <textarea
            value={input}
            onChange={(e) => onChange(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                onSend();
              }
            }}
            rows={1}
            placeholder={
              demoMode
                ? "Demo mode — try a question from above"
                : "Ask the coach anything — sets, recovery, nutrition…"
            }
            className="flex-1 resize-none outline-none text-sm bg-transparent placeholder:text-[var(--muted-2)] px-2 py-2 max-h-28"
            style={{ minHeight: "28px" }}
            onInput={(e) => {
              const t = e.target as HTMLTextAreaElement;
              t.style.height = "auto";
              t.style.height = `${Math.min(t.scrollHeight, 112)}px`;
            }}
          />
          <button
            onClick={onSend}
            disabled={!input.trim() || loading}
            className={`w-10 h-10 rounded-xl flex items-center justify-center shrink-0 transition-all ${
              input.trim() && !loading
                ? "bg-[var(--foreground)] hover:bg-[var(--brand-700)] text-white"
                : "bg-[var(--surface-2)] text-[var(--muted-2)] cursor-not-allowed"
            }`}
            aria-label="Send"
          >
            {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
          </button>
        </div>
        <p className="text-[10px] text-[var(--muted-2)] mt-1.5 pl-2">
          Enter to send · Shift+Enter for newline
        </p>
      </div>
    </div>
  );
});

function Footer() {
  return (
    <footer className="border-t border-[var(--border)] py-6">
      <div className="max-w-3xl mx-auto px-4 flex items-center justify-between text-xs text-[var(--muted)]">
        <span>
          <span className="font-display text-sm">Kinetic</span> · RAG personal trainer
        </span>
        <span>FastAPI · OpenAI · Next.js</span>
      </div>
    </footer>
  );
}
