# ERD Drawing Style Guide

## Output format

Embed the diagram directly in `Draft.md` as a fenced `mermaid` code block — **not** as an SVG or an image link to an external file. Mermaid ERDs do not render in VSCode preview when referenced as `![...](file.mmd)`.

Also save the raw Mermaid source as `figures/<slug>.mmd` as a source artifact (without the fenced block wrapper, but with the frontmatter `title`).

The Draft.md entry is:

```
```mermaid
erDiagram
    ...
```

*Figure N: <figure description>*
```

## Entity categories

The sketch distinguishes three types of entities. Treat them differently in the diagram:

**Object tables** (shown in bold in the sketch, have `key` and `version` fields) — these are the top-level versioned artifacts. Mark `key` as `PK` and version foreign key fields as `FK`.

**Child tables** (appear as columns in the sketch's markdown tables, linked via a `_version` field on the parent) — these are owned by a single Object. Show them with their own fields and a `PK` on their version field.

**Nomenclature tables** (shown in italics in the sketch, have a versioned identifier) — these are shared registries referenced by multiple Objects. Mark their version field as `PK`. Label edges to nomenclature tables as `"references (nomenclature)"` to visually distinguish them from ownership relationships.

## Relationships

Use crow's foot notation:

- Object → child tables: `||--o{` (one Object owns many child rows)
- Object → nomenclature: `}o--||` (many Objects may reference one nomenclature version)

Label ownership edges with what the child table represents (e.g. `"has BFCs"`, `"has boresights"`). Label nomenclature edges as `"references (nomenclature)"`.

## Fields

Include all fields from the sketch tables. Annotate:
- `key` fields: `PK`
- `_version` fields that are foreign keys to other tables: `FK`
- `_version` fields that identify the table's own version: `PK`

Use types that reflect the data: `string`, `float`, `int`, `boolean`, `geometry`.

## Figure description

The figure description (the italic line after the diagram) should:
- Name the top-level Object tables and what each one represents
- Explain what child tables each Object owns
- Explain which nomenclature tables are shared and by whom
- State why the versioned pointer structure matters (dependency propagation, lineage)
