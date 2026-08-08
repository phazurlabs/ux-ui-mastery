# W3C DTCG JSON Token Presets

Complete, valid W3C Design Tokens Community Group (DTCG) JSON for 6 industry presets. Every token file follows the 3-tier architecture (primitive → semantic → component) and is consumable by Style Dictionary 4.x, Figma Variables, and Tokens Studio.

---

## Style Dictionary 4.x Configuration

```javascript
// style-dictionary.config.mjs
import { register } from "@tokens-studio/sd-transforms";
import StyleDictionary from "style-dictionary";

register(StyleDictionary);

export default {
  source: ["tokens/**/*.json"],
  preprocessors: ["tokens-studio"],
  platforms: {
    css: {
      transformGroup: "tokens-studio",
      buildPath: "build/css/",
      files: [
        {
          destination: "tokens.css",
          format: "css/variables",
          options: {
            outputReferences: true,
          },
        },
      ],
    },
    tailwind: {
      transformGroup: "tokens-studio",
      buildPath: "build/tailwind/",
      files: [
        {
          destination: "theme.js",
          format: "javascript/module-flat",
        },
      ],
    },
    ios: {
      transformGroup: "ios-swift",
      buildPath: "build/ios/",
      files: [
        {
          destination: "Tokens.swift",
          format: "ios-swift/class.swift",
          className: "DesignTokens",
        },
      ],
    },
    android: {
      transformGroup: "compose",
      buildPath: "build/android/",
      files: [
        {
          destination: "Tokens.kt",
          format: "compose/object",
          className: "Tokens",
        },
      ],
    },
  },
};
```

## Figma Variables Mapping

| DTCG Tier | Figma Collection | Figma Modes |
|-----------|-----------------|-------------|
| Primitive | `Primitives` | Single mode |
| Semantic | `Semantic` | Light, Dark |
| Component | `Components` | Light, Dark |

Alias syntax: DTCG `"{color.blue.500}"` maps to Figma variable alias in the Primitives collection.

---

## Preset 1: Linear SaaS

### Primitive Tokens

