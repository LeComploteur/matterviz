import { dirname, resolve } from 'path'
import { defineConfig } from 'rolldown'
import svelte from 'rollup-plugin-svelte'
import { fileURLToPath } from 'url'

const __dirname = dirname(fileURLToPath(import.meta.url))

const sharedConfig = {
  plugins: [
    svelte({
      compilerOptions: { runes: true },
      include: [`**/*.svelte`], // DEBUG should also include `**/*.svelte.ts` but that fails the build command
      emitCss: true,
    }),
  ],
  resolve: {
    alias: {
      '$lib': resolve(__dirname, `../../src/lib`),
      '$lib/*': resolve(__dirname, `../../src/lib/*`),
    },
  },
  external: (id) => {
    // Keep Node.js builtins as external since they can't run in browser
    if (
      id.startsWith(`node:`) || [`fs`, `path`, `crypto`, `util`].includes(id)
    ) return true
    // Bundle everything else
    return false
  },
}

export default [
  defineConfig({
    input: `./src/structure.js`,
    output: {
      dir: `./matterviz/static/`,
      entryFileNames: `structure.js`,
      sourcemap: false,
      inlineDynamicImports: true,
    },
    ...sharedConfig,
  }),
  defineConfig({
    input: `./src/trajectory.js`,
    output: {
      dir: `./matterviz/static/`,
      entryFileNames: `trajectory.js`,
      sourcemap: false,
      inlineDynamicImports: true,
    },
    ...sharedConfig,
  }),
]
