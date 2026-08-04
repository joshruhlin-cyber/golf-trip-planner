/* =========================================================================
   CONTENT DATA
   Everything below in VANS and REVIEWS is placeholder content.
   To add your real vans/reviews, edit these arrays — see images/README.md
   for how photo files should be named and where to put them.
   ========================================================================= */

const VANS = [
  {
    id: "van-1",
    status: "available", // available | pending | sold
    category: "camper", // cargo | camper | 4x4
    title: "2022 Sprinter 2500 High Roof — Camper Conversion",
    price: 89500,
    mileage: "31,200 mi",
    engine: "2.0L I4 Turbo Diesel",
    drivetrain: "RWD",
    roof: "High Roof, 170\" WB",
    sleeps: "2-3",
    description: "Professionally converted camper build with solar power, a wet bath, and a full kitchen galley. Low miles, single owner, always garage kept. Ready for full-time travel or weekend trips.",
    features: ["400W solar + lithium battery bank", "Wet bath with shower", "Diesel heater", "Swivel captain seats", "Full kitchen galley", "Roof fan + insulated windows"],
    images: ["images/vans/van-1-1.jpg", "images/vans/van-1-2.jpg", "images/vans/van-1-3.jpg"]
  },
  {
    id: "van-2",
    status: "available",
    category: "4x4",
    title: "2021 Sprinter 2500 4x4 — High Roof Cargo",
    price: 74900,
    mileage: "42,800 mi",
    engine: "3.0L V6 Turbo Diesel",
    drivetrain: "4x4",
    roof: "High Roof, 144\" WB",
    sleeps: "N/A",
    description: "Factory 4x4 with the V6 diesel, perfect base for an off-grid build or as-is for a work van that can handle rough terrain. Clean Carfax, no accidents, recent service.",
    features: ["Factory 4x4 drivetrain", "V6 turbo diesel", "Tow package", "Backup camera", "Recent brakes + tires", "Clean Carfax"],
    images: ["images/vans/van-2-1.jpg", "images/vans/van-2-2.jpg"]
  },
  {
    id: "van-3",
    status: "pending",
    category: "camper",
    title: "2020 Sprinter 3500 4x4 — Luxury Camper Conversion",
    price: 129000,
    mileage: "58,400 mi",
    engine: "3.0L V6 Turbo Diesel",
    drivetrain: "4x4",
    roof: "High Roof, 170\" Extended",
    sleeps: "4",
    description: "Top-tier build with dual axle, air suspension, and a full-time livable interior. Includes washer/dryer combo and a fixed queen bed with garage storage below.",
    features: ["Air suspension", "Washer/dryer combo", "Fixed queen bed + garage", "600W solar", "Induction cooktop", "Air conditioning (cab + roof)"],
    images: ["images/vans/van-3-1.jpg", "images/vans/van-3-2.jpg", "images/vans/van-3-3.jpg"]
  },
  {
    id: "van-4",
    status: "available",
    category: "cargo",
    title: "2023 Sprinter 2500 — Standard Roof Cargo",
    price: 68500,
    mileage: "12,600 mi",
    engine: "2.0L I4 Turbo Diesel",
    drivetrain: "RWD",
    roof: "Standard Roof, 144\" WB",
    sleeps: "N/A",
    description: "Nearly new work-ready cargo van, still under factory warranty. Empty interior, ready for shelving, a conversion, or straight to work.",
    features: ["Factory warranty remaining", "Bluetooth + backup camera", "Shelving-ready interior", "Single owner", "Non-smoker vehicle"],
    images: ["images/vans/van-4-1.jpg", "images/vans/van-4-2.jpg"]
  },
  {
    id: "van-5",
    status: "sold",
    category: "camper",
    title: "2019 Sprinter 2500 — Weekend Camper Conversion",
    price: 61500,
    mileage: "67,900 mi",
    engine: "2.0L I4 Turbo Diesel",
    drivetrain: "RWD",
    roof: "High Roof, 144\" WB",
    sleeps: "2",
    description: "Simple, well-built weekend rig with a fold-out bed, small kitchenette, and 200W solar setup. Great entry point into van life.",
    features: ["200W solar", "Fold-out bed/bench", "Kitchenette + fridge", "Insulated + carpeted walls", "Roof vent fan"],
    images: ["images/vans/van-5-1.jpg", "images/vans/van-5-2.jpg"]
  },
  {
    id: "van-6",
    status: "available",
    category: "4x4",
    title: "2022 Sprinter 3500 4x4 — Dually Cargo",
    price: 82000,
    mileage: "24,300 mi",
    engine: "3.0L V6 Turbo Diesel",
    drivetrain: "4x4",
    roof: "High Roof, 170\" WB",
    sleeps: "N/A",
    description: "Heavy-duty dually 4x4 with serious payload capacity — ideal for a large conversion build or commercial use requiring extra towing and load capacity.",
    features: ["Dually rear axle", "Factory 4x4", "10,000 lb tow rating", "Heavy-duty suspension", "Clean title, one owner"],
    images: ["images/vans/van-6-1.jpg", "images/vans/van-6-2.jpg"]
  }
];