```json
{
  "color": {
    "$description": "Linear SaaS — raw color values in oklch",
    "gray": {
      "50": { "$value": "oklch(0.98 0.005 280)", "$type": "color" },
      "100": { "$value": "oklch(0.95 0.005 280)", "$type": "color" },
      "200": { "$value": "oklch(0.90 0.008 280)", "$type": "color" },
      "300": { "$value": "oklch(0.82 0.010 280)", "$type": "color" },
      "400": { "$value": "oklch(0.70 0.012 280)", "$type": "color" },
      "500": { "$value": "oklch(0.55 0.015 280)", "$type": "color" },
      "600": { "$value": "oklch(0.45 0.015 280)", "$type": "color" },
      "700": { "$value": "oklch(0.35 0.012 280)", "$type": "color" },
      "800": { "$value": "oklch(0.25 0.010 280)", "$type": "color" },
      "900": { "$value": "oklch(0.18 0.008 280)", "$type": "color" },
      "950": { "$value": "oklch(0.12 0.008 280)", "$type": "color" }
    },
    "violet": {
      "50": { "$value": "oklch(0.97 0.02 290)", "$type": "color" },
      "100": { "$value": "oklch(0.93 0.04 290)", "$type": "color" },
      "200": { "$value": "oklch(0.87 0.08 290)", "$type": "color" },
      "300": { "$value": "oklch(0.78 0.13 290)", "$type": "color" },
      "400": { "$value": "oklch(0.67 0.17 290)", "$type": "color" },
      "500": { "$value": "oklch(0.55 0.20 290)", "$type": "color" },
      "600": { "$value": "oklch(0.48 0.20 290)", "$type": "color" },
      "700": { "$value": "oklch(0.40 0.18 290)", "$type": "color" },
      "800": { "$value": "oklch(0.33 0.15 290)", "$type": "color" },
      "900": { "$value": "oklch(0.25 0.12 290)", "$type": "color" }
    },
    "green": {
      "500": { "$value": "oklch(0.60 0.17 145)", "$type": "color" }
    },
    "red": {
      "500": { "$value": "oklch(0.55 0.20 25)", "$type": "color" }
    },
    "amber": {
      "500": { "$value": "oklch(0.75 0.15 75)", "$type": "color" }
    },
    "blue": {
      "500": { "$value": "oklch(0.55 0.18 250)", "$type": "color" }
    },
    "white": { "$value": "#ffffff", "$type": "color" },
    "black": { "$value": "#000000", "$type": "color" }
  },
  "spacing": {
    "0": { "$value": "0", "$type": "dimension" },
    "px": { "$value": "1px", "$type": "dimension" },
    "0.5": { "$value": "2px", "$type": "dimension" },
    "1": { "$value": "4px", "$type": "dimension" },
    "1.5": { "$value": "6px", "$type": "dimension" },
    "2": { "$value": "8px", "$type": "dimension" },
    "3": { "$value": "12px", "$type": "dimension" },
    "4": { "$value": "16px", "$type": "dimension" },
    "5": { "$value": "20px", "$type": "dimension" },
    "6": { "$value": "24px", "$type": "dimension" },
    "8": { "$value": "32px", "$type": "dimension" },
    "10": { "$value": "40px", "$type": "dimension" },
    "12": { "$value": "48px", "$type": "dimension" },
    "16": { "$value": "64px", "$type": "dimension" },
    "20": { "$value": "80px", "$type": "dimension" },
    "24": { "$value": "96px", "$type": "dimension" }
  },
  "fontSize": {
    "xs": { "$value": "0.75rem", "$type": "dimension" },
    "sm": { "$value": "0.8125rem", "$type": "dimension" },
    "base": { "$value": "0.875rem", "$type": "dimension" },
    "lg": { "$value": "1rem", "$type": "dimension" },
    "xl": { "$value": "1.125rem", "$type": "dimension" },
    "2xl": { "$value": "1.25rem", "$type": "dimension" },
    "3xl": { "$value": "1.5rem", "$type": "dimension" },
    "4xl": { "$value": "2rem", "$type": "dimension" },
    "5xl": { "$value": "2.5rem", "$type": "dimension" }
  },
  "fontWeight": {
    "regular": { "$value": 400, "$type": "number" },
    "medium": { "$value": 500, "$type": "number" },
    "semibold": { "$value": 600, "$type": "number" },
    "bold": { "$value": 700, "$type": "number" }
  },
  "lineHeight": {
    "tight": { "$value": 1.2, "$type": "number" },
    "snug": { "$value": 1.35, "$type": "number" },
    "normal": { "$value": 1.5, "$type": "number" },
    "relaxed": { "$value": 1.65, "$type": "number" }
  },
  "borderRadius": {
    "none": { "$value": "0", "$type": "dimension" },
    "sm": { "$value": "4px", "$type": "dimension" },
    "md": { "$value": "6px", "$type": "dimension" },
    "lg": { "$value": "8px", "$type": "dimension" },
    "xl": { "$value": "12px", "$type": "dimension" },
    "2xl": { "$value": "16px", "$type": "dimension" },
    "full": { "$value": "9999px", "$type": "dimension" }
  },
  "duration": {
    "instant": { "$value": "50ms", "$type": "duration" },
    "fast": { "$value": "100ms", "$type": "duration" },
    "normal": { "$value": "150ms", "$type": "duration" },
    "moderate": { "$value": "250ms", "$type": "duration" },
    "slow": { "$value": "400ms", "$type": "duration" }
  }
}
```

### Semantic Tokens (Light Mode)

```json
{
  "color": {
    "bg": {
      "primary": { "$value": "{color.gray.50}", "$type": "color" },
      "subtle": { "$value": "oklch(0.96 0.003 280)", "$type": "color" },
      "surface": { "$value": "{color.white}", "$type": "color" },
      "surfaceRaised": { "$value": "{color.white}", "$type": "color" },
      "overlay": { "$value": "{color.white}", "$type": "color" }
    },
    "text": {
      "primary": { "$value": "{color.gray.900}", "$type": "color" },
      "secondary": { "$value": "{color.gray.500}", "$type": "color" },
      "tertiary": { "$value": "{color.gray.400}", "$type": "color" },
      "inverse": { "$value": "{color.white}", "$type": "color" },
      "link": { "$value": "{color.violet.500}", "$type": "color" }
    },
    "primary": {
      "base": { "$value": "{color.violet.500}", "$type": "color" },
      "hover": { "$value": "{color.violet.600}", "$type": "color" },
      "active": { "$value": "{color.violet.700}", "$type": "color" },
      "subtle": { "$value": "{color.violet.100}", "$type": "color" }
    },
    "border": {
      "default": { "$value": "{color.gray.200}", "$type": "color" },
      "subtle": { "$value": "{color.gray.100}", "$type": "color" },
      "strong": { "$value": "{color.gray.300}", "$type": "color" }
    },
    "feedback": {
      "success": { "$value": "{color.green.500}", "$type": "color" },
      "error": { "$value": "{color.red.500}", "$type": "color" },
      "warning": { "$value": "{color.amber.500}", "$type": "color" },
      "info": { "$value": "{color.blue.500}", "$type": "color" }
    }
  },
  "shadow": {
    "xs": { "$value": "0 1px 2px oklch(0 0 0 / 0.04)", "$type": "shadow" },
    "sm": { "$value": "0 1px 3px oklch(0 0 0 / 0.06), 0 1px 2px oklch(0 0 0 / 0.04)", "$type": "shadow" },
    "md": { "$value": "0 4px 6px oklch(0 0 0 / 0.07), 0 2px 4px oklch(0 0 0 / 0.04)", "$type": "shadow" },
    "lg": { "$value": "0 10px 15px oklch(0 0 0 / 0.08), 0 4px 6px oklch(0 0 0 / 0.04)", "$type": "shadow" },
    "xl": { "$value": "0 20px 25px oklch(0 0 0 / 0.10), 0 8px 10px oklch(0 0 0 / 0.04)", "$type": "shadow" }
  }
}
```

