import { defineConfig } from "vite";
import preact from "@preact/preset-vite";

export default defineConfig({
  plugins: [preact()],
  server: {
    proxy: {
      "/create_character": "http://localhost:8000",
      "/convert_character_json": "http://localhost:8000",
      "/openapi.json": "http://localhost:8000",
      "/docs": "http://localhost:8000",
    },
  },
});
