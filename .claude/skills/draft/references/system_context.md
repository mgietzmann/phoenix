# Guidelines: System Context Diagram

A system context diagram shows how a central system sits within its environment — who the actors are, what the system does, and how information or control flows between them. The diagram's job is to make the boundary of the system visible and to give every actor a clear role. Readers should be able to identify the core system and its primary relationships at a glance.

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

## What to watch for

- **Too many actors without grouping**: more than four ungrouped actors produces visual clutter. Look for natural groupings (same team, same function) and wrap them in a dashed bounding box.
- **Unlabelled arrows**: an arrow with no label forces the reader to guess what is exchanged. Label every flow, even if the label feels obvious — it confirms the diagram is correct, not just plausible.
- **Diagonal routing**: diagonal arrows are hard to follow and look accidental. Re-route using orthogonal segments with a single bend.
- **Overcrowded central system**: if the core system box has more than five or six bullets, the diagram is trying to document the system, not contextualise it. Strip the list to the capabilities that are visible at the system boundary.
- **Actors with vague responsibility bullets**: bullets like "uses the system" or "provides input" carry no information. Each bullet should name a specific responsibility that explains why this actor appears in the diagram.
- **Colour inconsistency**: if a governance actor is blue in one group and green in another, the colour stops encoding role. Assign colours by actor type, not by group position.