### Semantic Tokens (Dark Mode)

```json
{
  "color": {
    "bg": {
      "primary": { "$value": "{color.gray.950}", "$type": "color" },
      "subtle": { "$value": "oklch(0.14 0.008 280)", "$type": "color" },
      "surface": { "$value": "{color.gray.900}", "$type": "color" },
      "surfaceRaised": { "$value": "{color.gray.800}", "$type": "color" },
      "overlay": { "$value": "{color.gray.800}", "$type": "color" }
    },
    "text": {
      "primary": { "$value": "{color.gray.50}", "$type": "color" },
      "secondary": { "$value": "{color.gray.400}", "$type": "color" },
      "tertiary": { "$value": "{color.gray.500}", "$type": "color" },
      "inverse": { "$value": "{color.gray.900}", "$type": "color" },
      "link": { "$value": "{color.violet.400}", "$type": "color" }
    },
    "primary": {
      "base": { "$value": "{color.violet.400}", "$type": "color" },
      "hover": { "$value": "{color.violet.300}", "$type": "color" },
      "active": { "$value": "{color.violet.200}", "$type": "color" },
      "subtle": { "$value": "{color.violet.900}", "$type": "color" }
    },
    "border": {
      "default": { "$value": "{color.gray.700}", "$type": "color" },
      "subtle": { "$value": "{color.gray.800}", "$type": "color" },
      "strong": { "$value": "{color.gray.600}", "$type": "color" }
    }
  }
}
```

### Component Tokens

```json
{
  "button": {
    "primary": {
      "bg": { "$value": "{color.primary.base}", "$type": "color" },
      "bgHover": { "$value": "{color.primary.hover}", "$type": "color" },
      "text": { "$value": "{color.text.inverse}", "$type": "color" },
      "radius": { "$value": "{borderRadius.md}", "$type": "dimension" },
      "paddingX": { "$value": "{spacing.4}", "$type": "dimension" },
      "paddingY": { "$value": "{spacing.2}", "$type": "dimension" },
      "fontSize": { "$value": "{fontSize.sm}", "$type": "dimension" },
      "fontWeight": { "$value": "{fontWeight.medium}", "$type": "number" }
    },
    "secondary": {
      "bg": { "$value": "transparent", "$type": "color" },
      "bgHover": { "$value": "{color.bg.subtle}", "$type": "color" },
      "text": { "$value": "{color.text.primary}", "$type": "color" },
      "border": { "$value": "{color.border.default}", "$type": "color" }
    }
  },
  "input": {
    "bg": { "$value": "{color.bg.surface}", "$type": "color" },
    "border": { "$value": "{color.border.default}", "$type": "color" },
    "borderFocus": { "$value": "{color.primary.base}", "$type": "color" },
    "text": { "$value": "{color.text.primary}", "$type": "color" },
    "placeholder": { "$value": "{color.text.tertiary}", "$type": "color" },
    "radius": { "$value": "{borderRadius.md}", "$type": "dimension" },
    "paddingX": { "$value": "{spacing.3}", "$type": "dimension" },
    "paddingY": { "$value": "{spacing.2}", "$type": "dimension" }
  },
  "card": {
    "bg": { "$value": "{color.bg.surface}", "$type": "color" },
    "border": { "$value": "{color.border.subtle}", "$type": "color" },
    "radius": { "$value": "{borderRadius.lg}", "$type": "dimension" },
    "padding": { "$value": "{spacing.4}", "$type": "dimension" },
    "shadow": { "$value": "{shadow.sm}", "$type": "shadow" }
  },
  "badge": {
    "bg": { "$value": "{color.primary.subtle}", "$type": "color" },
    "text": { "$value": "{color.primary.base}", "$type": "color" },
    "radius": { "$value": "{borderRadius.full}", "$type": "dimension" },
    "paddingX": { "$value": "{spacing.2}", "$type": "dimension" },
    "paddingY": { "$value": "{spacing.0.5}", "$type": "dimension" },
    "fontSize": { "$value": "{fontSize.xs}", "$type": "dimension" }
  },
  "dialog": {
    "bg": { "$value": "{color.bg.surface}", "$type": "color" },
    "overlayBg": { "$value": "oklch(0 0 0 / 0.5)", "$type": "color" },
    "radius": { "$value": "{borderRadius.xl}", "$type": "dimension" },
    "padding": { "$value": "{spacing.6}", "$type": "dimension" },
    "shadow": { "$value": "{shadow.xl}", "$type": "shadow" }
  }
}
```

