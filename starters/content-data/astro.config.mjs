import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  base: process.env.GITHUB_ACTIONS === 'true' ? '/{{APP_NAME}}' : '/',
  vite: {
    plugins: [tailwindcss()],
  },
});