// Photos of past builds/sales — shown in the "Our Work" gallery, not tied
// to a specific current listing. Add new photos to images/gallery/ and add
// an entry here.
const GALLERY = [
  { src: "images/gallery/IMG_7421.jpg", caption: "4x4 conversion, out on the road" },
  { src: "images/gallery/IMG_7427.jpg", caption: "4x4 build, out exploring" },
  { src: "images/gallery/IMG_7423.jpg", caption: "4x4 build ready for the trail" },
  { src: "images/gallery/IMG_7420.jpg", caption: "Bed, kitchenette & custom accent paneling" },
  { src: "images/gallery/IMG_7422.jpg", caption: "Full kitchen, bed & LED lighting" },
  { src: "images/gallery/IMG_7419.jpg", caption: "Bench seating & fold-out table" },
  { src: "images/gallery/IMG_7425.jpg", caption: "4x4 conversion, custom interior" },
  { src: "images/gallery/IMG_7426.jpg", caption: "4x4 conversion at golden hour" },
  { src: "images/gallery/IMG_7424.jpg", caption: "Rear ladder & spare tire mount" }
];

const REVIEWS = [
  {
    name: "Megan T.",
    location: "Boulder, CO",
    rating: 5,
    vanPurchased: "2021 Sprinter 4x4",
    quote: "Josh was upfront about every detail on the van, down to a small paint chip I never would've noticed. No pressure, no upselling — just an honest transaction. Still running perfectly two years later."
  },
  {
    name: "Daniel R.",
    location: "Austin, TX",
    rating: 5,
    vanPurchased: "Camper Conversion",
    quote: "Bought a conversion sight-unseen and had it shipped to Texas. Communication was excellent throughout and the van showed up exactly as described. Would buy again without hesitation."
  },
  {
    name: "Priya S.",
    location: "Portland, OR",
    rating: 5,
    vanPurchased: "Cargo Van",
    quote: "Best van-buying experience I've had. Full maintenance records were ready before I even asked, and the pre-purchase inspection came back completely clean."
  },
  {
    name: "Marcus W.",
    location: "Denver, CO",
    rating: 4,
    vanPurchased: "2020 Sprinter 3500",
    quote: "Great van at a fair price. Process took a little longer than expected because of financing on my end, but Josh was patient and kept the van available for me."
  },
  {
    name: "Elena F.",
    location: "Salt Lake City, UT",
    rating: 5,
    vanPurchased: "Camper Conversion",
    quote: "We were nervous about buying a converted van from photos alone, but Josh sent extra video walkthroughs and answered every question. It's exactly what we hoped for."
  },
  {
    name: "Chris B.",
    location: "Flagstaff, AZ",
    rating: 5,
    vanPurchased: "2022 Sprinter 4x4",
    quote: "Fair pricing, zero pressure, and a genuinely nice guy to deal with. This was my second van purchase from Vandwellerz and it won't be my last."
  }
];

/* =========================================================================
   RENDERING
   ========================================================================= */