---

## Preset 2: Stripe Fintech

### Primitive Tokens

```json
{
  "color": {
    "$description": "Stripe Fintech — premium blue-purple, high-trust",
    "gray": {
      "50": { "$value": "oklch(0.98 0.004 260)", "$type": "color" },
      "100": { "$value": "oklch(0.95 0.005 260)", "$type": "color" },
      "200": { "$value": "oklch(0.91 0.007 260)", "$type": "color" },
      "300": { "$value": "oklch(0.83 0.009 260)", "$type": "color" },
      "400": { "$value": "oklch(0.71 0.011 260)", "$type": "color" },
      "500": { "$value": "oklch(0.56 0.013 260)", "$type": "color" },
      "600": { "$value": "oklch(0.46 0.013 260)", "$type": "color" },
      "700": { "$value": "oklch(0.36 0.011 260)", "$type": "color" },
      "800": { "$value": "oklch(0.26 0.009 260)", "$type": "color" },
      "900": { "$value": "oklch(0.18 0.007 260)", "$type": "color" },
      "950": { "$value": "oklch(0.12 0.006 260)", "$type": "color" }
    },
    "indigo": {
      "50": { "$value": "oklch(0.97 0.02 275)", "$type": "color" },
      "100": { "$value": "oklch(0.93 0.04 275)", "$type": "color" },
      "200": { "$value": "oklch(0.86 0.09 275)", "$type": "color" },
      "300": { "$value": "oklch(0.76 0.14 275)", "$type": "color" },
      "400": { "$value": "oklch(0.65 0.19 275)", "$type": "color" },
      "500": { "$value": "oklch(0.53 0.22 275)", "$type": "color" },
      "600": { "$value": "oklch(0.46 0.22 275)", "$type": "color" },
      "700": { "$value": "oklch(0.39 0.19 275)", "$type": "color" },
      "800": { "$value": "oklch(0.32 0.16 275)", "$type": "color" },
      "900": { "$value": "oklch(0.24 0.12 275)", "$type": "color" }
    },
    "cyan": {
      "400": { "$value": "oklch(0.75 0.12 200)", "$type": "color" },
      "500": { "$value": "oklch(0.65 0.15 200)", "$type": "color" }
    },
    "green": { "500": { "$value": "oklch(0.62 0.16 150)", "$type": "color" } },
    "red": { "500": { "$value": "oklch(0.55 0.22 25)", "$type": "color" } },
    "amber": { "500": { "$value": "oklch(0.76 0.14 80)", "$type": "color" } },
    "white": { "$value": "#ffffff", "$type": "color" }
  },
  "spacing": {
    "0": { "$value": "0", "$type": "dimension" },
    "1": { "$value": "4px", "$type": "dimension" },
    "2": { "$value": "8px", "$type": "dimension" },
    "3": { "$value": "12px", "$type": "dimension" },
    "4": { "$value": "16px", "$type": "dimension" },
    "5": { "$value": "20px", "$type": "dimension" },
    "6": { "$value": "24px", "$type": "dimension" },
    "8": { "$value": "32px", "$type": "dimension" },
    "10": { "$value": "40px", "$type": "dimension" },
    "12": { "$value": "48px", "$type": "dimension" },
    "16": { "$value": "64px", "$type": "dimension" },
    "24": { "$value": "96px", "$type": "dimension" }
  },
  "fontSize": {
    "sm": { "$value": "0.875rem", "$type": "dimension" },
    "base": { "$value": "1rem", "$type": "dimension" },
    "lg": { "$value": "1.125rem", "$type": "dimension" },
    "xl": { "$value": "1.25rem", "$type": "dimension" },
    "2xl": { "$value": "1.5rem", "$type": "dimension" },
    "3xl": { "$value": "1.875rem", "$type": "dimension" },
    "4xl": { "$value": "2.25rem", "$type": "dimension" },
    "5xl": { "$value": "3rem", "$type": "dimension" }
  },
  "borderRadius": {
    "sm": { "$value": "6px", "$type": "dimension" },
    "md": { "$value": "8px", "$type": "dimension" },
    "lg": { "$value": "12px", "$type": "dimension" },
    "xl": { "$value": "16px", "$type": "dimension" },
    "2xl": { "$value": "24px", "$type": "dimension" },
    "full": { "$value": "9999px", "$type": "dimension" }
  }
}
```

