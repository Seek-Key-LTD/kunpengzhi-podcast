export interface Env {
  DB?: D1Database;
  ASSETS: Fetcher;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    // API: /api/counter
    if (url.pathname === '/api/counter') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      if (!env.DB) {
        return Response.json(
          {
            error: 'D1 database binding "DB" is not configured yet in wrangler.toml',
            count: 0,
          },
          { status: 200, headers: corsHeaders }
        );
      }

      try {
        if (request.method === 'POST') {
          let body: { slug?: string; type?: string } = {};
          try {
            body = await request.json();
          } catch {
            // fallback
          }

          const rawSlug = body.slug || url.searchParams.get('slug') || '/';
          const type = body.type || url.searchParams.get('type') || 'view';
          const slug = decodeURIComponent(rawSlug).replace(/\/+$/, '') || '/';
          const id = `${type}:${slug}`;

          // Atomic upsert in D1
          const result = await env.DB.prepare(`
            INSERT INTO counters (id, slug, type, count, updated_at)
            VALUES (?1, ?2, ?3, 1, CURRENT_TIMESTAMP)
            ON CONFLICT(id) DO UPDATE SET
              count = count + 1,
              updated_at = CURRENT_TIMESTAMP
            RETURNING count;
          `).bind(id, slug, type).first<{ count: number }>();

          return Response.json(
            {
              success: true,
              slug,
              type,
              count: result ? result.count : 1,
            },
            { headers: corsHeaders }
          );
        }

        if (request.method === 'GET') {
          const rawSlug = url.searchParams.get('slug') || '/';
          const type = url.searchParams.get('type') || 'view';
          const slug = decodeURIComponent(rawSlug).replace(/\/+$/, '') || '/';
          const id = `${type}:${slug}`;

          const row = await env.DB.prepare(
            'SELECT count FROM counters WHERE id = ?1'
          ).bind(id).first<{ count: number }>();

          return Response.json(
            {
              success: true,
              slug,
              type,
              count: row ? row.count : 0,
            },
            { headers: corsHeaders }
          );
        }
      } catch (err: any) {
        return Response.json(
          {
            error: err.message || String(err),
            count: 0,
          },
          { status: 500, headers: corsHeaders }
        );
      }
    }

    // Forward all other requests to Hugo static assets
    return env.ASSETS.fetch(request);
  },
};
