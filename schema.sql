-- Cloudflare D1 Schema for Kunpengzhi Podcast Analytics & Counters
-- Supports both page views ('view') and future audio track plays ('play')

CREATE TABLE IF NOT EXISTS counters (
  id TEXT PRIMARY KEY,               -- Composite identifier: e.g. "view:/canon/第四期..." or "play:ep04"
  slug TEXT NOT NULL,                -- Page path or episode identifier
  type TEXT NOT NULL DEFAULT 'view', -- Metric type: 'view' (page view) or 'play' (audio play)
  count INTEGER NOT NULL DEFAULT 1,  -- Aggregate counter
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_counters_slug_type ON counters(slug, type);
