# Layout Classes (Reveal.js)

Use these classes on `<section>` elements in `index.html`.

## Core layouts
- `layout-title`: title slide with badge, subtitle, and metadata.
- `layout-section`: chapter divider with gradient panel.
- `layout-2col`: two-column text + callout or list.
- `layout-3col`: three equal columns for comparisons.
- `layout-image-left`: media box on left, text on right.
- `layout-image-right`: media box on right, text on left.
- `layout-code`: code block + guidance callout.
- `layout-quote`: single quote + attribution.
- `layout-table`: comparison table.
- `layout-full-bleed`: background emphasis with overlay.

## Helper classes
- `badge`: small uppercase tag.
- `callout`: boxed emphasis area.
- `stat`: large metric text.
- `subtle`: muted supporting text.
- `media-box`: placeholder for images/screens.
- `overlay`: padded panel for full-bleed slides.

## Snippets

### Title
```html
<section class="layout-title">
  <span class="badge">Practical Track</span>
  <h1>Lecture Title</h1>
  <p class="subtitle">Lecture 02 | Topic</p>
  <p class="subtle">90 slides / 180 minutes</p>
</section>
```

### Two-column
```html
<section class="layout-2col">
  <div>
    <h2>Key idea</h2>
    <ul>
      <li>Point A</li>
      <li>Point B</li>
    </ul>
  </div>
  <div class="callout">
    <p class="stat">99.9%</p>
    <p class="subtle">Target uptime</p>
  </div>
</section>
```

### Image left
```html
<section class="layout-image-left">
  <img class="media-box" src="assets/diagram.png" alt="Diagram" />
  <div>
    <h2>Flow overview</h2>
    <p>Describe the pipeline in 3 steps.</p>
  </div>
</section>
```

### Code
```html
<section class="layout-code">
  <h2>Readable pseudo-code</h2>
  <pre><code class="language-python">def validate_request(payload):
    if not payload.get("user_id"):
        return "missing user_id"
    return "ok"</code></pre>
  <div class="callout">
    <p><strong>Tip:</strong> keep code blocks short.</p>
  </div>
</section>
```

### Full-bleed
```html
<section
  class="layout-full-bleed"
  data-background-gradient="linear-gradient(120deg, rgba(15,118,110,0.18), rgba(37,99,235,0.12))"
>
  <div class="overlay">
    <h2>Workshop</h2>
    <p>Task instructions here.</p>
  </div>
</section>
```
