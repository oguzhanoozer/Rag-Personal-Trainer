import type { NextConfig } from "next";

// Render's fromService returns the bare host (e.g. kinetic-api.onrender.com).
// Locally we run http://localhost:8000.
function apiUrl(): string {
  const raw = process.env.API_URL || "http://localhost:8000";
  if (raw.startsWith("http://") || raw.startsWith("https://")) return raw;
  return `https://${raw}`;
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