### Semantic Tokens (Light)

```json
{
  "color": {
    "bg": {
      "primary": { "$value": "{color.white}", "$type": "color" },
      "subtle": { "$value": "{color.gray.50}", "$type": "color" },
      "surface": { "$value": "{color.white}", "$type": "color" }
    },
    "text": {
      "primary": { "$value": "{color.gray.900}", "$type": "color" },
      "secondary": { "$value": "{color.gray.500}", "$type": "color" },
      "tertiary": { "$value": "{color.gray.400}", "$type": "color" }
    },
    "primary": {
      "base": { "$value": "{color.indigo.500}", "$type": "color" },
      "hover": { "$value": "{color.indigo.600}", "$type": "color" },
      "subtle": { "$value": "{color.indigo.50}", "$type": "color" }
    },
    "secondary": {
      "base": { "$value": "{color.cyan.500}", "$type": "color" }
    },
    "border": {
      "default": { "$value": "{color.gray.200}", "$type": "color" },
      "subtle": { "$value": "{color.gray.100}", "$type": "color" }
    },
    "feedback": {
      "success": { "$value": "{color.green.500}", "$type": "color" },
      "error": { "$value": "{color.red.500}", "$type": "color" },
      "warning": { "$value": "{color.amber.500}", "$type": "color" }
    }
  }
}
```

---

## Preset 3: Shopify E-commerce

### Primitive Tokens

```json
{
  "color": {
    "$description": "Shopify E-commerce — green primary, merchant-friendly",
    "gray": {
      "50": { "$value": "oklch(0.98 0.003 90)", "$type": "color" },
      "100": { "$value": "oklch(0.96 0.004 90)", "$type": "color" },
      "200": { "$value": "oklch(0.91 0.006 90)", "$type": "color" },
      "300": { "$value": "oklch(0.84 0.008 90)", "$type": "color" },
      "400": { "$value": "oklch(0.72 0.010 90)", "$type": "color" },
      "500": { "$value": "oklch(0.57 0.012 90)", "$type": "color" },
      "600": { "$value": "oklch(0.47 0.012 90)", "$type": "color" },
      "700": { "$value": "oklch(0.37 0.010 90)", "$type": "color" },
      "800": { "$value": "oklch(0.26 0.008 90)", "$type": "color" },
      "900": { "$value": "oklch(0.18 0.006 90)", "$type": "color" }
    },
    "green": {
      "50": { "$value": "oklch(0.97 0.02 155)", "$type": "color" },
      "100": { "$value": "oklch(0.93 0.05 155)", "$type": "color" },
      "200": { "$value": "oklch(0.87 0.09 155)", "$type": "color" },
      "300": { "$value": "oklch(0.78 0.14 155)", "$type": "color" },
      "400": { "$value": "oklch(0.68 0.17 155)", "$type": "color" },
      "500": { "$value": "oklch(0.58 0.18 155)", "$type": "color" },
      "600": { "$value": "oklch(0.50 0.16 155)", "$type": "color" },
      "700": { "$value": "oklch(0.42 0.14 155)", "$type": "color" },
      "800": { "$value": "oklch(0.35 0.12 155)", "$type": "color" },
      "900": { "$value": "oklch(0.27 0.09 155)", "$type": "color" }
    },
    "red": { "500": { "$value": "oklch(0.55 0.22 25)", "$type": "color" } },
    "amber": { "500": { "$value": "oklch(0.76 0.14 75)", "$type": "color" } },
    "blue": { "500": { "$value": "oklch(0.55 0.18 250)", "$type": "color" } },
    "white": { "$value": "#ffffff", "$type": "color" }
  },
  "spacing": {
    "0": { "$value": "0", "$type": "dimension" },
    "1": { "$value": "4px", "$type": "dimension" },
    "2": { "$value": "8px", "$type": "dimension" },
    "3": { "$value": "12px", "$type": "dimension" },
    "4": { "$value": "16px", "$type": "dimension" },
    "6": { "$value": "24px", "$type": "dimension" },
    "8": { "$value": "32px", "$type": "dimension" },
    "12": { "$value": "48px", "$type": "dimension" },
    "16": { "$value": "64px", "$type": "dimension" }
  },
  "borderRadius": {
    "sm": { "$value": "6px", "$type": "dimension" },
    "md": { "$value": "8px", "$type": "dimension" },
    "lg": { "$value": "12px", "$type": "dimension" },
    "xl": { "$value": "16px", "$type": "dimension" },
    "full": { "$value": "9999px", "$type": "dimension" }
  }
}
```

### Semantic Tokens (Light)

