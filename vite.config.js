import { defineConfig } from "vite";

export default defineConfig({
  base: "/Abid-Gateway/",
  build: {
    outDir: "dist",
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: "index.html",
        instapayDemo: "instapay-demo.html",
      },
    },
  },
});
