/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        dnd: {
          red: "#8B1A1A",
          gold: "#C9A84C",
          dark: "#1A1A2E",
          panel: "#16213E",
          card: "#0F3460",
          border: "#2D4A7A",
        },
      },
    },
  },
  plugins: [],
};
