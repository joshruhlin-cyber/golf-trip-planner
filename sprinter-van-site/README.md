# Ruhlin Sprinter Vans — Website

A self-contained static website (plain HTML/CSS/JS, no build step) for listing
Mercedes Sprinter vans for sale.

## Running it locally

Just open `index.html` in a browser, or serve the folder:

```
cd sprinter-van-site
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Adding your real van photos

Photos go in `images/vans/`. Until real photos are added, the site shows
generated placeholder boxes automatically — nothing will look "broken."

1. Name your photo files to match what's referenced in `js/main.js`, e.g.
   `images/vans/van-1-1.jpg`, `van-1-2.jpg`, `van-1-3.jpg` for the first van's
   photos, `van-2-1.jpg` for the second van, etc. You can use `.jpg`, `.png`,
   or `.webp` — just make sure the filename + extension matches what you put
   in the `images` array for that van in `js/main.js`.
2. Recommended size: at least 1200px on the long edge, landscape orientation
   (4:3 or 16:10 works best with the layout).

## Editing van listings

Open `js/main.js` and edit the `VANS` array near the top of the file. Each
van is one object:

```js
{
  id: "van-7",                 // unique, used internally — just increment
  status: "available",         // "available" | "pending" | "sold"
  category: "cargo",           // "cargo" | "camper" | "4x4" — controls the filter buttons
  title: "2023 Sprinter 2500 — Cargo",
  price: 72000,                // number, no $ or commas
  mileage: "18,000 mi",
  engine: "2.0L I4 Turbo Diesel",
  drivetrain: "RWD",
  roof: "High Roof, 144\" WB",
  sleeps: "N/A",
  description: "...",
  features: ["...", "..."],
  images: ["images/vans/van-7-1.jpg", "images/vans/van-7-2.jpg"]
}
```

Add a new object to sell a new van, remove one when it's gone, or just flip
`status` to `"sold"` to keep it visible with a "Sold" badge (good for social
proof / showing turnover).

## Editing reviews

Same file, `REVIEWS` array. Each review is:

```js
{
  name: "Customer Name",
  location: "City, ST",
  rating: 5,               // 1-5
  vanPurchased: "2021 Sprinter 4x4",
  quote: "..."
}
```

## Site-wide details (phone, email, business name)

Currently these live directly in `index.html` (header, hero, contact
section, footer) — search for the phone number / email placeholders and
replace them with your real contact info.

## Contact form

The contact form on the page currently only validates input and shows a
confirmation message in the browser — it does not send an email anywhere
yet. To make it actually deliver messages, the easiest options are:

- **Formspree** (formspree.io) — add their form action URL, no backend needed.
- **Netlify Forms** — if you host on Netlify, add `data-netlify="true"` to the `<form>`.
- A simple backend endpoint of your own, if you'd rather handle it yourself.

Ask if you'd like this wired up to one of these.

## Deploying

Since this is a static site with no build step, you can host it on GitHub
Pages, Netlify, Vercel, or any static file host by pointing it at this
`sprinter-van-site/` folder.
