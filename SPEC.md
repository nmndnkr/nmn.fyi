# nmn.fyi build spec

Read this whole file before every session. It is the only source of truth for this project.

## What this site is

Naman Dhankhar's personal site. Its job is to get him hired in deep-tech venture capital.

The reader is a VC partner who opens the link from a warm intro or a forwarded deal, often on a phone. In 60 seconds they should know who Naman is, what he looks at, that he thinks clearly, and that he can build. Every decision serves that reader.

## Working rules (non-negotiable)

1. **One gate at a time.** Each gate is built on its own branch (`gate-0`, `gate-1`, ...). Never start the next gate until Naman approves the current one.
2. **Stop and report at the end of every gate** using the report format below. Then wait.
3. **Build only what this file specifies.** No extra features, pages, components, animations, libraries or "nice to haves." If something seems missing, propose it in the report under "Proposed, not built." Do not build it.
4. **If the spec is unclear, ask.** Do not guess.
5. **Never write Naman's content.** No positioning sentences, thesis text, project descriptions or bios. Use `TODO:` placeholders. He writes all prose.
6. **Never invent facts.** No metrics, dates, titles, company names, quotes or links that Naman has not supplied.
7. **No em dashes anywhere** in site copy, placeholders, or commit messages.
8. **Never publish confidential work.** If supplied content names specifics from EFL, BANF or Beyond Silicon (deal terms, internal numbers, unreleased plans), flag it in the report and do not publish it until Naman confirms it is public.
9. Before reporting, run `npm run build`. It must pass with zero errors and zero warnings you introduced.

### Report format (end of every gate)

```
GATE N DONE
Preview: <Vercel preview URL>
Changed: <bullets>
Unsure about: <bullets, or "nothing">
Needs Naman: <bullets, e.g. content to supply, DNS step>
Proposed, not built: <bullets, or "nothing">
```

### Naman's review at every gate

He opens the preview URL on his phone first, then on desktop, and checks:
- Would a partner get it in 60 seconds?
- Is there anything here he didn't ask for?
- Is anything broken, or anything he'd be embarrassed to send?

Anything flagged gets fixed on the same branch before the gate merges to `main`.

## Stack

- **Astro**, current stable version, static output. Use the current content collections API.
- **Plain CSS:** one global stylesheet with CSS custom properties. No Tailwind, no UI framework, no CSS-in-JS.
- **No client-side JavaScript** in v1. Astro's zero-JS default stays on.
- **Fonts self-hosted via npm:** `@fontsource/eb-garamond` (400, 400 italic) and `@fontsource/ibm-plex-mono` (400). No Google Fonts requests.
- **Hosting:** GitHub repo, Vercel auto-deploy. `main` deploys to nmn.fyi. Every other branch gets a Vercel preview URL.
- **Package manager:** npm.

## Design (Direction B: after thebrowser.company)

Restraint is the design. A quiet, well-set page of writing. Light mode only.

### Tokens (`src/styles/global.css`)

```css
:root {
  --bg: #EEEEE7;
  --ink: rgba(0, 0, 0, 0.85);
  --muted: rgba(0, 0, 0, 0.55);
  --rule: rgba(0, 0, 0, 0.15);

  --serif: "EB Garamond", Georgia, serif;
  --mono: "IBM Plex Mono", ui-monospace, monospace;

  --gutter: 20px;
  --measure: 62ch;
}
```

### Type

| Use | Font | Size | Line height | Other |
|---|---|---|---|---|
| Landing sentence | serif 400 | 28px desktop, 24px under 600px | 1.2 | centered, max-width 11em |
| Page title (h1) | serif 400 | 36px desktop, 30px mobile | 1.15 | left aligned |
| Section heading (h2) | serif 400 | 24px | 1.25 | |
| Body text | serif 400 | 19px | 1.55 | max-width var(--measure) |
| Labels, nav, metadata | mono 400 | 13px | 1.6 | uppercase, letter-spacing 0.15em |

Only weight 400 anywhere. Italic is for emphasis inside body text only.

### Links

- Nav and list links: `--ink`, no underline. On hover and focus: 1px underline, offset 4px.
- Links inside body text: always underlined, 1px, offset 3px.
- Visible `:focus-visible` outline (1px solid `--ink`, offset 3px).

### Layout

