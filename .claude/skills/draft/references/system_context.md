# Guidelines: System Context Diagram

A system context diagram shows how a central system sits within its environment — who the actors are, what the system does, and how information or control flows between them. The diagram's job is to make the boundary of the system visible and to give every actor a clear role. Readers should be able to identify the core system and its primary relationships at a glance.

---

## Format selection

### SVG (preferred)
**Best for:** Precision layouts, complex diagrams with many text elements, professional documentation.
- Complete control over positioning and sizing; no text overflow issues when sized correctly.
- Scalable to any resolution; editable in Inkscape or Illustrator.
- Requires conversion to PNG for some markdown viewers (see Conversion to PNG below).

**Use when:** Text containment is critical, professional appearance is required, or complex layouts with many interconnected elements are needed.

### Mermaid
**Best for:** Simple flowcharts, sequence diagrams, quick sketches.
- Text-based and easy to version-control; renders directly in many markdown viewers.
- Less control over exact positioning; may not render in all viewers.

**Use when:** Creating simple flow diagrams, quick iteration is needed, or text-based source is preferred.

### Draw.io
**Best for:** Visual editing, team collaboration, exporting to Visio format.
- Can have text overflow issues with complex diagrams; XML format is harder to version-control.

**Use when:** The team prefers visual editing or needs to export to `.vsdx`.

---

## Structure

### Central system
- Place the core system at or near the visual centre. It should be the most visually prominent element — larger and in a distinct colour.
- The central system box carries the system name, an optional one-line description, and a short bulleted list of its primary capabilities.
- All arrows ultimately connect to or from the central system. Do not draw actor-to-actor relationships; they belong in a separate diagram.

### Actors
- Each actor is a box that represents a person, team, or external system interacting with the core system.
- Each actor box carries the actor name and a short bulleted list of responsibilities (the things the actor does that are relevant to the system boundary).
- Group related actors inside a dashed bounding box with a group label. Grouping encodes organisational or functional affiliation, not interaction frequency.

### Arrows
- Each arrow represents a data or control flow crossing the system boundary.
- Label every arrow with a short noun phrase naming what is exchanged (e.g. "Fleet plans", "Fulfillment status"). Never leave an arrow unlabelled.
- Use orthogonal (right-angle) routing: arrows travel horizontally then vertically, or vertically then horizontally, with a single bend. Avoid diagonal lines.
- Arrow direction signals who initiates the flow, not just who receives. Use bidirectional arrows only when both directions carry distinct named flows that cannot be shown separately.

---

## Visual style

### Colour
Use the following palette consistently. Colour encodes the role of each element — do not vary it for decoration.

**Actor types:**
- Governance actors: `fill="#dae8fc" stroke="#6c8ebf"`
- Planning actors: `fill="#d5e8d4" stroke="#82b366"`
- Capacity actors: `fill="#fff2cc" stroke="#d6b656"`
- Development/operational actors: `fill="#ffe6cc" stroke="#d79b00"`
- External systems or data sources: `fill="#f8cecc" stroke="#b85450"`

**System elements:**
- Core system: `fill="#1ba1e2" stroke="#006EAF"`, white text
- Outputs or results: `fill="#e1d5e7" stroke="#9673a6"`
- Annotation boxes: `fill="#f5f5f5" stroke="#666666"`

**Grouping boxes:**
- Dashed groups: `fill="#f5f5f5" stroke="#666666" stroke-dasharray="8,8"`

If the diagram has fewer than three actor types, use only those colours. Do not assign colours that have no actors in their category.

### Typography
- Use Arial or a generic sans-serif throughout.
- Title: 20px bold, centred at the top of the canvas.
- Group labels: 14px bold, anchored at the top of the bounding box.
- Box titles (actor names, system name): 13px bold, centred within the box.
- Box body text (bullets): 11px, left-aligned, beginning at `box_x + 10`.
- Arrow labels: 11px, positioned adjacent to the horizontal segment of the arrow — 10px above the path or 15px below if above is crowded.

### Layout and spacing
- Canvas: 1400px wide × 720px tall is a reliable default for a diagram with five to ten actors. Scale proportionally for fewer or more actors.
- Leave at least 60px between actor groups and between groups and the central system.
- Leave at least 20px between boxes within a group.
- Align boxes to an implicit grid. Irregular placement is acceptable when it serves the logic of the layout, but avoid accidental misalignment.

---

## Box sizing

Use these formulas to calculate box dimensions before placing any elements.

**Height:**
- Single-line title, N bullets: `60 + (N × 15)` px
- Two-line title, N bullets: `74 + (N × 15)` px
- With subtitle (one-line title + subtitle line + N bullets): `90 + (N × 15)` px

**Width:**
```
Width = (longest text line in characters × 6.5)
      + 20  (bullet point and indent)
      + 20  (left and right margins)
```
Add a 10–15% buffer. Round up to the nearest 10px.

**Common sizes (quick reference):**

| Content type       | Bullets | Title lines | Height | Width range |
|--------------------|---------|-------------|--------|-------------|
| Small actor        | 3       | 1           | 105px  | 130–150px   |
| Standard actor     | 4       | 1           | 120px  | 130–160px   |
| Wide actor         | 4       | 1           | 120px  | 260–280px   |
| Two-line title     | 3       | 2           | 110px  | 140–160px   |
| External system    | 3       | 1           | 105px  | 150px       |
| Core system        | 4 + subtitle | 1      | 155px  | 300px       |
| Annotation         | 4       | 1           | 120px  | 300–330px   |

**Text Y-coordinates within a box** (origin = top-left corner of the box):
- Title: `box_y + 20`
- First bullet: `box_y + 50` (adjust to `box_y + 64` for a two-line title)
- Each subsequent bullet: previous bullet `y + 15`

---