```json
{
  "color": {
    "bg": {
      "primary": { "$value": "{color.white}", "$type": "color" },
      "subtle": { "$value": "{color.gray.50}", "$type": "color" }
    },
    "text": {
      "primary": { "$value": "{color.gray.900}", "$type": "color" },
      "secondary": { "$value": "{color.gray.600}", "$type": "color" }
    },
    "primary": {
      "base": { "$value": "{color.green.500}", "$type": "color" },
      "hover": { "$value": "{color.green.600}", "$type": "color" },
      "subtle": { "$value": "{color.green.50}", "$type": "color" }
    },
    "price": {
      "regular": { "$value": "{color.gray.900}", "$type": "color" },
      "sale": { "$value": "{color.red.500}", "$type": "color" },
      "savings": { "$value": "{color.green.600}", "$type": "color" }
    },
    "stock": {
      "inStock": { "$value": "{color.green.500}", "$type": "color" },
      "lowStock": { "$value": "{color.amber.500}", "$type": "color" },
      "outOfStock": { "$value": "{color.red.500}", "$type": "color" }
    }
  }
}
```

---

## Preset 4: Discord Social

### Primitive Tokens

```json
{
  "color": {
    "$description": "Discord Social — blurple primary, dark-first",
    "gray": {
      "50": { "$value": "oklch(0.97 0.003 270)", "$type": "color" },
      "100": { "$value": "oklch(0.93 0.005 270)", "$type": "color" },
      "200": { "$value": "oklch(0.87 0.008 270)", "$type": "color" },
      "300": { "$value": "oklch(0.75 0.010 270)", "$type": "color" },
      "400": { "$value": "oklch(0.60 0.012 270)", "$type": "color" },
      "500": { "$value": "oklch(0.47 0.014 270)", "$type": "color" },
      "600": { "$value": "oklch(0.38 0.014 270)", "$type": "color" },
      "700": { "$value": "oklch(0.30 0.012 270)", "$type": "color" },
      "800": { "$value": "oklch(0.23 0.010 270)", "$type": "color" },
      "900": { "$value": "oklch(0.18 0.008 270)", "$type": "color" },
      "950": { "$value": "oklch(0.13 0.007 270)", "$type": "color" }
    },
    "blurple": {
      "300": { "$value": "oklch(0.72 0.15 275)", "$type": "color" },
      "400": { "$value": "oklch(0.62 0.20 275)", "$type": "color" },
      "500": { "$value": "oklch(0.53 0.22 275)", "$type": "color" },
      "600": { "$value": "oklch(0.45 0.22 275)", "$type": "color" }
    },
    "green": { "500": { "$value": "oklch(0.65 0.16 150)", "$type": "color" } },
    "red": { "500": { "$value": "oklch(0.58 0.20 25)", "$type": "color" } },
    "yellow": { "500": { "$value": "oklch(0.82 0.14 90)", "$type": "color" } },
    "white": { "$value": "#ffffff", "$type": "color" }
  },
  "borderRadius": {
    "sm": { "$value": "4px", "$type": "dimension" },
    "md": { "$value": "8px", "$type": "dimension" },
    "lg": { "$value": "16px", "$type": "dimension" },
    "full": { "$value": "9999px", "$type": "dimension" }
  }
}
```

### Semantic Tokens (Dark — Default)

```json
{
  "color": {
    "bg": {
      "primary": { "$value": "{color.gray.800}", "$type": "color" },
      "secondary": { "$value": "{color.gray.700}", "$type": "color" },
      "tertiary": { "$value": "{color.gray.900}", "$type": "color" },
      "sidebar": { "$value": "{color.gray.950}", "$type": "color" }
    },
    "text": {
      "primary": { "$value": "{color.white}", "$type": "color" },
      "secondary": { "$value": "{color.gray.300}", "$type": "color" },
      "muted": { "$value": "{color.gray.400}", "$type": "color" },
      "link": { "$value": "{color.blurple.300}", "$type": "color" }
    },
    "primary": {
      "base": { "$value": "{color.blurple.500}", "$type": "color" },
      "hover": { "$value": "{color.blurple.400}", "$type": "color" }
    },
    "presence": {
      "online": { "$value": "{color.green.500}", "$type": "color" },
      "idle": { "$value": "{color.yellow.500}", "$type": "color" },
      "dnd": { "$value": "{color.red.500}", "$type": "color" },
      "offline": { "$value": "{color.gray.500}", "$type": "color" }
    },
    "mention": {
      "bg": { "$value": "oklch(0.53 0.22 275 / 0.15)", "$type": "color" },
      "text": { "$value": "{color.blurple.300}", "$type": "color" }
    }
  }
}
```

---

## Preset 5: Creative Agency

### Primitive Tokens

