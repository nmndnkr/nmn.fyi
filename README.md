# nmn.fyi

Personal site for Naman Dhankhar.

## Stack

Plain HTML, CSS, and JavaScript. There is no build step and no package
dependency to maintain.

## Run locally

```sh
python3 -m http.server 4173
```

Then open `http://localhost:4173`.

## Deploy

The included GitHub Actions workflow deploys only the public site files to
GitHub Pages whenever `main` is pushed. The `CNAME` file points the site at
`nmn.fyi`.

Before the first deployment:

1. Create a GitHub repository and push this folder to its `main` branch.
2. In the repository settings, set Pages source to **GitHub Actions**.
3. At the DNS provider, point `nmn.fyi` to GitHub Pages and add the matching
   `www` record if desired.

## Content changes

All page content lives in `index.html`. Visual styles are in `styles.css`, and
the lens/project interactions are in `script.js`.
