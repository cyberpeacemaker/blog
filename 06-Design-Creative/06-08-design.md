Act as a Lead UI Engineer. Before you write a single line of frontend code, ingest my DESIGN.md rules and structure your utility classes and components to mirror these exact parameters perfectly.

---

# Design System Guidelines (DESIGN.md)

This file contains the strict structural, aesthetic, and architectural rules for this project's user interface. All generated UI components, pages, and styles MUST strictly adhere to these constraints to ensure visual and functional cohesion.

---

## 1. Design Token Specifications

### Color Palette (Hex & Functional Naming)
*   **Primary (Brand):** `#4F46E5` (Indigo-600) | Hover: `#4338CA` (Indigo-700)
*   **Secondary:** `#0EA5E9` (Sky-500) | Hover: `#0284C7` (Sky-600)
*   **Success:** `#10B981` (Emerald-500)
*   **Warning:** `#F59E0B` (Amber-500)
*   **Danger/Error:** `#EF4444` (Red-500)
*   **Neutral Text:** Primary `#111827` (Gray-900) | Secondary `#4B5563` (Gray-600)
*   **Neutral Background:** Canvas `#F9FAFB` (Gray-50) | Surface Card `#FFFFFF`

### Typography & Hierarchy
*   **Primary Font Family:** Inter, sans-serif
*   **Mono Font Family:** JetBrains Mono, monospace (used for data, code, IDs)
*   **Scale:**
    *   `h1`: 2.25rem (36px) | Bold (700) | Tracking tight
    *   `h2`: 1.5rem (24px) | SemiBold (600)
    *   `h3`: 1.25rem (20px) | Medium (500)
    *   `body-base`: 1rem (16px) | Regular (400) | Line-height 1.5
    *   `body-sm`: 0.875rem (14px) | Regular (400) | Line-height 1.4

### Spacing & Layout Constraints
Use a strict **8px grid increment system** (or Tailwind counterparts):
*   `xs` / `space-1`: 4px (0.25rem)
*   `sm` / `space-2`: 8px (0.5rem) — Minimum interactive element spacing
*   `md` / `space-4`: 16px (1rem) — Standard grid padding, inner card margins
*   `lg` / `space-6`: 24px (1.5rem)
*   `xl` / `space-8`: 32px (2rem) — Section spacing

---

## 2. Global Layout & Component Rules

### Interactive & State Rules
*   **Border Radius:** All buttons, cards, and input fields must use a uniform `8px` (`rounded-lg`) corner radius.
*   **Focus States:** Active/focused inputs and buttons must render a clear target highlight ring: `focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2`.
*   **Transitions:** Interactive changes (hover, focus, active states) must have a smooth transition duration: `transition-all duration-200 ease-in-out`.

### Component Specifics

#### Buttons
*   **Primary:** Filled Primary color, white text. Center-aligned content.
*   **Secondary:** Outlined Gray-300 border, Neutral Text color, Canvas hover background.
*   **Destructive:** Filled Danger color, white text. Used only for permanent deletion actions.
*   *Rule:* All buttons must have an explicit `type="..."` attribute and a minimum touch target size of 44x44px.

#### Forms & Inputs
*   Always include a visible `<label>` paired semantically using the `htmlFor` attribute.
*   Validation errors must be rendered *below* the input block in the Danger color, accompanied by an `aria-live="polite"` wrapper for screen readers.

---

## 3. Accessibility (a11y) & Logic Constraints

*   **Contrast:** Every color pair (text on background) must hit a minimum contrast ratio of 4.5:1 to pass WCAG AA standards.
*   **Semantic HTML:** Never use a `<div>` or `<span>` for clickable behaviors. If an action mutates page state or submits data, construct it as a `<button>`. If it navigates to a new view or anchor link, construct it as an `<a>`.
*   **Icon-Only Elements:** Any button or link displaying *only* an icon must contain an explicit, descriptive `aria-label` attribute describing what it does.

---

## 4. How to Handle Contradictions

If a future prompt instructs you to build a feature or style that directly breaks a token or layout constraint detailed above, you must stop and:
1. Note the contradiction explicitly to the user.
2. Ask for explicit permission to override the system constraints before writing or rendering the implementation code.