```json
{
  "color": {
    "$description": "Creative Agency — bold, editorial, near-black + warm white",
    "neutral": {
      "50": { "$value": "oklch(0.98 0.005 60)", "$type": "color" },
      "100": { "$value": "oklch(0.95 0.006 60)", "$type": "color" },
      "200": { "$value": "oklch(0.90 0.008 60)", "$type": "color" },
      "800": { "$value": "oklch(0.22 0.008 60)", "$type": "color" },
      "900": { "$value": "oklch(0.14 0.005 60)", "$type": "color" },
      "950": { "$value": "oklch(0.08 0.003 60)", "$type": "color" }
    },
    "accent": {
      "vermillion": { "$value": "oklch(0.60 0.22 30)", "$type": "color" },
      "electric": { "$value": "oklch(0.58 0.24 265)", "$type": "color" },
      "acid": { "$value": "oklch(0.80 0.22 130)", "$type": "color" }
    },
    "white": { "$value": "oklch(0.98 0.005 60)", "$type": "color", "$description": "Warm white" },
    "black": { "$value": "oklch(0.08 0.003 60)", "$type": "color", "$description": "Near-black" }
  },
  "fontSize": {
    "body": { "$value": "1rem", "$type": "dimension" },
    "lg": { "$value": "1.25rem", "$type": "dimension" },
    "xl": { "$value": "1.5rem", "$type": "dimension" },
    "display-sm": { "$value": "2.5rem", "$type": "dimension" },
    "display-md": { "$value": "4rem", "$type": "dimension" },
    "display-lg": { "$value": "6rem", "$type": "dimension" },
    "display-xl": { "$value": "8rem", "$type": "dimension" }
  },
  "borderRadius": {
    "none": { "$value": "0", "$type": "dimension", "$description": "Sharp edges for editorial feel" },
    "full": { "$value": "9999px", "$type": "dimension" }
  }
}
```

### Semantic Tokens

```json
{
  "color": {
    "bg": {
      "primary": { "$value": "{color.black}", "$type": "color" },
      "surface": { "$value": "{color.neutral.900}", "$type": "color" },
      "contrast": { "$value": "{color.white}", "$type": "color" }
    },
    "text": {
      "primary": { "$value": "{color.white}", "$type": "color" },
      "secondary": { "$value": "{color.neutral.200}", "$type": "color" },
      "accent": { "$value": "{color.accent.vermillion}", "$type": "color" }
    },
    "primary": {
      "base": { "$value": "{color.accent.vermillion}", "$type": "color" }
    }
  }
}
```

---

## Preset 6: Healthcare

### Primitive Tokens

```json
{
  "color": {
    "$description": "Healthcare — calm, clinical trust, WCAG AAA",
    "gray": {
      "50": { "$value": "oklch(0.98 0.003 220)", "$type": "color" },
      "100": { "$value": "oklch(0.96 0.004 220)", "$type": "color" },
      "200": { "$value": "oklch(0.92 0.006 220)", "$type": "color" },
      "300": { "$value": "oklch(0.85 0.008 220)", "$type": "color" },
      "400": { "$value": "oklch(0.73 0.010 220)", "$type": "color" },
      "500": { "$value": "oklch(0.58 0.012 220)", "$type": "color" },
      "600": { "$value": "oklch(0.48 0.012 220)", "$type": "color" },
      "700": { "$value": "oklch(0.38 0.010 220)", "$type": "color" },
      "800": { "$value": "oklch(0.28 0.008 220)", "$type": "color" },
      "900": { "$value": "oklch(0.19 0.006 220)", "$type": "color" }
    },
    "teal": {
      "50": { "$value": "oklch(0.97 0.02 185)", "$type": "color" },
      "100": { "$value": "oklch(0.93 0.04 185)", "$type": "color" },
      "200": { "$value": "oklch(0.87 0.08 185)", "$type": "color" },
      "300": { "$value": "oklch(0.78 0.12 185)", "$type": "color" },
      "400": { "$value": "oklch(0.68 0.14 185)", "$type": "color" },
      "500": { "$value": "oklch(0.58 0.14 185)", "$type": "color" },
      "600": { "$value": "oklch(0.50 0.12 185)", "$type": "color" },
      "700": { "$value": "oklch(0.42 0.10 185)", "$type": "color" },
      "800": { "$value": "oklch(0.34 0.08 185)", "$type": "color" },
      "900": { "$value": "oklch(0.26 0.06 185)", "$type": "color" }
    },
    "red": {
      "500": { "$value": "oklch(0.55 0.20 25)", "$type": "color", "$description": "Critical alert" },
      "100": { "$value": "oklch(0.95 0.03 25)", "$type": "color" }
    },
    "amber": {
      "500": { "$value": "oklch(0.75 0.14 80)", "$type": "color", "$description": "Warning" },
      "100": { "$value": "oklch(0.95 0.03 80)", "$type": "color" }
    },
    "green": {
      "500": { "$value": "oklch(0.62 0.15 150)", "$type": "color", "$description": "Positive/stable" },
      "100": { "$value": "oklch(0.95 0.03 150)", "$type": "color" }
    },
    "blue": {
      "500": { "$value": "oklch(0.55 0.16 250)", "$type": "color", "$description": "Informational" }
    },
    "white": { "$value": "#ffffff", "$type": "color" }
  },
  "fontSize": {
    "sm": { "$value": "0.875rem", "$type": "dimension" },
    "base": { "$value": "1rem", "$type": "dimension", "$description": "16px — never smaller for patient-facing" },
    "lg": { "$value": "1.125rem", "$type": "dimension" },
    "xl": { "$value": "1.25rem", "$type": "dimension" },
    "2xl": { "$value": "1.5rem", "$type": "dimension" },
    "3xl": { "$value": "2rem", "$type": "dimension" }
  },
  "borderRadius": {
    "sm": { "$value": "6px", "$type": "dimension" },
    "md": { "$value": "10px", "$type": "dimension" },
    "lg": { "$value": "14px", "$type": "dimension" },
    "xl": { "$value": "20px", "$type": "dimension" },
    "full": { "$value": "9999px", "$type": "dimension" }
  }
}
```