const money = (n) => n.toLocaleString("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 });

const STATUS_LABEL = { available: "Available", pending: "Pending Sale", sold: "Sold" };

function placeholderImage(label) {
  const svg = `
    <svg xmlns="http://www.w3.org/2000/svg" width="640" height="480" viewBox="0 0 640 480">
      <defs>
        <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#f0ece3"/>
          <stop offset="1" stop-color="#e3ddd0"/>
        </linearGradient>
      </defs>
      <rect width="640" height="480" fill="url(#g)"/>
      <g fill="none" stroke="#b9812f" stroke-width="3" opacity="0.55">
        <rect x="150" y="190" width="340" height="110" rx="14"/>
        <circle cx="220" cy="315" r="26"/>
        <circle cx="420" cy="315" r="26"/>
      </g>
      <text x="320" y="380" font-family="Inter, sans-serif" font-size="20" fill="#3a4250" text-anchor="middle">${label}</text>
    </svg>`;
  return `data:image/svg+xml;utf8,${encodeURIComponent(svg)}`;
}

function attachImageFallback(img, label) {
  img.addEventListener("error", () => {
    img.onerror = null;
    img.src = placeholderImage(label);
  }, { once: true });
}

function renderVanCard(van) {
  const card = document.createElement("article");
  card.className = "van-card";
  card.dataset.category = van.category;

  card.innerHTML = `
    <div class="van-card-media">
      <span class="van-badge status-${van.status}">${STATUS_LABEL[van.status]}</span>
      <img alt="${van.title}" loading="lazy">
    </div>
    <div class="van-card-body">
      <h3 class="van-card-title">${van.title}</h3>
      <p class="van-card-price">${money(van.price)}</p>
      <div class="van-specs">
        <span><strong>${van.mileage}</strong>Mileage</span>
        <span><strong>${van.drivetrain}</strong>Drivetrain</span>
        <span><strong>${van.engine}</strong>Engine</span>
        <span><strong>${van.roof}</strong>Roof / WB</span>
      </div>
      <button class="btn btn-primary" data-van-id="${van.id}">View Details</button>
    </div>
  `;

  const img = card.querySelector("img");
  img.src = van.images[0];
  attachImageFallback(img, `${van.title} — Photo 1`);

  return card;
}

function renderReviewCard(review) {
  const card = document.createElement("article");
  card.className = "review-card";
  card.innerHTML = `
    <span class="review-stars" aria-hidden="true">${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</span>
    <p class="review-quote">&ldquo;${review.quote}&rdquo;</p>
    <div class="review-meta">
      <span class="review-name">${review.name}</span>
      <span class="review-sub">${review.location} &middot; ${review.vanPurchased}</span>
    </div>
  `;
  return card;
}

function renderVans(filter = "all") {
  const grid = document.getElementById("van-grid");
  grid.innerHTML = "";
  const filtered = filter === "all" ? VANS : VANS.filter(v => v.category === filter);
  filtered.forEach(van => grid.appendChild(renderVanCard(van)));
}

function renderReviews() {
  const grid = document.getElementById("review-grid");
  grid.innerHTML = "";
  REVIEWS.forEach(review => grid.appendChild(renderReviewCard(review)));
}

function renderGallery() {
  const grid = document.getElementById("gallery-grid");
  grid.innerHTML = "";
  GALLERY.forEach((item, idx) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "gallery-item";
    btn.dataset.index = idx;
    const img = document.createElement("img");
    img.src = item.src;
    img.alt = item.caption;
    img.loading = "lazy";
    attachImageFallback(img, item.caption);
    btn.appendChild(img);
    grid.appendChild(btn);
  });
}

function populateVanSelect() {
  const select = document.getElementById("van-interest");
  VANS.forEach(van => {
    const opt = document.createElement("option");
    opt.value = van.id;
    opt.textContent = van.title;
    select.appendChild(opt);
  });
}

/* =========================================================================
   VAN DETAIL MODAL
   ========================================================================= */

const modalOverlay = document.getElementById("van-modal");
const modalBody = document.getElementById("modal-body");

function openVanModal(van) {
  modalBody.innerHTML = `
    <div class="modal-gallery-main"><img id="modal-main-img" alt="${van.title}"></div>
    <div class="modal-thumbs" id="modal-thumbs"></div>
    <div class="modal-title-row">
      <h3>${van.title}</h3>
      <span class="modal-price">${money(van.price)}</span>
    </div>
    <p class="modal-desc">${van.description}</p>
    <div class="modal-spec-table">
      <div><span>Mileage</span>${van.mileage}</div>
      <div><span>Engine</span>${van.engine}</div>
      <div><span>Drivetrain</span>${van.drivetrain}</div>
      <div><span>Roof / Wheelbase</span>${van.roof}</div>
      <div><span>Sleeps</span>${van.sleeps}</div>
      <div><span>Status</span>${STATUS_LABEL[van.status]}</div>
    </div>
    <ul class="modal-features">${van.features.map(f => `<li>${f}</li>`).join("")}</ul>
    <a href="#contact" class="btn btn-primary" id="modal-inquire">Inquire About This Van</a>
  `;

  const mainImg = document.getElementById("modal-main-img");
  const thumbsWrap = document.getElementById("modal-thumbs");

  const setMain = (idx) => {
    mainImg.src = van.images[idx];
    attachImageFallback(mainImg, `${van.title} — Photo ${idx + 1}`);
    thumbsWrap.querySelectorAll("button").forEach((b, i) => b.classList.toggle("is-active", i === idx));
  };

  van.images.forEach((src, idx) => {
    const thumb = document.createElement("button");
    thumb.type = "button";
    const thumbImg = document.createElement("img");
    thumbImg.src = src;
    thumbImg.alt = `${van.title} thumbnail ${idx + 1}`;
    attachImageFallback(thumbImg, `Photo ${idx + 1}`);
    thumb.appendChild(thumbImg);
    thumb.addEventListener("click", () => setMain(idx));
    thumbsWrap.appendChild(thumb);
  });

  setMain(0);

  document.getElementById("modal-inquire").addEventListener("click", () => {
    closeVanModal();
    const select = document.getElementById("van-interest");
    if (select) select.value = van.id;
  });

  modalOverlay.hidden = false;
  document.body.style.overflow = "hidden";
}