## SVG template

Use this as a starting point for a new system context diagram:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="1400" height="720" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .title { font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; }
      .box-title { font-family: Arial, sans-serif; font-size: 13px; font-weight: bold; }
      .box-text { font-family: Arial, sans-serif; font-size: 11px; }
      .group-title { font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; }
      .arrow-text { font-family: Arial, sans-serif; font-size: 11px; }
    </style>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#333" />
    </marker>
  </defs>

  <!-- Main Title -->
  <text x="700" y="35" text-anchor="middle" class="title">Diagram Title</text>

  <!-- Actor Group -->
  <rect x="70" y="90" width="330" height="445" fill="#f5f5f5" stroke="#666666" stroke-width="1" stroke-dasharray="8,8" rx="5"/>
  <text x="235" y="110" text-anchor="middle" class="group-title" fill="#333">Actor Group</text>

  <!-- Actor Box (4 bullets, single-line title = 120px height) -->
  <rect x="90" y="130" width="280" height="120" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1" rx="5"/>
  <text x="230" y="150" text-anchor="middle" class="box-title">Actor Name</text>
  <text x="100" y="175" class="box-text">• Responsibility 1</text>
  <text x="100" y="190" class="box-text">• Responsibility 2</text>
  <text x="100" y="205" class="box-text">• Responsibility 3</text>
  <text x="100" y="220" class="box-text">• Responsibility 4</text>

  <!-- Central System -->
  <rect x="550" y="295" width="300" height="155" fill="#1ba1e2" stroke="#006EAF" stroke-width="1" rx="5"/>
  <text x="700" y="318" text-anchor="middle" class="box-title" fill="#ffffff">System Name</text>
  <text x="700" y="340" text-anchor="middle" class="box-text" fill="#ffffff">System Description</text>
  <text x="560" y="370" class="box-text" fill="#ffffff">• Feature 1</text>
  <text x="560" y="390" class="box-text" fill="#ffffff">• Feature 2</text>
  <text x="560" y="410" class="box-text" fill="#ffffff">• Feature 3</text>
  <text x="560" y="430" class="box-text" fill="#ffffff">• Feature 4</text>

  <!-- Orthogonal Arrow -->
  <path d="M 400 317 L 470 317 L 470 350 L 550 350" fill="none" stroke="#333" stroke-width="1" marker-end="url(#arrowhead)"/>
  <text x="420" y="340" class="arrow-text">Flow label</text>

</svg>
```

---

## SVG technical requirements

- The file must be a complete, self-contained SVG with `xmlns`, `width`, and `height` on the root `<svg>` element.
- Define all styles in a `<style>` block inside `<defs>`. Use the class names `.title`, `.group-title`, `.box-title`, `.box-text`, `.arrow-text`.
- Define the arrowhead marker in `<defs>` and reference it via `marker-end="url(#arrowhead)"`:
  ```xml
  <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
    <polygon points="0 0, 10 3, 0 6" fill="#333" />
  </marker>
  ```
- Route arrows with `<path>` elements using orthogonal segments (no curves):
  ```xml
  <!-- Horizontal then vertical -->
  <path d="M x1 y1 L x2 y1 L x2 y2 L x3 y2"
        fill="none" stroke="#333" stroke-width="1"
        marker-end="url(#arrowhead)"/>
  ```
- All text must be inside `<text>` elements, not rendered as paths.
- Do not reference external fonts or assets. The diagram must render correctly with no network access.
- Use `rx="5"` on all `<rect>` elements for consistent rounded corners.

---

## Best practices

1. **Start with content:** List all text first, measure longest lines before writing any SVG.
2. **Calculate dimensions:** Use the box sizing formulas before placing elements.
3. **Plan layout:** Sketch positions on paper before coding.
4. **Build incrementally:** Add boxes one at a time and verify positioning before continuing.
5. **Use consistent spacing:** Maintain regular gaps between elements (15–20px within groups, 60px between groups).
6. **Align to a grid:** Use consistent X or Y coordinates across boxes in the same column or row.
7. **Label arrows clearly:** Keep labels short and noun-phrase form; never leave an arrow unlabelled.
8. **Use colour meaningfully:** Assign colours by actor type, not position.
9. **Verify at scale:** View the diagram at actual render size to check text readability.
10. **Comment dimensions:** Add inline comments to SVG code noting box sizes for future edits.

---

## Conversion to PNG

Some markdown viewers do not render SVG directly. Convert with one of the following methods.

**Inkscape (CLI):**
```bash
inkscape diagram.svg --export-filename=diagram.png --export-dpi=150
```

**ImageMagick:**
```bash
convert -density 150 diagram.svg diagram.png
```

**Browser:** Open the SVG in Chrome or Firefox, then use DevTools to take a full-page screenshot.

**Recommended DPI:** 150 for documentation; 300 for print.

---

## What to watch for

- **Too many actors without grouping**: more than four ungrouped actors produces visual clutter. Look for natural groupings (same team, same function) and wrap them in a dashed bounding box.
- **Unlabelled arrows**: an arrow with no label forces the reader to guess what is exchanged. Label every flow, even if the label feels obvious — it confirms the diagram is correct, not just plausible.
- **Diagonal routing**: diagonal arrows are hard to follow and look accidental. Re-route using orthogonal segments with a single bend.
- **Overcrowded central system**: if the core system box has more than five or six bullets, the diagram is trying to document the system, not contextualise it. Strip the list to the capabilities that are visible at the system boundary.
- **Actors with vague responsibility bullets**: bullets like "uses the system" or "provides input" carry no information. Each bullet should name a specific responsibility that explains why this actor appears in the diagram.
- **Colour inconsistency**: if a governance actor is blue in one group and green in another, the colour stops encoding role. Assign colours by actor type, not by group position.
