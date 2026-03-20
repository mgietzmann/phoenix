# Guidelines: Conceptual Map

A conceptual map shows how ideas, entities, or processes relate to one another. The diagram's job is to make structure visible — which concepts are central, which are peripheral, and how they connect. Every element earns its place by clarifying a relationship the prose alone cannot show as efficiently.

---

## Structure

### Hierarchy and centrality
- Place the most central concept at or near the visual centre. Peripheral concepts radiate outward.
- Use spatial proximity to signal relatedness: concepts that belong to the same cluster should sit near each other.
- The layout should be legible at a glance. A reader should be able to identify the core before reading any labels.

### Nodes
- Each node represents one concept. Do not combine two distinct ideas into one node.
- Node size may encode importance: the most central concepts can be slightly larger, but do not overdo it — two sizes is usually enough.
- Use rounded rectangles as the default node shape. Reserve other shapes (circles, diamonds) for a distinct semantic category, and be consistent within a category.

### Edges
- Each edge represents one relationship. Label edges when the relationship is not self-evident from the connected concepts.
- Use directed arrows when the relationship has a clear direction (e.g. causes, leads to, depends on). Use undirected lines for symmetric relationships (e.g. co-occurs with, is associated with).
- Avoid crossing edges where possible. If crossings are unavoidable, route edges to make the crossing obvious rather than ambiguous.
- Do not use more than two or three distinct edge styles (solid, dashed, dotted). More than that creates visual noise without adding meaning.

---

## Visual style

### Colour
- Use a limited palette: a background colour, one or two node fill colours, and a distinct accent for the most central node or a highlighted category.
- Colour should encode meaning, not decorate. If two nodes share a colour, they belong to the same category.
- Ensure sufficient contrast between node fills and labels. Dark text on light fill or light text on dark fill — pick one and be consistent.
- Suggested neutral palette: white or very light grey background (`#f8f8f8`), mid-grey node fills (`#d0d8e4`), darker border strokes (`#5a6a7a`), near-black labels (`#1a1a2e`).

### Typography
- Use a single sans-serif font throughout. `sans-serif` as the SVG generic family is acceptable.
- Node labels: 13–15px, centred within the node.
- Edge labels: 11–12px, positioned at the midpoint of the edge, slightly offset from the line to avoid overlap.
- Title (if present): 16–18px, top-left or top-centre, set in the same font at a slightly heavier weight.

### Layout and spacing
- The SVG viewBox should be sized to the content, not arbitrarily large. Typical sizes: 700–1000px wide, 500–750px tall.
- Leave adequate padding around all nodes (at least 12px between a label and the node boundary, at least 30px between adjacent nodes).
- Align nodes to an implicit grid where possible. Irregular placement is acceptable when it serves the logic of the map, but avoid accidental misalignment.

### Lines and strokes
- Node borders: 1.5–2px stroke.
- Edges: 1.5px stroke. Use marker-end for arrowheads; keep arrowheads small and proportionate.
- Do not use drop shadows or gradients. Flat styling reads better at small sizes and in print.

---

## SVG technical requirements

- The file must be a complete, self-contained SVG: opening `<svg>` tag with `xmlns`, `viewBox`, and `width`/`height` attributes; all styles inline or in a `<style>` block within the file.
- Use `<defs>` to define arrowhead markers and reuse them via `marker-end`.
- All text must be inside `<text>` elements (not rendered as paths).
- Do not reference external fonts or assets. The diagram must render correctly with no network access.
- Use descriptive `id` attributes on significant elements (`node-upwelling`, `edge-upwelling-nutrients`) to make the SVG editable.

---

## What to watch for

- **Overcrowded centre**: if too many edges meet at the central node, the diagram becomes a hub-and-spoke chart rather than a map. Look for intermediate concepts that can absorb some connections.
- **Unlabelled edges**: an arrow between two nodes that could mean several things is worse than no arrow. Either label it or remove it.
- **Symmetric layout for asymmetric content**: a perfectly symmetric radial layout implies all concepts are equally related to the centre. If the content has directionality or sequence, let the layout reflect it.
- **Labels that fight the edges**: route edges to avoid running through node labels. If unavoidable, use a small white rectangle behind the label to create a clear background.
- **Edge labels in tight gaps**: when the gap between adjacent nodes is narrow (≤ 60px), position the edge label *below* the arrow rather than above it. This keeps the label in the background space between nodes and prevents it from overlapping with node fills.
- **Too many edge styles**: if you find yourself reaching for a fourth line style, the diagram is carrying too much information. Consider splitting it into two diagrams.