- **Landing:** content centered vertically and horizontally in the viewport. The name in mono caps (Naman Dhankhar) at roughly 115% of the sentence size, optically centered (text-indent matching letter-spacing), then 24px of space, then the sentence, then 32px of space, then the mono link list stacked vertically with line-height 2.2. Directly under the THESES link, the title of the most recently updated thesis, in serif 17px, `--muted`, linking to that thesis; it shows only once at least one thesis is published. Nothing else on the page. (Name above the sentence added at Naman's request, 2026-10-29.)
- **Subpages:** one column of width `var(--measure)`, centered, side padding `var(--gutter)`. At the top, a mono `NMN.FYI` link back to `/`. At the bottom, a mono footer row: `EMAIL · LINKEDIN · GITHUB`.
- **Lists** (theses, work, writing): each item is a row with the title in serif 22px, and metadata beneath in mono (status, date). Rows are separated by a 1px `--rule` line. No cards, no boxes, no images.
- No horizontal scroll at 375px width.

### Out of scope for v1 (do not build)

Dark mode or a theme toggle, animations or transitions, the contour/canvas hero, any JavaScript interactivity, analytics, a CMS or admin, comments, search, tag pages, RSS, newsletter signup, images on list pages, per-page OG images.

## Content model

All content lives in Markdown files. Adding content never requires touching code.

### Site config (`src/site.ts`)

```ts
export const site = {
  name: "Naman Dhankhar",
  sentence: "TODO: one sentence. Who you are, what you look at.",
  email: "TODO",
  linkedin: "TODO",
  github: "https://github.com/nmndnkr",
  description: "TODO: one line for search results and link previews.",
};
```

### Collections (`src/content/`)

**theses/** (`src/content/theses/<slug>.md`)
```yaml
title: string
summary: string        # one line, shown in the list
status: draft | developing | conviction
updated: YYYY-MM-DD    # shown on list and page
published: YYYY-MM-DD
```
Body sections, in this order, as h2: The claim, Why now, Market map, What I'd back, What kills it, Open questions.

**work/** (`src/content/work/<slug>.md`)
```yaml
title: string
oneLiner: string
year: number
tags: [string]         # max 3
repo: url (optional)
demo: url (optional)
```
Body sections as h2: Problem, What I built, What it taught me.

**writing/** (`src/content/writing/<slug>.md`)
```yaml
title: string
date: YYYY-MM-DD
summary: string
url: url (optional)    # if set, the list links out to it and no page is generated
```

Sort every list by `updated` or `date`, newest first. Validate frontmatter with the collection schema so a bad file fails the build instead of rendering broken.

## Pages

| Route | Content |
|---|---|
| `/` | Sentence plus links: THESES (with latest thesis title beneath, from Gate 3), WORK, WRITING, RESUME, EMAIL · LINKEDIN |
| `/theses` | List of theses: title, summary, status, updated |
| `/theses/[slug]` | Thesis page with status and updated date under the title |
| `/work` | List of work entries |
| `/work/[slug]` | Work page with repo and demo links if present |
| `/writing` | List of writing, linking out or to a page |
| `/writing/[slug]` | Only for entries without `url` |
| RESUME link | Goes straight to `/resume.pdf` (file in `public/`). No resume page. |
| `/404` | Mono `NMN.FYI` link and one serif line: "Nothing here." |

Every page has a `<title>` ("Naman Dhankhar" on the landing, "<Page> · Naman Dhankhar" elsewhere) and a meta description.

### Link preview (OG image)

One static image used on every page, so the link looks clean when pasted into email, Slack or iMessage.
- `public/og.png`, 1200 x 630. Background `--bg`. "Naman Dhankhar" in EB Garamond, ink, centered, with `site.sentence` beneath it in a smaller size. Nothing else.
- Generate it once with a one-off script, `scripts/og.mjs`, that renders an SVG to PNG with `sharp`. The script is not part of the site build. Naman reruns it if the sentence changes.
- Every page sets `og:title`, `og:description`, `og:image` (absolute URL on nmn.fyi), `og:url`, and `twitter:card` = `summary_large_image`.

## Gates

### Gate 0: Pipeline

- Create the Astro project (minimal template), initialize git, and push to a GitHub repo named `nmn-fyi`.
- Landing page shows only the text `nmn.fyi`.
- **Needs Naman:** connect the repo in Vercel and add the domain nmn.fyi. Write him exact step-by-step instructions for this in the report.
- **Done when:** nmn.fyi loads and pushing a test branch produces a preview URL.

### Gate 1: Content, unstyled

- Create `src/site.ts` and the landing page with the sentence and link list.
- Create stub pages for every route, each showing only an h1 and `TODO`.
- **No styling at all:** browser defaults only, semantic HTML.
- **Review question:** does the content say the right thing, with nothing missing and nothing extra?

### Gate 2: Styling

- Add the fonts, tokens, type, links and layout exactly as specified above.
- Style the landing page and the subpage shell (top link, column, footer) using the stub pages.
- **Review question:** on a phone, does it look deliberate and not templated?

### Gate 3: Theses

- Create the theses collection, schema, list page and detail page.
- Add `src/content/theses/_template.md` with the frontmatter and all six h2 headings, each followed by `TODO`. Exclude files starting with `_` from the build.
- Add the latest thesis title under THESES on the landing page, as specified in Layout.
- Publish the first thesis only when Naman supplies the text.
- **Review question:** can a partner get the argument in 3 minutes?

### Gate 4: Work

- Create the work collection, schema, list page and detail page.
- Add `_template.md` the same way. Two entries go live when Naman supplies the content.
- **Review question:** does each entry show judgment, not just stack?

### Gate 5: Writing, resume, 404, meta

- Create the writing collection, list page, and detail pages for entries without `url`.
- Wire the RESUME link to `/resume.pdf` (Naman supplies the file), add the 404 page, and add titles and meta descriptions to every page.
- Add the OG image and tags as specified under "Link preview." This needs the final sentence; if it isn't ready, build the script and tags and flag it under "Needs Naman."
- **Review question:** does every link work, including on a phone? Does the link preview look right when pasted into a message?

After Gate 5, the build is complete. Future work is content only.

## Adding content later (for Naman)

1. Copy `src/content/theses/_template.md` to a new file, e.g. `perovskite-commercialization.md`.
2. Fill in the frontmatter and the sections. Set `status` honestly (`draft` is fine) and `updated` to today.
3. Commit it to a new branch (the GitHub web editor works, even on a phone).
4. Open the Vercel preview link and check it on your phone.
5. Merge to `main`. It's live on nmn.fyi in about a minute.

When you revise a thesis, update the `updated` date and `status`. That's how partners see your thinking evolve.

## Proposed, not approved (do not build until Naman says yes)

Nothing currently. New proposals from the agent go in the gate report, not here.