### Semantic Tokens (Light)

```json
{
  "color": {
    "bg": {
      "primary": { "$value": "{color.white}", "$type": "color" },
      "subtle": { "$value": "{color.gray.50}", "$type": "color" },
      "surface": { "$value": "{color.white}", "$type": "color" }
    },
    "text": {
      "primary": { "$value": "{color.gray.900}", "$type": "color" },
      "secondary": { "$value": "{color.gray.600}", "$type": "color" }
    },
    "primary": {
      "base": { "$value": "{color.teal.500}", "$type": "color" },
      "hover": { "$value": "{color.teal.600}", "$type": "color" },
      "subtle": { "$value": "{color.teal.50}", "$type": "color" }
    },
    "alert": {
      "critical": { "$value": "{color.red.500}", "$type": "color" },
      "criticalBg": { "$value": "{color.red.100}", "$type": "color" },
      "warning": { "$value": "{color.amber.500}", "$type": "color" },
      "warningBg": { "$value": "{color.amber.100}", "$type": "color" },
      "stable": { "$value": "{color.green.500}", "$type": "color" },
      "stableBg": { "$value": "{color.green.100}", "$type": "color" },
      "info": { "$value": "{color.blue.500}", "$type": "color" }
    },
    "patientStatus": {
      "admitted": { "$value": "{color.teal.500}", "$type": "color" },
      "discharged": { "$value": "{color.gray.400}", "$type": "color" },
      "critical": { "$value": "{color.red.500}", "$type": "color" },
      "stable": { "$value": "{color.green.500}", "$type": "color" }
    }
  }
}
```

### Component Tokens

```json
{
  "alertBanner": {
    "critical": {
      "bg": { "$value": "{color.alert.criticalBg}", "$type": "color" },
      "border": { "$value": "{color.alert.critical}", "$type": "color" },
      "icon": { "$value": "{color.alert.critical}", "$type": "color" },
      "text": { "$value": "{color.gray.900}", "$type": "color" }
    },
    "warning": {
      "bg": { "$value": "{color.alert.warningBg}", "$type": "color" },
      "border": { "$value": "{color.alert.warning}", "$type": "color" },
      "icon": { "$value": "{color.alert.warning}", "$type": "color" },
      "text": { "$value": "{color.gray.900}", "$type": "color" }
    },
    "stable": {
      "bg": { "$value": "{color.alert.stableBg}", "$type": "color" },
      "border": { "$value": "{color.alert.stable}", "$type": "color" },
      "icon": { "$value": "{color.alert.stable}", "$type": "color" },
      "text": { "$value": "{color.gray.900}", "$type": "color" }
    }
  },
  "patientCard": {
    "bg": { "$value": "{color.bg.surface}", "$type": "color" },
    "border": { "$value": "{color.gray.200}", "$type": "color" },
    "radius": { "$value": "{borderRadius.lg}", "$type": "dimension" },
    "padding": { "$value": "24px", "$type": "dimension" }
  },
  "vitalSign": {
    "label": { "$value": "{color.text.secondary}", "$type": "color" },
    "value": { "$value": "{color.text.primary}", "$type": "color" },
    "unit": { "$value": "{color.text.secondary}", "$type": "color" },
    "fontSize": { "$value": "{fontSize.2xl}", "$type": "dimension" }
  }
}
```