function closeVanModal() {
  modalOverlay.hidden = true;
  document.body.style.overflow = "";
}

document.getElementById("modal-close").addEventListener("click", closeVanModal);
modalOverlay.addEventListener("click", (e) => {
  if (e.target === modalOverlay) closeVanModal();
});
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && !modalOverlay.hidden) closeVanModal();
});

document.getElementById("van-grid").addEventListener("click", (e) => {
  const btn = e.target.closest("[data-van-id]");
  if (!btn) return;
  const van = VANS.find(v => v.id === btn.dataset.vanId);
  if (van) openVanModal(van);
});

/* =========================================================================
   GALLERY LIGHTBOX
   ========================================================================= */

const lightboxOverlay = document.getElementById("gallery-lightbox");
const lightboxImg = document.getElementById("lightbox-img");
const lightboxCaption = document.getElementById("lightbox-caption");
let lightboxIndex = 0;

function showLightboxItem(idx) {
  lightboxIndex = (idx + GALLERY.length) % GALLERY.length;
  const item = GALLERY[lightboxIndex];
  lightboxImg.src = item.src;
  lightboxImg.alt = item.caption;
  attachImageFallback(lightboxImg, item.caption);
  lightboxCaption.textContent = item.caption;
}

function openLightbox(idx) {
  showLightboxItem(idx);
  lightboxOverlay.hidden = false;
  document.body.style.overflow = "hidden";
}

function closeLightbox() {
  lightboxOverlay.hidden = true;
  document.body.style.overflow = "";
}

document.getElementById("gallery-grid").addEventListener("click", (e) => {
  const btn = e.target.closest(".gallery-item");
  if (!btn) return;
  openLightbox(Number(btn.dataset.index));
});

document.getElementById("lightbox-close").addEventListener("click", closeLightbox);
document.getElementById("lightbox-prev").addEventListener("click", () => showLightboxItem(lightboxIndex - 1));
document.getElementById("lightbox-next").addEventListener("click", () => showLightboxItem(lightboxIndex + 1));
lightboxOverlay.addEventListener("click", (e) => {
  if (e.target === lightboxOverlay) closeLightbox();
});
document.addEventListener("keydown", (e) => {
  if (lightboxOverlay.hidden) return;
  if (e.key === "Escape") closeLightbox();
  if (e.key === "ArrowLeft") showLightboxItem(lightboxIndex - 1);
  if (e.key === "ArrowRight") showLightboxItem(lightboxIndex + 1);
});

/* =========================================================================
   FILTER BAR
   ========================================================================= */

document.getElementById("filter-bar").addEventListener("click", (e) => {
  const btn = e.target.closest(".filter-btn");
  if (!btn) return;
  document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("is-active"));
  btn.classList.add("is-active");
  renderVans(btn.dataset.filter);
});

/* =========================================================================
   MOBILE NAV
   ========================================================================= */

const navToggle = document.getElementById("nav-toggle");
const mainNav = document.getElementById("main-nav");

navToggle.addEventListener("click", () => {
  const isOpen = mainNav.classList.toggle("is-open");
  navToggle.setAttribute("aria-expanded", String(isOpen));
});

mainNav.querySelectorAll("a").forEach(link => {
  link.addEventListener("click", () => {
    mainNav.classList.remove("is-open");
    navToggle.setAttribute("aria-expanded", "false");
  });
});

/* =========================================================================
   CONTACT FORM
   Submits to Netlify Forms (see the data-netlify attribute on the <form>
   in index.html). Works automatically once this site is deployed on
   Netlify — no backend code needed. Submitting from anywhere else (e.g.
   opening index.html directly, or a non-Netlify host) will just fail the
   fetch and show an error message instead.
   ========================================================================= */

document.getElementById("contact-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const form = e.target;
  const note = document.getElementById("form-note");

  if (!form.checkValidity()) {
    note.textContent = "Please fill in your name, email, and message.";
    note.classList.add("is-error");
    return;
  }

  const body = new URLSearchParams(new FormData(form)).toString();

  fetch("/", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body })
    .then((res) => {
      if (!res.ok) throw new Error("Submission failed");
      note.classList.remove("is-error");
      note.textContent = "Thanks — your message has been sent. We'll be in touch within one business day.";
      form.reset();
    })
    .catch(() => {
      note.classList.add("is-error");
      note.textContent = "Something went wrong sending that — please call or email us directly.";
    });
});

/* =========================================================================
   INIT
   ========================================================================= */

document.getElementById("year").textContent = new Date().getFullYear();
renderVans();
renderGallery();
renderReviews();
populateVanSelect();
