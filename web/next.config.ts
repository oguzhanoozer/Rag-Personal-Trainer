import type { NextConfig } from "next";

// Resolve the backend URL across local dev and Render production.
// - Local dev: API_URL=http://localhost:8000 (set in .env.local)
// - Render production: API_URL comes from `fromService.property: host` and
//   is just the bare service name (e.g. "kinetic-api-i91p"). We append
//   ".onrender.com" and the https:// scheme.
function apiUrl(): string {
  const raw = (process.env.API_URL || "http://localhost:8000").trim();
  if (raw.startsWith("http://") || raw.startsWith("https://")) return raw;
  // Bare host from Render — add suffix if missing
  const host = raw.includes(".") ? raw : `${raw}.onrender.com`;
  return `https://${host}`;
}

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: "/api/ask",
        destination: `${apiUrl()}/api/ask`,
      },
    ];
  },
};

export default nextConfig;
